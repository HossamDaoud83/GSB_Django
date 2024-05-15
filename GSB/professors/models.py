# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TblBudget(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    doctors_count = models.IntegerField(db_column='Doctors Count', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    semester = models.CharField(max_length=15, blank=True, null=True)
    location = models.CharField(max_length=20, blank=True, null=True)
    teaching_fees = models.FloatField(blank=True, null=True)
    transfer_fees = models.FloatField(blank=True, null=True)
    hall_cost = models.FloatField(blank=True, null=True)
    accommodation_fees = models.FloatField(blank=True, null=True)
    travel_fees = models.FloatField(blank=True, null=True)
    administrative_fess = models.FloatField(blank=True, null=True)
    miscellaneous = models.FloatField(blank=True, null=True)
    advertising = models.FloatField(blank=True, null=True)
    assist_depart_fees = models.FloatField(blank=True, null=True)
    marketing_commission = models.FloatField(blank=True, null=True)
    revenues = models.FloatField(blank=True, null=True)
    expenses = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_budget'


class TblLailaEvaCourse(models.Model):
    timetableid = models.IntegerField(db_column='TimeTableID', blank=True, null=True)  # Field name made lowercase.
    recommendations = models.TextField(db_column='Recommendations', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_laila_eva_course'


class TblLailaEvaProff(models.Model):
    contactid = models.IntegerField(unique=True, blank=True, null=True)
    recommendations = models.TextField(db_column='Recommendations', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_laila_eva_proff'


class TblLailaMsDuration(models.Model):
    teamname = models.CharField(db_column='TeamName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    filename = models.CharField(db_column='FileName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    creation_time = models.CharField(db_column='Creation_Time', max_length=255, blank=True, null=True)  # Field name made lowercase.
    last_write = models.CharField(db_column='Last_Write', max_length=255, blank=True, null=True)  # Field name made lowercase.
    duration = models.TimeField(db_column='Duration', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_laila_ms_duration'


class Tblacademicdegreelist(models.Model):
    academicdegreelistid = models.AutoField(db_column='AcademicDegreeListID', primary_key=True)  # Field name made lowercase.
    academicdegree = models.CharField(db_column='AcademicDegree', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hourcost = models.DecimalField(db_column='HourCost', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblacademicdegreelist'


class Tblacademicmajorlist(models.Model):
    academicmajorlistid = models.AutoField(db_column='AcademicMajorListID', primary_key=True)  # Field name made lowercase.
    academicmajor = models.CharField(db_column='AcademicMajor', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblacademicmajorlist'


class Tblattendance(models.Model):
    attendanceid = models.AutoField(db_column='AttendanceID', primary_key=True)  # Field name made lowercase.
    timetableid = models.ForeignKey('Tbltimetable', models.DO_NOTHING, db_column='TimeTableID')  # Field name made lowercase.
    lectureday = models.DecimalField(db_column='LectureDay', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lecturedate = models.DateField(db_column='LectureDate', blank=True, null=True)  # Field name made lowercase.
    timefrom = models.TimeField(db_column='TimeFrom', blank=True, null=True)  # Field name made lowercase.
    timeto = models.TimeField(db_column='TimeTo', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblattendance'


class Tblbank(models.Model):
    bankid = models.AutoField(db_column='BankID', primary_key=True)  # Field name made lowercase.
    contactsid = models.ForeignKey('Tblcontacts', models.DO_NOTHING, db_column='ContactsID')  # Field name made lowercase.
    bankname = models.DecimalField(db_column='BankName', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    branch = models.CharField(db_column='Branch', max_length=50, blank=True, null=True)  # Field name made lowercase.
    accountno = models.CharField(db_column='AccountNo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    swiftcode = models.CharField(db_column='SwiftCode', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblbank'


class Tblbanklist(models.Model):
    banklistid = models.AutoField(db_column='BankListID', primary_key=True)  # Field name made lowercase.
    banklistname = models.CharField(db_column='BankListName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblbanklist'


class Tblcategorylist(models.Model):
    categorylistid = models.AutoField(db_column='CategoryListID', primary_key=True)  # Field name made lowercase.
    categoryname = models.CharField(db_column='CategoryName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblcategorylist'


class Tblcitylist(models.Model):
    citylistid = models.AutoField(db_column='CityListID', primary_key=True)  # Field name made lowercase.
    cityname = models.CharField(db_column='CityName', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblcitylist'


class Tblcontacts(models.Model):
    contactsid = models.AutoField(db_column='ContactsID', primary_key=True)  # Field name made lowercase.
    aastid = models.CharField(db_column='AASTID', unique=True, max_length=10, blank=True, null=True)  # Field name made lowercase.
    portal_pass = models.CharField(db_column='Portal_Pass', max_length=50, blank=True, null=True)  # Field name made lowercase.
    atitle = models.CharField(db_column='Atitle', max_length=20, blank=True, null=True)  # Field name made lowercase.
    aname = models.CharField(db_column='AName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    etitle = models.CharField(db_column='ETitle', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ename = models.CharField(db_column='EName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    esurname = models.CharField(db_column='ESurname', max_length=45, blank=True, null=True)  # Field name made lowercase.
    asurname = models.CharField(db_column='ASurname', max_length=45, blank=True, null=True)  # Field name made lowercase.
    phone1 = models.CharField(db_column='Phone1', max_length=15, blank=True, null=True)  # Field name made lowercase.
    phone2 = models.CharField(db_column='Phone2', max_length=15, blank=True, null=True)  # Field name made lowercase.
    aast_email = models.CharField(db_column='AAST_Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email1 = models.CharField(db_column='Email1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email2 = models.CharField(db_column='Email2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    zoom = models.CharField(db_column='Zoom', max_length=50, blank=True, null=True)  # Field name made lowercase.
    internal_external = models.CharField(db_column='Internal-External', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    city = models.IntegerField(db_column='City', blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=50, blank=True, null=True)  # Field name made lowercase.
    jobtitle = models.CharField(db_column='JobTitle', max_length=50, blank=True, null=True)  # Field name made lowercase.
    academicdegree = models.IntegerField(db_column='AcademicDegree', blank=True, null=True)  # Field name made lowercase.
    academicmajor = models.IntegerField(db_column='AcademicMajor', blank=True, null=True)  # Field name made lowercase.
    image = models.TextField(db_column='Image', blank=True, null=True)  # Field name made lowercase.
    cv = models.TextField(db_column='CV', blank=True, null=True)  # Field name made lowercase.
    bio = models.TextField(db_column='Bio', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=45, blank=True, null=True)  # Field name made lowercase.
    paymentdegree = models.IntegerField(db_column='PaymentDegree')  # Field name made lowercase.
    contreply = models.IntegerField(db_column='ContReply', blank=True, null=True)  # Field name made lowercase.
    delvexam = models.IntegerField(db_column='DelvExam', blank=True, null=True)  # Field name made lowercase.
    delvresults = models.IntegerField(db_column='DelvResults', blank=True, null=True)  # Field name made lowercase.
    otherfess = models.IntegerField(db_column='OtherFess', blank=True, null=True)  # Field name made lowercase.
    moodle_user = models.CharField(db_column='Moodle_User', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ms_teams_user = models.CharField(db_column='MS_Teams_User', max_length=50, blank=True, null=True)  # Field name made lowercase.
    totalfees = models.IntegerField(db_column='TotalFees', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblcontacts'
        verbose_name = 'Professor'
        verbose_name_plural = 'Professors Contacts'


class Tblcontracts(models.Model):
    timetableid = models.ForeignKey('Tbltimetable', models.DO_NOTHING, db_column='TimeTableID')  # Field name made lowercase.
    contactsid = models.IntegerField(db_column='ContactsID')  # Field name made lowercase.
    contractsent = models.CharField(db_column='ContractSent', max_length=4, blank=True, null=True)  # Field name made lowercase.
    contractsentdate = models.DateField(db_column='ContractSentDate', blank=True, null=True)  # Field name made lowercase.
    contractsid = models.AutoField(db_column='ContractsID', primary_key=True)  # Field name made lowercase. The composite primary key (ContractsID, TimeTableID) found, that is not supported. The first column is selected.
    contractdelivered = models.CharField(db_column='ContractDelivered', max_length=4, blank=True, null=True)  # Field name made lowercase.
    contractdelivereddate = models.DateField(db_column='ContractDeliveredDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblcontracts'
        unique_together = (('contractsid', 'timetableid'),)


class Tblcoursesuggest(models.Model):
    coursesuggestid = models.AutoField(db_column='CourseSuggestID', primary_key=True)  # Field name made lowercase.
    contactsid = models.ForeignKey(Tblcontacts, models.DO_NOTHING, db_column='ContactsID')  # Field name made lowercase.
    coursesuggest = models.DecimalField(db_column='CourseSuggest', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblcoursesuggest'


class Tbleducode(models.Model):
    educode = models.CharField(db_column='EduCode', primary_key=True, max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbleducode'


class Tblevaluation(models.Model):
    eva_id = models.AutoField(db_column='Eva_id', primary_key=True)  # Field name made lowercase.
    timetableid = models.IntegerField(db_column='TimeTableID', blank=True, null=True)  # Field name made lowercase.
    regno = models.IntegerField(db_column='RegNo', blank=True, null=True)  # Field name made lowercase.
    q1 = models.IntegerField(db_column='Q1', blank=True, null=True)  # Field name made lowercase.
    q2 = models.IntegerField(db_column='Q2', blank=True, null=True)
    q3 = models.IntegerField(db_column='Q3', blank=True, null=True)
    q4 = models.IntegerField(db_column='Q4', blank=True, null=True)
    q5 = models.IntegerField(db_column='Q5', blank=True, null=True)
    q6 = models.IntegerField(db_column='Q6', blank=True, null=True)
    q7 = models.IntegerField(db_column='Q7', blank=True, null=True)
    q8 = models.IntegerField(db_column='Q8', blank=True, null=True)
    q9 = models.IntegerField(db_column='Q9', blank=True, null=True)
    notes = models.TextField(db_column='Notes', blank=True, null=True)
    sent = models.CharField(db_column='Sent', max_length=20, blank=True)

    class Meta:
        managed = False
        db_table = 'tblevaluation'


class Tblevaluationold(models.Model):
    evaluationid = models.AutoField(db_column='EvaluationID', primary_key=True)  # Field name made lowercase.
    timetableid = models.IntegerField(db_column='TimetableID', blank=True, null=True)  # Field name made lowercase.
    evacount = models.IntegerField(db_column='EvaCount', blank=True, null=True)  # Field name made lowercase.
    coursegeneral = models.DecimalField(db_column='CourseGeneral', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    doctorcommit = models.DecimalField(db_column='DoctorCommit', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    doctormethod = models.DecimalField(db_column='DoctorMethod', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    timearrange = models.DecimalField(db_column='TimeArrange', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    coursebalance = models.DecimalField(db_column='CourseBalance', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    doctorcommunicate = models.DecimalField(db_column='DoctorCommunicate', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    courseoutline = models.DecimalField(db_column='CourseOutline', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    materials = models.DecimalField(db_column='Materials', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    doctorgeneral = models.DecimalField(db_column='DoctorGeneral', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    docsubjnotes = models.TextField(db_column='DocSubjNotes', blank=True, null=True)  # Field name made lowercase.
    empcommunicate = models.DecimalField(db_column='EmpCommunicate', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    emprespond = models.DecimalField(db_column='EmpRespond', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    empsolve = models.DecimalField(db_column='EmpSolve', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    empnotes = models.TextField(db_column='EmpNotes', blank=True, null=True)  # Field name made lowercase.
    doceva = models.DecimalField(db_column='DocEva', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    docrate = models.CharField(db_column='DocRate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    subjeva = models.DecimalField(db_column='SubjEva', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    subjrate = models.CharField(db_column='SubjRate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    empeva = models.DecimalField(db_column='EmpEva', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    emprate = models.CharField(db_column='EmpRate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    contract = models.CharField(db_column='Contract', max_length=200, blank=True, null=True)  # Field name made lowercase.
    exams = models.CharField(db_column='Exams', max_length=200, blank=True, null=True)  # Field name made lowercase.
    results = models.CharField(db_column='Results', max_length=200, blank=True, null=True)  # Field name made lowercase.
    doctorattend = models.CharField(db_column='DoctorAttend', max_length=200, blank=True, null=True)  # Field name made lowercase.
    normalresult = models.CharField(db_column='NormalResult', max_length=200, blank=True, null=True)  # Field name made lowercase.
    evasent = models.CharField(db_column='EvaSent', max_length=5, blank=True, null=True)  # Field name made lowercase.
    employeeentry = models.CharField(db_column='EmployeeEntry', max_length=200, blank=True, null=True)  # Field name made lowercase.
    employee = models.CharField(db_column='Employee', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblevaluationold'


class Tblexams(models.Model):
    examsid = models.AutoField(db_column='ExamsID', primary_key=True)  # Field name made lowercase. The composite primary key (ExamsID, TimeTableID) found, that is not supported. The first column is selected.
    timetableid = models.ForeignKey('Tbltimetable', models.DO_NOTHING, db_column='TimeTableID')  # Field name made lowercase.
    contactsid = models.IntegerField(db_column='ContactsID')  # Field name made lowercase.
    examdelivered = models.IntegerField(db_column='ExamDelivered', blank=True, null=True)  # Field name made lowercase.
    examdelivereddate = models.DateField(db_column='ExamDeliveredDate', blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblexams'
        unique_together = (('examsid', 'timetableid'),)


class Tblgrouplist(models.Model):
    grouplistid = models.AutoField(db_column='GroupListID', primary_key=True)  # Field name made lowercase.
    groupname = models.CharField(db_column='GroupName', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblgrouplist'


class Tblmajorlist(models.Model):
    majorlistid = models.AutoField(db_column='MajorListID', primary_key=True)  # Field name made lowercase.
    majorname = models.CharField(db_column='MajorName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblmajorlist'


class Tblpaymentdegreelist(models.Model):
    paymentdegreeid = models.AutoField(db_column='PaymentDegreeID', primary_key=True)  # Field name made lowercase.
    paymentdegree = models.CharField(db_column='PaymentDegree', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblpaymentdegreelist'


class Tblperioudlist(models.Model):
    perioudlistid = models.AutoField(db_column='PerioudListID', primary_key=True)  # Field name made lowercase.
    perioud = models.CharField(db_column='Perioud', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblperioudlist'


class Tblprogramlist(models.Model):
    programlistid = models.AutoField(db_column='ProgramListID', primary_key=True)  # Field name made lowercase.
    programname = models.CharField(db_column='ProgramName', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblprogramlist'


class TblresultMissing(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    registerno = models.IntegerField(db_column='RegisterNo', blank=True, null=True)  # Field name made lowercase.
    course_id = models.IntegerField(db_column='Course_ID', blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblresult_missing'


class Tblresults(models.Model):
    resultid = models.AutoField(db_column='ResultID', primary_key=True)  # Field name made lowercase.
    timetableid = models.IntegerField(db_column='TimeTableID', blank=True, null=True)  # Field name made lowercase.
    regno = models.IntegerField(db_column='RegNo', blank=True, null=True)  # Field name made lowercase.
    attendance = models.IntegerField(db_column='Attendance', blank=True, null=True)  # Field name made lowercase.
    project = models.IntegerField(db_column='Project', blank=True, null=True)  # Field name made lowercase.
    midterm = models.IntegerField(db_column='Midterm', blank=True, null=True)  # Field name made lowercase.
    final = models.IntegerField(db_column='Final', blank=True, null=True)  # Field name made lowercase.
    total = models.IntegerField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    letter = models.CharField(db_column='Letter', max_length=5, blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblresults'


class Tblroomlist(models.Model):
    roomlistid = models.AutoField(db_column='RoomListID', primary_key=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    building = models.CharField(db_column='Building', max_length=30, blank=True, null=True)  # Field name made lowercase.
    location = models.DecimalField(db_column='Location', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblroomlist'


class Tblsemesterlist(models.Model):
    semesterlistid = models.AutoField(db_column='SemesterListID', primary_key=True)  # Field name made lowercase.
    semestername = models.CharField(db_column='SemesterName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblsemesterlist'


class Tblsponsorlist(models.Model):
    sponsorlistid = models.AutoField(db_column='SponsorListID', primary_key=True)  # Field name made lowercase.
    sponsorname = models.CharField(db_column='SponsorName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblsponsorlist'


class Tblsubjectslist(models.Model):
    subjectid = models.AutoField(db_column='SubjectID', primary_key=True)  # Field name made lowercase.
    subjectcode = models.CharField(db_column='SubjectCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    subjectname = models.CharField(db_column='SubjectName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    program = models.CharField(db_column='Program', max_length=50, blank=True, null=True)  # Field name made lowercase.
    major_name = models.CharField(db_column='Major_Name', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblsubjectslist'


class Tbltimetable(models.Model):
    timetableid = models.AutoField(db_column='TimeTableID', primary_key=True)  # Field name made lowercase.
    contactsid = models.ForeignKey(Tblcontacts, models.DO_NOTHING, db_column='ContactsID')  # Field name made lowercase.
    coursename = models.DecimalField(db_column='CourseName', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    program = models.DecimalField(db_column='Program', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    term = models.CharField(db_column='Term', max_length=10, blank=True, null=True)  # Field name made lowercase.
    educode = models.CharField(db_column='EduCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    location = models.DecimalField(db_column='Location', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    category = models.DecimalField(db_column='Category', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    major = models.DecimalField(db_column='Major', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    group = models.DecimalField(db_column='Group', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    day = models.CharField(db_column='Day', max_length=10, blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    week = models.DecimalField(db_column='Week', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    timefrom = models.TimeField(db_column='TimeFrom', blank=True, null=True)  # Field name made lowercase.
    timeto = models.TimeField(db_column='TimeTo', blank=True, null=True)  # Field name made lowercase.
    room = models.DecimalField(db_column='Room', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    semester = models.DecimalField(db_column='Semester', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    quarter = models.CharField(db_column='Quarter', max_length=4, blank=True, null=True)  # Field name made lowercase.
    studytype = models.CharField(max_length=200, blank=True, null=True)
    finalexamdate = models.DateField(db_column='FinalExamDate', blank=True, null=True)  # Field name made lowercase.
    courseend = models.CharField(db_column='CourseEnd', max_length=4, blank=True, null=True)  # Field name made lowercase.
    educationnotes = models.CharField(db_column='EducationNotes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    timetabletype = models.CharField(db_column='TimetableType', max_length=6)  # Field name made lowercase.
    proffconfirm = models.CharField(db_column='ProffConfirm', max_length=7, blank=True, null=True)  # Field name made lowercase.
    studentconfirm = models.CharField(db_column='StudentConfirm', max_length=7, blank=True, null=True)  # Field name made lowercase.
    pgattend = models.CharField(db_column='PGAttend', max_length=7, blank=True, null=True)  # Field name made lowercase.
    paymentnotes = models.CharField(db_column='PaymentNotes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    moodleupload = models.CharField(db_column='MoodleUpload', max_length=20, blank=True, null=True)  # Field name made lowercase.
    teamupload = models.CharField(db_column='TeamUpload', max_length=20, blank=True, null=True)  # Field name made lowercase.
    evaluationdate = models.DateField(db_column='EvaluationDate', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    paysemester = models.CharField(db_column='PaySemester', max_length=30, blank=True, null=True)  # Field name made lowercase.
    payquarter = models.CharField(db_column='PayQuarter', max_length=10, blank=True, null=True)  # Field name made lowercase.
    paylocation = models.CharField(db_column='PayLocation', max_length=50, blank=True, null=True)  # Field name made lowercase.
    paystatus = models.CharField(db_column='PayStatus', max_length=20, blank=True, null=True)  # Field name made lowercase.
    paydate = models.DateField(db_column='PayDate', blank=True, null=True)  # Field name made lowercase.
    teamgroupid = models.CharField(db_column='TeamGroupID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    teaching_fees = models.FloatField(blank=True, null=True)
    transfer_fees = models.FloatField(blank=True, null=True)
    accommodation_fees = models.FloatField(blank=True, null=True)
    travel_fees = models.FloatField(blank=True, null=True)
    hall_fees = models.FloatField(blank=True, null=True)
    lec_durations = models.TimeField(db_column='Lec_Durations', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbltimetable'


class Tbltimetabletypelist(models.Model):
    idtimetabletype = models.AutoField(db_column='IDTimetableType', primary_key=True)  # Field name made lowercase.
    timetabletype = models.CharField(db_column='TimetableType', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbltimetabletypelist'


class Tblweeklist(models.Model):
    weeklistid = models.AutoField(db_column='WeekListID', primary_key=True)  # Field name made lowercase.
    weekname = models.CharField(db_column='WeekName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblweeklist'


class Tbusers(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    username = models.TextField(blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbusers'
