document.addEventListener('DOMContentLoaded', function () {
    // Get the theme switcher element
    const themeSwitcher = document.getElementById('theme-switcher');
    if (themeSwitcher) {
        themeSwitcher.addEventListener('change', function () {
            document.body.className = this.value;
        });
    }

    // Get the font family selector element
    const fontFamilySelector = document.getElementById('font-family-selector');
    if (fontFamilySelector) {
        fontFamilySelector.addEventListener('change', function () {
            document.body.style.fontFamily = this.value;
        });
    }
});
