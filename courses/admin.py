from django.contrib import admin

from .models import \
    Course, CourseVersion, CourseSemester, \
    Exam, ExamMark, Lecture, LabWork, PracticeWork

class CourseAdmin(admin.ModelAdmin):
    pass

admin.site.register(Course, CourseAdmin)


class CourseVersionAdmin(admin.ModelAdmin):
    pass

admin.site.register(CourseVersion, CourseVersionAdmin)


class CourseSemesterAdmin(admin.ModelAdmin):
    pass

admin.site.register(CourseSemester, CourseSemesterAdmin)


class ExamAdmin(admin.ModelAdmin):
    pass

admin.site.register(Exam, ExamAdmin)


class ExamMarkAdmin(admin.ModelAdmin):
    pass

admin.site.register(ExamMark, ExamMarkAdmin)


class LectureAdmin(admin.ModelAdmin):
    pass

admin.site.register(Lecture, LectureAdmin)

class LabWorkAdmin(admin.ModelAdmin):
    pass

admin.site.register(LabWork, LabWorkAdmin)

class PracticeWorkAdmin(admin.ModelAdmin):
    pass

admin.site.register(PracticeWork, PracticeWorkAdmin)