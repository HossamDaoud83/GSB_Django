# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Aastcomppayment(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    regno = models.IntegerField(db_column='RegNo', blank=True, null=True)  # Field name made lowercase.
    hours = models.IntegerField(db_column='Hours', blank=True, null=True)  # Field name made lowercase.
    egp = models.IntegerField(db_column='EGP', blank=True, null=True)  # Field name made lowercase.
    usd = models.IntegerField(db_column='USD', blank=True, null=True)  # Field name made lowercase.
    discount = models.CharField(db_column='Discount', max_length=800, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aastcomppayment'


class Aastcompregister(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    regno = models.IntegerField(db_column='RegNo', blank=True, null=True)  # Field name made lowercase.
    hours = models.IntegerField(db_column='Hours', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aastcompregister'


class Aastpayment(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    regno = models.IntegerField(db_column='RegNo', blank=True, null=True)  # Field name made lowercase.
    hours = models.IntegerField(db_column='Hours', blank=True, null=True)  # Field name made lowercase.
    egp = models.IntegerField(db_column='EGP', blank=True, null=True)  # Field name made lowercase.
    usd = models.IntegerField(db_column='USD', blank=True, null=True)  # Field name made lowercase.
    discount = models.CharField(db_column='Discount', max_length=200, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=200, blank=True, null=True)  # Field name made lowercase.
    payment = models.CharField(db_column='Payment', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aastpayment'


class Aastprereg(models.Model):
    regno = models.IntegerField(db_column='RegNo', primary_key=True)  # Field name made lowercase.
    program = models.CharField(max_length=250, blank=True, null=True)
    status = models.CharField(db_column='Status', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aastprereg'


class Aastreadyregister(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    regno = models.IntegerField(db_column='RegNo', blank=True, null=True)  # Field name made lowercase.
    hours = models.IntegerField(db_column='Hours', blank=True, null=True)  # Field name made lowercase.
    egp = models.IntegerField(db_column='EGP', blank=True, null=True)  # Field name made lowercase.
    usd = models.IntegerField(db_column='USD', blank=True, null=True)  # Field name made lowercase.
    discount = models.CharField(db_column='Discount', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aastreadyregister'


class Aastregister(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    regno = models.IntegerField(db_column='RegNo', blank=True, null=True)  # Field name made lowercase.
    hours = models.IntegerField(db_column='Hours', blank=True, null=True)  # Field name made lowercase.
    egp = models.IntegerField(db_column='EGP', blank=True, null=True)  # Field name made lowercase.
    usd = models.IntegerField(db_column='USD', blank=True, null=True)  # Field name made lowercase.
    discount = models.CharField(db_column='Discount', max_length=30, blank=True, null=True)  # Field name made lowercase.
    registration = models.CharField(db_column='Registration', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aastregister'


class AastunregisterTbl(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    regno = models.IntegerField(db_column='RegNo', unique=True, blank=True, null=True)  # Field name made lowercase.
    load = models.IntegerField(db_column='Load', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aastunregister_tbl'


class Aastwithdraw(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    regno = models.IntegerField(db_column='RegNo', unique=True, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aastwithdraw'


class Additiongrouplist(models.Model):
    additiongroupid = models.AutoField(db_column='AdditionGroupID', primary_key=True)  # Field name made lowercase.
    additiongroup = models.CharField(db_column='AdditionGroup', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'additiongrouplist'


class AttendTbl(models.Model):
    idlecture = models.AutoField(db_column='IDLecture', primary_key=True)  # Field name made lowercase.
    doctor = models.CharField(db_column='Doctor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coursename = models.CharField(db_column='CourseName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lect1 = models.IntegerField(db_column='Lect1', blank=True, null=True)  # Field name made lowercase.
    lect2 = models.IntegerField(db_column='Lect2', blank=True, null=True)  # Field name made lowercase.
    lect3 = models.IntegerField(db_column='Lect3', blank=True, null=True)  # Field name made lowercase.
    lect4 = models.IntegerField(db_column='Lect4', blank=True, null=True)  # Field name made lowercase.
    lect5 = models.IntegerField(db_column='Lect5', blank=True, null=True)  # Field name made lowercase.
    lect6 = models.IntegerField(db_column='Lect6', blank=True, null=True)  # Field name made lowercase.
    lect7 = models.IntegerField(db_column='Lect7', blank=True, null=True)  # Field name made lowercase.
    lect8 = models.IntegerField(db_column='Lect8', blank=True, null=True)  # Field name made lowercase.
    lect9 = models.IntegerField(db_column='Lect9', blank=True, null=True)  # Field name made lowercase.
    lect10 = models.IntegerField(db_column='Lect10', blank=True, null=True)  # Field name made lowercase.
    attendstatus = models.CharField(db_column='AttendStatus', max_length=255, blank=True, null=True)  # Field name made lowercase.
    attendnote = models.CharField(db_column='AttendNote', max_length=255, blank=True, null=True)  # Field name made lowercase.
    studentid = models.IntegerField(db_column='StudentID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'attend_tbl'


class Categorylist(models.Model):
    idcategory = models.AutoField(db_column='IDCategory', primary_key=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'categorylist'


class Collegelist(models.Model):
    collegeid = models.AutoField(db_column='CollegeID', primary_key=True)  # Field name made lowercase.
    college = models.CharField(db_column='College', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'collegelist'


class Companylist(models.Model):
    companyid = models.AutoField(db_column='CompanyID', primary_key=True)  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'companylist'


class Discountlist(models.Model):
    discountid = models.AutoField(db_column='DiscountID', primary_key=True)  # Field name made lowercase.
    discount = models.CharField(db_column='Discount', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'discountlist'


class Discsectorlist(models.Model):
    discsectorid = models.AutoField(db_column='DiscSectorID', primary_key=True)  # Field name made lowercase.
    discsector = models.CharField(db_column='DiscSector', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'discsectorlist'


class GraduationTbl(models.Model):
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    regno = models.FloatField(db_column='RegNo', primary_key=True)  # Field name made lowercase.
    pincode = models.IntegerField(db_column='PinCode', blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=255, blank=True, null=True)  # Field name made lowercase.
    major = models.CharField(db_column='Major', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gpa = models.CharField(db_column='GPA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    semester = models.CharField(db_column='Semester', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nationality = models.CharField(db_column='Nationality', max_length=255, blank=True, null=True)  # Field name made lowercase.
    program = models.CharField(db_column='Program', max_length=255, blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=255, blank=True, null=True)  # Field name made lowercase.
    discsector = models.CharField(db_column='DiscSector', max_length=255, blank=True, null=True)  # Field name made lowercase.
    discount = models.CharField(db_column='Discount', max_length=255, blank=True, null=True)  # Field name made lowercase.
    discountrate = models.CharField(db_column='DiscountRate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    job_field = models.CharField(db_column='Job Field', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    studylocation = models.CharField(db_column='StudyLocation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sponsor = models.CharField(db_column='Sponsor', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'graduation_tbl'


class Grouplist(models.Model):
    majorid = models.AutoField(db_column='MajorID', primary_key=True)  # Field name made lowercase.
    group = models.CharField(db_column='Group', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'grouplist'


class Jobfieldlist(models.Model):
    jobfieldid = models.AutoField(db_column='JobFieldID', primary_key=True)  # Field name made lowercase.
    jobfield = models.CharField(db_column='JobField', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'jobfieldlist'


class Majorlist(models.Model):
    majorid = models.AutoField(db_column='MajorID', primary_key=True)  # Field name made lowercase.
    group = models.CharField(db_column='Group', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'majorlist'


class Nationalitylist(models.Model):
    nationalid = models.AutoField(db_column='NationalID', primary_key=True)  # Field name made lowercase.
    nationality = models.CharField(db_column='Nationality', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nationalitylist'


class Professorslist(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'professorslist'


class Programlist(models.Model):
    programid = models.AutoField(db_column='ProgramID', primary_key=True)  # Field name made lowercase.
    programname = models.CharField(db_column='ProgramName', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'programlist'


class Staffevaluation(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    studentname = models.CharField(max_length=200, blank=True, null=True)
    regno = models.IntegerField(db_column='RegNo', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=200, blank=True, null=True)
    employee = models.CharField(db_column='Employee', max_length=200, blank=True, null=True)  # Field name made lowercase.
    q1 = models.IntegerField(db_column='Q1', blank=True, null=True)  # Field name made lowercase.
    q2 = models.IntegerField(db_column='Q2', blank=True, null=True)  # Field name made lowercase.
    q3 = models.IntegerField(db_column='Q3', blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.
    semester = models.CharField(db_column='Semester', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'staffevaluation'


class Studentaffairslist(models.Model):
    employeesid = models.AutoField(db_column='EmployeesID', primary_key=True)  # Field name made lowercase.
    studentaffairs = models.CharField(db_column='StudentAffairs', max_length=255, blank=True, null=True)  # Field name made lowercase.
    moodle_user = models.CharField(db_column='Moodle_User', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    manager = models.CharField(db_column='Manager', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'studentaffairslist'


class StudentsTbl(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    engname = models.CharField(db_column='EngName', max_length=255)  # Field name made lowercase.
    arabicname = models.CharField(db_column='ArabicName', max_length=255)  # Field name made lowercase.
    regno = models.IntegerField(db_column='RegNo', blank=True, null=True)  # Field name made lowercase.
    pincode = models.CharField(db_column='PinCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    initialreg = models.CharField(db_column='InitialReg', max_length=255, blank=True, null=True)  # Field name made lowercase.
    program = models.ForeignKey(Programlist, models.DO_NOTHING, db_column='Program')  # Field name made lowercase.
    prelevel = models.CharField(db_column='PreLevel', max_length=255, blank=True, null=True)  # Field name made lowercase.
    term = models.CharField(db_column='Term', max_length=255)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=255)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=255)  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=255, blank=True, null=True)  # Field name made lowercase.
    onlineadmission = models.CharField(db_column='OnlineAdmission', max_length=255, blank=True, null=True)  # Field name made lowercase.
    onlinenote = models.TextField(db_column='OnlineNote', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255)  # Field name made lowercase.
    ms_team_mail = models.CharField(db_column='MS_Team_Mail', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ms_team_pass = models.CharField(db_column='MS_Team_Pass', max_length=20, blank=True, null=True)  # Field name made lowercase.
    interview = models.DateTimeField(db_column='Interview', blank=True, null=True)  # Field name made lowercase.
    compresult = models.CharField(db_column='CompResult', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gpa = models.CharField(db_column='GPA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    discregister = models.CharField(db_column='DiscRegister', max_length=255, blank=True, null=True)  # Field name made lowercase.
    graduatesem = models.CharField(db_column='GraduateSem', max_length=255, blank=True, null=True)  # Field name made lowercase.
    studylocation = models.CharField(db_column='StudyLocation', max_length=255)  # Field name made lowercase.
    sponsor = models.CharField(db_column='Sponsor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coordinator = models.CharField(db_column='Coordinator', max_length=255, blank=True, null=True)  # Field name made lowercase.
    emergencyphone = models.CharField(db_column='EmergencyPhone', max_length=255, blank=True, null=True)  # Field name made lowercase.
    marketing = models.CharField(db_column='Marketing', max_length=255, blank=True, null=True)  # Field name made lowercase.
    intakesemester = models.CharField(db_column='IntakeSemester', max_length=255, blank=True, null=True)  # Field name made lowercase.
    amatresult = models.CharField(db_column='AMATResult', max_length=255, blank=True, null=True)  # Field name made lowercase.
    toeflresult = models.CharField(db_column='TOEFLResult', max_length=255, blank=True, null=True)  # Field name made lowercase.
    regdate = models.CharField(db_column='RegDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    regtime = models.CharField(db_column='RegTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    college = models.ForeignKey(Collegelist, models.DO_NOTHING, db_column='College', blank=True, null=True)  # Field name made lowercase.
    discount = models.ForeignKey(Discountlist, models.DO_NOTHING, db_column='Discount', blank=True, null=True)  # Field name made lowercase.
    discsector = models.ForeignKey(Discsectorlist, models.DO_NOTHING, db_column='DiscSector', blank=True, null=True)  # Field name made lowercase.
    jobfield = models.ForeignKey(Jobfieldlist, models.DO_NOTHING, db_column='JobField', blank=True, null=True)  # Field name made lowercase.
    nationality = models.ForeignKey(Nationalitylist, models.DO_NOTHING, db_column='Nationality', blank=True, null=True)  # Field name made lowercase.
    employee = models.ForeignKey(Studentaffairslist, models.DO_NOTHING, db_column='Employee')  # Field name made lowercase.
    wd_we = models.CharField(db_column='WD_WE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    additiongroup = models.ForeignKey(Additiongrouplist, models.DO_NOTHING, db_column='AdditionGroup', blank=True, null=True)  # Field name made lowercase.
    gdmtomba = models.IntegerField(db_column='GdmToMba', blank=True, null=True)  # Field name made lowercase.
    claim = models.CharField(db_column='Claim', max_length=5, blank=True, null=True)  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=255)  # Field name made lowercase.
    sms = models.IntegerField(db_column='SMS', blank=True, null=True)  # Field name made lowercase.
    studylevel = models.IntegerField(db_column='StudyLevel', blank=True, null=True)  # Field name made lowercase.
    cardfregno = models.IntegerField(db_column='CardfRegNo', blank=True, null=True)  # Field name made lowercase.
    thesisresult = models.CharField(db_column='ThesisResult', max_length=255, blank=True, null=True)  # Field name made lowercase.
    category = models.ForeignKey(Categorylist, models.DO_NOTHING, db_column='Category')  # Field name made lowercase.
    regnotes = models.TextField(db_column='RegNotes', blank=True, null=True)  # Field name made lowercase.
    image = models.CharField(db_column='Image', max_length=255, blank=True, null=True)  # Field name made lowercase.
    major = models.ForeignKey(Majorlist, models.DO_NOTHING, db_column='Major', blank=True, null=True)  # Field name made lowercase.
    majornote = models.CharField(db_column='MajorNote', max_length=50, blank=True, null=True)  # Field name made lowercase.
    group = models.ForeignKey(Grouplist, models.DO_NOTHING, db_column='Group', blank=True, null=True)  # Field name made lowercase.
    regtype = models.CharField(db_column='RegType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    educode = models.CharField(db_column='Educode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    onlinenumber = models.CharField(db_column='OnlineNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    onlinepassword = models.CharField(db_column='OnlinePassword', max_length=255, blank=True, null=True)  # Field name made lowercase.
    registrationpaid = models.IntegerField(db_column='RegistrationPaid', blank=True, null=True)  # Field name made lowercase.
    toeflexamfees = models.IntegerField(db_column='TOEFLExamFees', blank=True, null=True)  # Field name made lowercase.
    amatexamfees = models.IntegerField(db_column='AMATExamFees', blank=True, null=True)  # Field name made lowercase.
    toeflprepfees = models.IntegerField(db_column='TOEFLPrepFees', blank=True, null=True)  # Field name made lowercase.
    amatprepfees = models.IntegerField(db_column='AMATPrepFees', blank=True, null=True)  # Field name made lowercase.
    discsuggest = models.CharField(db_column='DiscSuggest', max_length=255, blank=True, null=True)  # Field name made lowercase.
    discreason = models.CharField(db_column='DiscReason', max_length=255, blank=True, null=True)  # Field name made lowercase.
    position = models.CharField(db_column='Position', max_length=255, blank=True, null=True)  # Field name made lowercase.
    picgraduate = models.IntegerField(db_column='PicGraduate', blank=True, null=True)  # Field name made lowercase.
    branch = models.CharField(db_column='Branch', max_length=20, blank=True, null=True)  # Field name made lowercase.
    budget_cat = models.CharField(db_column='Budget_Cat', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mary_fname = models.CharField(db_column='Mary_FName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    mary_lname = models.CharField(db_column='Mary_LName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    usd = models.CharField(db_column='USD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    discountrate = models.CharField(db_column='DiscountRate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pay_egp = models.IntegerField(db_column='Pay_EGP', blank=True, null=True)  # Field name made lowercase.
    pay_usd = models.IntegerField(db_column='Pay_USD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'students_tbl'


class Tblassigntoreq(models.Model):
    idassign = models.AutoField(db_column='IDAssign', primary_key=True)  # Field name made lowercase.
    assignto = models.CharField(db_column='AssignTo', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblassigntoreq'


class Tblcategoryreqlist(models.Model):
    idcatreq = models.AutoField(db_column='IDCatReq', primary_key=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblcategoryreqlist'


class Tblcitylist(models.Model):
    citylistid = models.AutoField(db_column='CityListID', primary_key=True)  # Field name made lowercase.
    cityname = models.CharField(db_column='CityName', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblcitylist'


class Tblcompexamanswers(models.Model):
    regno = models.IntegerField(db_column='RegNo', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=254, blank=True, null=True)  # Field name made lowercase.
    started = models.CharField(db_column='Started', max_length=254, blank=True, null=True)  # Field name made lowercase.
    completed = models.CharField(db_column='Completed', max_length=254, blank=True, null=True)  # Field name made lowercase.
    time_taken = models.CharField(db_column='Time_taken', max_length=254, blank=True, null=True)  # Field name made lowercase.
    q1 = models.TextField(db_column='Q1', blank=True, null=True)  # Field name made lowercase.
    q2 = models.TextField(db_column='Q2', blank=True, null=True)  # Field name made lowercase.
    q3 = models.TextField(db_column='Q3', blank=True, null=True)  # Field name made lowercase.
    q4 = models.TextField(db_column='Q4', blank=True, null=True)  # Field name made lowercase.
    q5 = models.TextField(db_column='Q5', blank=True, null=True)  # Field name made lowercase.
    q6 = models.TextField(db_column='Q6', blank=True, null=True)  # Field name made lowercase.
    q7 = models.TextField(db_column='Q7', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblcompexamanswers'


class Tbldbapublish(models.Model):
    publishid = models.AutoField(db_column='PublishID', primary_key=True)  # Field name made lowercase.
    studentid = models.ForeignKey(StudentsTbl, models.DO_NOTHING, db_column='StudentID', blank=True, null=True)  # Field name made lowercase.
    publishname = models.CharField(db_column='PublishName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    publishlocation = models.CharField(db_column='PublishLocation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    publishdata = models.CharField(db_column='PublishData', max_length=255, blank=True, null=True)  # Field name made lowercase.
    publishdate = models.DateTimeField(db_column='PublishDate', blank=True, null=True)  # Field name made lowercase.
    publishstatus = models.IntegerField(db_column='PublishStatus', blank=True, null=True)  # Field name made lowercase.
    publishlink = models.TextField(db_column='PublishLink', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbldbapublish'


class Tbldbathesis(models.Model):
    thesisid = models.AutoField(db_column='ThesisID', primary_key=True)  # Field name made lowercase.
    studentid = models.ForeignKey(StudentsTbl, models.DO_NOTHING, db_column='StudentID', blank=True, null=True)  # Field name made lowercase.
    thesisname = models.CharField(db_column='ThesisName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    supervisor1 = models.IntegerField(db_column='Supervisor1', blank=True, null=True)  # Field name made lowercase.
    supervisor2 = models.IntegerField(db_column='Supervisor2', blank=True, null=True)  # Field name made lowercase.
    supervisor3 = models.IntegerField(db_column='Supervisor3', blank=True, null=True)  # Field name made lowercase.
    supervisor4 = models.IntegerField(db_column='Supervisor4', blank=True, null=True)  # Field name made lowercase.
    internalaudit = models.IntegerField(db_column='InternalAudit', blank=True, null=True)  # Field name made lowercase.
    externalaudit = models.IntegerField(db_column='ExternalAudit', blank=True, null=True)  # Field name made lowercase.
    deliverydate = models.DateTimeField(db_column='DeliveryDate', blank=True, null=True)  # Field name made lowercase.
    discusdate = models.DateTimeField(db_column='DiscusDate', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    thesislink = models.TextField(db_column='ThesisLink', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbldbathesis'


class Tbldeanreg(models.Model):
    iddean = models.AutoField(db_column='IDDean', primary_key=True)  # Field name made lowercase.
    idrequest = models.ForeignKey('Tblstudentsreq', models.DO_NOTHING, db_column='IDRequest', blank=True, null=True)  # Field name made lowercase.
    action = models.CharField(db_column='Action', max_length=255, blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.
    approveal = models.CharField(db_column='Approveal', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbldeanreg'


class Tbledunotes(models.Model):
    eduid = models.AutoField(db_column='EduID', primary_key=True)  # Field name made lowercase.
    studentid = models.IntegerField(db_column='StudentID', blank=True, null=True)  # Field name made lowercase.
    educationnote = models.TextField(db_column='EducationNote', blank=True, null=True)  # Field name made lowercase.
    educationsememster = models.ForeignKey('Tblsemesterslist', models.DO_NOTHING, db_column='EducationSememster', blank=True, null=True)  # Field name made lowercase.
    employee = models.CharField(db_column='Employee', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbledunotes'


class Tbledureq(models.Model):
    idedu = models.AutoField(db_column='IDEdu', primary_key=True)  # Field name made lowercase.
    idrequest = models.ForeignKey('Tblstudentsreq', models.DO_NOTHING, db_column='IDRequest', blank=True, null=True)  # Field name made lowercase.
    action = models.CharField(db_column='Action', max_length=255, blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.
    approveal = models.CharField(db_column='Approveal', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbledureq'


class Tblestimated(models.Model):
    estid = models.AutoField(db_column='EstID', primary_key=True)  # Field name made lowercase.
    estimatedname = models.ForeignKey(Categorylist, models.DO_NOTHING, db_column='EstimatedName', blank=True, null=True)  # Field name made lowercase.
    estimatedno = models.IntegerField(db_column='EstimatedNo', blank=True, null=True)  # Field name made lowercase.
    estsemester = models.CharField(db_column='EstSemester', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblestimated'


class Tblfinreq(models.Model):
    idfin = models.AutoField(db_column='IDFin', primary_key=True)  # Field name made lowercase.
    idrequest = models.ForeignKey('Tblstudentsreq', models.DO_NOTHING, db_column='IDRequest', blank=True, null=True)  # Field name made lowercase.
    action = models.CharField(db_column='Action', max_length=255, blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.
    approveal = models.CharField(db_column='Approveal', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblfinreq'


class Tblgpa(models.Model):
    regno = models.IntegerField(db_column='RegNo', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gpa = models.DecimalField(db_column='GPA', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    achievement = models.IntegerField(db_column='Achievement', blank=True, null=True)  # Field name made lowercase.
    program = models.CharField(db_column='Program', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblgpa'


class Tblitreq(models.Model):
    idit = models.AutoField(db_column='IDIT', primary_key=True)  # Field name made lowercase.
    idrequest = models.ForeignKey('Tblstudentsreq', models.DO_NOTHING, db_column='IDRequest', blank=True, null=True)  # Field name made lowercase.
    action = models.CharField(db_column='Action', max_length=255, blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.
    approveal = models.CharField(db_column='Approveal', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblitreq'


class Tblmajor(models.Model):
    id = models.OneToOneField(StudentsTbl, models.DO_NOTHING, db_column='ID', primary_key=True)  # Field name made lowercase.
    major2 = models.IntegerField(db_column='Major2', blank=True, null=True)  # Field name made lowercase.
    week = models.CharField(db_column='Week', max_length=255, blank=True, null=True)  # Field name made lowercase.
    majornote = models.TextField(db_column='MajorNote', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblmajor'


class Tblmissinggradpapers(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    regno = models.IntegerField(db_column='RegNo', unique=True, blank=True, null=True)  # Field name made lowercase.
    disclaimer = models.CharField(db_column='Disclaimer', max_length=10, blank=True, null=True)  # Field name made lowercase.
    gradstatement = models.CharField(db_column='GradStatement', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblmissinggradpapers'


class Tblmissingpapers(models.Model):
    idmissing = models.AutoField(db_column='IDMissing', primary_key=True)  # Field name made lowercase.
    studentid = models.IntegerField(db_column='StudentID', blank=True, null=True)  # Field name made lowercase.
    application = models.IntegerField(db_column='Application', blank=True, null=True)  # Field name made lowercase.
    ba = models.IntegerField(db_column='BA', blank=True, null=True)  # Field name made lowercase.
    batrans = models.IntegerField(db_column='BATrans', blank=True, null=True)  # Field name made lowercase.
    pic = models.IntegerField(db_column='Pic', blank=True, null=True)  # Field name made lowercase.
    idpassport = models.IntegerField(db_column='IDPassport', blank=True, null=True)  # Field name made lowercase.
    bastatusrpt = models.IntegerField(db_column='BAStatusRpt', blank=True, null=True)  # Field name made lowercase.
    diploma = models.IntegerField(db_column='Diploma', blank=True, null=True)  # Field name made lowercase.
    master = models.IntegerField(db_column='Master', blank=True, null=True)  # Field name made lowercase.
    mastertrans = models.IntegerField(db_column='MasterTrans', blank=True, null=True)  # Field name made lowercase.
    embassy = models.IntegerField(db_column='Embassy', blank=True, null=True)  # Field name made lowercase.
    mscstatusrpt = models.IntegerField(db_column='MscStatusRpt', blank=True, null=True)  # Field name made lowercase.
    toefl = models.IntegerField(db_column='TOEFL', blank=True, null=True)  # Field name made lowercase.
    initialaccept = models.IntegerField(db_column='InitialAccept', blank=True, null=True)  # Field name made lowercase.
    completed = models.IntegerField(db_column='Completed', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblmissingpapers'


class Tblpayment(models.Model):
    studentid = models.IntegerField(db_column='StudentID', blank=True, null=True)  # Field name made lowercase.
    idbill = models.AutoField(db_column='IDBill', primary_key=True)  # Field name made lowercase.
    semester = models.CharField(db_column='Semester', max_length=255)  # Field name made lowercase.
    paymenttype = models.CharField(db_column='PaymentType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    paymentcat = models.IntegerField(db_column='PaymentCat')  # Field name made lowercase.
    paydate = models.DateTimeField(db_column='PayDate', blank=True, null=True)  # Field name made lowercase.
    billnote = models.TextField(db_column='BillNote', blank=True, null=True)  # Field name made lowercase.
    billno = models.IntegerField(db_column='BillNo', blank=True, null=True)  # Field name made lowercase.
    feespound = models.IntegerField(db_column='FeesPound', blank=True, null=True)  # Field name made lowercase.
    feesdollar = models.IntegerField(db_column='FeesDollar', blank=True, null=True)  # Field name made lowercase.
    employee = models.CharField(db_column='Employee', max_length=255, blank=True, null=True)  # Field name made lowercase.
    entrydate = models.DateTimeField(db_column='EntryDate', blank=True, null=True)  # Field name made lowercase.
    register = models.IntegerField(db_column='Register', blank=True, null=True)  # Field name made lowercase.
    aastpaid = models.IntegerField(db_column='AASTPaid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblpayment'


class Tblpaymentcatlist(models.Model):
    paymentcatid = models.AutoField(db_column='PaymentCatID', primary_key=True)  # Field name made lowercase.
    paymentcat = models.CharField(db_column='PaymentCat', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblpaymentcatlist'


class Tblregfollow(models.Model):
    regid = models.AutoField(db_column='RegID', primary_key=True)  # Field name made lowercase.
    studentid = models.ForeignKey(StudentsTbl, models.DO_NOTHING, db_column='StudentID', blank=True, null=True)  # Field name made lowercase.
    regnote = models.TextField(db_column='RegNote', blank=True, null=True)  # Field name made lowercase.
    regstatus = models.ForeignKey('Tblregstatuslist', models.DO_NOTHING, db_column='RegStatus', blank=True, null=True)  # Field name made lowercase.
    update = models.IntegerField(db_column='Update', blank=True, null=True)  # Field name made lowercase.
    employee = models.CharField(db_column='Employee', max_length=255, blank=True, null=True)  # Field name made lowercase.
    notedate = models.DateTimeField(db_column='NoteDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblregfollow'


class Tblregreq(models.Model):
    idreg = models.AutoField(db_column='IDReg', primary_key=True)  # Field name made lowercase.
    idrequest = models.ForeignKey('Tblstudentsreq', models.DO_NOTHING, db_column='IDRequest', blank=True, null=True)  # Field name made lowercase.
    action = models.CharField(db_column='Action', max_length=255, blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.
    approveal = models.CharField(db_column='Approveal', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblregreq'


class Tblregstatuslist(models.Model):
    regstatusid = models.AutoField(db_column='RegStatusID', primary_key=True)  # Field name made lowercase.
    regstatus = models.CharField(db_column='RegStatus', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblregstatuslist'


class Tblsemesterslist(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    semester = models.CharField(db_column='Semester', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblsemesterslist'


class Tblservicespayment(models.Model):
    idserv = models.AutoField(db_column='IDServ', primary_key=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    paymenttype = models.CharField(db_column='PaymentType', max_length=255)  # Field name made lowercase.
    fees = models.IntegerField(db_column='Fees')  # Field name made lowercase.
    feestxt = models.CharField(db_column='FeesTxt', max_length=255)  # Field name made lowercase.
    currancy = models.CharField(db_column='Currancy', max_length=255)  # Field name made lowercase.
    entrydate = models.DateTimeField(db_column='EntryDate', blank=True, null=True)  # Field name made lowercase.
    paid = models.IntegerField(db_column='Paid', blank=True, null=True)  # Field name made lowercase.
    employeesign = models.CharField(db_column='EmployeeSign', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblservicespayment'


class Tblsponsorlist(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sponsor = models.CharField(db_column='Sponsor', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblsponsorlist'


class Tblstatuslist(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    statuslist = models.CharField(db_column='StatusList', max_length=255, blank=True, null=True)  # Field name made lowercase.
    policy = models.CharField(db_column='Policy', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblstatuslist'


class Tblstudentsreq(models.Model):
    idrequest = models.AutoField(db_column='IDRequest', primary_key=True)  # Field name made lowercase.
    id = models.ForeignKey(StudentsTbl, models.DO_NOTHING, db_column='ID', blank=True, null=True)  # Field name made lowercase.
    term = models.CharField(db_column='Term', max_length=255)  # Field name made lowercase.
    semester = models.CharField(db_column='Semester', max_length=255)  # Field name made lowercase.
    requestkind = models.ForeignKey(Tblcategoryreqlist, models.DO_NOTHING, db_column='RequestKind')  # Field name made lowercase.
    description = models.TextField(db_column='Description')  # Field name made lowercase.
    entrydate = models.DateTimeField(db_column='EntryDate')  # Field name made lowercase.
    assignto = models.TextField(db_column='AssignTo', blank=True, null=True)  # Field name made lowercase.
    assignto0 = models.TextField(db_column='AssignTo0', blank=True, null=True)  # Field name made lowercase.
    assigncomment = models.TextField(db_column='AssignComment', blank=True, null=True)  # Field name made lowercase.
    receivedate = models.DateTimeField(db_column='ReceiveDate', blank=True, null=True)  # Field name made lowercase.
    attachment = models.TextField(db_column='Attachment', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=255)  # Field name made lowercase.
    statuscomment = models.TextField(db_column='StatusComment', blank=True, null=True)  # Field name made lowercase.
    studentcall = models.IntegerField(db_column='StudentCall', blank=True, null=True)  # Field name made lowercase.
    employeesign = models.CharField(db_column='EmployeeSign', max_length=255, blank=True, null=True)  # Field name made lowercase.
    priority = models.CharField(db_column='Priority', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblstudentsreq'


class Tblsubjectslist(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    subjectname = models.CharField(db_column='SubjectName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    subjectcode = models.CharField(db_column='SubjectCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    program = models.ForeignKey(Programlist, models.DO_NOTHING, db_column='Program', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblsubjectslist'


class Tblsubjectsregister(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    idstudent = models.IntegerField(db_column='IDStudent', blank=True, null=True)  # Field name made lowercase.
    subjectname = models.IntegerField(db_column='SubjectName', blank=True, null=True)  # Field name made lowercase.
    doctorname = models.IntegerField(db_column='DoctorName', blank=True, null=True)  # Field name made lowercase.
    semester = models.CharField(db_column='Semester', max_length=255, blank=True, null=True)  # Field name made lowercase.
    quarter = models.IntegerField(db_column='Quarter', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblsubjectsregister'


class Tblsysgroup(models.Model):
    sysid = models.AutoField(db_column='SysID', primary_key=True)  # Field name made lowercase.
    studentid = models.IntegerField(db_column='StudentID', blank=True, null=True)  # Field name made lowercase.
    sysgroup = models.CharField(db_column='SysGroup', max_length=255, blank=True, null=True)  # Field name made lowercase.
    semester = models.IntegerField(db_column='Semester', blank=True, null=True)  # Field name made lowercase.
    sysnote = models.TextField(db_column='SysNote', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblsysgroup'


class Tblviceedureq(models.Model):
    idviceedu = models.AutoField(db_column='IDViceEdu', primary_key=True)  # Field name made lowercase.
    idrequest = models.ForeignKey(Tblstudentsreq, models.DO_NOTHING, db_column='IDRequest', blank=True, null=True)  # Field name made lowercase.
    action = models.CharField(db_column='Action', max_length=255, blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.
    approveal = models.CharField(db_column='Approveal', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblviceedureq'


class Tblviceregreq(models.Model):
    idvicest = models.AutoField(db_column='IDViceSt', primary_key=True)  # Field name made lowercase.
    idrequest = models.ForeignKey(Tblstudentsreq, models.DO_NOTHING, db_column='IDRequest', blank=True, null=True)  # Field name made lowercase.
    action = models.CharField(db_column='Action', max_length=255, blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.
    approveal = models.CharField(db_column='Approveal', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblviceregreq'


class Tblworkinfo(models.Model):
    id = models.OneToOneField(StudentsTbl, models.DO_NOTHING, db_column='ID', primary_key=True)  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=255, blank=True, null=True)  # Field name made lowercase.
    position = models.CharField(db_column='Position', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblworkinfo'


class WithdrawTbl(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    regno = models.CharField(db_column='RegNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pincode = models.CharField(db_column='PinCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    semester = models.CharField(db_column='Semester', max_length=255, blank=True, null=True)  # Field name made lowercase.
    program = models.CharField(db_column='Program', max_length=255, blank=True, null=True)  # Field name made lowercase.
    introductory = models.CharField(db_column='Introductory', max_length=255, blank=True, null=True)  # Field name made lowercase.
    term = models.CharField(db_column='Term', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pay_reg = models.CharField(db_column='Pay+Reg', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    payonly = models.CharField(db_column='PayOnly', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nonpay = models.CharField(db_column='NonPay', max_length=255, blank=True, null=True)  # Field name made lowercase.
    major = models.CharField(db_column='Major', max_length=255, blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=255, blank=True, null=True)  # Field name made lowercase.
    group = models.CharField(db_column='Group', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wd_we = models.CharField(db_column='WD/WE', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    company = models.CharField(db_column='Company', max_length=255, blank=True, null=True)  # Field name made lowercase.
    job_field = models.CharField(db_column='Job Field', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'withdraw_tbl'
