from dataclasses import dataclass
@dataclass
class Diagnosis:
    category:str; severity:str; diagnosis:str; resolution:str; customer_response:str
RULES=[
(('timeout','latency','slow','504'),Diagnosis('performance','high','Request latency or upstream timeout detected.','Check latency, dependencies, recent deployments and timeout configuration.','We identified a performance/timeout condition and are validating the affected dependency.')),
(('permission denied','forbidden','403','access denied'),Diagnosis('permissions','medium','The service or user lacks a required permission.','Verify service accounts, roles, file permissions and recent policy changes.','We identified an access-permission issue and are validating authorization.')),
(('disk full','no space left','storage full'),Diagnosis('disk','high','The host appears to have exhausted available disk capacity.','Inspect filesystem usage, rotate safe logs and restore capacity.','We identified a storage-capacity issue and are restoring safe capacity.')),
(('database','db connection','connection refused','sql'),Diagnosis('database','high','The symptoms indicate a database connectivity problem.','Check database health, connection limits, credentials and network reachability.','We identified a database connectivity issue and are validating database health.'))]
def diagnose(title,description,category='general'):
    text=f'{title} {description}'.lower()
    for keys,result in RULES:
        if any(k in text for k in keys): return result
    return Diagnosis(category if category!='general' else 'general','medium','Insufficient evidence for automatic diagnosis; guided investigation required.','Collect logs, reproduction steps, recent changes and environment details before escalation.','We have started investigating and are collecting diagnostic information.')
def response_is_consistent(d):
    return all([d.diagnosis.strip(),d.resolution.strip(),d.customer_response.strip(),d.severity in {'low','medium','high','critical'},d.category.strip()])
