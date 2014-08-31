from os.path import splitext, join

def upload_student_work_to(self, folder, filename, info=None):
    if info is None:
        info = ''
    else:
        info = ' (' + info + ')'
    id = str(self.id)
    if self.student:
        name = str(self.student.surname_initials)
    else:
        name = 'Аноним'
    title = str(self.title)
    ext = splitext(filename)[1].lower()
    fullname = '{name} - {title}{info}{ext}'.format(
        name=name,
        title=title,
        info=info,
        ext=ext
    )
    return join(folder, id, fullname)
