const initSlider = () => {
    const imageList = document.querySelector(".slider-wrapper .image-list");
    const sliderScrollbar = document.querySelector(".class-container .slider-scrollbar");
    const scrollbarThumb = sliderScrollbar.querySelector(".scrollbar-thumb");
    const maxScrollLeft = imageList.scrollWidth - imageList.clientWidth;
    
    let scrollAmount = 2; // Controls how fast the images scroll
    let reverse = false; // Flag to reverse the scroll direction
    let intervalId; // Interval ID to track the auto-scroll interval

    // Function to auto-scroll the images
    const autoScroll = () => {
        if (!reverse) {
            imageList.scrollLeft += scrollAmount;
            if (imageList.scrollLeft >= maxScrollLeft) {
                reverse = true; // Reverse the scroll direction when reaching the last image
            }
        } else {
            imageList.scrollLeft -= scrollAmount;
            if (imageList.scrollLeft <= 0) {
                reverse = false; // Reverse the scroll direction when reaching the first image
            }
        }
        updateScrollThumbPosition(); // Update the scrollbar thumb based on the scroll position
    };

    // Function to start auto-scrolling
    const startAutoScroll = () => {
        if (!intervalId) { // Prevent multiple intervals from being set
            intervalId = setInterval(autoScroll, 50); // Set the speed of auto-scrolling
        }
    };

    // Function to stop auto-scrolling
    const stopAutoScroll = () => {
        if (intervalId) {
            clearInterval(intervalId); // Clear the interval to stop auto-scrolling
            intervalId = null; // Reset the interval ID
        }
    };

    // Update scrollbar thumb position based on image scroll
    const updateScrollThumbPosition = () => {
        const scrollPosition = imageList.scrollLeft;
        const thumbPosition = (scrollPosition / maxScrollLeft) * (sliderScrollbar.clientWidth - scrollbarThumb.offsetWidth);
        scrollbarThumb.style.left = `${thumbPosition}px`;
    };

    // Handle scrollbar thumb drag
    scrollbarThumb.addEventListener("mousedown", (e) => {
        const startX = e.clientX;
        const thumbPosition = scrollbarThumb.offsetLeft;
        const maxThumbPosition = sliderScrollbar.getBoundingClientRect().width - scrollbarThumb.offsetWidth;

        const handleMouseMove = (e) => {
            const deltaX = e.clientX - startX;
            const newThumbPosition = thumbPosition + deltaX;
            const boundedPosition = Math.max(0, Math.min(maxThumbPosition, newThumbPosition));
            const scrollPosition = (boundedPosition / maxThumbPosition) * maxScrollLeft;

            scrollbarThumb.style.left = `${boundedPosition}px`;
            imageList.scrollLeft = scrollPosition;
        };

        const handleMouseUp = () => {
            document.removeEventListener("mousemove", handleMouseMove);
            document.removeEventListener("mouseup", handleMouseUp);
        };

        document.addEventListener("mousemove", handleMouseMove);
        document.addEventListener("mouseup", handleMouseUp);
    });

    // Observe when the slider section is in view to start/stop auto-scrolling
    const classesSection = document.querySelector('.our-classes');
    const observer = new IntersectionObserver((entries) => {
        if (entries[0].isIntersecting) {
            startAutoScroll(); // Start auto-scrolling when the slider is in view
        } else {
            stopAutoScroll(); // Stop auto-scrolling when the slider is out of view
        }
    }, { threshold: 0.5 }); // Trigger when 50% of the section is in view

    observer.observe(classesSection); // Start observing the slider section
};

// Initialize the slider once the page is fully loaded
window.addEventListener("load", initSlider);
