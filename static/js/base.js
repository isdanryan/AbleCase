// Set event listener to check when user scrolls down page
document.addEventListener('DOMContentLoaded', function () {
    window.addEventListener('scroll', function () {
        var backToTopButton = document.getElementById('back-to-top');
        if (window.scrollY > 50) {
            // Display button after scroll
            backToTopButton.style.display = 'block';
        } else {
            backToTopButton.style.display = 'none';
        }
    });

    // Add event listener to check when button is pressed
    var backToTopButton = document.getElementById('back-to-top');
    backToTopButton.addEventListener('click', function () {
        scrollToTop(200); // Set auto-scroll duration
    });
});

// Scroll up to top of page
function scrollToTop(duration) {
    var start = window.scrollY;
    var startTime = 'now' in window.performance ? performance.now() : new Date().getTime();

    function scrollStep(timestamp) {
        var currentTime = 'now' in window.performance ? performance.now() : new Date().getTime();
        var elapsed = currentTime - startTime;
        var progress = Math.min(elapsed / duration, 1);

        window.scrollTo(0, start * (1 - progress));

        if (progress < 1) {
            requestAnimationFrame(scrollStep);
        }
    }

    requestAnimationFrame(scrollStep);
}