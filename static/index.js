const navItems = document.querySelector('nav-item > a')

for (navItem in navItems) {
    navItem.addEventListener('click', () => {
        navItem.classList.add('active')
    })
}