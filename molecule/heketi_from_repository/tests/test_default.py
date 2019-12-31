import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_heketi_installed(host):

    # Heketi Service Name
    service_name = 'heketi-sds'

    # Heketi command path
    command_path = '/usr/bin/heketi'

    # Heketi service path
    service_file_path = '/usr/lib/systemd/system/heketi-sds.service'

    # Check that command exists
    assert host.file(command_path).exists

    # Execute command and get result
    command_run = host.run(command_path + ' --version')

    # Assert that run is OK
    assert command_run.rc == 0

    # Check that command is link
    assert host.file(command_path).is_link

    # Check that command exists
    assert host.file(service_file_path).exists

    # Check that command is file
    assert host.file(command_path).is_file

    # Check that Heketi service is started
    assert host.service(service_name).is_running is True
