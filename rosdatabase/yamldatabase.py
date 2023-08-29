import numpy as np
import yaml

class Database:
    def __init__(self, backup_file):
        self.data = {}
        self.backup_file = backup_file
        
        # Load data from backup file if it exists
        try:
            with open(self.backup_file, 'r') as f:
                self.data = yaml.safe_load(f) or {}
        except FileNotFoundError:
            pass

    def __str__(self) -> str:
        data_string = ""
        for key in self.data:
            data_string += f"{key}: {self.get_entry(key)}\n"
        return data_string
        
    def add_entry(self, key, value):
        if isinstance(value, np.ndarray):
            value = ['np.ndarray', value.tolist()]
        self.data[key] = value
        self._update_backup()
        
    def get_entry(self, key):
        value = self.data.get(key)
        if isinstance(value, list) and value[0] == 'np.ndarray':
            value = np.array(value[1])
        return value
        
    def remove_entry(self, key):
        if key in self.data:
            del self.data[key]
            self._update_backup()
        
    def _update_backup(self):
        with open(self.backup_file, 'w') as f:
            yaml.dump(self.data, f)
            
