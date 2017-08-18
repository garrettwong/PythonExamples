import subprocess

class ProcessManager:
    def execute(self, cmd):
        self.subprocess = subprocess
        self.subprocess.call(['ls', '-all'])
        self.subprocess.call(['touch', 'hi.txt'])

        self.subprocess.call(['rm', 'hi.txt'])
        
        subprocess.check_output(["echo", "Hello World!"])


if __name__ == "__main__":
    pm = ProcessManager()
    
    pm.execute('ls')
        