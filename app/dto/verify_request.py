from dataclasses import dataclass
from dto.validatable import Validatable
from util.file import isFileExist
from os.path import isabs
from constant import STORAGE_DIR_NAME, SIGNATURE_DIR_NAME


@dataclass
class VerifyRequest(Validatable):
    hashOption: str
    filePath: str
    signaturePath: str
    
    def __init__(self, hashOption: int, filePath: str, signaturePath: str):
        self.hashOption = hashOption
        self.filePath = filePath
        self.signaturePath = signaturePath
        
        if not isabs(self.filePath):
            self.filePath = f"{STORAGE_DIR_NAME}/{filePath}"
            
        if not isabs(self.signaturePath):
            self.signaturePath = f"{SIGNATURE_DIR_NAME}/{signaturePath}"
    
    def validate(self):
        fieldNames = {
            "hashOption": "Hash algorithm option",
            "filePath": "File",
            "signaturePath": "Signature",
        }
        
        self.isDigit(self.hashOption, fieldNames["hashOption"])
        self.fileExists(self.filePath, fieldNames["filePath"])
        self.fileExists(self.signaturePath, fieldNames["signaturePath"])
        self.fileHasExtension(self.filePath, fieldNames["filePath"], ".pdf")
        self.fileHasExtension(self.signaturePath, fieldNames["signaturePath"], "")
