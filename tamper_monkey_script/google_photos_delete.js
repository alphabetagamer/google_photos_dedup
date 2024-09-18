// ==UserScript==
// @name         Google Photos Auto-Delete
// @namespace    http://tampermonkey.net/
// @version      1.1
// @description  Loops through Google Photos URLs and deletes the images by clicking "Move to Trash".
// @author       You
// @match        https://photos.google.com/*
// @grant        none
// ==/UserScript==


(function() {
    'use strict';

    // List of Google Photos URLs to delete
    const photoUrls = []
    // Index to keep track of the current URL
    const cookieName = 'refreshCount';
    const initialValue = -1;
    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(';').shift();
        return null;
    }

    // Function to set a cookie
    function setCookie(name, value, days) {
        const date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        const expires = `; expires=${date.toUTCString()}`;
        document.cookie = `${name}=${value}${expires}; path=/`;
    }
    let refreshCount = parseInt(getCookie(cookieName));

    // If the cookie does not exist, set it with the initial value
    if (isNaN(refreshCount)) {
        refreshCount = initialValue;
    } else {
        // Increment the cookie value by 1
        refreshCount += 1;
    }

    // Function to navigate to the next photo URL
    function openNextPhoto() {
        if (refreshCount < photoUrls.length) {
            console.log("Current Index",refreshCount); console.log("Picture at",photoUrls[refreshCount]);
            try{
            window.location.href = photoUrls[refreshCount];
            }
            catch(error){
                console.log("Current Index",refreshCount); console.log("Picture at",photoUrls[refreshCount]);
            }
            //currentIndex+=1;
        }
            else {
            console.log("Finished deleting all selected photos.");
        }
    }

    // Function to delete the current photo
    function deleteCurrentPhoto() {
        const deleteButton = document.querySelector('[aria-label="Delete"]');
        if (deleteButton) {
            console.log("Deleting photo...");
            deleteButton.click();

            // Confirm deletion by clicking the "Move to trash" button
            setTimeout(() => {
                const spans = document.querySelectorAll('span');
                let found = false;
                spans.forEach(span => {
                    if (span.textContent.trim() === "Move to trash") {
                        const confirmButton = span.closest('button');
                        if (confirmButton) {
                            confirmButton.click();
                            console.log("Photo moved to trash.");
                            found = true;
                        }
                    }
                });
                if (!found) {
                    console.log("Move to trash button not found.");
                }
            }, 2000); // Adjust timing as needed

            // Move to the next photo after deletion
            setTimeout(openNextPhoto, 5000); // Wait for 5 seconds before opening the next photo
        } else {
            console.log("Delete button not found. Moving to next photo.");
            openNextPhoto();
        }
    }
    setCookie(cookieName, refreshCount, 7); // 7 days expiry

    // Log the current refresh count
    console.log("Page has been refreshed",refreshCount," times.");
    // Listen for page load completion
    window.addEventListener('load', () => {
        setTimeout(deleteCurrentPhoto, 3000); // Wait for 3 seconds before attempting to delete
    });

})();
