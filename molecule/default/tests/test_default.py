import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_heketi_installed(host):

    # System Distribution
    os_distribution = host.system_info.distribution

    # System Release
    os_release = int(host.system_info.release.split('.')[0])

    # Log
    print('OS [Dist : {}, Major : {}]'.format(os_distribution, os_release))

    # Heketi Service Name
    service_name = 'heketi'

    # Heketi command path
    command_path = '/usr/bin/heketi'

    # Heketi service path
    service_file_path = '/usr/lib/systemd/system/heketi.service'

    # Heketi service path Ubuntu
    service_file_path_ubuntu = '/lib/systemd/system/heketi.service'

    # Heketi service path centos6
    service_file_path_centos6 = '/etc/rc.d/init.d/heketi'

    # Check that command exists
    assert host.file(command_path).exists

    # Check that command is link
    assert host.file(command_path).is_symlink

    # Execute command and get result
    command_run = host.run(command_path + ' --version')

    # Assert that run is OK
    assert command_run.rc == 0

    # Check that command is file
    assert host.file(command_path).is_file

    # If OS in not CentOS 6
    if os_distribution == 'CentOS' and os_release > 6:

        # Check that command exists
        assert host.file(service_file_path).exists

        # Check that Heketi service is started
        assert host.service(service_name).is_running is True

    elif os_distribution == 'CentOS' and os_release == 6:

        # Check that command exists
        assert host.file(service_file_path_centos6).exists

    else:

        # Check that command exists
        assert host.file(service_file_path_ubuntu).exists

        # Check that Heketi service is started
        assert host.service(service_name).is_running is True
