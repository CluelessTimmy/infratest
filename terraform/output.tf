output "instance_names"{
    description = "Instance Names"
    value = for instance_name, name in google_compute_instance.vm : instance_name =>  google_compute_instance.vm[instance_name].hostname
}