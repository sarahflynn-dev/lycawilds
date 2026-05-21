function onSubmit(token) {
    for (const form of document.getElementsByClassName("recaptcha-form")) {
        if (form.checkValidity()) {
            form.submit();
        } else {
            grecaptcha.reset();
            form.reportValidity();
        }
    }
}