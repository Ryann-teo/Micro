"""Phase 2 content for individual concepts.

Maps concept slug -> dict with optional keys:
  "math": str of HTML (KaTeX picks up $...$ and $$...$$ automatically)
  "widget": str of HTML (inline SVG or Plotly container with a script tag)
  "examples": str of HTML (use <ul><li>...</li></ul> for bullet lists)

Anything absent renders as the Phase 2 placeholder in build_site.py.
"""

PHASE2 = {
    "competitive-equilibrium": {
        "math": r"""<p>A <strong>competitive equilibrium</strong> in a pure exchange economy with $I$ consumers and $L$ goods is a price vector $p^* \in \mathbb{R}^L_{++}$ and an allocation $(x_i^*)_{i=1}^I$ such that (i) each $x_i^*$ solves $\max u_i(x_i)$ subject to $p^* \cdot x_i \leq p^* \cdot \omega_i$, and (ii) markets clear: $\sum_i x_i^* = \sum_i \omega_i$.</p>

<p>The key feature is that agents take prices as given and choose only their own bundle. No agent coordinates with another. Equilibrium emerges because the price vector reconciles all individual plans simultaneously.</p>

<p>To derive existence in the 2-good, 2-person Edgeworth box, we look for $p^* = (p_1^*, p_2^*)$ such that excess demand $z(p) = \sum_i (x_i(p, p\cdot \omega_i) - \omega_i)$ is zero.</p>

<ol>
<li>Each consumer solves $\max u_i(x_{i1}, x_{i2})$ subject to $p_1 x_{i1} + p_2 x_{i2} = p_1 \omega_{i1} + p_2 \omega_{i2}$. The interior FOC gives $MRS_i = p_1/p_2$.</li>
<li>By Walras' law, $p \cdot z(p) \equiv 0$, so if good 2 clears then good 1 clears too. We only need one market equation.</li>
<li>Continuity of $z$ plus boundary behaviour (excess demand explodes as a price tends to zero) gives a fixed point via Brouwer, hence $p^*$ exists.</li>
<li>At $p^*$, $MRS_1 = MRS_2 = p_1^*/p_2^*$, so the allocation sits on the contract curve, confirming the First Welfare Theorem.</li>
</ol>

<p>The First Welfare Theorem (Micro2025 Lecture 4, Varian Ch. 17) states: any competitive equilibrium is Pareto efficient, provided preferences are locally non-satiated and there are no externalities. The proof is one paragraph. Suppose $(x_i^*)$ is not Pareto efficient. Then there exists $(\hat x_i)$ with $u_i(\hat x_i) \geq u_i(x_i^*)$ for all $i$ and strict for some. Local non-satiation plus utility maximisation imply $p^* \cdot \hat x_i \geq p^* \cdot \omega_i$ for all $i$ and strict for some, hence $p^* \cdot \sum_i \hat x_i > p^* \cdot \sum_i \omega_i$, contradicting feasibility.</p>

<p>The Second Welfare Theorem provides the converse: any Pareto efficient allocation can be supported as a competitive equilibrium after suitable lump-sum transfers, provided preferences are convex. This is the formal basis for the equity-efficiency separation that motivates much of Topic 1.</p>

<p>References: Micro2025.pdf Topic 1 Lectures 3-5; Varian, <em>Microeconomic Analysis</em>, Ch. 17-18; Mas-Colell, Whinston, Green Ch. 15-16.</p>""",
        "widget": r"""<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <defs>
    <marker id="ce-arrow" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
      <path d="M0,0 L8,4 L0,8 z" fill="#333"/>
    </marker>
  </defs>
  <rect x="80" y="40" width="440" height="320" fill="none" stroke="#333" stroke-width="2"/>
  <text x="50" y="50" font-size="13" fill="#555">$O_B$</text>
  <text x="525" y="375" font-size="13" fill="#555">$O_A$</text>
  <text x="295" y="20" font-size="13" fill="#555">good 1</text>
  <text x="555" y="205" font-size="13" fill="#555">good 2</text>
  <path d="M 80 280 Q 200 200 300 160 Q 400 130 520 110" fill="none" stroke="#1f77b4" stroke-width="2"/>
  <text x="120" y="275" font-size="12" fill="#1f77b4">$u_A$ indiff.</text>
  <path d="M 80 220 Q 200 250 300 280 Q 400 310 520 340" fill="none" stroke="#d62728" stroke-width="2"/>
  <text x="430" y="335" font-size="12" fill="#d62728">$u_B$ indiff.</text>
  <line x1="120" y1="360" x2="500" y2="80" stroke="#2ca02c" stroke-width="1.5" stroke-dasharray="6 4"/>
  <text x="470" y="100" font-size="12" fill="#2ca02c">budget line, slope $-p_1/p_2$</text>
  <circle cx="300" cy="220" r="6" fill="#9467bd"/>
  <text x="310" y="215" font-size="13" fill="#9467bd">$E^*$ (CE)</text>
  <circle cx="180" cy="310" r="5" fill="#555"/>
  <text x="190" y="320" font-size="12" fill="#555">endowment $\omega$</text>
  <line x1="180" y1="310" x2="295" y2="225" stroke="#555" stroke-width="1" marker-end="url(#ce-arrow)"/>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Edgeworth box. At the competitive equilibrium $E^*$, the common budget line is tangent to both indifference curves, so $MRS_A = MRS_B = p_1^*/p_2^*$ and the allocation lies on the contract curve.</p>""",
        "examples": r"""<ul>
<li><strong>Stock and commodity exchanges</strong> approximate the price-taking ideal: thousands of small participants, public prices, near-instant clearing. The price reconciles plans without any central planner observing preferences.</li>
<li><strong>Online ad auctions</strong> (Google, Meta) are a real-time competitive market for impressions. Walrasian-style equilibrium logic predicts the marginal value of an impression equals the marginal cost across advertisers.</li>
<li><strong>Electricity wholesale markets</strong> (Nord Pool, ERCOT) implement a Walrasian auctioneer literally: the system operator solves for a clearing price that equates supply and demand at each node.</li>
<li><strong>Evaluation move:</strong> Kate Doornik rewards essays that distinguish the <em>positive</em> claim (markets clear, FWT holds) from the <em>normative</em> claim (the resulting allocation is desirable). The FWT says nothing about distribution. Pair it with the Second Welfare Theorem to make the equity-efficiency separation explicit.</li>
<li><strong>Evaluation move:</strong> the convexity assumption in SWT is load-bearing. Without convex preferences, supporting prices need not exist, and the planner cannot decentralise the chosen Pareto point.</li>
<li><strong>Standard limitation:</strong> FWT fails under externalities, public goods, asymmetric information, or non-convexities. These failures motivate Topic 3 on market failure.</li>
<li>Cross-reference: see [[Concepts/First Welfare Theorem]] and [[Concepts/Edgeworth Box]] for the supporting structure, and [[Concepts/Pigouvian Tax]] for the corrective response when FWT fails.</li>
</ul>""",
    },

    "quasi-linear-utility": {
        "math": r"""<p><strong>Quasi-linear utility</strong> takes the form $u(x_1, \dots, x_{L-1}, m) = v(x_1, \dots, x_{L-1}) + m$, where $m$ is a numeraire good (often interpreted as money or composite consumption) and $v$ is concave in the other goods. The defining feature is that utility is linear in $m$ and separable from the other arguments.</p>

<p>The behavioural consequence is that demand for the non-numeraire goods is <em>independent of income</em>, provided the consumer is not at a corner. To see this, set $p_m = 1$ and consider $\max v(x) + m$ subject to $p \cdot x + m = w$.</p>

<ol>
<li>Substitute the constraint: $\max v(x) + w - p \cdot x$.</li>
<li>FOC in each $x_l$: $\partial v / \partial x_l = p_l$. Wealth $w$ does not appear.</li>
<li>Hence Marshallian demand $x^*(p)$ depends only on prices. All income effects load onto $m$.</li>
<li>The indirect utility is $V(p, w) = v(x^*(p)) - p \cdot x^*(p) + w$, additively separable in $w$.</li>
</ol>

<p>Two implications matter for welfare analysis. First, <strong>Marshallian and Hicksian demand coincide</strong> for the non-numeraire goods, so consumer surplus, compensating variation, and equivalent variation are all equal: $CV = EV = \Delta CS$. This is why quasi-linear preferences are the default in partial equilibrium welfare economics (Varian Ch. 10, Hindriks-Myles Ch. 5).</p>

<p>Second, in a quasi-linear economy, <strong>utility is transferable</strong> via $m$. The Pareto frontier is a straight line with slope $-1$ in the utility space (between any two agents), and the efficient quantity of any non-numeraire good is independent of the distribution of wealth. This is the technical condition that makes the Kaldor-Hicks criterion coincide with Pareto efficiency, and it underpins the cost-benefit logic used throughout Topic 3.</p>

<p>For a public good $G$ financed by quasi-linear agents with $u_i = v_i(G) + m_i$, the efficient level solves $\sum_i v_i'(G) = c'(G)$, the Samuelson condition, with no distributional caveat because money utility is constant.</p>

<p>Limitation: quasi-linearity rules out income effects on the goods of interest. For goods that are a non-trivial share of the budget (housing, food in developing countries), the assumption is poor and welfare measures diverge. Hausman (1981) shows how to recover exact welfare measures from estimated Marshallian demand when quasi-linearity fails.</p>

<p>References: Micro2025.pdf Topic 1 Lecture 2 and Topic 3 Lecture 1; Varian <em>Microeconomic Analysis</em> Ch. 7 and 10; Mas-Colell Ch. 3 Appendix.</p>""",
        "widget": r"""<div id="widget-quasi-linear" style="height:380px"></div>
<div style="margin-top:0.5em;font-size:0.9em">
  <label>Wealth $w$: <input id="ql-wealth" type="range" min="2" max="10" step="0.5" value="6" style="vertical-align:middle"></label>
  <span id="ql-wealth-val">6</span>
</div>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Indifference curves for $u = 2\sqrt{x} + m$. Moving the wealth slider shifts the curves vertically but the optimal $x^*$ (where slope equals $p_x = 1$) stays fixed. This is the income-independence property.</p>
<script>
setTimeout(function(){
  function curves(w){
    var xs = [];
    for (var i=1; i<=80; i++) xs.push(0.1 + i*0.1);
    var traces = [];
    var levels = [w-2, w-1, w, w+1, w+2];
    var colors = ['#1f77b4','#2ca02c','#d62728','#9467bd','#ff7f0e'];
    levels.forEach(function(L, idx){
      var ms = xs.map(function(x){ return L - 2*Math.sqrt(x); });
      traces.push({x:xs, y:ms, mode:'lines', name:'u='+L.toFixed(1),
                   line:{color:colors[idx], width:2}});
    });
    var bm = xs.map(function(x){ return w - x; });
    traces.push({x:xs, y:bm, mode:'lines', name:'budget',
                 line:{color:'#333', width:2, dash:'dash'}});
    traces.push({x:[1], y:[w-1], mode:'markers+text', name:'x*',
                 marker:{color:'#000', size:10}, text:['x*=1'],
                 textposition:'top right', showlegend:false});
    return traces;
  }
  var w0 = 6;
  Plotly.newPlot('widget-quasi-linear', curves(w0), {
    margin:{t:20,r:20,b:40,l:50},
    xaxis:{title:'x (non-numeraire good)', range:[0, 8]},
    yaxis:{title:'m (numeraire)', range:[0, 10]},
    showlegend:false
  }, {displayModeBar:false});
  document.getElementById('ql-wealth').addEventListener('input', function(e){
    var w = parseFloat(e.target.value);
    document.getElementById('ql-wealth-val').textContent = w;
    Plotly.react('widget-quasi-linear', curves(w), {
      margin:{t:20,r:20,b:40,l:50},
      xaxis:{title:'x (non-numeraire good)', range:[0, 8]},
      yaxis:{title:'m (numeraire)', range:[0, 10]},
      showlegend:false
    });
  });
}, 500);
</script>""",
        "examples": r"""<ul>
<li><strong>Auction theory</strong> assumes quasi-linear bidders ($u_i = v_i - p$) so the seller can compare bids directly in money. Without quasi-linearity, the Vickrey-Clarke-Groves mechanisms lose their efficiency guarantee.</li>
<li><strong>Cost-benefit analysis</strong> of infrastructure (HS2, Crossrail) reports sums of willingness to pay across households. This aggregation is only welfare-meaningful under quasi-linearity, otherwise winners and losers cannot be netted by adding pounds.</li>
<li><strong>Insurance and risk-sharing models</strong> sometimes use $u = v(c) + m$ where $c$ is a contingent consumption profile, allowing closed-form premium calculations.</li>
<li><strong>Evaluation move:</strong> Kate Doornik often rewards essays that flag <em>when</em> quasi-linearity is invoked silently. For example, claiming a Pigouvian tax raises welfare typically uses $\Delta CS + \Delta PS - \text{externality}$, which presumes transferable utility.</li>
<li><strong>Evaluation move:</strong> distinguish quasi-linear in money from quasi-linear in leisure. The labour supply literature often uses $u = v(c) - \phi(\ell)$, which is quasi-linear in consumption and gives a wage elasticity of labour supply that is purely substitution-driven.</li>
<li><strong>Standard limitation:</strong> Hausman (1981) and Vartia (1983) show that for goods with material income elasticity (housing, transport in poor households), CS overstates true welfare loss by 5-15%. The default partial-equilibrium toolkit is mildly biased.</li>
<li>Cross-reference: see [[Concepts/Consumer Surplus]] for the welfare measure this assumption justifies, and [[Concepts/Samuelson Condition]] for the public-good FOC that exploits transferable utility.</li>
</ul>""",
    },

    "pigouvian-tax": {
        "math": r"""<p>A <strong>Pigouvian tax</strong> is a per-unit levy on an activity that generates a negative externality, set equal to the marginal external damage at the social optimum. It internalises the externality by aligning private with social marginal cost.</p>

<p>Setup: a competitive industry produces $q$ at private marginal cost $c'(q)$, facing inverse demand $p(q)$. Production imposes external damage $d(q)$ with $d'(q) > 0$. Social welfare is $W(q) = \int_0^q p(s)\,ds - c(q) - d(q)$.</p>

<ol>
<li>Private equilibrium without intervention: firms set $p = c'(q)$, giving $q^M$ where $p(q^M) = c'(q^M)$.</li>
<li>Social optimum: $W'(q^*) = 0$ gives $p(q^*) = c'(q^*) + d'(q^*)$.</li>
<li>Since $d' > 0$ and $p$ is downward-sloping, $q^* < q^M$. Unregulated output is too high.</li>
<li>Impose a per-unit tax $t$ on producers. The firm now sets $p = c'(q) + t$. To replicate $q^*$, choose $t^* = d'(q^*)$.</li>
<li>At $t^*$, private FOC becomes $p(q^*) = c'(q^*) + d'(q^*)$, matching the social FOC. The market decentralises the optimum.</li>
</ol>

<p>The deadweight loss eliminated is the area between the social marginal cost curve and the demand curve, between $q^*$ and $q^M$: $DWL = \int_{q^*}^{q^M} [c'(q) + d'(q) - p(q)]\,dq$. Tax revenue $t^* q^*$ flows to the government and can be rebated lump-sum without distorting the corrected allocation, because labour supply effects are zero in the partial-equilibrium frame.</p>

<p>Equivalence with quantity instruments (Weitzman 1974): under certainty, a Pigouvian tax $t^*$ and a tradeable permit cap $\bar Q = q^*$ produce the same allocation. Under uncertainty about marginal abatement cost, the welfare ranking depends on the relative slopes of marginal damage and marginal cost: taxes are preferred when MD is flatter than MC, permits when steeper.</p>

<p>Key qualifications. (i) The tax must equal $d'(q^*)$, not $d'(q^M)$. Setting the tax at the marginal damage observed at the distorted equilibrium over-corrects. (ii) If the externality varies by source (a power plant near a city versus a remote one), a uniform tax is second-best; first-best requires differentiated rates. (iii) Coase (1960) noted that with low transaction costs and well-defined property rights, parties can bargain to the efficient outcome without government intervention, making the Pigouvian instrument unnecessary.</p>

<p>References: Micro2025.pdf Topic 3 Lecture 2; Hindriks and Myles, <em>Intermediate Public Economics</em>, Ch. 7; Varian Ch. 24.</p>""",
        "widget": r"""<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <line x1="60" y1="350" x2="560" y2="350" stroke="#333" stroke-width="1.5"/>
  <line x1="60" y1="350" x2="60" y2="40" stroke="#333" stroke-width="1.5"/>
  <text x="555" y="370" font-size="12">$q$</text>
  <text x="40" y="50" font-size="12">$p$</text>
  <line x1="60" y1="80" x2="540" y2="340" stroke="#1f77b4" stroke-width="2"/>
  <text x="495" y="335" font-size="12" fill="#1f77b4">Demand $p(q)$</text>
  <line x1="60" y1="280" x2="540" y2="160" stroke="#2ca02c" stroke-width="2"/>
  <text x="500" y="155" font-size="12" fill="#2ca02c">PMC $= c'(q)$</text>
  <line x1="60" y1="220" x2="540" y2="100" stroke="#d62728" stroke-width="2"/>
  <text x="500" y="95" font-size="12" fill="#d62728">SMC $= c' + d'$</text>
  <line x1="370" y1="350" x2="370" y2="220" stroke="#555" stroke-dasharray="4 3"/>
  <line x1="60" y1="220" x2="370" y2="220" stroke="#555" stroke-dasharray="4 3"/>
  <circle cx="370" cy="220" r="5" fill="#d62728"/>
  <text x="378" y="215" font-size="12" fill="#d62728">$E^*$</text>
  <text x="365" y="368" font-size="12">$q^*$</text>
  <line x1="445" y1="350" x2="445" y2="260" stroke="#555" stroke-dasharray="4 3"/>
  <circle cx="445" cy="260" r="5" fill="#2ca02c"/>
  <text x="453" y="255" font-size="12" fill="#2ca02c">$E^M$</text>
  <text x="440" y="368" font-size="12">$q^M$</text>
  <line x1="300" y1="195" x2="300" y2="255" stroke="#9467bd" stroke-width="2"/>
  <line x1="295" y1="195" x2="305" y2="195" stroke="#9467bd" stroke-width="2"/>
  <line x1="295" y1="255" x2="305" y2="255" stroke="#9467bd" stroke-width="2"/>
  <text x="310" y="230" font-size="13" fill="#9467bd">$t^* = d'(q^*)$</text>
  <polygon points="370,220 445,260 445,225 370,220 370,220" fill="#ffcccc" opacity="0.55"/>
  <text x="395" y="245" font-size="11" fill="#a00">DWL</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">The Pigouvian tax $t^* = d'(q^*)$ shifts the firm's effective supply from PMC to SMC, contracting output from $q^M$ to $q^*$ and eliminating the shaded deadweight loss.</p>""",
        "examples": r"""<ul>
<li><strong>London Congestion Charge</strong> (2003 onward): a flat daily fee for driving in central London, justified as a Pigouvian instrument against road congestion and local air pollution. Leape (2006) estimated traffic fell 18% and welfare rose, though the flat structure misses the time-varying marginal damage that a first-best charge would track.</li>
<li><strong>EU Emissions Trading System (ETS)</strong>: a cap-and-trade scheme for $\mathrm{CO}_2$. By Weitzman logic, permits dominate when marginal damage is steep (climate tipping points), which is the standard defence for quantity instruments in climate policy.</li>
<li><strong>US federal gasoline tax</strong> (18.4 cents per gallon since 1993): far below the Parry-Small (2005) estimate of optimal external cost (about $1 per gallon), so it is Pigouvian in form but under-set in level.</li>
<li><strong>Evaluation move:</strong> Kate Doornik rewards essays that distinguish setting $t = d'(q^*)$ from $t = d'(q^M)$. The latter is the common student error and leads to over-correction. Pinning the tax to the optimal quantity, not the distorted one, is the substantive point.</li>
<li><strong>Evaluation move:</strong> raise the double-dividend hypothesis (Bovenberg and de Mooij 1994). Whether revenue recycling can eliminate other distortionary taxes depends on labour-market interactions ignored in the partial-equilibrium diagram.</li>
<li><strong>Standard limitation:</strong> the regulator must observe $d'(q^*)$. For diffuse externalities (greenhouse gases) the marginal damage estimates span an order of magnitude. Coase argued that for small-numbers externalities, bargaining outperforms taxation.</li>
<li>Cross-reference: see [[Concepts/Externality]] for the underlying market failure and [[Concepts/Coase Theorem]] for the property-rights alternative.</li>
</ul>""",
    },

    "samuelson-condition": {
        "math": r"""<p>The <strong>Samuelson condition</strong> (Samuelson 1954) characterises the Pareto-efficient quantity of a pure public good. With $I$ consumers, one private good $x$ and one public good $G$, produced from a single resource with marginal rate of transformation $MRT_{Gx}$, efficiency requires:</p>

$$\sum_{i=1}^I MRS^i_{Gx} = MRT_{Gx}.$$

<p>The right-hand side is the social marginal cost of one more unit of $G$ (in private-good units). The left-hand side is the sum of marginal willingness to pay across consumers, summed because every consumer enjoys the same $G$ simultaneously: public goods are non-rival.</p>

<p>Contrast with a private good $x$, where efficiency requires $MRS^i_{xy} = MRT_{xy}$ for each $i$ separately. Private goods get horizontally summed demand; public goods get vertically summed willingness to pay.</p>

<ol>
<li>Each consumer has $u_i(x_i, G)$, with feasibility $\sum_i x_i + c(G) = \Omega$ where $\Omega$ is the aggregate resource endowment.</li>
<li>Pareto problem: $\max u_1(x_1, G)$ subject to $u_i(x_i, G) \geq \bar u_i$ for $i \geq 2$ and the resource constraint, with multipliers $\lambda_i$ and $\mu$.</li>
<li>FOC in $x_i$: $\partial u_i / \partial x_i = \mu$ for all $i$. So $\mu$ is the common shadow value of the private good.</li>
<li>FOC in $G$: $\sum_i \lambda_i (\partial u_i / \partial G) = \mu c'(G)$, with $\lambda_1 = 1$.</li>
<li>Divide the $G$-FOC by $\mu$ and use $\lambda_i = \mu / (\partial u_i / \partial x_i)$ implied by the $x_i$-FOCs: $\sum_i (\partial u_i/\partial G)/(\partial u_i / \partial x_i) = c'(G)$, which is $\sum_i MRS^i_{Gx} = MRT_{Gx}$.</li>
</ol>

<p>Comparison with private provision. If each consumer chooses contribution $g_i$ taking others' contributions as given, the Nash FOC is $MRS^i = c'(G)$ for each contributor. Adding these across contributors gives a sum on the left, but each contributor sets her own MRS equal to MC, not the sum. Result: $G^{Nash} < G^*$, the standard <strong>free-rider</strong> underprovision.</p>

<p>With quasi-linear preferences $u_i = v_i(G) + x_i$, the Samuelson condition simplifies to $\sum_i v_i'(G^*) = c'(G^*)$, which is the FOC used in essay computations. The efficient $G^*$ is independent of the distribution of wealth, a transferable-utility feature inherited from quasi-linearity.</p>

<p>References: Micro2025.pdf Topic 3 Lecture 3; Hindriks and Myles Ch. 6; Varian Ch. 23.</p>""",
        "widget": r"""<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <line x1="70" y1="350" x2="560" y2="350" stroke="#333" stroke-width="1.5"/>
  <line x1="70" y1="350" x2="70" y2="40" stroke="#333" stroke-width="1.5"/>
  <text x="555" y="370" font-size="12">$G$</text>
  <text x="40" y="50" font-size="12">price</text>
  <line x1="70" y1="230" x2="500" y2="320" stroke="#1f77b4" stroke-width="2"/>
  <text x="505" y="320" font-size="12" fill="#1f77b4">$MRS_1$</text>
  <line x1="70" y1="260" x2="500" y2="335" stroke="#2ca02c" stroke-width="2"/>
  <text x="505" y="338" font-size="12" fill="#2ca02c">$MRS_2$</text>
  <line x1="70" y1="290" x2="500" y2="345" stroke="#ff7f0e" stroke-width="2"/>
  <text x="505" y="350" font-size="12" fill="#ff7f0e">$MRS_3$</text>
  <line x1="70" y1="110" x2="500" y2="300" stroke="#d62728" stroke-width="2.5"/>
  <text x="505" y="298" font-size="12" fill="#d62728">$\sum MRS_i$</text>
  <line x1="70" y1="180" x2="500" y2="200" stroke="#555" stroke-width="2"/>
  <text x="505" y="200" font-size="12" fill="#555">$MRT = c'(G)$</text>
  <line x1="285" y1="350" x2="285" y2="190" stroke="#555" stroke-dasharray="4 3"/>
  <circle cx="285" cy="190" r="5" fill="#d62728"/>
  <text x="278" y="368" font-size="12">$G^*$</text>
  <line x1="155" y1="350" x2="155" y2="187" stroke="#888" stroke-dasharray="3 3"/>
  <circle cx="155" cy="187" r="4" fill="#1f77b4"/>
  <text x="148" y="368" font-size="11" fill="#888">$G^{Nash}$</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Vertical sum of marginal willingness to pay (red) crosses MRT at $G^*$. At any single consumer's MRS the curve intersects MRT far to the left, indicating free-rider underprovision $G^{Nash} < G^*$.</p>""",
        "examples": r"""<ul>
<li><strong>National defence</strong> is the textbook pure public good: non-rival (my protection does not diminish yours) and non-excludable. Defence budgets are set by political process, an attempt at implementing the Samuelson condition through voting rather than markets.</li>
<li><strong>Open-source software</strong> (Linux kernel, Wikipedia) is non-rival in use. Empirical work by Lerner and Tirole estimates that voluntary contributions implement a fraction of the Samuelson optimum, with the gap explained by reputational and intrinsic motives, not pure free-riding.</li>
<li><strong>Scientific research basic findings</strong>: a proof or a measured constant is non-rival once published. Government R&D subsidies (UKRI, NSF) are a partial Samuelson-style correction.</li>
<li><strong>Evaluation move:</strong> the practical critique is that the planner cannot observe each $MRS_i$ directly. This motivates the <strong>Clarke-Groves mechanism</strong>, which makes truth-telling a dominant strategy at the cost of failing budget balance (Green and Laffont 1979).</li>
<li><strong>Evaluation move:</strong> distinguish pure public goods (national defence) from impure ones (congestible roads, club goods). The Samuelson condition needs modification when there is rivalry at the margin; see Buchanan (1965) on clubs.</li>
<li><strong>Standard limitation:</strong> Bergstrom, Blume, Varian (1986) show that the underprovision result depends on linear contribution technology. With increasing returns to private contribution, Nash equilibria can support corner solutions where a single agent provides everything.</li>
<li>Cross-reference: see [[Concepts/Public Good]] for the rivalry-excludability taxonomy and [[Concepts/Lindahl Prices]] for the decentralised price mechanism that implements the Samuelson allocation.</li>
</ul>""",
    },

    "lindahl-prices": {
        "math": r"""<p><strong>Lindahl prices</strong> (Lindahl 1919) are personalised prices for a public good that decentralise the Samuelson optimum. Each consumer $i$ faces her own price per unit of $G$, denoted $\tau_i$, with $\sum_i \tau_i = c'(G^*)$. Given $\tau_i$, each consumer chooses her preferred $G$, and at a <strong>Lindahl equilibrium</strong> all consumers demand the same quantity, which equals the efficient $G^*$.</p>

<p>Formally, a Lindahl equilibrium is $(\tau_1^*, \dots, \tau_I^*, G^*)$ such that:</p>

<ol>
<li>$G^* \in \arg\max_G \{u_i(\omega_i - \tau_i^* G, G)\}$ for every $i$. Each consumer, taking her own personalised price as given, prefers exactly $G^*$.</li>
<li>$\sum_i \tau_i^* = c'(G^*)$. The personalised prices sum to marginal cost, so the production side breaks even.</li>
</ol>

<p>Derivation in the quasi-linear case $u_i = v_i(G) + x_i$ with $x_i = \omega_i - \tau_i G$:</p>

<ol>
<li>Consumer $i$'s problem: $\max_G v_i(G) - \tau_i G$. FOC: $v_i'(G) = \tau_i$.</li>
<li>For all consumers to demand the same $G$, set $\tau_i^* = v_i'(G^*)$. The price equals the marginal willingness to pay.</li>
<li>Producer side: $\sum_i \tau_i^* = \sum_i v_i'(G^*) = c'(G^*)$ by the Samuelson condition.</li>
<li>Solving these jointly gives the efficient $G^*$ and a personalised price for each consumer equal to her marginal benefit at the optimum.</li>
</ol>

<p>So Lindahl pricing is the analogue of Walrasian pricing for public goods. Just as a competitive equilibrium decentralises Pareto efficiency for private goods via a common price, a Lindahl equilibrium decentralises Samuelson efficiency via personalised prices.</p>

<p><strong>Existence and welfare.</strong> Foley (1970) showed that under standard assumptions (convex preferences, continuous utilities) a Lindahl equilibrium exists. Both Welfare Theorems extend: every Lindahl equilibrium is Pareto efficient, and any efficient public-good allocation can be supported as a Lindahl equilibrium after lump-sum redistribution of the private good.</p>

<p><strong>The implementation problem.</strong> The mechanism requires the planner to know each $v_i'$ to set $\tau_i^*$. Consumers have an incentive to <em>misreport</em>: if I announce a low marginal benefit, my price is reduced while $G$ is barely affected. The Lindahl equilibrium is not <strong>strategy-proof</strong>. This is the central practical objection and motivates the demand-revelation mechanisms (Clarke-Groves) discussed in Topic 3 Lecture 4.</p>

<p>References: Micro2025.pdf Topic 3 Lecture 3; Hindriks and Myles Ch. 6.4; Mas-Colell Ch. 16.</p>""",
        "widget": r"""<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <line x1="70" y1="350" x2="560" y2="350" stroke="#333" stroke-width="1.5"/>
  <line x1="70" y1="350" x2="70" y2="40" stroke="#333" stroke-width="1.5"/>
  <text x="555" y="370" font-size="12">$G$</text>
  <text x="35" y="50" font-size="12">price</text>
  <line x1="70" y1="120" x2="500" y2="290" stroke="#1f77b4" stroke-width="2"/>
  <text x="505" y="290" font-size="12" fill="#1f77b4">$v_1'(G)$</text>
  <line x1="70" y1="200" x2="500" y2="320" stroke="#2ca02c" stroke-width="2"/>
  <text x="505" y="322" font-size="12" fill="#2ca02c">$v_2'(G)$</text>
  <line x1="70" y1="180" x2="500" y2="220" stroke="#555" stroke-width="2"/>
  <text x="505" y="220" font-size="12" fill="#555">$c'(G)$</text>
  <line x1="320" y1="350" x2="320" y2="200" stroke="#888" stroke-dasharray="4 3"/>
  <text x="313" y="368" font-size="12">$G^*$</text>
  <circle cx="320" cy="218" r="4" fill="#1f77b4"/>
  <circle cx="320" cy="290" r="4" fill="#2ca02c"/>
  <line x1="70" y1="218" x2="320" y2="218" stroke="#1f77b4" stroke-dasharray="3 3"/>
  <line x1="70" y1="290" x2="320" y2="290" stroke="#2ca02c" stroke-dasharray="3 3"/>
  <text x="80" y="213" font-size="12" fill="#1f77b4">$\tau_1^* = v_1'(G^*)$</text>
  <text x="80" y="305" font-size="12" fill="#2ca02c">$\tau_2^* = v_2'(G^*)$</text>
  <line x1="350" y1="190" x2="350" y2="260" stroke="#9467bd" stroke-width="2"/>
  <line x1="345" y1="190" x2="355" y2="190" stroke="#9467bd" stroke-width="2"/>
  <line x1="345" y1="260" x2="355" y2="260" stroke="#9467bd" stroke-width="2"/>
  <text x="360" y="230" font-size="12" fill="#9467bd">$\tau_1^* + \tau_2^* = c'(G^*)$</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Two-consumer Lindahl equilibrium. Each consumer's personalised price equals her own $v_i'(G^*)$; the prices sum vertically to the marginal cost, mirroring the Samuelson condition.</p>""",
        "examples": r"""<ul>
<li><strong>Property tax differentials</strong>: Tiebout (1956) sorting across local jurisdictions is sometimes interpreted as approximate Lindahl pricing for local public goods (schools, parks). Households with stronger preference for schools self-select into higher-tax districts.</li>
<li><strong>Voluntary club fees</strong>: members of professional bodies (RSA, BMA) pay different rates based on income or grade, an admittedly crude Lindahl analogue when membership generates partial public-good benefits within the profession.</li>
<li><strong>Carbon contribution funds</strong>: some firms offer customers a per-tonne carbon offset price calibrated to individual willingness to pay, a private experiment in personalised pricing of a public bad.</li>
<li><strong>Evaluation move:</strong> stress that Lindahl prices are a <em>conceptual</em> not <em>implementable</em> solution. Kate Doornik tends to reward essays that note the strategic misreporting problem: announcing $v_i' = 0$ gets the consumer $G^*$ for free if everyone else reports truthfully.</li>
<li><strong>Evaluation move:</strong> Lindahl equilibrium pairs Pareto efficiency with proportional cost sharing by marginal benefit, which has a fairness appeal absent from Samuelson. This is the link to the Lindahl-as-equity argument in Foley (1970).</li>
<li><strong>Standard limitation:</strong> existence relies on convex preferences and continuous utilities; with non-convexities (lumpy public projects like a bridge), Lindahl equilibrium may not exist and integer programming approaches are needed.</li>
<li>Cross-reference: see [[Concepts/Samuelson Condition]] for the efficiency condition Lindahl pricing implements, and [[Concepts/Mechanism Design]] for the strategy-proof alternatives that respond to the implementation critique.</li>
</ul>""",
    },
    "expected-utility": {
        "math": r"""
<p>A lottery $L$ over a finite outcome set $X = \{x_1, \dots, x_n\}$ is a probability vector $(p_1, \dots, p_n)$ with $p_i \geq 0$ and $\sum_i p_i = 1$. A preference relation $\succsim$ on the set of lotteries $\mathcal{L}$ admits an <em>expected utility</em> (vNM) representation if there exists $u : X \to \mathbb{R}$ such that</p>
$$ L \succsim L' \iff U(L) := \sum_{i=1}^n p_i\, u(x_i) \;\geq\; \sum_{i=1}^n p'_i\, u(x_i) = U(L'). $$
<p>The Bernoulli utility $u$ is unique up to a positive affine transformation, $u \mapsto a u + b$ with $a > 0$.</p>

<p><strong>Representation theorem (von Neumann-Morgenstern).</strong> If $\succsim$ on $\mathcal{L}$ satisfies completeness, transitivity, continuity and the independence axiom, then $\succsim$ admits an expected utility representation.</p>

<ol>
  <li>Fix a best lottery $\bar L$ and a worst lottery $\underline L$ with $\bar L \succ \underline L$. By continuity, for every $L$ there is a unique $\alpha(L) \in [0,1]$ such that $L \sim \alpha(L)\bar L + (1-\alpha(L))\underline L$.</li>
  <li>Independence implies $\alpha$ is linear in mixtures: $\alpha(\beta L_1 + (1-\beta) L_2) = \beta \alpha(L_1) + (1-\beta)\alpha(L_2)$.</li>
  <li>Define $U(L) = \alpha(L)$. Linearity in probabilities gives $U(L) = \sum_i p_i U(\delta_{x_i})$, so set $u(x_i) = U(\delta_{x_i})$ and recover $U(L) = \sum_i p_i u(x_i)$.</li>
</ol>

<p><strong>Risk attitudes.</strong> An agent is <em>risk averse</em> iff $u$ is concave, i.e. for any non-degenerate lottery $\tilde w$ with mean $\bar w$,</p>
$$ E[u(\tilde w)] \leq u(\bar w) \quad \text{(Jensen).} $$
<p>The <em>certainty equivalent</em> $\mathrm{CE}$ solves $u(\mathrm{CE}) = E[u(\tilde w)]$, and the <em>risk premium</em> is $\pi = \bar w - \mathrm{CE} \geq 0$ for a risk averse agent. Convex $u$ gives risk loving, linear $u$ risk neutral.</p>

<p>References: Mas-Colell, Whinston, Green Chapter 6.1 to 6.3; Varian Chapter 12; Micro2025.pdf Topic 6.</p>
""",
        "widget": r"""
<div id="widget-expected-utility" style="width:100%; min-height:420px;"></div>
<script>
(function(){
  function draw(){
    if (typeof Plotly === 'undefined') { setTimeout(draw, 200); return; }
    var w = [], u = [];
    for (var i=1; i<=100; i+=0.5){ w.push(i); u.push(Math.sqrt(i)); }
    var w1 = 16, w2 = 81, p = 0.5;
    var EW = p*w1 + (1-p)*w2;
    var EU = p*Math.sqrt(w1) + (1-p)*Math.sqrt(w2);
    var CE = EU*EU;
    var traces = [
      {x: w, y: u, mode:'lines', name:'u(w)=sqrt(w)', line:{color:'#4F9EF7', width:3}},
      {x: [w1, w2], y: [Math.sqrt(w1), Math.sqrt(w2)], mode:'lines+markers',
        name:'lottery chord', line:{color:'#888', dash:'dash'}, marker:{size:8}},
      {x: [EW], y: [Math.sqrt(EW)], mode:'markers+text', name:'u(E[w])',
        marker:{size:10, color:'#2ecc71'}, text:['u(E[w])'], textposition:'top center'},
      {x: [EW], y: [EU], mode:'markers+text', name:'E[u(w)]',
        marker:{size:10, color:'#e67e22'}, text:['E[u(w)]'], textposition:'bottom center'},
      {x: [CE], y: [EU], mode:'markers+text', name:'CE',
        marker:{size:10, color:'#e74c3c'}, text:['CE'], textposition:'bottom left'},
      {x: [CE, EW], y: [EU, EU], mode:'lines', name:'risk premium',
        line:{color:'#e74c3c', width:2}}
    ];
    var layout = {
      title:'Expected utility, certainty equivalent and risk premium',
      paper_bgcolor:'rgba(0,0,0,0)', plot_bgcolor:'rgba(0,0,0,0)',
      font:{color:'inherit'},
      xaxis:{title:'wealth w', gridcolor:'rgba(128,128,128,0.2)'},
      yaxis:{title:'utility u(w)', gridcolor:'rgba(128,128,128,0.2)'},
      showlegend:true, margin:{t:50,l:50,r:20,b:50}
    };
    Plotly.newPlot('widget-expected-utility', traces, layout, {responsive:true});
  }
  setTimeout(draw, 500);
})();
</script>
""",
        "examples": r"""<ul>
<li><strong>Insurance demand.</strong> A risk averse agent with concave $u$ pays a premium up to $\pi$ above the actuarially fair price, which explains why insurance markets exist even with positive loading.</li>
<li><strong>Portfolio choice.</strong> Merton's two-fund result and the CAPM rest on a vNM agent maximising $E[u(\tilde w)]$ over risky returns.</li>
<li><strong>Health and labour economics.</strong> Willingness to pay for mortality reduction is derived from $E[u]$ over alive and dead states.</li>
<li><strong>Essay: normative vs descriptive.</strong> vNM is often defended as a coherence requirement (Dutch book style), while Kahneman and Tversky show systematic violations such as the Allais and common ratio paradoxes.</li>
<li><strong>Essay: cardinality without interpersonal comparability.</strong> $u$ is cardinal up to affine transform, so welfare comparisons across agents still require additional assumptions.</li>
<li><strong>Limitation.</strong> EU rules out probability weighting and reference dependence, ignores ambiguity (Ellsberg) and treats state-dependent preferences only with extra structure.</li>
<li>See also [[Concepts/Independence Axiom]] and [[Concepts/Arrow-Pratt ARA]].</li>
</ul>""",
    },
    "independence-axiom": {
        "math": r"""
<p>The <em>independence axiom</em> states that for any three lotteries $L, L', L'' \in \mathcal{L}$ and any $\alpha \in (0,1]$,</p>
$$ L \succsim L' \iff \alpha L + (1-\alpha) L'' \;\succsim\; \alpha L' + (1-\alpha) L''. $$
<p>Mixing both lotteries with the same third lottery $L''$ on the same odds leaves the ranking unchanged. Together with completeness, transitivity and continuity, independence is necessary and sufficient for an expected utility representation.</p>

<p><strong>Linearity in probabilities.</strong> Independence forces the utility functional $U$ to be linear in the probability vector. To see this, take $L, L'$ with $U(L) = U(L')$ and apply independence with $L''$ arbitrary,</p>
$$ U(\alpha L + (1-\alpha) L'') = \alpha U(L) + (1-\alpha) U(L''). $$
<p>Linearity is exactly what makes indifference curves in the probability simplex straight and parallel.</p>

<ol>
  <li>Consider three outcomes $x_1 < x_2 < x_3$. A lottery is a point $(p_1, p_3)$ in the Marschak-Machina triangle, with $p_2 = 1 - p_1 - p_3$.</li>
  <li>Expected utility is $U = p_1 u_1 + (1-p_1-p_3)u_2 + p_3 u_3$, linear in $(p_1, p_3)$.</li>
  <li>Indifference curves $U = \mathrm{const}$ are therefore parallel straight lines with slope $-(u_2 - u_1)/(u_3 - u_2)$.</li>
</ol>

<p><strong>Allais paradox.</strong> Empirically, indifference curves "fan out" near the certainty edge, violating parallelism. Subjects prefer a sure 1m to a lottery with a small chance of 0, yet flip the preference once a common 0.89 probability of 0 is added to both. This is a direct violation of independence with $L''$ equal to "win 0 with probability 1".</p>

<p>References: Mas-Colell, Whinston, Green Chapter 6.B; Machina (1987 JEP); Micro2025.pdf Topic 6 lecture notes.</p>
""",
        "widget": r"""
<div style="width:100%; display:flex; justify-content:center;">
  <svg viewBox="0 0 420 380" xmlns="http://www.w3.org/2000/svg" style="max-width:520px; width:100%; height:auto;">
    <defs>
      <marker id="arr-ia" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
        <path d="M0,0 L6,3 L0,6 z" fill="currentColor"/>
      </marker>
    </defs>
    <g font-family="sans-serif" font-size="12" fill="currentColor" stroke="currentColor">
      <line x1="60" y1="320" x2="360" y2="320" stroke-width="1.5" marker-end="url(#arr-ia)"/>
      <line x1="60" y1="320" x2="60" y2="40" stroke-width="1.5" marker-end="url(#arr-ia)"/>
      <text x="370" y="324" stroke="none">p1</text>
      <text x="44" y="36" stroke="none">p3</text>
      <line x1="60" y1="40" x2="360" y2="320" stroke="#888" stroke-dasharray="4 4"/>
      <text x="52" y="335" stroke="none" fill="currentColor">x2</text>
      <text x="358" y="335" stroke="none" fill="currentColor">x1</text>
      <text x="44" y="52" stroke="none" fill="currentColor">x3</text>
      <g stroke="#4F9EF7" stroke-width="2" fill="none">
        <line x1="60" y1="260" x2="180" y2="40"/>
        <line x1="100" y1="320" x2="280" y2="40"/>
        <line x1="200" y1="320" x2="360" y2="120"/>
        <line x1="280" y1="320" x2="360" y2="220"/>
      </g>
      <text x="180" y="200" stroke="none" fill="#4F9EF7" font-size="11">parallel vNM</text>
      <text x="180" y="216" stroke="none" fill="#4F9EF7" font-size="11">indifference lines</text>
      <g stroke="#e67e22" stroke-width="1.5" stroke-dasharray="3 3" fill="none">
        <path d="M60,250 Q150,180 200,40"/>
        <path d="M120,320 Q220,200 290,40"/>
      </g>
      <text x="240" y="280" stroke="none" fill="#e67e22" font-size="11">Allais "fanning"</text>
      <text x="240" y="296" stroke="none" fill="#e67e22" font-size="11">violates independence</text>
    </g>
  </svg>
</div>
<p style="text-align:center; font-size:0.9em; opacity:0.8;">Marschak-Machina triangle. Outcomes ordered $x_1 &lt; x_2 &lt; x_3$. vNM indifference curves are parallel straight lines; Allais behaviour produces curves that fan out from the lower right.</p>
""",
        "examples": r"""<ul>
<li><strong>Allais common consequence paradox.</strong> Choices over (1m sure vs 0.10 chance of 5m, 0.89 of 1m, 0.01 of 0) and over (0.11 chance of 1m vs 0.10 chance of 5m) routinely reverse, a textbook independence violation.</li>
<li><strong>Common ratio paradox.</strong> Scaling both lotteries by the same factor changes choices, again contradicting independence.</li>
<li><strong>Rabin calibration.</strong> Concave EU with reasonable small stakes risk aversion implies absurd large stakes risk aversion, suggesting the failure is not just probabilities but the EU functional itself.</li>
<li><strong>Essay: normative defence.</strong> Independence can be motivated by a "sure thing" argument: if the third branch is irrelevant when realised, it should be irrelevant ex ante. Debates pit this against the descriptive evidence.</li>
<li><strong>Essay: weakening independence.</strong> Machina's local EU, rank-dependent utility (Quiggin) and cumulative prospect theory all relax independence while keeping monotonicity.</li>
<li><strong>Limitation.</strong> Without independence, dynamic consistency typically breaks, raising the question of whether to model agents as sophisticated, naive or resolute.</li>
<li>See also [[Concepts/Expected Utility]] and [[Concepts/Arrow-Pratt ARA]].</li>
</ul>""",
    },
    "arrow-pratt-ara": {
        "math": r"""
<p>For a twice differentiable Bernoulli utility $u$ with $u' > 0$, the <em>Arrow-Pratt coefficient of absolute risk aversion</em> at wealth $w$ is</p>
$$ A(w) \;=\; -\frac{u''(w)}{u'(w)}. $$
<p>It is invariant to positive affine transformations of $u$, unlike $u''$ alone, so it is a genuine measure of curvature in utility units.</p>

<p><strong>Risk premium approximation.</strong> Consider a small lottery $\tilde \varepsilon$ with $E[\tilde\varepsilon] = 0$ and $\mathrm{Var}(\tilde\varepsilon) = \sigma^2$. The risk premium $\pi(w, \tilde\varepsilon)$ solves</p>
$$ u(w - \pi) \;=\; E[u(w + \tilde\varepsilon)]. $$

<ol>
  <li>Taylor expand the left side: $u(w - \pi) \approx u(w) - \pi u'(w)$ for small $\pi$.</li>
  <li>Taylor expand the right side to second order: $E[u(w+\tilde\varepsilon)] \approx u(w) + u'(w) E[\tilde\varepsilon] + \tfrac{1}{2} u''(w) E[\tilde\varepsilon^2] = u(w) + \tfrac{1}{2} u''(w) \sigma^2$.</li>
  <li>Equate the two expansions and cancel $u(w)$: $-\pi u'(w) = \tfrac{1}{2} u''(w) \sigma^2$.</li>
  <li>Solve for $\pi$, $$ \pi \;\approx\; -\tfrac{1}{2}\frac{u''(w)}{u'(w)}\sigma^2 \;=\; \tfrac{1}{2} A(w)\, \sigma^2. $$</li>
</ol>

<p>So $A(w)$ is, up to a factor of two, the marginal risk premium per unit variance for small risks. The corresponding measure for proportional risks is the <em>relative</em> coefficient $R(w) = w A(w) = -w u''(w)/u'(w)$, with premium $\pi/w \approx \tfrac{1}{2} R(w) \sigma_r^2$ where $\sigma_r$ is the standard deviation of the proportional risk $\tilde\varepsilon/w$.</p>

<p><strong>Pratt's theorem.</strong> The following are equivalent: (i) $A_1(w) \geq A_2(w)$ for all $w$, (ii) $u_1 = \phi \circ u_2$ for some increasing concave $\phi$, (iii) $\pi_1(w, \tilde\varepsilon) \geq \pi_2(w, \tilde\varepsilon)$ for all $w$ and all $\tilde\varepsilon$.</p>

<p>References: Pratt (1964 Econometrica); Mas-Colell, Whinston, Green Chapter 6.C; Gravelle and Rees Chapter 17; Micro2025.pdf Topic 6.</p>
""",
        "widget": r"""
<div style="display:flex; flex-direction:column; gap:8px;">
  <label>Curvature parameter a:
    <input id="ap-slider" type="range" min="0.1" max="3" step="0.1" value="1" style="width:60%; vertical-align:middle;"/>
    <span id="ap-val">1.0</span>
  </label>
  <div>Approximate risk premium $\tfrac{1}{2} A(w)\sigma^2$ at $w=4$, $\sigma^2=1$: <span id="ap-pi">0.5</span></div>
</div>
<div id="widget-arrow-pratt-ara" style="width:100%; min-height:380px;"></div>
<script>
(function(){
  function draw(){
    if (typeof Plotly === 'undefined') { setTimeout(draw, 200); return; }
    var slider = document.getElementById('ap-slider');
    var valEl = document.getElementById('ap-val');
    var piEl = document.getElementById('ap-pi');
    function utility(w, a){ return (1 - Math.exp(-a*w))/a; }
    function compute(a){
      var xs=[], ys=[];
      for (var w=0.1; w<=10; w+=0.1){ xs.push(w); ys.push(utility(w,a)); }
      var w0 = 4, sig2 = 1;
      var pi = 0.5 * a * sig2;
      var EW = w0;
      var Eu = 0.5*utility(w0-1,a) + 0.5*utility(w0+1,a);
      return {xs:xs, ys:ys, pi:pi, EW:EW, Eu:Eu, uEW:utility(EW,a), CE: w0 - pi};
    }
    function plot(a){
      var r = compute(a);
      var traces = [
        {x:r.xs, y:r.ys, mode:'lines', name:'u(w)', line:{color:'#4F9EF7', width:3}},
        {x:[r.EW-1, r.EW+1], y:[utility(r.EW-1,a), utility(r.EW+1,a)],
          mode:'lines+markers', name:'lottery chord', line:{color:'#888', dash:'dash'}},
        {x:[r.CE, r.EW], y:[r.Eu, r.Eu], mode:'lines+markers',
          name:'risk premium', line:{color:'#e74c3c', width:3}}
      ];
      var layout = {
        paper_bgcolor:'rgba(0,0,0,0)', plot_bgcolor:'rgba(0,0,0,0)',
        font:{color:'inherit'},
        xaxis:{title:'wealth', gridcolor:'rgba(128,128,128,0.2)'},
        yaxis:{title:'utility', gridcolor:'rgba(128,128,128,0.2)'},
        margin:{t:30,l:50,r:20,b:50}, showlegend:true
      };
      Plotly.react('widget-arrow-pratt-ara', traces, layout, {responsive:true});
      piEl.textContent = r.pi.toFixed(3);
    }
    slider.addEventListener('input', function(){
      var a = parseFloat(slider.value);
      valEl.textContent = a.toFixed(1);
      plot(a);
    });
    plot(parseFloat(slider.value));
  }
  setTimeout(draw, 500);
})();
</script>
""",
        "examples": r"""<ul>
<li><strong>Insurance pricing.</strong> The maximum premium a household will pay above the fair price is approximately $\tfrac{1}{2} A(w)\sigma^2$, so estimates of $A$ from survey lotteries feed directly into demand for cover.</li>
<li><strong>Portfolio share in risky assets.</strong> Under mean-variance, the optimal risky share is roughly $\mu / (A(w)\sigma^2)$, linking measured $A$ to observed equity holdings.</li>
<li><strong>Health and safety regulation.</strong> Value of statistical life calculations use $A(w)$ implicitly when translating between income and mortality risk tradeoffs.</li>
<li><strong>Essay: why the ratio, not $u''$.</strong> Affine reparameterisations scale $u''$ but cancel in the ratio, so $A$ is the right curvature measure for behaviour.</li>
<li><strong>Essay: Pratt's theorem.</strong> Comparative risk aversion is fully ordinal, $u_1$ is more risk averse than $u_2$ iff one is a concave transform of the other.</li>
<li><strong>Limitation.</strong> The approximation $\pi \approx \tfrac{1}{2} A \sigma^2$ is local; for large risks third moments and higher start to matter, motivating prudence ($-u'''/u''$) and temperance.</li>
<li>See also [[Concepts/CARA Utility]], [[Concepts/CRRA Utility]] and [[Concepts/DARA Utility]].</li>
</ul>""",
    },
    "cara-utility": {
        "math": r"""
<p><em>Constant absolute risk aversion</em> (CARA) is the family of Bernoulli utilities with $A(w) = a$ independent of wealth. The ODE $-u''/u' = a$ integrates to</p>
$$ u(w) \;=\; -\frac{1}{a} e^{-a w}, \qquad a > 0. $$
<p>Up to positive affine transforms this is the unique CARA utility; $a = 0$ gives risk neutrality as a limiting case.</p>

<ol>
  <li>Check $u'(w) = e^{-aw} > 0$ and $u''(w) = -a e^{-aw} < 0$, so $u$ is strictly increasing and concave.</li>
  <li>Compute $A(w) = -u''(w)/u'(w) = a$, constant in $w$.</li>
  <li>Relative risk aversion is $R(w) = w A(w) = a w$, increasing linearly in wealth.</li>
</ol>

<p><strong>Mean-variance form under normality.</strong> Let $\tilde w \sim \mathcal{N}(\mu, \sigma^2)$. Using the moment generating function of the normal,</p>
$$ E[-\tfrac{1}{a} e^{-a \tilde w}] \;=\; -\tfrac{1}{a} \exp\!\left(-a\mu + \tfrac{1}{2} a^2 \sigma^2\right). $$
<p>Since $-\tfrac{1}{a} e^{-a x}$ is monotone in $x$, maximising expected utility is equivalent to maximising</p>
$$ \mu - \tfrac{a}{2}\sigma^2, $$
<p>the canonical mean-variance objective. This is the principal reason CARA plus normal returns is the workhorse of textbook portfolio choice.</p>

<p><strong>Exact risk premium.</strong> For $\tilde\varepsilon \sim \mathcal{N}(0, \sigma^2)$, the certainty equivalent is $\mathrm{CE} = w - \tfrac{a}{2}\sigma^2$, so $\pi = \tfrac{a}{2}\sigma^2$. The risk premium is independent of initial wealth, capturing the "constant absolute" property exactly, not just locally.</p>

<p><strong>Empirical issue.</strong> Wealth invariance is the main weakness: doubling wealth leaves the dollar premium for a given absolute lottery unchanged, which contradicts the observation that richer households accept larger absolute gambles. This motivates moving to CRRA or DARA.</p>

<p>References: Mas-Colell, Whinston, Green Chapter 6.C; Varian Chapter 12.4; Gravelle and Rees Chapter 17.</p>
""",
        "widget": r"""
<div style="display:flex; flex-direction:column; gap:8px;">
  <label>Absolute risk aversion a:
    <input id="cara-slider" type="range" min="0.1" max="2" step="0.05" value="0.5" style="width:60%; vertical-align:middle;"/>
    <span id="cara-val">0.50</span>
  </label>
  <label>Wealth level w:
    <input id="cara-w" type="range" min="1" max="20" step="0.5" value="5" style="width:60%; vertical-align:middle;"/>
    <span id="cara-w-val">5.0</span>
  </label>
  <div>Risk premium for a sigma=1 lottery: <span id="cara-pi">0.25</span> (does not change with w)</div>
</div>
<div id="widget-cara-utility" style="width:100%; min-height:380px;"></div>
<script>
(function(){
  function draw(){
    if (typeof Plotly === 'undefined') { setTimeout(draw, 200); return; }
    var aS = document.getElementById('cara-slider'), aV = document.getElementById('cara-val');
    var wS = document.getElementById('cara-w'), wV = document.getElementById('cara-w-val');
    var piEl = document.getElementById('cara-pi');
    function u(x,a){ return -Math.exp(-a*x)/a; }
    function plot(){
      var a = parseFloat(aS.value), w0 = parseFloat(wS.value);
      aV.textContent = a.toFixed(2); wV.textContent = w0.toFixed(1);
      var xs=[], ys=[];
      for (var x=0.1; x<=25; x+=0.2){ xs.push(x); ys.push(u(x,a)); }
      var sig = 1;
      var pi = 0.5*a*sig*sig;
      piEl.textContent = pi.toFixed(3);
      var Eu = 0.5*u(w0-sig,a) + 0.5*u(w0+sig,a);
      var CE = w0 - pi;
      var traces = [
        {x:xs, y:ys, mode:'lines', name:'u(w) CARA', line:{color:'#4F9EF7', width:3}},
        {x:[w0-sig, w0+sig], y:[u(w0-sig,a), u(w0+sig,a)], mode:'lines+markers',
          name:'lottery chord', line:{color:'#888', dash:'dash'}},
        {x:[CE, w0], y:[Eu, Eu], mode:'lines+markers', name:'risk premium',
          line:{color:'#e74c3c', width:3}}
      ];
      var layout = {
        paper_bgcolor:'rgba(0,0,0,0)', plot_bgcolor:'rgba(0,0,0,0)',
        font:{color:'inherit'},
        xaxis:{title:'wealth', gridcolor:'rgba(128,128,128,0.2)'},
        yaxis:{title:'utility', gridcolor:'rgba(128,128,128,0.2)'},
        margin:{t:30,l:50,r:20,b:50}
      };
      Plotly.react('widget-cara-utility', traces, layout, {responsive:true});
    }
    aS.addEventListener('input', plot); wS.addEventListener('input', plot);
    plot();
  }
  setTimeout(draw, 500);
})();
</script>
""",
        "examples": r"""<ul>
<li><strong>Mean-variance portfolio choice.</strong> CARA preferences with normal returns deliver the textbook risky share $\alpha^* = (\mu - r)/(a\sigma^2)$, used in introductory finance and the original Merton problem when wealth effects are suppressed.</li>
<li><strong>Principal-agent models.</strong> Holmstrom and Milgrom (1987) use CARA plus normal noise so that incentive contracts collapse to a tractable certainty equivalent with risk cost $\tfrac{a}{2}\sigma^2$.</li>
<li><strong>Insurance under additive risk.</strong> Optimal coinsurance with CARA does not depend on initial wealth, a simplifying benchmark even if empirically too strong.</li>
<li><strong>Essay: why CARA is analytically convenient.</strong> Linearity of certainty equivalents in mean and variance removes wealth as a state variable, which makes dynamic problems with normal shocks recursive and closed-form.</li>
<li><strong>Essay: empirical implausibility.</strong> Constant absolute risk aversion implies that a millionaire and a student would reject the same fair gamble of plus or minus 100. Survey and field evidence reject this; richer agents accept larger absolute bets.</li>
<li><strong>Limitation.</strong> CARA implies relative risk aversion $R(w) = aw$ increasing without bound, which clashes with consumption-based asset pricing where roughly constant $R$ is preferred.</li>
<li>See also [[Concepts/CRRA Utility]] and [[Concepts/DARA Utility]].</li>
</ul>""",
    },
    "crra-utility": {
        "math": r"""
<p><em>Constant relative risk aversion</em> (CRRA) is the family with $R(w) = w A(w) = \gamma$ constant. Solving $-w u''/u' = \gamma$ with $u' > 0$ yields the power utility</p>
$$ u(w) \;=\; \begin{cases} \dfrac{w^{1-\gamma}}{1-\gamma} & \gamma > 0,\ \gamma \neq 1, \\[4pt] \ln w & \gamma = 1. \end{cases} $$
<p>$\gamma = 1$ is the limiting log case (apply L'Hopital to the bracket above).</p>

<ol>
  <li>Differentiate, $u'(w) = w^{-\gamma}$ and $u''(w) = -\gamma w^{-\gamma - 1}$.</li>
  <li>Then $A(w) = -u''/u' = \gamma / w$, decreasing in wealth (so CRRA is also DARA whenever $\gamma > 0$).</li>
  <li>Relative risk aversion is $R(w) = w A(w) = \gamma$, constant.</li>
</ol>

<p><strong>Proportional risk premium.</strong> For a small multiplicative lottery $\tilde w = w(1 + \tilde\varepsilon)$ with $E[\tilde\varepsilon] = 0$ and $\mathrm{Var}(\tilde\varepsilon) = \sigma_r^2$, the Arrow-Pratt approximation gives</p>
$$ \frac{\pi}{w} \;\approx\; \tfrac{1}{2} R(w)\, \sigma_r^2 \;=\; \tfrac{1}{2}\gamma\, \sigma_r^2. $$
<p>The risk premium scales proportionally with wealth: a doubling of $w$ doubles the dollar premium for the same proportional risk. This is the empirical regularity CARA fails to capture.</p>

<p><strong>Lognormal closed form.</strong> If $\ln \tilde w \sim \mathcal{N}(m, s^2)$, then $E[u(\tilde w)] = E[\tilde w^{1-\gamma}]/(1-\gamma)$ and using the lognormal moment formula,</p>
$$ \ln \mathrm{CE} \;=\; m + \tfrac{1-\gamma}{2}\, s^2, $$
<p>so $\ln(\bar w / \mathrm{CE}) \approx \tfrac{\gamma}{2} s^2$. Log returns and CRRA together give exact mean-log-variance objectives, the foundation of consumption-based asset pricing.</p>

<p><strong>Stationarity.</strong> CRRA is the only utility for which optimal consumption and portfolio shares are independent of wealth, which is why balanced growth in macro typically requires $\gamma$ constant.</p>

<p>References: Mas-Colell, Whinston, Green Chapter 6.C; Varian Chapter 12; Mehra and Prescott (1985) for the equity premium puzzle; Micro2025.pdf Topic 6.</p>
""",
        "widget": r"""
<div style="display:flex; flex-direction:column; gap:8px;">
  <label>Relative risk aversion gamma:
    <input id="crra-slider" type="range" min="0.2" max="5" step="0.1" value="2" style="width:60%; vertical-align:middle;"/>
    <span id="crra-val">2.0</span>
  </label>
  <label>Wealth level w:
    <input id="crra-w" type="range" min="1" max="20" step="0.5" value="5" style="width:60%; vertical-align:middle;"/>
    <span id="crra-w-val">5.0</span>
  </label>
  <div>Risk premium for proportional sigma=0.2 lottery: <span id="crra-pi">0.20</span> (scales with w)</div>
</div>
<div id="widget-crra-utility" style="width:100%; min-height:380px;"></div>
<script>
(function(){
  function draw(){
    if (typeof Plotly === 'undefined') { setTimeout(draw, 200); return; }
    var gS = document.getElementById('crra-slider'), gV = document.getElementById('crra-val');
    var wS = document.getElementById('crra-w'), wV = document.getElementById('crra-w-val');
    var piEl = document.getElementById('crra-pi');
    function u(x,g){
      if (Math.abs(g-1) < 1e-4) return Math.log(x);
      return Math.pow(x, 1-g)/(1-g);
    }
    function plot(){
      var g = parseFloat(gS.value), w0 = parseFloat(wS.value);
      gV.textContent = g.toFixed(1); wV.textContent = w0.toFixed(1);
      var xs=[], ys=[];
      for (var x=0.2; x<=25; x+=0.2){ xs.push(x); ys.push(u(x,g)); }
      var sigR = 0.2;
      var pi = 0.5 * g * sigR * sigR * w0;
      piEl.textContent = pi.toFixed(3);
      var wlo = w0*(1 - sigR), whi = w0*(1 + sigR);
      var Eu = 0.5*u(wlo,g) + 0.5*u(whi,g);
      var CE = w0 - pi;
      var traces = [
        {x:xs, y:ys, mode:'lines', name:'u(w) CRRA', line:{color:'#4F9EF7', width:3}},
        {x:[wlo, whi], y:[u(wlo,g), u(whi,g)], mode:'lines+markers',
          name:'lottery chord', line:{color:'#888', dash:'dash'}},
        {x:[CE, w0], y:[Eu, Eu], mode:'lines+markers', name:'risk premium',
          line:{color:'#e74c3c', width:3}}
      ];
      var layout = {
        paper_bgcolor:'rgba(0,0,0,0)', plot_bgcolor:'rgba(0,0,0,0)',
        font:{color:'inherit'},
        xaxis:{title:'wealth', gridcolor:'rgba(128,128,128,0.2)'},
        yaxis:{title:'utility', gridcolor:'rgba(128,128,128,0.2)'},
        margin:{t:30,l:50,r:20,b:50}
      };
      Plotly.react('widget-crra-utility', traces, layout, {responsive:true});
    }
    gS.addEventListener('input', plot); wS.addEventListener('input', plot);
    plot();
  }
  setTimeout(draw, 500);
})();
</script>
""",
        "examples": r"""<ul>
<li><strong>Consumption-based asset pricing.</strong> The stochastic discount factor under CRRA is $M_{t+1} = \beta (c_{t+1}/c_t)^{-\gamma}$, giving the Euler equation that underpins Hansen-Singleton and Mehra-Prescott.</li>
<li><strong>Equity premium puzzle.</strong> Matching the historical 6 percent equity premium with reasonable consumption volatility requires $\gamma$ around 30, far above survey estimates near 2 to 4; Mehra and Prescott (1985) is the canonical statement.</li>
<li><strong>Balanced growth in macro.</strong> Log utility ($\gamma = 1$) is the only specification giving a constant savings rate in the Ramsey model, which is why it appears so often in growth theory.</li>
<li><strong>Essay: wealth-invariant portfolio share.</strong> CRRA delivers a risky asset share that is independent of wealth, consistent with the rough constancy of equity portfolio weights across the wealth distribution.</li>
<li><strong>Essay: tension with HARA evidence.</strong> Some field studies find $R$ falling mildly with wealth, motivating HARA forms that nest CRRA and CARA.</li>
<li><strong>Limitation.</strong> CRRA conflates risk aversion with the elasticity of intertemporal substitution ($\mathrm{EIS} = 1/\gamma$), a coupling broken by Epstein-Zin preferences.</li>
<li>See also [[Concepts/CARA Utility]], [[Concepts/DARA Utility]] and [[Concepts/Arrow-Pratt ARA]].</li>
</ul>""",
    },
    "dara-utility": {
        "math": r"""
<p>A utility $u$ exhibits <em>decreasing absolute risk aversion</em> (DARA) if its Arrow-Pratt coefficient is strictly decreasing in wealth,</p>
$$ A(w) \;=\; -\frac{u''(w)}{u'(w)} \quad \text{with} \quad A'(w) < 0. $$
<p>Equivalently, the risk premium $\pi(w, \tilde\varepsilon)$ for a fixed absolute lottery $\tilde\varepsilon$ falls as $w$ rises: richer agents are willing to accept larger dollar gambles.</p>

<p><strong>Characterisation via $u'''$.</strong> Differentiate $A$,</p>
$$ A'(w) \;=\; -\frac{u'''(w) u'(w) - [u''(w)]^2}{[u'(w)]^2}. $$
<p>Hence $A'(w) < 0$ is equivalent to</p>
$$ u'''(w) \;>\; \frac{[u''(w)]^2}{u'(w)} \;>\; 0. $$

<ol>
  <li>DARA therefore requires <em>prudence</em>, $u''' > 0$. Kimball (1990) calls $P(w) = -u'''/u''$ the coefficient of absolute prudence; DARA is the statement $P(w) > A(w)$.</li>
  <li>Examples: log utility has $A(w) = 1/w$, decreasing. Power utility $w^{1-\gamma}/(1-\gamma)$ with $\gamma > 0$ has $A(w) = \gamma/w$, also DARA. Exponential utility is <em>not</em> DARA: $A$ is constant.</li>
  <li>Quadratic utility $u(w) = w - bw^2$ is the canonical counterexample, having <em>increasing</em> ARA on its domain of monotonicity.</li>
</ol>

<p><strong>Implication for precautionary saving.</strong> Under DARA with $u''' > 0$, adding a mean-zero future income risk raises optimal saving relative to the certainty case (Leland 1968, Sandmo 1970, Kimball 1990). The strength of the response is governed by prudence $P(w)$ rather than by $A(w)$ directly.</p>

<p><strong>Implication for portfolio choice.</strong> Under DARA, the dollar holding of a risky asset rises with wealth (Arrow 1965): risky investment is a normal good. CARA forces a constant dollar holding, which contradicts the empirical pattern.</p>

<p>References: Arrow (1965 Aspects of the Theory of Risk Bearing); Kimball (1990 Econometrica); Mas-Colell, Whinston, Green Chapter 6.C; Gravelle and Rees Chapter 17.</p>
""",
        "widget": r"""
<div style="display:flex; flex-direction:column; gap:8px;">
  <label>Wealth w:
    <input id="dara-w" type="range" min="2" max="30" step="0.5" value="5" style="width:60%; vertical-align:middle;"/>
    <span id="dara-w-val">5.0</span>
  </label>
  <div>For sigma=1 lottery: log utility pi = <span id="dara-pi-log">0.10</span>, CARA(a=0.5) pi = <span id="dara-pi-cara">0.25</span></div>
</div>
<div id="widget-dara-utility" style="width:100%; min-height:380px;"></div>
<script>
(function(){
  function draw(){
    if (typeof Plotly === 'undefined') { setTimeout(draw, 200); return; }
    var wS = document.getElementById('dara-w'), wV = document.getElementById('dara-w-val');
    var piLog = document.getElementById('dara-pi-log');
    var piCara = document.getElementById('dara-pi-cara');
    var a = 0.5;
    function uLog(x){ return Math.log(x); }
    function uCara(x){ return -Math.exp(-a*x)/a; }
    function ceLog(w0, sig){
      var Eu = 0.5*uLog(w0-sig) + 0.5*uLog(w0+sig);
      return Math.exp(Eu);
    }
    function plot(){
      var w0 = parseFloat(wS.value);
      wV.textContent = w0.toFixed(1);
      var xs=[], yL=[], yC=[];
      for (var x=0.5; x<=35; x+=0.3){ xs.push(x); yL.push(uLog(x)); yC.push(uCara(x)); }
      var sig = 1;
      var piL = w0 - ceLog(w0, sig);
      var piCa = 0.5 * a * sig * sig;
      piLog.textContent = piL.toFixed(3);
      piCara.textContent = piCa.toFixed(3);
      var traces = [
        {x:xs, y:yL, mode:'lines', name:'log u (DARA)', line:{color:'#4F9EF7', width:3}, yaxis:'y'},
        {x:xs, y:yC, mode:'lines', name:'CARA, a=0.5', line:{color:'#e67e22', width:3}, yaxis:'y2'},
        {x:[w0], y:[uLog(w0)], mode:'markers', name:'w (log)',
          marker:{size:10, color:'#4F9EF7'}, yaxis:'y'},
        {x:[w0], y:[uCara(w0)], mode:'markers', name:'w (CARA)',
          marker:{size:10, color:'#e67e22'}, yaxis:'y2'}
      ];
      var layout = {
        paper_bgcolor:'rgba(0,0,0,0)', plot_bgcolor:'rgba(0,0,0,0)',
        font:{color:'inherit'},
        xaxis:{title:'wealth', gridcolor:'rgba(128,128,128,0.2)'},
        yaxis:{title:'log u', gridcolor:'rgba(128,128,128,0.2)', side:'left'},
        yaxis2:{title:'CARA u', overlaying:'y', side:'right', showgrid:false},
        margin:{t:30,l:50,r:60,b:50}, legend:{orientation:'h'}
      };
      Plotly.react('widget-dara-utility', traces, layout, {responsive:true});
    }
    wS.addEventListener('input', plot);
    plot();
  }
  setTimeout(draw, 500);
})();
</script>
""",
        "examples": r"""<ul>
<li><strong>Precautionary saving.</strong> Empirical and quantitative life-cycle work uses DARA preferences to generate the observed buffer-stock saving response to income risk; without prudence the consumption Euler equation is certainty-equivalent.</li>
<li><strong>Risky asset as a normal good.</strong> Arrow's theorem says dollar holdings of risky assets rise with wealth iff utility is DARA. SCF and HRS data are consistent with weak DARA in the cross section.</li>
<li><strong>Development and microinsurance.</strong> DARA rationalises why poor households appear extremely risk averse to small absolute losses, while wealthier ones tolerate larger absolute exposures.</li>
<li><strong>Essay: prudence vs risk aversion.</strong> $A$ governs the willingness to bear risk, $P = -u'''/u''$ governs the response of saving to risk. DARA needs $P > A$, so prudence has to dominate the curvature effect.</li>
<li><strong>Essay: ranking common utilities.</strong> Quadratic is IARA (bad), CARA is constant, log and power with $\gamma > 0$ are DARA, HARA nests all three on its domain.</li>
<li><strong>Limitation.</strong> DARA is a qualitative property; without restricting to CRRA or HARA, it does not pin down the level of risk aversion, so calibration still needs an extra moment.</li>
<li>See also [[Concepts/CARA Utility]], [[Concepts/CRRA Utility]] and [[Concepts/Arrow-Pratt ARA]].</li>
</ul>""",
    },
    "adverse-selection": {
        "math": r"""<p>Akerlof's lemons model. Sellers know quality $q \in [0, \bar q]$ with density $f(q)$; buyers see only the distribution. Buyers' willingness to pay is $\beta \cdot \mathbb{E}[q \mid \text{traded}]$ with $\beta > 1$, sellers' reservation is $q$ itself.</p>
<ol>
<li>At candidate price $p$, only types with $q \leq p$ choose to sell.</li>
<li>Conditional expected quality is $\bar q(p) = \mathbb{E}[q \mid q \leq p]$.</li>
<li>Market-clearing price satisfies $p = \beta \cdot \bar q(p)$.</li>
<li>If $\beta \cdot \bar q(p) < p$ for every $p > 0$, the only equilibrium has zero trade (full unravelling). With a uniform $[0,1]$ distribution and $\beta < 2$, this is the unique outcome.</li>
</ol>
<p>The market breaks because each price selects only worse-than-expected sellers, dragging the price down to the floor. See Lecture 7, Gravelle and Rees Ch 19.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:600px;background:#fff">
  <line x1="60" y1="280" x2="560" y2="280" stroke="#333" />
  <line x1="60" y1="280" x2="60" y2="40" stroke="#333" />
  <text x="300" y="305" text-anchor="middle" font-size="13">Quality $q$ (sellers willing to trade)</text>
  <text x="20" y="160" text-anchor="middle" font-size="13" transform="rotate(-90 20,160)">Price</text>
  <line x1="60" y1="280" x2="560" y2="40" stroke="#5b8def" stroke-width="2" />
  <text x="500" y="60" fill="#5b8def" font-size="13">supply: $p = q$</text>
  <line x1="60" y1="280" x2="560" y2="200" stroke="#d81b60" stroke-width="2" />
  <text x="500" y="190" fill="#d81b60" font-size="13">demand: $p = 1.5 \bar q$</text>
  <circle cx="60" cy="280" r="6" fill="#333" />
  <text x="80" y="275" font-size="12">unique equilibrium at $p = 0$</text>
</svg>
<p style="font-size:.88em;color:var(--text-soft)">Demand line for $\beta = 1.5$ sits below the supply line for all $q > 0$, so the lemons market unravels to zero trade.</p>""",
        "examples": r"""<ul>
<li><strong>Health insurance markets (US, pre-ACA).</strong> High-risk types disproportionately buy; community-rated premia rise; healthy types drop out. The ACA's individual mandate was a direct response.</li>
<li><strong>Used cars (Akerlof 1970).</strong> Original motivating example. Mitigations: dealer warranties, lemon laws, manufacturer-certified pre-owned schemes.</li>
<li><strong>Job markets for senior hires.</strong> Outside options are private; high types may signal via track record, degrees, or interview tests.</li>
<li><strong>Essay move (2024 Q9).</strong> Contrast AS with moral hazard: AS is about hidden type at the moment of contracting; MH is about hidden action after contracting. Both vanish under symmetric information; under asymmetric information, only one is relevant per context.</li>
<li><strong>Essay move.</strong> Mitigations: signalling (Spence), screening (Rothschild-Stiglitz), mandatory pooling (ACA, social insurance), warranties (reimbursement contracts).</li>
<li>See also [[Concepts/Akerlof Lemons Market]], [[Concepts/Spence Signalling]], [[Concepts/Rothschild-Stiglitz Screening]], [[Concepts/Moral Hazard]].</li>
</ul>""",
    },
    "moral-hazard": {
        "math": r"""<p>Risk-averse agent, risk-neutral principal, two effort levels $e_L, e_H$ with $c(e_H) > c(e_L)$, two outcomes (high profit $\pi_H$, low profit $\pi_L$) with $\Pr(\pi_H \mid e_H) = p_H > p_L = \Pr(\pi_H \mid e_L)$.</p>
<p>The principal designs wages $(w_L, w_H)$ paid contingent on observed profit. The agent solves:</p>
$$\max_{e} \; \Pr(\pi_H \mid e) u(w_H) + \Pr(\pi_L \mid e) u(w_L) - c(e).$$
<ol>
<li><strong>IR:</strong> $p_H u(w_H) + (1 - p_H) u(w_L) - c(e_H) \geq \bar u$.</li>
<li><strong>IC:</strong> $[p_H - p_L] [u(w_H) - u(w_L)] \geq c(e_H) - c(e_L)$.</li>
<li>Observable effort: principal sets a flat wage $w^* = u^{-1}(\bar u + c(e_H))$, agent bears no risk, first-best is implemented.</li>
<li>Unobservable effort: both IR and IC bind. Solving with $u(w) = \sqrt{w}$ yields a two-equation linear system in $\sqrt{w_L}, \sqrt{w_H}$ and the second-best wages satisfy $w_H > w_L$.</li>
</ol>
<p>See Bolton and Dewatripont Ch 4, Laffont and Martimort Ch 4.</p>""",
        "widget": r"""<svg viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:600px;background:#fff">
  <line x1="60" y1="320" x2="560" y2="320" stroke="#333" />
  <line x1="60" y1="320" x2="60" y2="40" stroke="#333" />
  <text x="300" y="345" text-anchor="middle" font-size="13">$w_L$</text>
  <text x="30" y="180" text-anchor="middle" font-size="13" transform="rotate(-90 30,180)">$w_H$</text>
  <path d="M 60,260 Q 250,200 400,140 T 560,80" stroke="#5b8def" stroke-width="2" fill="none" />
  <text x="430" y="125" fill="#5b8def" font-size="12">IR binding (high effort)</text>
  <line x1="60" y1="290" x2="560" y2="90" stroke="#d81b60" stroke-width="2" />
  <text x="420" y="170" fill="#d81b60" font-size="12">IC binding</text>
  <circle cx="245" cy="180" r="6" fill="#333" />
  <text x="255" y="175" font-size="12">$(w_L^{**}, w_H^{**})$</text>
  <line x1="60" y1="320" x2="560" y2="40" stroke="#999" stroke-dasharray="4" />
  <text x="500" y="55" fill="#999" font-size="12">$w_L = w_H$ (first-best)</text>
</svg>
<p style="font-size:.88em;color:var(--text-soft)">Second-best contract sits where IR and IC both bind. Distance from the 45-degree line measures the risk imposed on the agent.</p>""",
        "examples": r"""<ul>
<li><strong>Executive compensation.</strong> Stock and option grants tie pay to firm performance to motivate effort. Critics: signal noise (CEO performance hard to attribute), risk imposed on managers.</li>
<li><strong>Insurance deductibles.</strong> Co-pays and deductibles keep insured agents partly exposed to losses so they take care. Pure first-dollar coverage maximises moral hazard.</li>
<li><strong>Bank bailouts (too-big-to-fail).</strong> Implicit bailout guarantees reduce bank-shareholder skin-in-the-game and incentivise excess risk-taking. Dodd-Frank and Basel III impose capital and resolution requirements to push risk-bearing back.</li>
<li><strong>Essay move.</strong> Risk aversion is what creates agency cost. With a risk-neutral agent, selling the firm to the agent implements first-best.</li>
<li><strong>Essay move (Peltzman effect).</strong> When safety improves (seatbelts, airbags, anti-lock brakes) agents drive faster; net safety gain is smaller than the engineering effect alone.</li>
<li>See also [[Concepts/Principal-Agent Problem]], [[Concepts/Incentive Compatibility]], [[Concepts/Agency Cost]], [[Concepts/Linear Contracts]].</li>
</ul>""",
    },
    "principal-agent-problem": {
        "math": r"""<p>Canonical two-state two-effort setup. Agent has $u(w) = \sqrt{w}$ and effort costs $c(e_L) = 0$, $c(e_H) = c$. Probabilities of the high outcome are $p_H$ under high effort and $p_L < p_H$ under low effort.</p>
<p>The principal implementing high effort solves:</p>
$$\min_{w_L, w_H} p_H w_H + (1 - p_H) w_L \quad \text{s.t.}\; \text{IR}, \text{IC}.$$
<ol>
<li>IR: $p_H \sqrt{w_H} + (1 - p_H) \sqrt{w_L} - c \geq \bar u$.</li>
<li>IC: $(p_H - p_L)(\sqrt{w_H} - \sqrt{w_L}) \geq c$.</li>
<li>Both bind at the optimum. Let $u_H = \sqrt{w_H}, u_L = \sqrt{w_L}$. Then $u_H - u_L = c / (p_H - p_L)$ and $p_H u_H + (1 - p_H) u_L = \bar u + c$.</li>
<li>Solve linearly: $u_L = \bar u + c - p_H \cdot c / (p_H - p_L)$ and $u_H = u_L + c / (p_H - p_L)$.</li>
<li>Wages: $w_L^{**} = u_L^2, w_H^{**} = u_H^2$.</li>
</ol>
<p>The principal compares the expected profit under high effort (with these wages) against the first-best low-effort profit (flat wage $\bar u^2$) to decide which effort to implement.</p>""",
        "widget": r"""<svg viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:600px;background:#fff">
  <line x1="60" y1="320" x2="560" y2="320" stroke="#333" />
  <line x1="60" y1="320" x2="60" y2="40" stroke="#333" />
  <text x="300" y="345" text-anchor="middle" font-size="13">$w_L$</text>
  <text x="30" y="180" text-anchor="middle" font-size="13" transform="rotate(-90 30,180)">$w_H$</text>
  <circle cx="200" cy="200" r="6" fill="#5b8def" />
  <text x="210" y="195" font-size="12" fill="#5b8def">first-best $(w^*, w^*)$</text>
  <circle cx="120" cy="120" r="6" fill="#d81b60" />
  <text x="130" y="115" font-size="12" fill="#d81b60">second-best $(w_L^{**}, w_H^{**})$</text>
  <rect x="120" y="120" width="80" height="80" fill="#d81b60" fill-opacity="0.1" stroke="#d81b60" stroke-dasharray="3" />
  <text x="245" y="160" font-size="11" fill="#666">risk imposed</text>
</svg>
<p style="font-size:.88em;color:var(--text-soft)">First-best gives a flat wage. Second-best spreads wages around the 45-degree line; the gap is the risk imposed on the agent.</p>""",
        "examples": r"""<ul>
<li><strong>CEO pay.</strong> Stock options align CEO incentives with shareholder returns but expose CEOs to market risk they cannot diversify (firm-specific human capital plus equity grant).</li>
<li><strong>Sharecropping.</strong> Landlord-tenant arrangements split harvest 50-50 to balance risk-sharing with effort incentives.</li>
<li><strong>Franchise contracts.</strong> Franchisor charges franchisee a fixed fee plus royalty rate; the royalty captures incentive intensity.</li>
<li><strong>Essay move.</strong> Agency cost rises with risk aversion ($r$) and output noise ($\sigma^2$). Low-noise output measures shrink the second-best wage spread.</li>
<li><strong>Essay move.</strong> When the principal can monitor effort cheaply (modern productivity-tracking tools), the second-best collapses toward first-best.</li>
<li>See also [[Concepts/Individual Rationality]], [[Concepts/Incentive Compatibility]], [[Concepts/Agency Cost]], [[Concepts/Linear Contracts]].</li>
</ul>""",
    },
    "individual-rationality": {
        "math": r"""<p>The participation constraint. The agent will sign the contract only if expected utility under the chosen effort meets or exceeds the outside option $\bar u$:</p>
$$\sum_i p_i(e^*) u(w_i) - c(e^*) \geq \bar u.$$
<ol>
<li>$\bar u$ is the agent's reservation utility, given by their best outside option (next-best job, unemployment benefit, etc.).</li>
<li>At the principal's optimum, IR binds: any slack means the principal could reduce wages by a small amount and still attract the agent, raising profit. So IR holds with equality.</li>
<li>Binding IR pins down the level of expected utility offered. The principal extracts all surplus above $\bar u$.</li>
<li>Comparative statics: a tighter labour market raises $\bar u$, shifts IR outward, and reduces principal profit. Government wage floors or unemployment benefits operate the same way.</li>
</ol>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:600px;background:#fff">
  <line x1="60" y1="280" x2="560" y2="280" stroke="#333" />
  <line x1="60" y1="280" x2="60" y2="40" stroke="#333" />
  <text x="300" y="305" text-anchor="middle" font-size="13">$w$</text>
  <text x="30" y="160" text-anchor="middle" font-size="13" transform="rotate(-90 30,160)">$u(w) = \sqrt{w}$</text>
  <path d="M 60,280 Q 200,140 560,80" stroke="#5b8def" stroke-width="2" fill="none" />
  <line x1="60" y1="180" x2="560" y2="180" stroke="#d81b60" stroke-dasharray="4" />
  <text x="450" y="170" fill="#d81b60" font-size="12">reservation $\bar u$</text>
  <line x1="280" y1="280" x2="280" y2="180" stroke="#666" stroke-dasharray="3" />
  <text x="290" y="270" font-size="12" fill="#666">$w^*$ where IR binds</text>
</svg>
<p style="font-size:.88em;color:var(--text-soft)">IR pins down the wage at which the agent is exactly indifferent between accepting and walking away.</p>""",
        "examples": r"""<ul>
<li><strong>Reservation wages.</strong> Empirical labour-economics estimates put reservation wages around 80 to 90 percent of last earned wage in the first months of unemployment, rising as benefits run down.</li>
<li><strong>Health insurance markets.</strong> If the outside option is uninsured catastrophe risk, IR is satisfied at relatively unfavourable contract terms; mandatory pooling tightens IR for low-risk types.</li>
<li><strong>Workfare programmes.</strong> Conditional benefits raise $\bar u$ for low-skill workers, pushing employers to raise wages.</li>
<li><strong>Essay move.</strong> Surplus extraction is the principal's reward for designing the contract. If competition forces the principal to compete for the agent (multiple principals), the IR slack accrues to the agent as rent.</li>
<li><strong>Limitation.</strong> Real outside options depend on search frictions, information about job availability, and bargaining timing; the static IR model is a useful abstraction not an exact prediction.</li>
<li>See also [[Concepts/Principal-Agent Problem]], [[Concepts/Incentive Compatibility]], [[Concepts/First-Best Contract]].</li>
</ul>""",
    },
    "incentive-compatibility": {
        "math": r"""<p>The agent must weakly prefer the principal's desired effort to any other effort. In a two-effort model, this is the IC constraint:</p>
$$\sum_i [p_i(e_H) - p_i(e_L)] u(w_i) \geq c(e_H) - c(e_L).$$
<ol>
<li>The left-hand side is the difference in expected utility from the wage schedule between high and low effort. The right-hand side is the extra effort cost.</li>
<li>For two states with high and low outcomes, IC becomes $(p_H - p_L)[u(w_H) - u(w_L)] \geq c(e_H) - c(e_L)$.</li>
<li>IC creates a wedge: $w_H$ must exceed $w_L$ by enough to compensate the agent for the higher effort cost. The size of the wedge depends on $(p_H - p_L)$, the signal-to-effort ratio.</li>
<li>Informativeness principle (Holmstrom 1979): any signal correlated with effort, beyond profit, should enter the optimal wage schedule. Conversely, signals uncorrelated with effort should not.</li>
</ol>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:600px;background:#fff">
  <line x1="60" y1="280" x2="560" y2="280" stroke="#333" />
  <line x1="60" y1="280" x2="60" y2="40" stroke="#333" />
  <text x="300" y="305" text-anchor="middle" font-size="13">$\sqrt{w_L}$</text>
  <text x="30" y="160" text-anchor="middle" font-size="13" transform="rotate(-90 30,160)">$\sqrt{w_H}$</text>
  <line x1="60" y1="240" x2="500" y2="40" stroke="#d81b60" stroke-width="2" />
  <text x="380" y="80" fill="#d81b60" font-size="12">IC: $\sqrt{w_H} - \sqrt{w_L} \geq c/(p_H - p_L)$</text>
  <line x1="60" y1="280" x2="560" y2="40" stroke="#999" stroke-dasharray="4" />
  <text x="500" y="55" fill="#999" font-size="12">$w_L = w_H$</text>
  <polygon points="60,240 500,40 560,40 560,280 60,280" fill="#d81b60" fill-opacity="0.07" />
  <text x="200" y="200" font-size="12" fill="#d81b60">IC-feasible region</text>
</svg>
<p style="font-size:.88em;color:var(--text-soft)">IC requires the wage schedule to lie below the dashed line. The wedge $c/(p_H - p_L)$ is the minimum incentive intensity.</p>""",
        "examples": r"""<ul>
<li><strong>Executive stock options.</strong> The strike price and vesting schedule are calibrated so that CEO effort changes option value enough to offset the effort cost.</li>
<li><strong>Sales commissions.</strong> Per-unit commission rate plus base salary is a classic linear contract; commission rate captures incentive intensity.</li>
<li><strong>Relative performance evaluation.</strong> Including peer firms' performance in the bonus formula filters out common shocks (a Holmstrom informativeness application).</li>
<li><strong>Clawback clauses.</strong> Recover paid bonuses if performance is later restated; effectively sharpens IC by removing the upside reward without sustained good performance.</li>
<li><strong>Essay move.</strong> IC is binding only when effort is unobservable; with observable effort, the principal sets a flat wage and forces $e_H$ by contract.</li>
<li>See also [[Concepts/Individual Rationality]], [[Concepts/Principal-Agent Problem]], [[Concepts/Linear Contracts]].</li>
</ul>""",
    },
    "agency-cost": {
        "math": r"""<p>The welfare loss from unobservable effort. Let $\pi^{FB}$ be the principal's expected profit when effort is observable (first-best) and $\pi^{SB}$ when it is not (second-best). Agency cost is</p>
$$AC = \pi^{FB} - \pi^{SB} \geq 0.$$
<ol>
<li>Two components. (i) Risk premium: $w_L^{**} \neq w_H^{**}$ imposes risk; the principal must raise expected wage to keep IR binding. (ii) Effort distortion: if $AC$ is large, the principal may prefer to implement low effort, foregoing the surplus from high effort.</li>
<li>Two-state $\sqrt{w}$ algebra: $AC = (p_H - p_L) \cdot c \cdot \big[ \text{wage spread term} \big]$. With binding IR and IC, the wage spread scales as $c / (p_H - p_L)$.</li>
<li>$AC$ is increasing in agent risk aversion (curvature of $u$), in the gap $c(e_H) - c(e_L)$, and decreasing in the signal informativeness $p_H - p_L$.</li>
<li>$AC$ falls to zero when (a) effort is observable, (b) the agent is risk neutral (sell the firm), or (c) the signal perfectly reveals effort.</li>
</ol>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:600px;background:#fff">
  <line x1="60" y1="280" x2="560" y2="280" stroke="#333" />
  <line x1="60" y1="280" x2="60" y2="40" stroke="#333" />
  <text x="300" y="305" text-anchor="middle" font-size="13">scenario</text>
  <text x="30" y="160" text-anchor="middle" font-size="13" transform="rotate(-90 30,160)">expected profit</text>
  <rect x="120" y="100" width="120" height="180" fill="#5b8def" />
  <text x="180" y="295" text-anchor="middle" font-size="12">first-best</text>
  <text x="180" y="90" text-anchor="middle" font-size="12" fill="#5b8def">$\pi^{FB}$</text>
  <rect x="320" y="160" width="120" height="120" fill="#d81b60" />
  <text x="380" y="295" text-anchor="middle" font-size="12">second-best</text>
  <text x="380" y="150" text-anchor="middle" font-size="12" fill="#d81b60">$\pi^{SB}$</text>
  <rect x="320" y="100" width="120" height="60" fill="#fbb6ce" fill-opacity="0.7" />
  <text x="380" y="135" text-anchor="middle" font-size="12" fill="#742a2a">agency cost $AC$</text>
</svg>
<p style="font-size:.88em;color:var(--text-soft)">The pink bar is the welfare loss from unobservable effort: foregone surplus plus risk premium.</p>""",
        "examples": r"""<ul>
<li><strong>Executive pay-for-performance literature.</strong> Estimated agency cost of unobserved CEO effort is in the order of 1 to 3 percent of firm value in S&P 500 companies.</li>
<li><strong>Microcredit and joint-liability lending.</strong> Group-lending arrangements push the agency cost back onto borrowers via peer monitoring (cheaper signal of effort).</li>
<li><strong>Government contracting.</strong> Cost-plus contracts have higher agency cost than fixed-price contracts; the optimal mix depends on cost uncertainty (Laffont-Tirole).</li>
<li><strong>Essay move.</strong> Higher signal informativeness shrinks $AC$. Real-time productivity tracking, performance ranking against peers, and post-trade reporting are all attempts to raise the signal.</li>
<li><strong>Essay move (2024 Q9).</strong> AC is the canonical welfare cost of moral hazard. Compare to the analogous cost of adverse selection (loss from full unravelling): both vanish under symmetric information.</li>
<li>See also [[Concepts/Moral Hazard]], [[Concepts/Principal-Agent Problem]], [[Concepts/Risk vs Insurance Trade-off]].</li>
</ul>""",
    },
}
