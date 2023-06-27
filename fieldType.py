
class fieldType (object):
  def __init__ (self, **kwargs):
    self.__dict__ = kwargs
    self.suffix = self.kind[2:]

    tt = self.suffix[0]
    ss = self.suffix[1]

    th = {'R': 'REAL', 'I': 'INTEGER', 'L': 'LOGICAL'}
    td = {'R':  '0.0', 'I':       '0', 'L': '.FALSE.'}

    self.type = th[tt] + '(KIND=' + self.kind + ')'
    self.default = td[tt] + '_' + self.kind
    self.alias = self.suffix == 'RB'

    self.name = 'FIELD_%s%s' % (self.rank, self.suffix);
    self.rank = int (self.rank)
    self.shape = ','.join ([':'] * int (self.rank))
    self.viewRank = self.rank-1
    self.viewShape = ','.join ([':'] * (self.rank-1))
    self.lbptr = ', '.join (list (map (lambda i: "LBOUNDS(" + str (i+1) + "):", range (0, self.rank))))


kinds = ['JPRM', 'JPRB', 'JPRD', 'JPIM', 'JPLM']


def getFieldTypeList (ranks=[2,3,4,5], kinds=kinds):
  return [fieldType (kind=kind, rank=rank) for (kind) in kinds for rank in ranks]

def useParkind1 (kinds=kinds):
  return 'USE PARKIND1, ONLY : ' + ','.join (kinds)