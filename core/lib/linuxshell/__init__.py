import os
import paramiko
import warnings


class LinuxShell:

    def __init__(self, host, port=22, user=None, password=None):
        self._host = host
        self._port = port
        self._user = user

        self._cron_path = "hardcoded"
        if host != 'localhost':
            try:
                self.client = paramiko.SSHClient()
                self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                warnings.filterwarnings(action='ignore', module='.*paramiko.*')
                self.client.connect(host, port, user, allow_agent=True)
            except paramiko.AuthenticationException:
                raise ConnectionError('Could not connect via SSH Client Make sure you have the proper credentials'
                                      ' configure in your local config file')

    def run_cron(self, cron_name):
        if self._host == 'localhost':
            return self.run_cron_local(cron_name)
        else:
            return self.run_cron_remote(cron_name)

    def run_cron_local(self, cron_name):
        data = []
        full_path = os.path.join("/usr/bin/php", self._cron_path, cron_name)
        try:
            if self._user:
                stdin, stdout, stderr = self.client.exec_command(
                    f'sudo -u {self._user} {full_path} 2>/dev/null')
                for line in stdout:
                    data.append(line.strip('\n'))
        finally:
            self.client.close()
        return data

    def run_cron_remote(self, cron_name):
        data = []
        full_path = os.path.join(self._cron_path, cron_name)
        try:
            stdin, stdout, stderr = self.client.exec_command(f"runcron {full_path}")
            for line in stdout:
                data.append(line.strip('\n'))
        finally:
            self.client.close()
        return data

