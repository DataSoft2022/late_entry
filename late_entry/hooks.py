from . import __version__ as app_version

app_name = "late_entry"
app_title = "Late Entry"
app_publisher = "omneyaeid827@gmail.com"
app_description = "Attandance policy"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "omneyaeid827@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

doc_events = {
    "Employee Checkin": {
        "before_insert": "late_entry.late_entry.hook.employee_late_entry.apply_late_entry_permissions",
        "before_save":  "late_entry.late_entry.hook.employee_late_entry.apply_late_entry_permissions",
    }
}

# include js, css files in header of desk.html
# app_include_css = "/assets/late_entry/css/late_entry.css"
# app_include_js = "/assets/late_entry/js/late_entry.js"

# include js, css files in header of web template
# web_include_css = "/assets/late_entry/css/late_entry.css"
# web_include_js = "/assets/late_entry/js/late_entry.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "late_entry/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "late_entry.install.before_install"
# after_install = "late_entry.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "late_entry.uninstall.before_uninstall"
# after_uninstall = "late_entry.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "late_entry.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"late_entry.tasks.all"
#	],
#	"daily": [
#		"late_entry.tasks.daily"
#	],
#	"hourly": [
#		"late_entry.tasks.hourly"
#	],
#	"weekly": [
#		"late_entry.tasks.weekly"
#	]
#	"monthly": [
#		"late_entry.tasks.monthly"
#	]
# }

# Testing
# -------

# before_tests = "late_entry.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "late_entry.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "late_entry.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Request Events
# ----------------
# before_request = ["late_entry.utils.before_request"]
# after_request = ["late_entry.utils.after_request"]

# Job Events
# ----------
# before_job = ["late_entry.utils.before_job"]
# after_job = ["late_entry.utils.after_job"]

# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"late_entry.auth.validate"
# ]

