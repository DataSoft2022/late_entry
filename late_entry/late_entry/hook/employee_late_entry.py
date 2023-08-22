from datetime import datetime, timedelta, date

import frappe
from frappe.utils.logger import get_logger


def apply_late_entry_permissions(check_in_doc, *args, **kwargs):
    logger = get_logger("Add Additional Salary")
    if check_in_doc.log_type.lower() == 'in':
        if frappe.db.exists("Permission", {"employee": check_in_doc.employee}):
            employee_checkin_date = datetime.strptime(check_in_doc.time, '%Y-%m-%d %H:%M:%S').date()
            employee_checkin_time = datetime.strptime(check_in_doc.time, '%Y-%m-%d %H:%M:%S').time()
            permission = frappe.get_doc("Permission", {"employee": check_in_doc.employee, "date": employee_checkin_date,
                                                       'docstatus': 1})

            if not datetime.strptime(str(permission.from_time + timedelta(hours=1, minutes=1, seconds=59)),
                                     "%H:%M:%S").time() >= employee_checkin_time > permission.from_time:
                if (datetime.strptime('09:00:00', '%H:%M:%S')).time() < employee_checkin_time <= (
                        datetime.strptime('09:30:59', '%H:%M:%S')).time():
                    deduction = 0

                elif (datetime.strptime('09:30:59', '%H:%M:%S')).time() < employee_checkin_time <= (
                        datetime.strptime('09:45:59', '%H:%M:%S')).time():
                    deduction = 0.25

                elif (datetime.strptime('09:45:59', '%H:%M:%S')).time() < employee_checkin_time <= (
                        datetime.strptime('10:00:59', '%H:%M:%S')).time():
                    deduction = 0.5

                else:
                    deduction = 1

                if deduction > 0:
                    try:
                        additional_salary_doc = frappe.new_doc("Additional Salary")
                        additional_salary_doc.employee = check_in_doc.employee
                        additional_salary_doc.salary_component = 'Deduction W.days'
                        additional_salary_doc.amount = deduction
                        additional_salary_doc.payroll_date = employee_checkin_date
                        additional_salary_doc.save()
                        additional_salary_doc.submit()
                    except Exception as e:
                        import traceback
                        logger.error(traceback.format_exc())
                        frappe.log_error(
                            message=f"While making Additional Salary for employee {check_in_doc.employee}, an error occurred {str(e)}",
                            title="additional_salary")
