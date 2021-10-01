# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

'''
class CoadCorpApplicant(models.Model):
    applicant_code = models.CharField(max_length=-1, blank=True, null=True)
    applicant_name = models.CharField(max_length=-1, blank=True, null=True)
    appl_eng_name = models.CharField(max_length=-1, blank=True, null=True)
    corpor_no = models.CharField(max_length=-1, blank=True, null=True)
    user_no = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coad_corp_applicant'


class LstdLegalstatusCode(models.Model):
    leg_status_code = models.CharField(max_length=-1, blank=True, null=True)
    leg_status_name = models.CharField(max_length=-1, blank=True, null=True)
    leg_status_name_eng = models.CharField(max_length=-1, blank=True, null=True)
    leg_status_exp = models.CharField(max_length=-1, blank=True, null=True)
    leg_status_exp_eng = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lstd_legalstatus_code'


class LstdLegalstatusEvent(models.Model):
    appl_no = models.CharField(max_length=-1, blank=True, null=True)
    serial_no = models.IntegerField(blank=True, null=True)
    event_serial_no = models.IntegerField(blank=True, null=True)
    event_code = models.CharField(max_length=-1, blank=True, null=True)
    event_name = models.CharField(max_length=-1, blank=True, null=True)
    event_date = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lstd_legalstatus_event'


class LstdLegalstatusHistory(models.Model):
    appl_no = models.CharField(max_length=-1, blank=True, null=True)
    serial_no = models.IntegerField(blank=True, null=True)
    leg_status_code = models.CharField(max_length=-1, blank=True, null=True)
    leg_status_name = models.CharField(max_length=-1, blank=True, null=True)
    leg_status_date = models.CharField(max_length=-1, blank=True, null=True)
    leg_status_eng = models.CharField(max_length=-1, blank=True, null=True)
    leg_status_exp = models.CharField(max_length=-1, blank=True, null=True)
    leg_status_exp_eng = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lstd_legalstatus_history'


class NddiApplDueDate(models.Model):
    appl_no = models.CharField(max_length=-1, blank=True, null=True)
    serial_no = models.IntegerField(blank=True, null=True)
    due_cause_no = models.CharField(max_length=-1, blank=True, null=True)
    send_due_date = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nddi_appl_due_date'


class NddiRgstDueDate(models.Model):
    reg_no = models.CharField(max_length=-1, blank=True, null=True)
    send_no = models.CharField(max_length=-1, blank=True, null=True)
    send_date = models.CharField(max_length=-1, blank=True, null=True)
    docu_code = models.CharField(max_length=-1, blank=True, null=True)
    docu_name = models.CharField(max_length=-1, blank=True, null=True)
    send_due_date = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nddi_rgst_due_date'


class NddiTrialDueDate(models.Model):
    trial_no = models.CharField(max_length=-1, blank=True, null=True)
    send_no = models.CharField(max_length=-1, blank=True, null=True)
    send_exp_date = models.CharField(max_length=-1, blank=True, null=True)
    docu_code = models.CharField(max_length=-1, blank=True, null=True)
    docu_name = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nddi_trial_due_date'


class PtrhRightHolderAll(models.Model):
    reg_no = models.CharField(max_length=-1, blank=True, null=True)
    asso_point = models.CharField(max_length=-1, blank=True, null=True)
    rank_no = models.IntegerField(blank=True, null=True)
    reg_sep = models.CharField(max_length=-1, blank=True, null=True)
    right_sep = models.CharField(max_length=-1, blank=True, null=True)
    right_serial_no = models.IntegerField(blank=True, null=True)
    right_person_name = models.CharField(max_length=-1, blank=True, null=True)
    address = models.CharField(max_length=-1, blank=True, null=True)
    country_code = models.CharField(max_length=-1, blank=True, null=True)
    reg_date = models.CharField(max_length=-1, blank=True, null=True)
    right_person_no = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ptrh_right_holder_all'


class PuapAbstract(models.Model):
    appl_no = models.CharField(max_length=-1, blank=True, null=True)
    abstract_point = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'puap_abstract'


class PuapAdministrativeprocess(models.Model):
    appl_no = models.CharField(max_length=-1, blank=True, null=True)
    receipt_send_no = models.CharField(max_length=-1, blank=True, null=True)
    receipt_send_date = models.CharField(max_length=-1, blank=True, null=True)
    docu_name = models.CharField(max_length=-1, blank=True, null=True)
    docu_name_eng = models.CharField(max_length=-1, blank=True, null=True)
    process_state = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'puap_administrativeprocess'


class PuapBibliographic(models.Model):
    appl_no = models.CharField(max_length=-1, blank=True, null=True)
    appl_date = models.CharField(max_length=-1, blank=True, null=True)
    show_no = models.CharField(max_length=-1, blank=True, null=True)
    show_date = models.CharField(max_length=-1, blank=True, null=True)
    reg_no = models.CharField(max_length=-1, blank=True, null=True)
    reg_date = models.CharField(max_length=-1, blank=True, null=True)
    pub_no = models.CharField(max_length=-1, blank=True, null=True)
    pub_date = models.CharField(max_length=-1, blank=True, null=True)
    ori_appl_no = models.CharField(max_length=-1, blank=True, null=True)
    ori_appl_date = models.CharField(max_length=-1, blank=True, null=True)
    translate_send_date = models.CharField(max_length=-1, blank=True, null=True)
    int_appl_no = models.CharField(max_length=-1, blank=True, null=True)
    int_appl_date = models.CharField(max_length=-1, blank=True, null=True)
    int_show_no = models.CharField(max_length=-1, blank=True, null=True)
    int_show_date = models.CharField(max_length=-1, blank=True, null=True)
    invent_name = models.CharField(max_length=-1, blank=True, null=True)
    intent_name_eng = models.CharField(max_length=-1, blank=True, null=True)
    final_content = models.CharField(max_length=-1, blank=True, null=True)
    reg_content = models.CharField(max_length=-1, blank=True, null=True)
    is_trial_claim = models.CharField(max_length=-1, blank=True, null=True)
    trial_claim_date = models.CharField(max_length=-1, blank=True, null=True)
    request_no = models.CharField(max_length=-1, blank=True, null=True)
    change_request_no = models.IntegerField(blank=True, null=True)
    appl_division = models.CharField(max_length=-1, blank=True, null=True)
    tech_assign_or_not = models.CharField(max_length=-1, blank=True, null=True)
    tech_show_or_not = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'puap_bibliographic'


class PuapClaim(models.Model):
    appl_no = models.CharField(max_length=-1, blank=True, null=True)
    claim_term = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'puap_claim'


class PuapCpc(models.Model):
    appl_no = models.CharField(max_length=-1, blank=True, null=True)
    pat_class_serial_no = models.IntegerField(blank=True, null=True)
    cpc_code = models.CharField(max_length=-1, blank=True, null=True)
    cpc_change_date = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'puap_cpc'


class PuapDesignatedcountry(models.Model):
    appl_no = models.CharField(max_length=-1, blank=True, null=True)
    design_country_group = models.CharField(max_length=-1, blank=True, null=True)
    design_country_name = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'puap_designatedcountry'


class PuapFamily(models.Model):
    appl_no = models.CharField(max_length=-1, blank=True, null=True)
    family_sep = models.CharField(max_length=-1, blank=True, null=True)
    family_no = models.CharField(max_length=-1, blank=True, null=True)
    family_country_code = models.CharField(max_length=20, blank=True, null=True)
    family_country_name = models.CharField(max_length=-1, blank=True, null=True)
    liter_code = models.CharField(max_length=-1, blank=True, null=True)
    family_appl_no = models.CharField(max_length=-1, blank=True, null=True)
    liter_no = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'puap_family'


class PuapIpc(models.Model):
    appl_no = models.CharField(max_length=-1, blank=True, null=True)
    pat_class_serial_no = models.IntegerField(blank=True, null=True)
    ipc_code = models.CharField(max_length=-1, blank=True, null=True)
    ipc_change_date = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'puap_ipc'


class PuapPriority(models.Model):
    appl_no = models.CharField(max_length=-1, blank=True, null=True)
    priority_serial_no = models.IntegerField(blank=True, null=True)
    priority_appl_no = models.CharField(max_length=-1, blank=True, null=True)
    priority_appl_date = models.CharField(max_length=-1, blank=True, null=True)
    country_code = models.CharField(max_length=20, blank=True, null=True)
    country_name = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'puap_priority'


class PuapPriortechnologydocument(models.Model):
    appl_no = models.CharField(max_length=-1, blank=True, null=True)
    ptd_serial_no = models.IntegerField(blank=True, null=True)
    ptd_no = models.CharField(max_length=-1, blank=True, null=True)
    is_trial_accept = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'puap_priortechnologydocument'


class PuapRelatedperson(models.Model):
    appl_no = models.CharField(max_length=-1, blank=True, null=True)
    relation_code = models.CharField(max_length=20, blank=True, null=True)
    relation_sep = models.CharField(max_length=-1, blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    name_eng = models.CharField(max_length=-1, blank=True, null=True)
    address = models.CharField(max_length=-1, blank=True, null=True)
    country_code = models.CharField(max_length=20, blank=True, null=True)
    internaltiohal_level = models.CharField(max_length=-1, blank=True, null=True)
    address_eng = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'puap_relatedperson'


class PuapRnd(models.Model):
    appl_no = models.CharField(max_length=-1, blank=True, null=True)
    rnd_serial_no = models.IntegerField(blank=True, null=True)
    rnd_project_no = models.CharField(max_length=-1, blank=True, null=True)
    research_part_name = models.CharField(max_length=-1, blank=True, null=True)
    research_business_name = models.CharField(max_length=-1, blank=True, null=True)
    research_project_name = models.CharField(max_length=-1, blank=True, null=True)
    super_part_name = models.CharField(max_length=-1, blank=True, null=True)
    research_period_field = models.CharField(db_column='research_period_', max_length=-1, blank=True, null=True)  # Field renamed because it ended with '_'.
    research_manage_part_name = models.CharField(max_length=-1, blank=True, null=True)
    research_project_distribute = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'puap_rnd'


class PuapSpecification(models.Model):
    appl_no = models.CharField(max_length=-1, blank=True, null=True)
    specification_point = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'puap_specification'


class PupdIntHistoryKr(models.Model):
    appl_no = models.CharField(max_length=-1, blank=True, null=True)
    send_no = models.CharField(max_length=-1, blank=True, null=True)
    send_date = models.CharField(max_length=-1, blank=True, null=True)
    send_docu_name = models.CharField(max_length=-1, blank=True, null=True)
    send_docu_name_eng = models.CharField(max_length=-1, blank=True, null=True)
    action_state = models.CharField(max_length=-1, blank=True, null=True)
    action_state_eng = models.CharField(max_length=-1, blank=True, null=True)
    process = models.CharField(max_length=-1, blank=True, null=True)
    trial_no = models.CharField(max_length=-1, blank=True, null=True)
    reg_no = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pupd_int_history_kr'


class RcanApplicantnmchhistory(models.Model):
    patent_per_no = models.CharField(max_length=-1, blank=True, null=True)
    change_his_order = models.CharField(max_length=-1, blank=True, null=True)
    receipt_no = models.CharField(max_length=-1, blank=True, null=True)
    change_date = models.CharField(max_length=-1, blank=True, null=True)
    patent_per_name_kor = models.CharField(max_length=-1, blank=True, null=True)
    patent_per_name_eng = models.CharField(max_length=-1, blank=True, null=True)
    kor_name_is_change = models.CharField(max_length=-1, blank=True, null=True)
    eng_name_is_change = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rcan_applicantnmchhistory'


class RegdLastRgHolder(models.Model):
    reg_no = models.CharField(max_length=-1, blank=True, null=True)
    final_right_name = models.CharField(max_length=-1, blank=True, null=True)
    final_right_no = models.CharField(max_length=-1, blank=True, null=True)
    final_right_address = models.CharField(max_length=-1, blank=True, null=True)
    final_right_country = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regd_last_rg_holder'


class RegdRgBs(models.Model):
    reg_no = models.CharField(max_length=-1, blank=True, null=True)
    reg_date = models.CharField(max_length=-1, blank=True, null=True)
    appl_no = models.CharField(max_length=-1, blank=True, null=True)
    appl_date = models.CharField(max_length=-1, blank=True, null=True)
    pub_no = models.CharField(max_length=-1, blank=True, null=True)
    pub_date = models.CharField(max_length=-1, blank=True, null=True)
    invent_name = models.CharField(max_length=-1, blank=True, null=True)
    intent_name_eng = models.CharField(max_length=-1, blank=True, null=True)
    nom_class_code = models.CharField(max_length=-1, blank=True, null=True)
    situation_date = models.CharField(max_length=-1, blank=True, null=True)
    exp_date = models.CharField(max_length=-1, blank=True, null=True)
    request_no = models.IntegerField(blank=True, null=True)
    pre_appl_no = models.CharField(max_length=-1, blank=True, null=True)
    pre_appl_date = models.CharField(max_length=-1, blank=True, null=True)
    priority_assert_no = models.IntegerField(blank=True, null=True)
    priority_assert_country = models.CharField(max_length=-1, blank=True, null=True)
    priority_assert_date = models.CharField(max_length=-1, blank=True, null=True)
    limit_cause_code = models.CharField(max_length=-1, blank=True, null=True)
    limit_date = models.CharField(max_length=-1, blank=True, null=True)
    limit_cause = models.CharField(max_length=-1, blank=True, null=True)
    priority_no = models.IntegerField(blank=True, null=True)
    reg_international_no = models.CharField(max_length=-1, blank=True, null=True)
    reg_international_date = models.CharField(max_length=-1, blank=True, null=True)
    is_pre_reg = models.CharField(max_length=-1, blank=True, null=True)
    is_partial_exam = models.CharField(max_length=-1, blank=True, null=True)
    is_delete_include = models.CharField(max_length=-1, blank=True, null=True)
    is_restore_include = models.CharField(max_length=-1, blank=True, null=True)
    reg_pub_no = models.CharField(max_length=-1, blank=True, null=True)
    reg_pub_date = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regd_rg_bs'


class RegdRgfee(models.Model):
    reg_no = models.CharField(max_length=-1, blank=True, null=True)
    start_career_year = models.IntegerField(blank=True, null=True)
    final_career_year = models.IntegerField(blank=True, null=True)
    reg_fee = models.IntegerField(blank=True, null=True)
    fee_date = models.CharField(max_length=-1, blank=True, null=True)
    reg_date = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regd_rgfee'


class RegdRk(models.Model):
    reg_no = models.CharField(max_length=-1, blank=True, null=True)
    asso_code = models.CharField(max_length=-1, blank=True, null=True)
    rank_no = models.IntegerField(blank=True, null=True)
    reg_sep_code = models.CharField(max_length=-1, blank=True, null=True)
    docu_code = models.CharField(max_length=-1, blank=True, null=True)
    docu_name = models.CharField(max_length=-1, blank=True, null=True)
    receipt_no = models.CharField(max_length=-1, blank=True, null=True)
    receipt_date = models.CharField(max_length=-1, blank=True, null=True)
    reg_date = models.CharField(max_length=-1, blank=True, null=True)
    is_delete_include = models.CharField(max_length=-1, blank=True, null=True)
    delete_cause_code = models.CharField(max_length=-1, blank=True, null=True)
    delete_cause_name = models.CharField(max_length=-1, blank=True, null=True)
    delete_date = models.CharField(max_length=-1, blank=True, null=True)
    reg_cause_code = models.CharField(max_length=-1, blank=True, null=True)
    reg_cause_name = models.CharField(max_length=-1, blank=True, null=True)
    reg_cause_date = models.CharField(max_length=-1, blank=True, null=True)
    reg_goal = models.TextField(blank=True, null=True)
    div_reg_no = models.CharField(max_length=-1, blank=True, null=True)
    delete_giveup_no = models.IntegerField(blank=True, null=True)
    succ_state_adm_name = models.CharField(max_length=-1, blank=True, null=True)
    succ_state_adm_office = models.CharField(max_length=-1, blank=True, null=True)
    succ_office = models.CharField(max_length=-1, blank=True, null=True)
    pledge_exp_content = models.CharField(max_length=-1, blank=True, null=True)
    pledge_liq_date = models.CharField(max_length=-1, blank=True, null=True)
    pledge_exp_date = models.CharField(max_length=-1, blank=True, null=True)
    pledge_special_point = models.TextField(blank=True, null=True)
    attorney_clause_no = models.CharField(max_length=-1, blank=True, null=True)
    pre_dec_trial_no = models.CharField(max_length=-1, blank=True, null=True)
    pre_dec_claim_date = models.CharField(max_length=-1, blank=True, null=True)
    case_indication = models.CharField(max_length=-1, blank=True, null=True)
    claim_purport = models.TextField(blank=True, null=True)
    dec_valid_trial_no = models.CharField(max_length=-1, blank=True, null=True)
    final_year_month_date = models.CharField(max_length=-1, blank=True, null=True)
    dec_valid_invalid_claim_no = models.IntegerField(blank=True, null=True)
    trial_substance = models.TextField(blank=True, null=True)
    withdrawl_trial_no = models.CharField(max_length=-1, blank=True, null=True)
    withdrawl_rela_trial_no = models.CharField(max_length=-1, blank=True, null=True)
    withdrawl_date = models.CharField(max_length=-1, blank=True, null=True)
    req_event_indicate = models.CharField(max_length=-1, blank=True, null=True)
    duration_ext_appl_no = models.CharField(max_length=-1, blank=True, null=True)
    duration_ext_appl_date = models.CharField(max_length=-1, blank=True, null=True)
    duration_ext_dec_date = models.CharField(max_length=-1, blank=True, null=True)
    duration_ext_year = models.IntegerField(blank=True, null=True)
    duration_ext_month = models.IntegerField(blank=True, null=True)
    duration_ext_day = models.IntegerField(blank=True, null=True)
    duration_ext_claim_no = models.IntegerField(blank=True, null=True)
    duration_ext_per_content = models.CharField(max_length=-1, blank=True, null=True)
    duration_ext_claim_scope = models.CharField(max_length=-1, blank=True, null=True)
    objection_no = models.CharField(max_length=-1, blank=True, null=True)
    objection_date = models.CharField(max_length=-1, blank=True, null=True)
    objection_reason = models.CharField(max_length=-1, blank=True, null=True)
    oppo_dec_objection_no = models.CharField(max_length=-1, blank=True, null=True)
    oppo_dec_date = models.CharField(max_length=-1, blank=True, null=True)
    oppo_dec_substance = models.CharField(max_length=-1, blank=True, null=True)
    duration_renew_appl_date = models.CharField(max_length=-1, blank=True, null=True)
    duration_renew_appl_no = models.CharField(max_length=-1, blank=True, null=True)
    duration_renew_dec_date = models.CharField(max_length=-1, blank=True, null=True)
    div_shift_reg_no = models.CharField(max_length=-1, blank=True, null=True)
    nom_extra_appl_date = models.CharField(max_length=-1, blank=True, null=True)
    nom_extra_appl_no = models.CharField(max_length=-1, blank=True, null=True)
    nom_extra_pub_no = models.CharField(max_length=-1, blank=True, null=True)
    nom_extra_pub_date = models.CharField(max_length=-1, blank=True, null=True)
    nom_extra_dec_date = models.CharField(max_length=-1, blank=True, null=True)
    ori_reg_no = models.CharField(max_length=-1, blank=True, null=True)
    renew_reg_repre_code = models.CharField(max_length=-1, blank=True, null=True)
    is_delete_nom_search_move = models.CharField(max_length=-1, blank=True, null=True)
    reg_create_date = models.CharField(max_length=-1, blank=True, null=True)
    upper_tech_check_claim_n = models.CharField(max_length=-1, blank=True, null=True)
    tech_check_claim_date = models.CharField(max_length=-1, blank=True, null=True)
    tech_check_claim_purport = models.CharField(max_length=-1, blank=True, null=True)
    tech_check_final_date = models.CharField(max_length=-1, blank=True, null=True)
    tech_check_final_substance = models.CharField(max_length=-1, blank=True, null=True)
    part_delete_content = models.CharField(max_length=-1, blank=True, null=True)
    pledge_interest_agreement = models.CharField(max_length=-1, blank=True, null=True)
    pledge_penalty_agreement = models.CharField(max_length=-1, blank=True, null=True)
    remain_no = models.IntegerField(blank=True, null=True)
    dec_reg_invalid_claim_content = models.CharField(max_length=-1, blank=True, null=True)
    remain_content = models.CharField(max_length=-1, blank=True, null=True)
    dec_delete_quantity = models.IntegerField(blank=True, null=True)
    dec_reg_delete_content = models.CharField(max_length=-1, blank=True, null=True)
    intl_reg_no = models.CharField(max_length=-1, blank=True, null=True)
    intl_duration_exp_date = models.CharField(max_length=-1, blank=True, null=True)
    intl_late_renew_date = models.CharField(max_length=-1, blank=True, null=True)
    intl_reg_valid_date = models.CharField(max_length=-1, blank=True, null=True)
    nom_extra_reg_pub_no = models.CharField(max_length=-1, blank=True, null=True)
    nom_extra_reg_pub_date = models.CharField(max_length=-1, blank=True, null=True)
    nom_extra_pub_off_no = models.CharField(max_length=-1, blank=True, null=True)
    nom_extra_reg_pub_comm_code = models.CharField(max_length=-1, blank=True, null=True)
    dec_valid_cancel_trial_content = models.CharField(max_length=-1, blank=True, null=True)
    duration_ext_length = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regd_rk'


class RegdRkLcns(models.Model):
    reg_no = models.CharField(max_length=-1, blank=True, null=True)
    asso_code = models.CharField(max_length=-1, blank=True, null=True)
    asso_code_name = models.CharField(max_length=-1, blank=True, null=True)
    rank_no = models.IntegerField(blank=True, null=True)
    reg_sep_code = models.CharField(max_length=-1, blank=True, null=True)
    reg_sep_name = models.CharField(max_length=-1, blank=True, null=True)
    docu_code = models.CharField(max_length=-1, blank=True, null=True)
    docu_name = models.CharField(max_length=-1, blank=True, null=True)
    receipt_date = models.CharField(max_length=-1, blank=True, null=True)
    is_delete_valid = models.CharField(max_length=-1, blank=True, null=True)
    delete_cause_code = models.CharField(max_length=-1, blank=True, null=True)
    delete_cause_name = models.CharField(max_length=-1, blank=True, null=True)
    delete_date = models.CharField(max_length=-1, blank=True, null=True)
    reg_cause_code = models.CharField(max_length=-1, blank=True, null=True)
    reg_cause_name = models.CharField(max_length=-1, blank=True, null=True)
    reg_cause_date = models.CharField(max_length=-1, blank=True, null=True)
    reg_purpose = models.TextField(blank=True, null=True)
    div_reg_no = models.CharField(max_length=-1, blank=True, null=True)
    license_usage_start_date = models.CharField(max_length=-1, blank=True, null=True)
    license_usage_end_date = models.CharField(max_length=-1, blank=True, null=True)
    license_usage_code = models.CharField(max_length=-1, blank=True, null=True)
    license_usage_content = models.CharField(max_length=-1, blank=True, null=True)
    license_usage_area_name = models.CharField(max_length=-1, blank=True, null=True)
    other_license_factor = models.CharField(max_length=-1, blank=True, null=True)
    delete_giveup_no = models.CharField(max_length=-1, blank=True, null=True)
    succ_state_adm_name = models.CharField(max_length=-1, blank=True, null=True)
    succ_state_adm_office = models.CharField(max_length=-1, blank=True, null=True)
    succ_office = models.CharField(max_length=-1, blank=True, null=True)
    pledge_exp_content = models.CharField(max_length=-1, blank=True, null=True)
    pledge_liq_date = models.CharField(max_length=-1, blank=True, null=True)
    pledge_exp_date = models.CharField(max_length=-1, blank=True, null=True)
    pledge_special_point = models.TextField(blank=True, null=True)
    attorney_clause_no = models.CharField(max_length=-1, blank=True, null=True)
    pre_dec_trial_no = models.CharField(max_length=-1, blank=True, null=True)
    pre_dec_claim_date = models.CharField(max_length=-1, blank=True, null=True)
    pre_dec_case_indication = models.CharField(max_length=-1, blank=True, null=True)
    pre_dec_claim_purport = models.TextField(blank=True, null=True)
    dec_valid_trial_no = models.CharField(max_length=-1, blank=True, null=True)
    trial_final_date = models.CharField(max_length=-1, blank=True, null=True)
    dec_valid_invalid_claim_no = models.CharField(max_length=-1, blank=True, null=True)
    trial_substance = models.TextField(blank=True, null=True)
    withdrawl_trial_no = models.CharField(max_length=-1, blank=True, null=True)
    withdrawl_date = models.CharField(max_length=-1, blank=True, null=True)
    req_event_indicate = models.CharField(max_length=-1, blank=True, null=True)
    duration_ext_appl_no = models.CharField(max_length=-1, blank=True, null=True)
    duration_ext_appl_date = models.CharField(max_length=-1, blank=True, null=True)
    duration_ext_dec_date = models.CharField(max_length=-1, blank=True, null=True)
    duration_ext_length = models.CharField(max_length=-1, blank=True, null=True)
    duration_ext_year = models.CharField(max_length=-1, blank=True, null=True)
    duration_ext_month = models.CharField(max_length=-1, blank=True, null=True)
    duration_ext_day = models.CharField(max_length=-1, blank=True, null=True)
    duration_ext_length_2 = models.CharField(max_length=-1, blank=True, null=True)
    duration_ext_claim_no = models.CharField(max_length=-1, blank=True, null=True)
    duration_ext_per_content = models.CharField(max_length=-1, blank=True, null=True)
    duration_ext_claim_scope = models.CharField(max_length=-1, blank=True, null=True)
    objection_no = models.CharField(max_length=-1, blank=True, null=True)
    objection_date = models.CharField(max_length=-1, blank=True, null=True)
    objection_reason = models.CharField(max_length=-1, blank=True, null=True)
    oppo_dec_objection_no = models.CharField(max_length=-1, blank=True, null=True)
    oppo_dec_date = models.CharField(max_length=-1, blank=True, null=True)
    oppo_dec_substance = models.CharField(max_length=-1, blank=True, null=True)
    duration_renew_appl_date = models.CharField(max_length=-1, blank=True, null=True)
    duration_renew_appl_no = models.CharField(max_length=-1, blank=True, null=True)
    duration_renew_dec_date = models.CharField(max_length=-1, blank=True, null=True)
    div_shift_reg_no = models.CharField(max_length=-1, blank=True, null=True)
    nom_extra_appl_date = models.CharField(max_length=-1, blank=True, null=True)
    nom_extra_appl_no = models.CharField(max_length=-1, blank=True, null=True)
    nom_extra_pub_no = models.CharField(max_length=-1, blank=True, null=True)
    nom_extra_pub_date = models.CharField(max_length=-1, blank=True, null=True)
    nom_extra_dec_date = models.CharField(max_length=-1, blank=True, null=True)
    ori_reg_no = models.CharField(max_length=-1, blank=True, null=True)
    upper_tech_check_claim_no = models.CharField(max_length=-1, blank=True, null=True)
    tech_check_claim_date = models.CharField(max_length=-1, blank=True, null=True)
    tech_check_claim_purport = models.CharField(max_length=-1, blank=True, null=True)
    tech_check_final_date = models.CharField(max_length=-1, blank=True, null=True)
    tech_check_final_substance = models.CharField(max_length=-1, blank=True, null=True)
    license_fee_content = models.CharField(max_length=-1, blank=True, null=True)
    license_fee_pay_method = models.CharField(max_length=-1, blank=True, null=True)
    license_fee_pay_period = models.CharField(max_length=-1, blank=True, null=True)
    part_delete_content = models.CharField(max_length=-1, blank=True, null=True)
    pledge_interest_agreement = models.CharField(max_length=-1, blank=True, null=True)
    pledge_penalty_agreement = models.CharField(max_length=-1, blank=True, null=True)
    dec_reg_invalid_claim_content = models.CharField(max_length=-1, blank=True, null=True)
    remain_content = models.CharField(max_length=-1, blank=True, null=True)
    dec_delete_quantity = models.CharField(max_length=-1, blank=True, null=True)
    dec_reg_delete_content = models.CharField(max_length=-1, blank=True, null=True)
    intl_reg_no = models.CharField(max_length=-1, blank=True, null=True)
    intl_duration_exp_date = models.CharField(max_length=-1, blank=True, null=True)
    intl_late_renew_date = models.CharField(max_length=-1, blank=True, null=True)
    intl_reg_valid_date = models.CharField(max_length=-1, blank=True, null=True)
    merge_intl_reg_no = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regd_rk_lcns'


class RegdRkLcnsRelPsn(models.Model):
    reg_no = models.CharField(max_length=-1, blank=True, null=True)
    asso_code = models.CharField(max_length=-1, blank=True, null=True)
    asso_name = models.CharField(max_length=-1, blank=True, null=True)
    rank_no = models.CharField(max_length=-1, blank=True, null=True)
    reg_sep_code = models.CharField(max_length=-1, blank=True, null=True)
    reg_sep_attr = models.CharField(max_length=-1, blank=True, null=True)
    rank_rela_code = models.CharField(max_length=-1, blank=True, null=True)
    rank_rela_attr = models.CharField(max_length=-1, blank=True, null=True)
    rank_rela_no = models.CharField(max_length=-1, blank=True, null=True)
    rank_rela_name = models.CharField(max_length=-1, blank=True, null=True)
    rank_rela_address = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regd_rk_lcns_rel_psn'


class RegdRkRelPsn(models.Model):
    reg_no = models.CharField(max_length=-1, blank=True, null=True)
    asso_code = models.CharField(max_length=-1, blank=True, null=True)
    rank_no = models.IntegerField(blank=True, null=True)
    reg_sep_code = models.CharField(max_length=-1, blank=True, null=True)
    rank_rela_code = models.CharField(max_length=-1, blank=True, null=True)
    rank_rela_no = models.CharField(max_length=-1, blank=True, null=True)
    rank_rela_name = models.CharField(max_length=-1, blank=True, null=True)
    rank_rela_address = models.CharField(max_length=-1, blank=True, null=True)
    rank_rela_country = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regd_rk_rel_psn'


class SandApplicantRpst(models.Model):
    applicant_code = models.CharField(max_length=-1, blank=True, null=True)
    applicant_name = models.CharField(max_length=-1, blank=True, null=True)
    appl_rep_code = models.CharField(max_length=-1, blank=True, null=True)
    appl_rep_name = models.CharField(max_length=-1, blank=True, null=True)
    appl_rep_eng_name = models.CharField(max_length=-1, blank=True, null=True)
    address = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sand_applicant_rpst'


class SccdCpcCode(models.Model):
    cpc_code = models.CharField(max_length=-1, blank=True, null=True)
    revision_date = models.CharField(max_length=-1, blank=True, null=True)
    cpc_expl_kor = models.TextField(blank=True, null=True)
    cpc_expl_eng = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sccd_cpc_code'


class SccdEpcCode(models.Model):
    epc_code = models.CharField(max_length=-1, blank=True, null=True)
    epc_expl_eng = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sccd_epc_code'


class SccdFiCode(models.Model):
    fi_code = models.CharField(max_length=-1, blank=True, null=True)
    fi_expl_kor = models.TextField(blank=True, null=True)
    fi_expl_eng = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sccd_fi_code'


class SccdFtermCode(models.Model):
    fterm_code = models.CharField(max_length=-1, blank=True, null=True)
    fterm_expl_kor = models.TextField(blank=True, null=True)
    fterm_expl_eng = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sccd_fterm_code'


class SccdIpcCode(models.Model):
    ipc_code = models.CharField(max_length=-1, blank=True, null=True)
    revision_date = models.CharField(max_length=-1, blank=True, null=True)
    ipc_expl_kor = models.TextField(blank=True, null=True)
    ipc_expl_eng = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sccd_ipc_code'


class SccdUpcCode(models.Model):
    upc_code = models.CharField(max_length=-1, blank=True, null=True)
    upc_expl_eng = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sccd_upc_code'


class TcsdTm5CommonStatusDescriptors(models.Model):
    appl_no = models.CharField(max_length=-1, blank=True, null=True)
    state_code = models.CharField(max_length=-1, blank=True, null=True)
    state_expl = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tcsd_tm5_common_status_descriptors'


class TmabAgent(models.Model):
    appl_no = models.CharField(max_length=-1, blank=True, null=True)
    serial_no = models.IntegerField(blank=True, null=True)
    country_code = models.CharField(max_length=8, blank=True, null=True)
    country_code_name = models.CharField(max_length=-1, blank=True, null=True)
    agent_code = models.CharField(max_length=-1, blank=True, null=True)
    agent_name = models.CharField(max_length=-1, blank=True, null=True)
    agent_name_eng = models.CharField(max_length=-1, blank=True, null=True)
    agent_postal_code = models.CharField(max_length=-1, blank=True, null=True)
    agent_address = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmab_agent'


class TmabApplicant(models.Model):
    appl_no = models.CharField(max_length=-1, blank=True, null=True)
    serial_no = models.IntegerField(blank=True, null=True)
    country_code = models.CharField(max_length=8, blank=True, null=True)
    country_code_name = models.CharField(max_length=-1, blank=True, null=True)
    applicant_code = models.CharField(max_length=-1, blank=True, null=True)
    applicant_name = models.CharField(max_length=-1, blank=True, null=True)
    applicant_name_eng = models.CharField(max_length=-1, blank=True, null=True)
    applicant_postal_code = models.CharField(max_length=-1, blank=True, null=True)
    applicant_address = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmab_applicant'

'''


class TmabTbKt10(models.Model):
    appl_no = models.CharField(max_length=20, blank=True, null=False, primary_key=True)
    appl_date = models.CharField(max_length=20, blank=True, null=True)
    pub_no = models.CharField(max_length=20, blank=True, null=True)
    pub_date = models.CharField(max_length=20, blank=True, null=True)
    reg_no = models.CharField(max_length=20, blank=True, null=True)
    reg_date = models.CharField(max_length=20, blank=True, null=True)
    tm_name_kor = models.CharField(max_length=1000, blank=True, null=True)
    tm_name_eng = models.CharField(max_length=1000, blank=True, null=True)
    final_decision_code = models.CharField(max_length=5, blank=True, null=True)
    final_decision_code_name = models.CharField(max_length=300, blank=True, null=True)
    final_decision_date = models.CharField(max_length=8, blank=True, null=True)
    tm_category_code = models.CharField(max_length=5, blank=True, null=True)
    tm_category_code_name = models.CharField(max_length=300, blank=True, null=True)
    tm_class_code = models.CharField(max_length=5, blank=True, null=True)
    tm_class_code_name = models.CharField(max_length=300, blank=True, null=True)
    goods_class_ver = models.CharField(max_length=5, blank=True, null=True)
    has_tm_image = models.CharField(max_length=5, blank=True, null=True)
    has_pub = models.CharField(max_length=5, blank=True, null=True)
    has_amend_pub = models.CharField(max_length=5, blank=True, null=True)
    has_ori_appl = models.CharField(max_length=5, blank=True, null=True)
    has_trial = models.CharField(max_length=5, blank=True, null=True)
    has_priority = models.CharField(max_length=5, blank=True, null=True)
    intl_reg_no = models.CharField(max_length=20, blank=True, null=True)
    intl_reg_no_date = models.CharField(max_length=20, blank=True, null=True)
    subsequent_designation_date = models.CharField(max_length=20, blank=True, null=True)
    final_retro_code = models.CharField(max_length=20, blank=True, null=True)
    final_retro_code_name = models.CharField(max_length=300, blank=True, null=True)
    final_retro_date = models.CharField(max_length=20, blank=True, null=True)
    tm_name_date = models.CharField(max_length=20, blank=True, null=True)
    exp_date = models.CharField(max_length=20, blank=True, null=True)
    init_update_date = models.CharField(max_length=50, blank=True, null=True)
    final_modified_date = models.CharField(max_length=50, blank=True, null=True)
    legal_status = models.CharField(max_length=20, blank=True, null=True)
    is_service_start = models.CharField(max_length=5, blank=True, null=True)
    pub_reg_no = models.CharField(max_length=20, blank=True, null=True)
    pub_reg_date = models.CharField(max_length=20, blank=True, null=True)
    is_full_pub_reg = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmab_tb_kt10'


'''
class TmabTbKt11(models.Model):
    appl_no = models.CharField(max_length=-1, blank=True, null=True)
    vien_class_code = models.CharField(max_length=-1, blank=True, null=True)
    vien_class_expl = models.CharField(max_length=-1, blank=True, null=True)
    vien_class_priority = models.CharField(max_length=-1, blank=True, null=True)
    init_update_date = models.CharField(max_length=-1, blank=True, null=True)
    final_modified_date = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmab_tb_kt11'
'''


class TmabTbKt13(models.Model):
    appl_no = models.CharField(max_length=20, blank=True, null=True)
    priority_serial_no = models.IntegerField(blank=True, null=True)
    priority_appl_no = models.CharField(max_length=100, blank=True, null=True)
    priority_appl_date = models.CharField(max_length=20, blank=True, null=True)
    priority_country_code = models.CharField(max_length=8, blank=True, null=True)
    priority_country_code_name = models.CharField(max_length=150, blank=True, null=True)
    init_update_date = models.CharField(max_length=20, blank=True, null=True)
    final_modified_date = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmab_tb_kt13'


class TmabTbKt14(models.Model):
    appl_no = models.CharField(max_length=20, blank=True, null=False, primary_key=True)
    ori_appl_no = models.CharField(max_length=20, blank=True, null=True)
    ori_appl_date = models.CharField(max_length=20, blank=True, null=True)
    init_update_date = models.CharField(max_length=20, blank=True, null=True)
    final_modified_date = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmab_tb_kt14'


'''
class TmabTbKt15(models.Model):
    appl_no = models.CharField(max_length=-1, blank=True, null=True)
    serial_no = models.IntegerField(blank=True, null=True)
    goods_class = models.CharField(max_length=-1, blank=True, null=True)
    goods_name_kor = models.CharField(max_length=-1, blank=True, null=True)
    goods_name_eng = models.CharField(max_length=-1, blank=True, null=True)
    similar_group = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmab_tb_kt15'


class TmpcCheck(models.Model):
    distinct_no = models.CharField(max_length=-1, blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    serial_no = models.IntegerField(blank=True, null=True)
    nom_serial_no = models.IntegerField(blank=True, null=True)
    sep_code_name = models.CharField(max_length=-1, blank=True, null=True)
    nice_class_ver = models.CharField(max_length=-1, blank=True, null=True)
    classification_code = models.CharField(max_length=-1, blank=True, null=True)
    nom_mark_name = models.TextField(blank=True, null=True)
    extra_del_code = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmpc_check'


class TmpcTrademarkclassificationcode(models.Model):
    distinct_no = models.CharField(max_length=-1, blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    serial_no = models.IntegerField(blank=True, null=True)
    nom_serial_no = models.IntegerField(blank=True, null=True)
    sep_code_name = models.CharField(max_length=-1, blank=True, null=True)
    nice_class_ver = models.CharField(max_length=-1, blank=True, null=True)
    classification_code = models.CharField(max_length=-1, blank=True, null=True)
    nom_mark_name = models.TextField(blank=True, null=True)
    extra_del_code = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmpc_trademarkclassificationcode'
'''
'''
class TmpdIntHistoryKt(models.Model):
    #id = models.AutoField(primary_key=True)
    appl_no = models.CharField(max_length=20, blank=True, null=False, primary_key=True)
    send_no = models.CharField(max_length=20, blank=True, null=True)
    send_date = models.CharField(max_length=20, blank=True, null=True)
    send_docu_name = models.CharField(max_length=500, blank=True, null=True)
    send_docu_name_eng = models.CharField(max_length=500, blank=True, null=True)
    action_state = models.CharField(max_length=300, blank=True, null=True)
    action_state_eng = models.CharField(max_length=500, blank=True, null=True)
    process = models.CharField(max_length=20, blank=True, null=True)
    trial_no = models.CharField(max_length=20, blank=True, null=True)
    regist_no = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmpd_int_history_kt'

'''