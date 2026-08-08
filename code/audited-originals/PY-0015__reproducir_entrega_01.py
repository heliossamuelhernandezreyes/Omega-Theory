from pathlib import Path
import numpy as np, pandas as pd, matplotlib.pyplot as plt
import hashlib, json, zipfile, shutil
from scipy.linalg import eigvalsh
from scipy.stats import linregress

BASE=Path('/mnt/data'); OUT=BASE/'OMEGA_THEORY_V1_1_ENTREGA_01_GEOMETRIA_TRANSICIONES'
if OUT.exists(): shutil.rmtree(OUT)
folders={k:OUT/v for k,v in {
'docs':'01_DOCUMENTOS','num':'02_PRUEBAS_NUMERICAS','code':'03_CODIGO','fig':'04_FIGURAS','data':'05_DATOS','manifest':'06_MANIFIESTO'}.items()}
for p in folders.values(): p.mkdir(parents=True,exist_ok=True)

def effective_branching(w):
    w=np.asarray(w,float); w=w[w>0]; q=w/w.sum(); return float(np.exp(-(q*np.log(q)).sum()))
def mobility_tensor(D,r): return sum(rate*np.outer(d,d) for rate,d in zip(r,D))
def directional_inertia(M,v):
    v=np.asarray(v,float); v=v/np.linalg.norm(v); mu=float(v@M@v); return np.inf if mu<=1e-15 else 1/mu
def rates_from_cost(c,law):
    c=np.asarray(c,float)
    return {'inverse':1/c,'exp_beta_0p5':np.exp(-.5*c),'exp_beta_1':np.exp(-c)}[law]

D=np.array([[1,0],[-1,0],[0,1],[0,-1]],float)
systems={'A_uniforme':np.array([1,1,1,1],float),'B_anisotropo':np.array([1,1,10,10],float),'C_colectivo':np.array([3,3,3,3],float)}
rows=[]
for name,costs in systems.items():
  for law in ['inverse','exp_beta_0p5','exp_beta_1']:
    rates=rates_from_cost(costs,law); M=mobility_tensor(D,rates); eig=np.linalg.eigvalsh(M)
    rows.append(dict(system=name,rate_law=law,n_compatible_transitions=4,n_raw_transitions=8,scalar_p=.5,effective_branching=effective_branching(rates),theta_total_update_rate=rates.sum(),M_xx=M[0,0],M_xy=M[0,1],M_yy=M[1,1],mobility_eigen_min=eig.min(),mobility_eigen_max=eig.max(),anisotropy_ratio=eig.max()/eig.min(),inertia_x=directional_inertia(M,[1,0]),inertia_y=directional_inertia(M,[0,1])))
test1=pd.DataFrame(rows); test1.to_csv(folders['num']/ 'TEST_01_MISMO_P_DISTINTA_GEOMETRIA.csv',index=False)

states=[format(i,'03b') for i in range(8)]; valid={'000','111'}
hyper_edges={('000','111'),('111','000')}; graph_edges=set()
for s in states:
  bits=list(s)
  for i in range(3):
    t=bits.copy(); t[i]='1' if bits[i]=='0' else '0'; graph_edges.add((s,''.join(t)))
def reachable(start,edges,allowed=None):
  adj={}
  for a,b in edges:
    if allowed is not None and (a not in allowed or b not in allowed): continue
    adj.setdefault(a,[]).append(b)
  seen={start}; stack=[start]
  while stack:
    u=stack.pop()
    for v in adj.get(u,[]):
      if v not in seen: seen.add(v); stack.append(v)
  return seen
hyper_reach=reachable('000',hyper_edges,valid); graph_restrict=reachable('000',graph_edges,valid); graph_full=reachable('000',graph_edges)
test2=pd.DataFrame([
 dict(representation='directed_hypergraph_collective',identity_valid_states_reachable=len(hyper_reach&valid),all_states_reachable=len(hyper_reach),invalid_intermediate_states_reachable=len(hyper_reach-valid),can_reach_111_preserving_identity=True,interpretation='Represents collective update directly.'),
 dict(representation='ordinary_graph_restricted_to_identity',identity_valid_states_reachable=len(graph_restrict&valid),all_states_reachable=len(graph_restrict),invalid_intermediate_states_reachable=0,can_reach_111_preserving_identity=False,interpretation='Loses valid collective transition.'),
 dict(representation='ordinary_graph_allowing_intermediates',identity_valid_states_reachable=len(graph_full&valid),all_states_reachable=len(graph_full),invalid_intermediate_states_reachable=len(graph_full-valid),can_reach_111_preserving_identity=False,interpretation='Creates invalid intermediate states.')])
test2.to_csv(folders['num']/ 'TEST_02_GRAFO_VS_HIPERGRAFO.csv',index=False)

def two_cluster_generator(n=5,epsilon=1e-3):
  N=2*n; W=np.zeros((N,N))
  for cluster in [range(n),range(n,2*n)]:
    for i in cluster:
      for j in cluster:
        if i!=j: W[i,j]=1/(n-1)
  W[n-1,n]=epsilon; W[n,n-1]=epsilon; Q=W.copy(); np.fill_diagonal(Q,-W.sum(axis=1)); return Q

eps_values=np.array([0,1e-10,1e-9,1e-8,1e-7,1e-6,1e-5,1e-4,1e-3,1e-2,1e-1,1.0])
cont=[]
for eps in eps_values:
  vals=eigvalsh(-two_cluster_generator(5,eps)); vals[np.abs(vals)<1e-13]=0; pos=vals[vals>0]; gap=pos.min() if len(pos) else 0
  cont.append(dict(epsilon_bridge_rate=eps,connected_components_from_zero_modes=int(np.sum(vals==0)),spectral_gap=gap,mixing_time_proxy_1_over_gap=np.inf if gap==0 else 1/gap,continuity_ontologically_unbroken=eps>0))
test3=pd.DataFrame(cont); test3.to_csv(folders['num']/ 'TEST_03_RUPTURA_CONTINUIDAD.csv',index=False)
fit_df=test3[(test3.epsilon_bridge_rate>0)&(test3.epsilon_bridge_rate<=1e-3)]; fit=linregress(np.log10(fit_df.epsilon_bridge_rate),np.log10(fit_df.spectral_gap))
pd.DataFrame([dict(fit_domain='1e-10 <= epsilon <= 1e-3',spectral_gap_power_exponent=fit.slope,spectral_gap_prefactor=10**fit.intercept,R2=fit.rvalue**2)]).to_csv(folders['num']/ 'TEST_03_AJUSTE_ESCALAMIENTO.csv',index=False)

rates=np.ones(4); M=mobility_tensor(D,rates); drift=np.sum(rates[:,None]*D,axis=0)
test4=pd.DataFrame([dict(M_xx=M[0,0],M_xy=M[0,1],M_yx=M[1,0],M_yy=M[1,1],isotropy_error_frobenius=np.linalg.norm(M-np.trace(M)/2*np.eye(2)),drift_x=drift[0],drift_y=drift[1])]); test4.to_csv(folders['num']/ 'TEST_04_RED_HOMOGENEA.csv',index=False)

plt.figure(figsize=(7,5)); q=test3[test3.epsilon_bridge_rate>0]; plt.loglog(q.epsilon_bridge_rate,q.spectral_gap,marker='o'); plt.xlabel('Tasa mínima de puente ε'); plt.ylabel('Brecha espectral'); plt.title('Continuidad efectiva'); plt.tight_layout(); plt.savefig(folders['fig']/ 'FIG_01_BRECHA_VS_EPSILON.png',dpi=180); plt.close()
plt.figure(figsize=(7,5)); q=q[np.isfinite(q.mixing_time_proxy_1_over_gap)]; plt.loglog(q.epsilon_bridge_rate,q.mixing_time_proxy_1_over_gap,marker='o'); plt.xlabel('Tasa mínima de puente ε'); plt.ylabel('Tiempo de mezcla proxy'); plt.title('Aislamiento efectivo sin ruptura'); plt.tight_layout(); plt.savefig(folders['fig']/ 'FIG_02_MEZCLA_VS_EPSILON.png',dpi=180); plt.close()

summary={'test1_same_scalar_p':{'scalar_p_all_systems':.5,'inverse_law_theta':test1[test1.rate_law=='inverse'].set_index('system').theta_total_update_rate.to_dict(),'inverse_law_anisotropy':test1[test1.rate_law=='inverse'].set_index('system').anisotropy_ratio.to_dict()},'test2_collective_update':{'hypergraph_reaches_valid_target':True,'ordinary_graph_restricted_reaches_valid_target':False,'ordinary_graph_invalid_intermediates':len(graph_full-valid)},'test3_continuity':{'power_exponent':fit.slope,'R2':fit.rvalue**2,'zero_epsilon_components':int(test3.iloc[0].connected_components_from_zero_modes),'positive_epsilon_components':int(test3.iloc[1].connected_components_from_zero_modes)},'test4_homogeneous':test4.iloc[0].to_dict()}
(folders['data']/ 'RESUMEN_RESULTADOS.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False),encoding='utf-8')

(OUT/'00_LEEME.md').write_text('''# Omega Theory v1.1 — Entrega 01\n## Geometría local de transiciones compatibles\n\nPrimera entrega matemática oficial posterior al canon v1.0.\n\n**Resultado principal:** un grafo ordinario no conserva siempre una actualización colectiva. El candidato mínimo es un hipergrafo dirigido y ponderado de eventos de actualización, con el grafo como caso particular.\n\nSe incluyen cuatro pruebas numéricas, código, tablas, figuras, dudas ontológicas y manifiesto.\n''',encoding='utf-8')

(folders['docs']/ '01_PREGUNTA_ONTOLOGICA.md').write_text('''# Pregunta ontológica\n\n¿Cuál es el objeto mínimo que conserva continuaciones compatibles, costos colectivos, accesibilidad y continuidad de identidad?\n\nSe comparan grafo, hipergrafo y operador lineal. La decisión provisional favorece el hipergrafo de eventos porque una actualización simultánea no debe descomponerse introduciendo estados que ontológicamente nunca existen.\n''',encoding='utf-8')

(folders['docs']/ '02_DERIVACION_MATEMATICA.md').write_text(r'''# Derivación matemática inicial

Un evento compatible se representa por

\[
e=(S_e,T_e,\Delta_e,w_e,c_e,\chi_e),
\]

donde el soporte \(S_e\) puede incluir varias relaciones simultáneas, \(w_e\) es accesibilidad, \(c_e\) costo y \(\chi_e\) preservación de identidad.

La geometría local es

\[
\mathfrak G_x=\{e:x\overset e\longrightarrow T_e\}.
\]

La proyección escalar histórica

\[
p(x)=\frac{|\mathcal E_x^{\rm compatible}|}{|\mathcal E_x^{\rm raw}|}
\]

no conserva pesos, costos, soporte ni dirección.

Para tasas \(r_e\), la diversidad efectiva es

\[
B_{\rm eff}=\exp\!\left(-\sum_e q_e\log q_e\right),\qquad q_e=\frac{r_e}{\sum_f r_f}.
\]

La ley tasa–costo aún no está derivada; se comparan \(1/c\), \(e^{-c/2}\) y \(e^{-c}\).

El tensor local de movilidad es

\[
M_x=\sum_e r_e\,\Delta\xi_e\Delta\xi_e^{\mathsf T}.
\]

La movilidad direccional y la inercia candidata son

\[
\mu_x(v)=v^{\mathsf T}M_xv,\qquad I_x(v)=\mu_x(v)^{-1}.
\]

La tasa total candidata es

\[
\Theta_x=\sum_e r_e.
\]

Para un puente mínimo \(\varepsilon\), la ruptura exacta ocurre en \(\varepsilon=0\), mientras el aislamiento efectivo se mide por

\[
\tau_{\rm mix}\sim \lambda_1^{-1}.
\]
''',encoding='utf-8')

inv=test1[test1.rate_law=='inverse']
res='# Resultados numéricos\n\n## Mismo p, distinta geometría\n\nTodos tienen p=0.5.\n\n'+inv[['system','theta_total_update_rate','anisotropy_ratio','inertia_x','inertia_y']].to_markdown(index=False)
res+=f'''\n\n## Actualización colectiva\n\nEl hipergrafo conecta 000 con 111 preservando identidad. El grafo restringido pierde la transición; el grafo no restringido introduce {len(graph_full-valid)} estados inválidos.\n\n## Continuidad\n\n\[\lambda_1\simeq {10**fit.intercept:.6g}\,\varepsilon^{{{fit.slope:.6f}}},\qquad R^2={fit.rvalue**2:.8f}.\]\n\nPara ε>0 hay una sola componente, pero el tiempo de mezcla diverge cuando ε→0+.\n\n## Control homogéneo\n\nError de isotropía: {test4.iloc[0].isotropy_error_frobenius:.3e}. Deriva: ({test4.iloc[0].drift_x:.3e},{test4.iloc[0].drift_y:.3e}).\n'''
(folders['docs']/ '03_RESULTADOS_NUMERICOS.md').write_text(res,encoding='utf-8')

(folders['docs']/ '04_RESULTADOS_NEGATIVOS.md').write_text('''# Resultados negativos y límites\n\n- El escalar p es insuficiente.\n- Un grafo ordinario no es universal para eventos colectivos.\n- La ley tasa–costo no está derivada.\n- Una tasa mínima positiva evita ruptura exacta, pero no aislamiento efectivo.\n- Todavía no se derivan reloj, masa ni gravedad.\n''',encoding='utf-8')

(folders['docs']/ '05_DUDAS_ONTOLOGICAS.md').write_text('''# Dudas ontológicas abiertas\n\n## ODG-004\n¿Qué fija la tasa: accesibilidad, costo o ambos?\n\n## ODG-005\n¿La continuidad exige tasa estrictamente positiva o pueden existir componentes ontológicamente separadas?\n\n## ODG-006\n¿Cómo se deriva la preservación de identidad χ_e sin imponerla?\n\n## ODG-007\n¿Puede una actualización fundamental tener soporte infinito?\n''',encoding='utf-8')

(folders['docs']/ '06_COMPARACION_OBSERVACIONAL.md').write_text('''# Comparación observacional\n\nNo corresponde aún una comparación física directa. Esta entrega construye el objeto estructural. La siguiente fase deberá derivar tasa de reloj, movilidad/inercia y regla de trayectoria antes de comparar con dilatación temporal, caída libre o límite newtoniano.\n''',encoding='utf-8')

(folders['docs']/ '07_SIGUIENTE_PASO.md').write_text('''# Entrega 02 — Inercia relacional\n\nSe compararán: soporte mínimo, costo de retorno, inversa de movilidad y tiempo de escape espectral. Deben sobrevivir composición, coarse-graining, renombrado y ausencia de estados intermedios artificiales.\n''',encoding='utf-8')

# Standalone reproduction script (compact but executable)
shutil.copy2('/tmp/make_omega_delivery1.py', folders['code']/ 'reproducir_entrega_01.py')

files=[]
for p in OUT.rglob('*'):
  if p.is_file(): files.append(dict(relative_path=str(p.relative_to(OUT)),size_bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
pd.DataFrame(files).to_csv(folders['manifest']/ 'MANIFIESTO_ARCHIVOS.csv',index=False)
(folders['manifest']/ 'METADATA.json').write_text(json.dumps({'package':OUT.name,'created_utc':pd.Timestamp.utcnow().isoformat(),'main_candidate':'directed weighted update hypergraph','tests':4,'direct_observational_comparison':False,'next_delivery':'relational inertia'},indent=2),encoding='utf-8')

zip_path=BASE/f'{OUT.name}.zip'
if zip_path.exists(): zip_path.unlink()
with zipfile.ZipFile(zip_path,'w',zipfile.ZIP_DEFLATED) as z:
  for p in sorted(OUT.rglob('*')):
    if p.is_file(): z.write(p,arcname=f'{OUT.name}/{p.relative_to(OUT)}')
print(zip_path)
print('files',len(files),'fit',fit.slope,fit.rvalue**2)
print(inv[['system','theta_total_update_rate','anisotropy_ratio','inertia_x','inertia_y']].to_string(index=False))
