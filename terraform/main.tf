resource "google_compute_instance" "vm" {
    for_each = var.instances

    project = var.project_id
    name = each.key
    description = each.value.description
    machine_type = each.value.machine_type
    zone = each.value.zone
    hostname = "${each.key}-${each.value.zone}.asx.com.au"
	
    //Checks if the the input "service_account" is not equal to an empty string, if not empty generate a service_account block with content email and scope
    dynamic service_account {
        for_each = var.service_account != "" ? [1] : []
        content {
            email = var.service_account
            scopes = var.scopes
        }
    }
}
