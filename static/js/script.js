document.addEventListener('DOMContentLoaded', function () {
    // Get the theme switcher element
    const themeSwitcher = document.getElementById('theme-switcher');
    if (themeSwitcher) {
        themeSwitcher.addEventListener('change', function () {
            document.body.className = this.value;
            updateNavLinkColors();
        });
    }

    // Get the font family selector element
    const fontFamilySelector = document.getElementById('font-family-selector');
    if (fontFamilySelector) {
        fontFamilySelector.addEventListener('change', function () {
            document.body.style.fontFamily = this.value;
        });
    }

    function updateNavLinkColors() {
        const navLinks = document.querySelectorAll('.navLink');
        navLinks.forEach(link => {
            if (document.body.classList.contains('dark')) {
                link.style.color = '#ffffff';
            } else {
                link.style.color = '#000000';
            }
        });
    }

    // Initial call to set the correct colors
    updateNavLinkColors();
});
