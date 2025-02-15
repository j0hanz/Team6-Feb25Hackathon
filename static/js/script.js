document.addEventListener('DOMContentLoaded', function () {
    // Get the theme switcher element
    const themeSwitcher = document.getElementById('theme-switcher');
    if (themeSwitcher) {
        themeSwitcher.addEventListener('change', function () {
            document.body.className = this.value;
        });
    }
});
