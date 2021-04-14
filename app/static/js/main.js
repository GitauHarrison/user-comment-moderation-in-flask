let allowed = false;
const allow_link = document.getElementById('allow_comment');

function AllowComment(event) {
    event.preventDefault();
    if (!allowed) {
        allow_link.disable = true;
        allow_link.innerHTML = 'Allowing';
        display_user_comments().then(() => {
            allow_link.disable = false;
            allow_link.innerHTML = 'Allow';
        }).catch(() => {
            allow_link.innerHTML = 'Allow';
            allow_link.disable = false;
        });

    }
    else {
        fetch('{{ url_for('admin') }}');
    }
}

allow_link.addEventListener('click', AllowComment);