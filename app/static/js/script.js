let notification = document.querySelector('.notification')

document.querySelector('.contact-form').addEventListener('submit', function (event) {
    event.preventDefault()
    let formData = new FormData(this)
    let data = {}
    formData.forEach((value, key) => {
        data[key] = value
    })

    // check for valid email
    if (!data.email.match('\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}\\b')) {
        displayNotification('red', 'Submitted email is not valid.')
        return
    }

    let username_pattern = '^[a-zA-Z0-9_-]+$' // alnum characters, "-", "_"
    if (!data.name.match(username_pattern)) {
        displayNotification('red', 'Invalid name. Please use alphanumeric characters.')
        return;
    }

    displayNotification('green', 'Your message has been sent successfully! You will be redirected shortly.')
    setTimeout(() => this.submit(), 1500)
})

function displayNotification(color, text) {
    let notification = document.querySelector('.notification')
    notification.style.color = color
    notification.textContent = text
}