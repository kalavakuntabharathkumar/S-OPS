from app.troubleshooting import diagnose,response_is_consistent
def test_timeout_rule():
    r=diagnose('Checkout timeout','Requests return 504 timeout errors.')
    assert r.category=='performance' and r.severity=='high' and response_is_consistent(r)
def test_permission_rule(): assert diagnose('Access denied','User gets 403 forbidden.').category=='permissions'
def test_unknown_is_guided(): assert response_is_consistent(diagnose('Something failed','No diagnostic evidence available.'))
