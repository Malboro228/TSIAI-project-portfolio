document.addEventListener('DOMContentLoaded', function() {
    var projects = document.querySelectorAll('.project');
    projects.forEach(function(project) {
        project.addEventListener('click', function() {
            var url = project.getAttribute('data-url');
            if (url) {
                window.location.href = url;
            }
        });
    });

    document.getElementById("emailLink").addEventListener("click", function(event) {
        event.preventDefault(); 
        var emailAddress = "alloj5prime@mail.com";
        var subject = encodeURIComponent("Pytania na temat projetu");
        var body = encodeURIComponent("Witam, Artem,");
        window.location.href = "mailto:" + emailAddress + "?subject=" + subject + "&body=" + body;
    });
});

