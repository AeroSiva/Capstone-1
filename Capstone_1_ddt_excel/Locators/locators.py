class Orangehrm_locators:
    # Login page
    username_ip_name = 'username'
    password_ip_name = 'password'
    login_btn_xpath = '//button[@type="submit"]'
    invalid_login_alert_css = 'div.oxd-alert-content.oxd-alert-content--error>p'

    # Dashboard page
    userdropdown_icon_xpath = '//div[@class="oxd-topbar-header-userarea"]//i'
    logout_link_xpath = '//a[@href="/web/index.php/auth/logout"]'
    PIM_module_xpath = '//a[@href="/web/index.php/pim/viewPimModule"]'
    pim_add_xpah = '//button[text()=" Add "]'

    # Employee details pim
    first_name_name ='firstName'
    last_name_name = 'lastName'
    employee_id_xpath = '//label[text()="Employee Id"]/parent::div/following-sibling::div/input'
    create_login_details_css = 'div.oxd-switch-wrapper>label>span'
    username_ip_cre_login_xpath = '//label[text()="Username"]/parent::div/following-sibling::div/input'
    password_ip_cre_login_xpath = '//label[text()="Password"]/parent::div/following-sibling::div/input'
    confirm_password_ip_cre_login_xpath = '//label[text()="Confirm Password"]/parent::div/following-sibling::div/input'
    save_button_xpath = '//button[text()=" Save "]'
    saved_invalid_notification = '//div[@class="oxd-toast-container oxd-toast-container--bottom"]'
    saved_or_invalid_not_add_ele = '//div[@class="oxd-toast-container oxd-toast-container--bottom"]/*'

    # pim page search employee
    employee_name_xpath = '//input[@placeholder="Type for hints..."]'
    pim_employee_id_xpath = '//label[text()="Employee Id"]/parent::div/following-sibling::div/input'
    search_button_xpath = '//button[text()=" Search "]'
    edit_ess_user_pencil_icon_css = 'i.oxd-icon.bi-pencil-fill'
    nationality_caret_down_fill_css = 'i.oxd-icon.bi-caret-down-fill.oxd-select-text--arrow'
    select_record_cbes_css = "div.oxd-table-row.oxd-table-row--with-border.oxd-table-row--clickable>div>div.oxd-table-card-cell-checkbox"
    select_record_cbes_xpath = '//div[@class="oxd-table-row oxd-table-row--with-border oxd-table-row--clickable"]/div/div[@class="oxd-table-card-cell-checkbox"]'
    id_record_es_xpath = '//div[@class="oxd-table-row oxd-table-row--with-border oxd-table-row--clickable"]/div/div[@class="oxd-table-card-cell-checkbox"]/parent::div/following-sibling::div[1]/div'
    delete_selected_dye_xpath = '//button[text()=" Delete Selected "]'
    delete_notifi_yes_btn_xpath = '(//div[@class="oxd-sheet oxd-sheet--rounded oxd-sheet--white oxd-dialog-sheet oxd-dialog-sheet--shadow oxd-dialog-sheet--gutters orangehrm-dialog-popup"]//button)[3]'

    # Personal detail page
    # Personal detail page
    per_nick_name_xpath = '//label[text()="Nickname"]/parent::div/following-sibling::div/input'
    per_other_id__ip_xpath = '//label[text()="Other Id"]/parent::div/following-sibling::div/input'
    per_driver_lic_ip_xpath ='(//input)[8]'
    per_lic_exp_dat_cip_xpath ='//label[text()="License Expiry Date"]/parent::div/following-sibling::div//input'#'(//input[@placeholder="dd-mm-yyyy"])[1]'#'(//input[@placeholder="yyyy-mm-dd"])[1]'
    per_ssn_n_ip_xpath = '//label[text()="SSN Number"]/parent::div/following-sibling::div/input'
    per_sin_n_ip_xpath = '//label[text()="SIN Number"]/parent::div/following-sibling::div/input'
    per_nationality_dd_xpath = '//label[text()="Nationality"]/parent::div/following-sibling::div//i'
    per_nationality_dyop_xpath = '//div[@class="oxd-select-wrapper"]//div[@class="oxd-select-dropdown --positon-bottom"]'#'//div[@class="oxd-select-wrapper"]//div[@class="oxd-select-dropdown]/div'
    per_nationality_dyop_afgha_xpath = '//div[@class="oxd-select-wrapper"]//div[@class="oxd-select-dropdown --positon-bottom"]//span[text()="Afghan"]'#'//div[@class="oxd-select-wrapper"]//span[text()="Afghan"]' #Indian"
    per_nationality_ipv_xpath ='//label[text()="Nationality"]/parent::div/following-sibling::div//div[@class="oxd-select-text-input"]'
    per_nationality_dyop_indi_xpath = '//div[@class="oxd-select-wrapper"]//div[@class="oxd-select-dropdown --positon-bottom"]//span[text()="Indian"]'#'//div[@class="oxd-select-wrapper"]//span[text()="Afghan"]' #Indian"
    per_martial_status_dd_xpath = '//label[text()="Marital Status"]/parent::div/following-sibling::div//i'
    per_martial_status_dop_xpath = '//div[@class="oxd-select-wrapper"]//div[@class="oxd-select-dropdown --positon-bottom"]'#'//div[@class="oxd-select-wrapper"]//div[@class="oxd-select-dropdown]/div'
    per_martial_status_dop_single_xpath = '//div[@class="oxd-select-wrapper"]//div[@class="oxd-select-dropdown --positon-bottom"]//span[text()="Married"]'#'(//div[@class="oxd-select-wrapper"]//div[@class="oxd-select-dropdown]/div)[2]'
    per_dob_ip_xpath = '//label[text()="Date of Birth"]/parent::div/following-sibling::div//input'
    per_gender_rd_xpath = '//label[text()="Male"]/span'
    per_military_ser_ip_xpath = '//label[text()="Military Service"]/parent::div/following-sibling::div/input'
    per_per_det_save_btn_xpath = '(//div[@class="oxd-layout-context"]//form)[1]//button'
    per_blood_type_dd_xpath = '//label[text()="Blood Type"]/parent::div/following-sibling::div//i'
    per_blood_type_ap_xpath = '//div[@class="oxd-select-wrapper"]//div[@class="oxd-select-dropdown --positon-bottom"]//span[text()="A+"]'
    per_blood_type_op_xpath = '//div[@class="oxd-select-wrapper"]//div[@class="oxd-select-dropdown --positon-bottom"]//span[text()="O+"]'
    per_blood_type_it_xpath = '//label[text()="Blood Type"]/parent::div/following-sibling::div//div[@class="oxd-select-text-input"]'
    per_cus_field_save_btn_xpath = '(//div[@class="oxd-layout-context"]//form)[2]//button'    



