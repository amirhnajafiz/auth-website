function deleteNote(noteId) {
    fetch('/delete-note', {
        method: 'POST',
        body: JSON.stringify({ noteId: noteId })
    }).then((_res) => {
        window.location.href = "/"
    })
}

function editFilter(filter) {
    window.location.href = '/?key=' + filter;
}

function moveToRegister() {
    window.location.href = "/sign-up";
}