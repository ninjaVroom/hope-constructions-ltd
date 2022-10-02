from datetime import datetime

from backend.settings import DEBUG
from Libraries.functions.print.main import app_debug_printer


class CodeExecutionTimer(object):
    def __init__(self, *args):
        super(CodeExecutionTimer, self).__init__(*args)
    
    _starttime: datetime|None = None
    _endtime: datetime|None = None
    
    def starttime(self):
        if DEBUG:
            self._starttime = datetime.now()
    @property
    def getStarttime(self):
        return self._starttime
        
    def endtime(self):
        if DEBUG:
            self._endtime = datetime.now()
    @property
    def getEndtime(self):
        return self._endtime

    @property
    def printExecTime(self):
        if DEBUG:
            starttime = self._starttime
            endtime = self._endtime

            if (starttime is not None) and (endtime is not None):
                diff = endtime - starttime
                app_debug_printer(__file__, description="starttime", output=starttime,)
                app_debug_printer(__file__, description="endtime", output=endtime,)
                return app_debug_printer(__file__, description="Code-Execution-Timer", output=diff,)
            return app_debug_printer(__file__, description="Code-Execution-Timer", output="No time data",)
