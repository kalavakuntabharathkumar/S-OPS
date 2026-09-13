const $=id=>document.getElementById(id);
async function load(){
  const [t,m]=await Promise.all([fetch('/api/tickets').then(r=>r.json()),fetch('/api/metrics').then(r=>r.json())]);
  $('metrics').innerHTML=`<b>${m.total_tickets} tickets</b> · <b>${m.open_tickets} open</b> · <b>${m.resolution_rate_percent}% resolved</b> · <b>${m.high_priority_tickets} high priority</b>`;
  $('tickets').innerHTML=t.map(x=>`<article><b>#${x.id} ${esc(x.title)}</b> <i>${esc(x.priority)}</i> <i>${esc(x.severity)}</i><p>${esc(x.description)}</p><small>${esc(x.category)} · ${esc(x.status)} · ${esc(x.channel)} · ${esc(x.assignee)}</small><details><summary>Technical details</summary><p><b>Requester:</b> ${esc(x.requester)}</p><p><b>Diagnosis:</b> ${esc(x.diagnosis)}</p><p><b>Resolution:</b> ${esc(x.resolution)}</p><p><b>Customer response:</b> ${esc(x.customer_response)}</p>${x.status!=='resolved'?`<button onclick='resolveTicket(${x.id})'>Mark resolved</button>`:''}</details></article>`).join('');
  $('ticketForm').onsubmit=async e=>{e.preventDefault();const r=await fetch('/api/tickets',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({title:$('title').value,description:$('description').value,requester:$('requester').value,channel:$('channel').value,priority:$('priority').value,assignee:$('assignee').value})});const x=await r.json();$('result').textContent=r.ok?`Ticket #${x.id} created\n\nDiagnosis: ${x.diagnosis}\n\nResolution: ${x.resolution}\n\nCustomer response: ${x.customer_response}`:JSON.stringify(x,null,2);e.target.reset();load()};
}
async function resolveTicket(id){await fetch(`/api/tickets/${id}/resolve`,{method:'POST'});load()}
function esc(v){return String(v).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#039;'}[c]))}
load();