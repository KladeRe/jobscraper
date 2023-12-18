from duuni_app.models import ProgrammingLanguage

programming_languages = ["Python", "Java", "Javascript", "Typescript", "C++", "C#", "React", "Angular", "Vue", "SQL", "noSQL", "PHP", ".NET", "HTML", "CSS", "Node.js", "Kotlin", "Swift", "Rust", "C ", "Go", "Flutter", "Cobol", "Azure", "Express", "Bash", "Docker", "Kubernetes", "AWS", "REST"]
def turnToEntry(language):
    return ProgrammingLanguage.objects.create(name=language)
programming_language_entries = list(map(turnToEntry, programming_languages))