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

    "walras-law": {
        "math": r"""
<p><strong>Statement.</strong> In a pure exchange economy with $L$ goods, $I$ consumers, endowments $\omega^i \in \mathbb{R}^L_+$ and Walrasian demand $x^i(p, p\cdot\omega^i)$, define aggregate excess demand $z(p) = \sum_i \bigl(x^i(p, p\cdot\omega^i) - \omega^i\bigr)$. Walras' Law states that for every price vector $p \in \mathbb{R}^L_{++}$,</p>
<p>$$p \cdot z(p) \equiv 0.$$</p>
<p><strong>Derivation.</strong> The derivation rests on individual budget balance under local non-satiation.</p>
<ol>
<li>Each consumer $i$ chooses $x^i$ to maximise $u^i$ subject to $p\cdot x^i \le p\cdot \omega^i$. With local non-satiation the budget constraint binds, so $p\cdot x^i(p, p\cdot\omega^i) = p\cdot \omega^i$.</li>
<li>Summing across all $I$ consumers gives $\sum_i p\cdot x^i = \sum_i p\cdot \omega^i$, i.e. $p\cdot \sum_i x^i = p\cdot \sum_i \omega^i$.</li>
<li>Subtracting the right side from the left, $p\cdot \bigl(\sum_i x^i - \sum_i \omega^i\bigr) = 0$, which is $p\cdot z(p) = 0$.</li>
</ol>
<p><strong>The $n-1$ corollary.</strong> Suppose markets $1, \dots, L-1$ all clear, i.e. $z_\ell(p) = 0$ for $\ell = 1, \dots, L-1$. Then $p_L z_L(p) = p\cdot z(p) - \sum_{\ell < L} p_\ell z_\ell(p) = 0$. Since $p_L > 0$, we get $z_L(p) = 0$. So one market clearing condition is redundant.</p>
<p><strong>Caveat.</strong> Walras' Law is an identity in $p$, not a market clearing statement. It says spending equals income in value, not that quantities clear. Equilibrium adds $z(p^*) = 0$, which (combined with $p\cdot z \equiv 0$) is what we solve for.</p>
<p><em>Sources.</em> Micro2025.pdf Lecture 1; Varian <em>Microeconomic Analysis</em> Ch. 17.4; Mas-Colell, Whinston, Green Ch. 15.B; Hindriks and Myles Ch. 2.</p>
""",
        "widget": r"""
<svg id="widget-walras-law" viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <text x="300" y="30" text-anchor="middle" font-size="14" font-weight="bold">Excess demands sum to zero in value</text>
  <line x1="60" y1="240" x2="540" y2="240" stroke="#333"/>
  <text x="60" y="258" font-size="11">Good 1</text>
  <text x="200" y="258" font-size="11">Good 2</text>
  <text x="340" y="258" font-size="11">Good 3</text>
  <text x="480" y="258" font-size="11">Sum (value)</text>
  <rect x="80" y="140" width="60" height="100" fill="#4a90e2" opacity="0.8"/>
  <text x="110" y="135" text-anchor="middle" font-size="11">+30</text>
  <rect x="220" y="180" width="60" height="60" fill="#4a90e2" opacity="0.8"/>
  <text x="250" y="175" text-anchor="middle" font-size="11">+15</text>
  <rect x="360" y="240" width="60" height="45" fill="#e25c5c" opacity="0.8"/>
  <text x="390" y="300" text-anchor="middle" font-size="11">-45</text>
  <rect x="500" y="239" width="40" height="2" fill="#333"/>
  <text x="520" y="235" text-anchor="middle" font-size="11" font-weight="bold">0</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Walras' Law: weighted by prices, market imbalances must offset across goods.</p>
""",
        "examples": r"""
<ul>
<li><strong>Computing GE in textbook problems:</strong> when asked to solve a two-good exchange economy, set one market clearing condition and use Walras' Law to confirm the second clears automatically. Saves a tedious algebra step.</li>
<li><strong>CGE policy models:</strong> applied general equilibrium models (e.g. GTAP for trade policy) impose Walras' Law as a consistency check on the numerical code. A violation flags a bug in the demand or production block.</li>
<li><strong>Essay move (Doornik favourite):</strong> stress that Walras' Law is an identity from budget balance, distinct from equilibrium, which adds the requirement that each $z_\ell = 0$ individually. Confusing the two is the most common Part A error.</li>
<li><strong>Essay move:</strong> link to the numeraire choice. Because $p\cdot z \equiv 0$, multiplying all prices by $\lambda > 0$ does not change excess demand, so equilibria are pinned down only up to scalar multiplication.</li>
<li><strong>Limitation:</strong> if local non-satiation fails (bliss points, satiated preferences), individual budget constraints need not bind and the identity breaks. Walras' Law then becomes an inequality: $p\cdot z(p) \le 0$.</li>
<li><strong>Cross-reference:</strong> see [[Concepts/Excess Demand]] for the homogeneity property that complements Walras' Law in pinning down equilibrium.</li>
</ul>
""",
    },
    "excess-demand": {
        "math": r"""
<p><strong>Definition.</strong> For good $\ell$ at price vector $p$, aggregate excess demand is</p>
<p>$$z_\ell(p) = \sum_{i=1}^{I} x^i_\ell(p, p\cdot\omega^i) - \sum_{i=1}^{I} \omega^i_\ell,$$</p>
<p>i.e. aggregate Marshallian demand minus aggregate endowment. The vector $z(p) = (z_1(p), \dots, z_L(p))$ is the aggregate excess demand function.</p>
<p><strong>Three properties.</strong></p>
<ol>
<li><em>Continuity.</em> If every $x^i$ is continuous in $p$ (which holds for strictly convex preferences), $z(p)$ is continuous on $\mathbb{R}^L_{++}$.</li>
<li><em>Homogeneity of degree zero.</em> For any $\lambda > 0$, $z(\lambda p) = z(p)$. Budget sets are invariant to proportional price scaling.</li>
<li><em>Walras' Law.</em> $p\cdot z(p) = 0$ for all $p \in \mathbb{R}^L_{++}$.</li>
</ol>
<p><strong>Equilibrium.</strong> A Walrasian equilibrium is a price vector $p^*$ such that $z(p^*) \le 0$, with $z_\ell(p^*) = 0$ whenever $p^*_\ell > 0$. Under free disposal we usually look for $z(p^*) = 0$ exactly.</p>
<p><strong>Tatonnement intuition.</strong> Out of equilibrium, the auctioneer adjusts prices in the direction of excess demand:</p>
<p>$$\dot p_\ell = \kappa_\ell z_\ell(p), \quad \kappa_\ell > 0.$$</p>
<p>Goods in excess demand get more expensive; goods in excess supply get cheaper. Stability of this dynamic requires conditions on $z$ (e.g. gross substitutes); without them, the price adjustment can cycle or diverge (Scarf 1960).</p>
<p><em>Sources.</em> Micro2025.pdf Lecture 1; Varian Ch. 17.5; Mas-Colell, Whinston, Green Ch. 17.B; Hindriks and Myles Ch. 2.2.</p>
""",
        "widget": r"""
<svg id="widget-excess-demand" viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <line x1="60" y1="280" x2="560" y2="280" stroke="#333"/>
  <line x1="300" y1="40" x2="300" y2="280" stroke="#333"/>
  <text x="560" y="295" font-size="11">$p_1/p_2$</text>
  <text x="280" y="40" font-size="11">$z_1$</text>
  <path d="M 80 80 Q 200 160, 300 200 T 540 270" fill="none" stroke="#4a90e2" stroke-width="2"/>
  <circle cx="380" cy="222" r="4" fill="#e25c5c"/>
  <text x="395" y="218" font-size="11" fill="#e25c5c">equilibrium $p^*$</text>
  <line x1="380" y1="222" x2="380" y2="280" stroke="#e25c5c" stroke-dasharray="3,3"/>
  <text x="100" y="120" font-size="11" fill="#4a90e2">$z_1 > 0$: price rises</text>
  <text x="450" y="265" font-size="11" fill="#4a90e2">$z_1 < 0$: price falls</text>
  <text x="305" y="280" font-size="11">0</text>
  <text x="300" y="20" text-anchor="middle" font-size="13" font-weight="bold">Excess demand and tatonnement</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">As the relative price of good 1 rises, its excess demand falls; equilibrium occurs where $z_1(p^*) = 0$.</p>
""",
        "examples": r"""
<ul>
<li><strong>Solving a 2x2 exchange economy:</strong> for Cobb-Douglas agents with shares $\alpha^A, \alpha^B$ and endowments $\omega^A, \omega^B$, compute $z_1(p)$, set to zero and solve for $p_1/p_2$.</li>
<li><strong>Oil price shocks (real-world):</strong> a sudden supply cut generates $z_{\text{oil}}(p) > 0$ at the old price. The price adjusts upward to choke off excess demand. This is the tatonnement story applied to a specific market.</li>
<li><strong>Essay move:</strong> emphasise that homogeneity of degree zero is what justifies normalising prices and discussing only relative prices. Without it, GE would have no determinate solution in nominal terms.</li>
<li><strong>Essay move:</strong> distinguish gross excess demand (what a price-taker would buy) from net trade (gross demand minus endowment). The aggregate identity holds for both, but net trade is the policy-relevant quantity.</li>
<li><strong>Limitation:</strong> aggregate excess demand inherits almost no structure from individual rationality. The Sonnenschein-Mantel-Debreu theorem shows any continuous function satisfying homogeneity and Walras' Law can arise as aggregate $z(p)$.</li>
<li><strong>Cross-reference:</strong> see [[Concepts/Walras Law]] for the value-identity that ties excess demands together.</li>
</ul>
""",
    },
    "homogeneity-degree-zero": {
        "math": r"""
<p><strong>Definition.</strong> A function $f: \mathbb{R}^L_{++} \to \mathbb{R}^k$ is homogeneous of degree zero if $f(\lambda p) = f(p)$ for every $\lambda > 0$ and every $p$. In consumer theory, both Marshallian demand $x^i(p, m)$ (in $(p, m)$ jointly) and aggregate excess demand $z(p)$ have this property.</p>
<p><strong>Derivation for demand.</strong> The consumer solves $\max u(x)$ subject to $p\cdot x \le m$. Scaling $(p, m) \to (\lambda p, \lambda m)$ gives constraint $\lambda p \cdot x \le \lambda m$, equivalent to $p\cdot x \le m$. The feasible set is identical, so the optimum is identical:</p>
<p>$$x(\lambda p, \lambda m) = x(p, m).$$</p>
<p><strong>Derivation for excess demand.</strong> Consumer $i$ has income $m^i = p\cdot \omega^i$ generated by endowments. Scaling prices by $\lambda$ scales income by $\lambda$ as well, so $x^i(\lambda p, \lambda p\cdot \omega^i) = x^i(p, p\cdot\omega^i)$. Hence</p>
<p>$$z(\lambda p) = \sum_i x^i(\lambda p, \lambda p\cdot\omega^i) - \sum_i \omega^i = z(p).$$</p>
<p><strong>Euler's identity.</strong> Differentiating $x_\ell(\lambda p, \lambda m) = x_\ell(p, m)$ with respect to $\lambda$ at $\lambda = 1$ yields</p>
<p>$$\sum_{k=1}^{L} p_k \frac{\partial x_\ell}{\partial p_k} + m \frac{\partial x_\ell}{\partial m} = 0.$$</p>
<p>This relates own-price, cross-price, and income effects: useful in checking demand-system estimates for internal consistency.</p>
<p><strong>Implication.</strong> Only relative prices matter, so we can pick a numeraire and normalise one price to 1. The equilibrium price vector is determined only up to a positive scalar.</p>
<p><em>Sources.</em> Micro2025.pdf Lecture 1; Varian Ch. 7.1, 17.5; Mas-Colell, Whinston, Green Ch. 2.E.</p>
""",
        "widget": r"""
<svg id="widget-homogeneity-degree-zero" viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <text x="300" y="20" text-anchor="middle" font-size="13" font-weight="bold">Doubling all prices and income leaves the budget set unchanged</text>
  <line x1="60" y1="270" x2="280" y2="270" stroke="#333"/>
  <line x1="60" y1="60" x2="60" y2="270" stroke="#333"/>
  <line x1="60" y1="80" x2="240" y2="270" stroke="#4a90e2" stroke-width="2"/>
  <text x="150" y="155" font-size="11" fill="#4a90e2">($p_x$, $p_y$, $m$)</text>
  <circle cx="140" cy="170" r="4" fill="#e25c5c"/>
  <text x="60" y="285" font-size="11">$x$</text>
  <text x="40" y="65" font-size="11">$y$</text>
  <line x1="340" y1="270" x2="560" y2="270" stroke="#333"/>
  <line x1="340" y1="60" x2="340" y2="270" stroke="#333"/>
  <line x1="340" y1="80" x2="520" y2="270" stroke="#4a90e2" stroke-width="2"/>
  <text x="430" y="155" font-size="11" fill="#4a90e2">($2p_x$, $2p_y$, $2m$)</text>
  <circle cx="420" cy="170" r="4" fill="#e25c5c"/>
  <text x="340" y="285" font-size="11">$x$</text>
  <text x="320" y="65" font-size="11">$y$</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Scaling prices and money income by the same factor leaves real choices unaffected.</p>
""",
        "examples": r"""
<ul>
<li><strong>Inflation accounting:</strong> if a pure unit-of-account change doubles all nominal prices and nominal incomes overnight, real consumption choices and excess demands are unchanged. This is the formal statement of money neutrality in a static GE model.</li>
<li><strong>Currency redenomination:</strong> when Turkey dropped six zeros in 2005, every price and wage scaled identically; nothing real happened. Homogeneity captures the irrelevance of the units.</li>
<li><strong>Essay move:</strong> distinguish homogeneity of degree zero in $(p, m)$ jointly (Marshallian demand) from homogeneity in $p$ alone (Hicksian demand). Mixing these up is a classic exam slip.</li>
<li><strong>Essay move:</strong> link to numeraire choice. Because $z(p)$ has only $L - 1$ degrees of freedom in $p$, we lose nothing by setting $p_L = 1$ and solving for the remaining prices.</li>
<li><strong>Limitation:</strong> if utility depends on nominal balances (cash-in-advance, money-in-the-utility-function), homogeneity fails and money is no longer neutral. This is the entry point into monetary economics.</li>
<li><strong>Cross-reference:</strong> see [[Concepts/Numeraire Good]] for how the property is exploited in practice.</li>
</ul>
""",
    },
    "numeraire-good": {
        "math": r"""
<p><strong>Setup.</strong> In a Walrasian economy with $L$ goods, equilibrium prices satisfy $z(p^*) = 0$. Because $z$ is homogeneous of degree zero, if $p^*$ is an equilibrium so is $\lambda p^*$ for any $\lambda > 0$. So the equilibrium price vector is determined only up to scale: we have $L$ unknowns but only $L - 1$ independent equations (Walras' Law removes one).</p>
<p><strong>Numeraire fix.</strong> Pick one good (say good $L$) and set its price $p_L \equiv 1$. The good is then called the <em>numeraire</em>. All other prices are expressed in units of good $L$: $p_\ell$ is now "units of good $L$ per unit of good $\ell$."</p>
<p><strong>Why it works.</strong> By homogeneity, any equilibrium $p^*$ can be rescaled by $\lambda = 1/p^*_L$ to give $\tilde p^* = p^*/p^*_L$ with $\tilde p^*_L = 1$. So fixing the numeraire selects one representative from each equivalence class of equilibria.</p>
<p><strong>Choice of numeraire.</strong> Conventionally we pick whichever good makes the algebra cleanest:</p>
<ol>
<li><em>Cobb-Douglas problems:</em> setting $p_y = 1$ and solving for $p_x$ often cancels nicely.</li>
<li><em>Trade models:</em> the imported good or "rest-of-world bundle" is a natural numeraire.</li>
<li><em>Monetary models:</em> "money" is the numeraire but does not enter utility, hence the dichotomy between real and nominal.</li>
</ol>
<p><strong>Consequence.</strong> With the numeraire fixed, we have $L - 1$ relative prices and $L - 1$ independent market clearing conditions (after invoking Walras' Law), giving a well-posed system.</p>
<p><em>Sources.</em> Micro2025.pdf Lecture 1; Varian Ch. 17.5; Mas-Colell, Whinston, Green Ch. 15.B.</p>
""",
        "widget": r"""
<svg id="widget-numeraire-good" viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <text x="300" y="22" text-anchor="middle" font-size="13" font-weight="bold">Three equivalent price vectors, one equilibrium</text>
  <rect x="40" y="50" width="160" height="220" fill="#fff" stroke="#333"/>
  <text x="120" y="75" text-anchor="middle" font-size="12" font-weight="bold">$p$</text>
  <text x="60" y="110" font-size="11">$p_1 = 2$</text>
  <text x="60" y="135" font-size="11">$p_2 = 4$</text>
  <text x="60" y="160" font-size="11">$p_3 = 6$</text>
  <text x="60" y="230" font-size="11" fill="#555">ratios 1 : 2 : 3</text>
  <rect x="220" y="50" width="160" height="220" fill="#fff" stroke="#333"/>
  <text x="300" y="75" text-anchor="middle" font-size="12" font-weight="bold">$p / p_3$</text>
  <text x="240" y="110" font-size="11">$p_1 = 1/3$</text>
  <text x="240" y="135" font-size="11">$p_2 = 2/3$</text>
  <text x="240" y="160" font-size="11">$p_3 = 1$ (numeraire)</text>
  <text x="240" y="230" font-size="11" fill="#555">ratios 1 : 2 : 3</text>
  <rect x="400" y="50" width="160" height="220" fill="#fff" stroke="#333"/>
  <text x="480" y="75" text-anchor="middle" font-size="12" font-weight="bold">$p / p_1$</text>
  <text x="420" y="110" font-size="11">$p_1 = 1$ (numeraire)</text>
  <text x="420" y="135" font-size="11">$p_2 = 2$</text>
  <text x="420" y="160" font-size="11">$p_3 = 3$</text>
  <text x="420" y="230" font-size="11" fill="#555">ratios 1 : 2 : 3</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Homogeneity of degree zero means any of these three price vectors describes the same equilibrium.</p>
""",
        "examples": r"""
<ul>
<li><strong>Solving Edgeworth problems:</strong> with two goods, set $p_y = 1$ so the only unknown is $p_x$. The single market clearing equation pins it down.</li>
<li><strong>National accounts:</strong> GDP is measured in a numeraire (the dollar, the pound). The choice does not affect real magnitudes, only nominal scales, which is why real growth rates are unit-free.</li>
<li><strong>Essay move:</strong> stress that fixing a numeraire is a normalisation, not an economic assumption. Switching numeraire changes the numbers but not the equilibrium allocation.</li>
<li><strong>Essay move:</strong> link to the count of equations and unknowns: $L$ prices minus 1 numeraire equals $L - 1$ unknowns; $L$ market clearing conditions minus Walras' Law equals $L - 1$ equations. Standard counting argument justification for existence.</li>
<li><strong>Limitation:</strong> in dynamic or monetary models with nominal rigidities (sticky prices, debt contracts), the choice of numeraire can have real effects because not all prices scale together. Homogeneity then fails for those frictions.</li>
<li><strong>Cross-reference:</strong> see [[Concepts/Homogeneity of Degree Zero]] for the property that makes numeraire choice legitimate.</li>
</ul>
""",
    },
    "cobb-douglas-demand": {
        "math": r"""
<p><strong>Setup.</strong> Consumer has Cobb-Douglas utility $u(x, y) = x^\alpha y^{1-\alpha}$ with $0 < \alpha < 1$, prices $p_x, p_y$, and money income $m$. The budget constraint is $p_x x + p_y y = m$.</p>
<p><strong>Derivation via the Lagrangian.</strong></p>
<ol>
<li>Write the Lagrangian $\mathcal{L} = x^\alpha y^{1-\alpha} - \lambda(p_x x + p_y y - m)$.</li>
<li>FOCs: $\alpha x^{\alpha-1} y^{1-\alpha} = \lambda p_x$ and $(1-\alpha) x^\alpha y^{-\alpha} = \lambda p_y$.</li>
<li>Dividing one FOC by the other eliminates $\lambda$: $\frac{\alpha}{1-\alpha} \cdot \frac{y}{x} = \frac{p_x}{p_y}$, so $y = \frac{(1-\alpha) p_x x}{\alpha p_y}$.</li>
<li>Substitute into the budget constraint: $p_x x + p_y \cdot \frac{(1-\alpha) p_x x}{\alpha p_y} = m$, which simplifies to $p_x x \cdot \bigl(1 + (1-\alpha)/\alpha\bigr) = m$, giving $p_x x = \alpha m$.</li>
</ol>
<p><strong>Result.</strong> The Marshallian demands are</p>
<p>$$x^*(p, m) = \frac{\alpha m}{p_x}, \qquad y^*(p, m) = \frac{(1-\alpha) m}{p_y}.$$</p>
<p>Equivalently, the consumer spends a constant share $\alpha$ of income on $x$ and $1-\alpha$ on $y$, regardless of prices. The indirect utility is $v(p, m) = m \cdot \alpha^\alpha (1-\alpha)^{1-\alpha} / (p_x^\alpha p_y^{1-\alpha})$.</p>
<p><strong>Properties.</strong> Demands are homogeneous of degree zero in $(p, m)$; income elasticity is 1 (homothetic preferences); own-price elasticity is $-1$; cross-price elasticity is 0. The expenditure function is $e(p, u) = u \cdot (p_x/\alpha)^\alpha (p_y/(1-\alpha))^{1-\alpha}$.</p>
<p><em>Sources.</em> Micro2025.pdf Lecture 2; Varian Ch. 5.2, 6.4; Hindriks and Myles Ch. 1.</p>
""",
        "widget": r"""
<svg id="widget-cobb-douglas-demand" viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <text x="300" y="22" text-anchor="middle" font-size="13" font-weight="bold">Cobb-Douglas: indifference curves and the optimum</text>
  <line x1="80" y1="270" x2="540" y2="270" stroke="#333"/>
  <line x1="80" y1="50" x2="80" y2="270" stroke="#333"/>
  <text x="545" y="285" font-size="11">$x$</text>
  <text x="65" y="55" font-size="11">$y$</text>
  <path d="M 120 240 Q 200 130, 380 90" fill="none" stroke="#aaa" stroke-width="1.5"/>
  <path d="M 130 260 Q 240 180, 460 130" fill="none" stroke="#4a90e2" stroke-width="2"/>
  <path d="M 140 270 Q 280 230, 510 180" fill="none" stroke="#aaa" stroke-width="1.5"/>
  <line x1="80" y1="100" x2="500" y2="270" stroke="#e25c5c" stroke-width="2"/>
  <text x="430" y="100" font-size="11" fill="#e25c5c">budget line</text>
  <circle cx="240" cy="172" r="5" fill="#000"/>
  <text x="248" y="170" font-size="11">$(x^*, y^*)$</text>
  <line x1="240" y1="172" x2="240" y2="270" stroke="#888" stroke-dasharray="2,2"/>
  <line x1="240" y1="172" x2="80" y2="172" stroke="#888" stroke-dasharray="2,2"/>
  <text x="240" y="285" font-size="11">$\alpha m/p_x$</text>
  <text x="40" y="175" font-size="11">$(1-\alpha)m/p_y$</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">At the optimum the budget line is tangent to the highest reachable indifference curve.</p>
""",
        "examples": r"""
<ul>
<li><strong>Macro calibration:</strong> in RBC and growth models the production function is Cobb-Douglas $Y = K^\alpha L^{1-\alpha}$ with $\alpha \approx 0.33$, matching the long-run capital share in US data. The same algebra applies, with constant factor shares as the empirical anchor.</li>
<li><strong>Consumer expenditure surveys:</strong> some commodity groups (food, transport) have stable expenditure shares across income deciles, consistent with a Cobb-Douglas approximation. Departures (e.g. Engel's Law for food) flag where the model misses.</li>
<li><strong>Essay move:</strong> note that Cobb-Douglas implies unit income elasticity for every good, contradicting Engel's Law (food share falls with income). It is a workhorse for tractability, not a serious empirical model.</li>
<li><strong>Essay move:</strong> derive the result directly from the FOC ratio $MRS = p_x/p_y$ to show why constant share pops out of the multiplicative structure. Tutors reward seeing the mechanism, not just the formula.</li>
<li><strong>Limitation:</strong> Cobb-Douglas has unit elasticity of substitution between goods. If the empirical relationship is closer to fixed proportions (Leontief) or perfect substitutes, the predicted demand response to price changes is badly wrong.</li>
<li><strong>Cross-reference:</strong> see [[Concepts/Edgeworth Box]] for how Cobb-Douglas demands give clean closed forms in 2x2 exchange equilibrium.</li>
</ul>
""",
    },
    "edgeworth-box": {
        "math": r"""
<p><strong>Setup.</strong> Two agents $A, B$ with strictly convex preferences $\succsim^A, \succsim^B$ over two goods $x, y$. Endowments $\omega^A = (\omega^A_x, \omega^A_y)$, $\omega^B = (\omega^B_x, \omega^B_y)$. The box has width $\bar X = \omega^A_x + \omega^B_x$ and height $\bar Y = \omega^A_y + \omega^B_y$.</p>
<p><strong>Pareto efficiency.</strong> An allocation $(x^A, y^A, x^B, y^B)$ with $x^A + x^B = \bar X$, $y^A + y^B = \bar Y$ is Pareto efficient iff there is no other feasible allocation that makes one agent strictly better off without making the other worse off. With smooth strictly convex preferences and interior allocations, this requires</p>
<p>$$MRS^A_{x,y} = MRS^B_{x,y},$$</p>
<p>i.e. the indifference curves are tangent. The locus of such tangencies is the <em>contract curve</em>.</p>
<p><strong>Walrasian equilibrium.</strong> Given prices $(p_x, p_y)$ each agent faces income $m^i = p_x \omega^i_x + p_y \omega^i_y$ and chooses $(x^i, y^i)$ to maximise $u^i$ subject to $p\cdot x^i \le m^i$. Equilibrium $(p^*, x^{A*}, x^{B*})$ requires:</p>
<ol>
<li>$x^A$ optimal at prices $p^*$ given $m^A$.</li>
<li>$x^B$ optimal at prices $p^*$ given $m^B$.</li>
<li>Markets clear: $x^{A*} + x^{B*} = \bar X$, $y^{A*} + y^{B*} = \bar Y$.</li>
</ol>
<p><strong>Geometric characterisation.</strong> Equilibrium is the point on the contract curve where the budget line through the endowment $\omega$ with slope $-p_x^*/p_y^*$ is tangent to both indifference curves. Each agent's MRS equals the price ratio:</p>
<p>$$MRS^A = MRS^B = \frac{p_x^*}{p_y^*}.$$</p>
<p><strong>First welfare theorem.</strong> Every Walrasian equilibrium is Pareto efficient, so the equilibrium allocation lies on the contract curve. The Edgeworth box gives the clearest visual of this result.</p>
<p><em>Sources.</em> Micro2025.pdf Lecture 2; Varian Ch. 17.1 to 17.3; Mas-Colell, Whinston, Green Ch. 15.B.</p>
""",
        "widget": r"""
<svg id="widget-edgeworth-box" viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <text x="300" y="20" text-anchor="middle" font-size="13" font-weight="bold">Edgeworth box: endowment, contract curve, equilibrium</text>
  <rect x="80" y="40" width="440" height="240" fill="none" stroke="#333" stroke-width="1.5"/>
  <text x="70" y="290" font-size="11">$O_A$</text>
  <text x="525" y="50" font-size="11">$O_B$</text>
  <text x="300" y="305" font-size="11">$x$</text>
  <text x="55" y="160" font-size="11">$y$</text>
  <path d="M 80 280 Q 230 200, 380 130 Q 460 90, 520 40" fill="none" stroke="#888" stroke-width="1.5" stroke-dasharray="4,3"/>
  <text x="200" y="250" font-size="11" fill="#888">contract curve</text>
  <circle cx="150" cy="220" r="5" fill="#e25c5c"/>
  <text x="115" y="215" font-size="11" fill="#e25c5c">$\omega$</text>
  <circle cx="320" cy="160" r="5" fill="#000"/>
  <text x="328" y="158" font-size="11">$(x^*, y^*)$</text>
  <line x1="80" y1="270" x2="520" y2="80" stroke="#4a90e2" stroke-width="1.5"/>
  <text x="450" y="115" font-size="11" fill="#4a90e2">budget line</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Equilibrium sits where the budget line through $\omega$ is tangent to both agents' indifference curves on the contract curve.</p>
""",
        "examples": r"""
<ul>
<li><strong>Two-country trade as exchange:</strong> when production is fixed, a two-country two-good world is just a giant Edgeworth box. Each country's endowment is its autarky production; trade moves both countries to a Pareto-efficient point. The terms of trade are the equilibrium price ratio.</li>
<li><strong>Risk sharing:</strong> in a state-contingent commodity space, the Edgeworth box represents two agents pooling income across states. The contract curve characterises efficient risk-sharing arrangements (equal MRS across states).</li>
<li><strong>Essay move:</strong> use the box to illustrate the first welfare theorem (equilibrium on the contract curve) and the second welfare theorem (any contract-curve point is supportable as an equilibrium after the right lump-sum redistribution of endowments).</li>
<li><strong>Essay move:</strong> show that the core (the set of allocations no coalition can block) coincides with the segment of the contract curve between the two agents' indifference curves through $\omega$. As the economy is replicated, the core shrinks to the Walrasian equilibrium (Debreu-Scarf).</li>
<li><strong>Limitation:</strong> the box assumes only two agents and two goods. With many agents or production, the geometry no longer captures everything, but the MRS equals price-ratio intuition survives.</li>
<li><strong>Cross-reference:</strong> see [[Concepts/PPF and MRT]] for the production analogue once we move from pure exchange to production economies.</li>
</ul>
""",
    },
    "ppf-and-mrt": {
        "math": r"""
<p><strong>Setup.</strong> Two goods $x, y$ produced from a fixed factor endowment (say labour $\bar L$). Production functions $x = f(L_x)$, $y = g(L_y)$ with $f, g$ strictly increasing and concave. The production possibility frontier is the set of $(x, y)$ such that there exist $L_x, L_y \ge 0$ with $L_x + L_y = \bar L$, $x = f(L_x)$, $y = g(L_y)$.</p>
<p><strong>Slope: the MRT.</strong> Total differentiation gives $dL_x + dL_y = 0$ and</p>
<p>$$dx = f'(L_x) dL_x, \quad dy = g'(L_y) dL_y.$$</p>
<p>So $\frac{dy}{dx}\bigg|_{PPF} = -\frac{g'(L_y)}{f'(L_x)}.$ The marginal rate of transformation is</p>
<p>$$MRT_{x,y} = \frac{g'(L_y)}{f'(L_x)} = \frac{MP_L^y}{MP_L^x}.$$</p>
<p>Equivalently, $MRT = MC_x / MC_y$ (the ratio of marginal costs). The PPF is concave to the origin when $f, g$ are strictly concave, because shifting labour into a sector with diminishing returns gives ever-smaller output gains.</p>
<p><strong>Equilibrium conditions.</strong> In a competitive economy, firms equate $p_x f'(L_x) = w$ and $p_y g'(L_y) = w$, giving</p>
<p>$$\frac{p_x}{p_y} = \frac{g'(L_y)}{f'(L_x)} = MRT.$$</p>
<p>Consumers equate $MRS = p_x/p_y$. So at a competitive equilibrium,</p>
<p>$$MRS = MRT,$$</p>
<p>which is the textbook condition for Pareto efficiency in a production economy: the consumer's willingness to substitute equals the economy's technical ability to transform.</p>
<p><em>Sources.</em> Micro2025.pdf Lecture 3; Varian Ch. 18.1 to 18.2; Mas-Colell, Whinston, Green Ch. 15.C.</p>
""",
        "widget": r"""
<svg id="widget-ppf-and-mrt" viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <text x="300" y="22" text-anchor="middle" font-size="13" font-weight="bold">PPF, MRT, and the tangent price line</text>
  <line x1="80" y1="280" x2="540" y2="280" stroke="#333"/>
  <line x1="80" y1="50" x2="80" y2="280" stroke="#333"/>
  <text x="545" y="295" font-size="11">$x$</text>
  <text x="65" y="55" font-size="11">$y$</text>
  <path d="M 80 80 Q 220 90, 380 180 Q 460 230, 520 280" fill="none" stroke="#4a90e2" stroke-width="2.5"/>
  <text x="430" y="125" font-size="11" fill="#4a90e2">PPF</text>
  <line x1="170" y1="60" x2="430" y2="290" stroke="#e25c5c" stroke-width="1.5" stroke-dasharray="3,3"/>
  <text x="370" y="80" font-size="11" fill="#e25c5c">slope $-p_x/p_y$</text>
  <circle cx="300" cy="150" r="5" fill="#000"/>
  <text x="305" y="145" font-size="11">production point</text>
  <text x="310" y="170" font-size="11">$MRT = p_x/p_y$</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">In equilibrium, the relative price line is tangent to the concave PPF at the chosen production point.</p>
""",
        "examples": r"""
<ul>
<li><strong>Comparative statics of a price shock:</strong> if $p_x/p_y$ rises (say world demand for $x$ shifts up), the tangency point slides along the PPF toward more $x$ and less $y$. The economy reallocates labour from $y$ to $x$.</li>
<li><strong>Bowed-out PPF intuition:</strong> the concavity reflects diminishing returns in each sector and factors with different sector-specific productivities. A linear PPF (Ricardian) is the special case of constant returns and a single homogeneous factor.</li>
<li><strong>Essay move:</strong> distinguish the geometric MRT (slope of the PPF) from the economic MRT (ratio of marginal costs). They coincide here because labour is the only factor and is paid the same wage in both sectors.</li>
<li><strong>Essay move:</strong> link MRT equals MRS to the first welfare theorem. Decentralised competitive trades enforce both equalities through the common price ratio, so the equilibrium allocation is Pareto efficient.</li>
<li><strong>Limitation:</strong> the construction assumes that the factor (labour) is freely mobile between sectors. With sector-specific capital, the short-run PPF is more concave than the long-run one, and the MRT depends on which factors are mobile.</li>
<li><strong>Cross-reference:</strong> see [[Concepts/Ricardian Trade Model]] for the linear-PPF special case that drives comparative-advantage trade.</li>
</ul>
""",
    },

    "hicksian-demand": {
        "math": r"""
<p>The <strong>Hicksian (compensated) demand</strong> $h_i(\mathbf{p}, u)$ solves the expenditure minimisation problem (EMP): for given prices $\mathbf{p}$ and a target utility level $u$,
$$ \min_{\mathbf{x}\ge 0}\ \mathbf{p}\cdot\mathbf{x}\quad \text{s.t.}\quad U(\mathbf{x}) \ge u. $$
The value function is the <strong>expenditure function</strong> $e(\mathbf{p}, u) = \mathbf{p}\cdot h(\mathbf{p}, u)$.</p>

<p>Hicksian demand isolates the pure <em>substitution effect</em>: when $p_i$ rises, utility is held fixed by a compensating income transfer, so the consumer rebundles only because relative prices have changed. Contrast this with Marshallian demand $x_i(\mathbf{p}, m)$, which mixes substitution and income effects.</p>

<p><strong>Key results</strong> (Varian Ch. 8; Micro2025.pdf Topic 2 Lecture 3):</p>

<ol>
<li><strong>Shephard's lemma:</strong> $\dfrac{\partial e(\mathbf{p}, u)}{\partial p_i} = h_i(\mathbf{p}, u)$. Differentiate the expenditure function with respect to price $i$ and you recover the compensated demand for good $i$.</li>
<li><strong>Slutsky equation:</strong> the Marshallian price response decomposes as
$$ \frac{\partial x_i}{\partial p_j} = \underbrace{\frac{\partial h_i}{\partial p_j}}_{\text{substitution}} - \underbrace{x_j \frac{\partial x_i}{\partial m}}_{\text{income effect}}. $$
The substitution matrix $\partial h_i / \partial p_j$ is symmetric and negative semi-definite, so own-price compensated demand always slopes weakly downward: <em>Giffen behaviour is ruled out in Hicksian demand</em>.</li>
<li><strong>Duality:</strong> $h_i(\mathbf{p}, u) = x_i(\mathbf{p}, e(\mathbf{p}, u))$ and $x_i(\mathbf{p}, m) = h_i(\mathbf{p}, v(\mathbf{p}, m))$, where $v$ is the indirect utility function. EMP and UMP are mirror images.</li>
</ol>

<p>Hicksian demand is the right object for <strong>welfare measurement</strong>. The compensating variation (CV) and equivalent variation (EV) of a price change from $\mathbf{p}^0$ to $\mathbf{p}^1$ are
$$ CV = e(\mathbf{p}^1, u^0) - e(\mathbf{p}^0, u^0), \qquad EV = e(\mathbf{p}^1, u^1) - e(\mathbf{p}^0, u^1), $$
both computed by integrating Hicksian demand, not Marshallian demand. Consumer surplus from Marshallian demand is only an approximation, exact when the income effect is zero (quasilinear preferences).</p>

<p><em>References:</em> Varian, Ch. 8 (Slutsky equation, expenditure function); Hindriks and Myles Ch. 14 on welfare measurement; Mas-Colell, Whinston and Green Ch. 3.</p>
""",
        "widget": r"""
<svg id="widget-hicksian-demand" viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fff">
  <defs><marker id="arrow-hd" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#333"/></marker></defs>
  <line x1="60" y1="280" x2="560" y2="280" stroke="#333" stroke-width="1.5" marker-end="url(#arrow-hd)"/>
  <line x1="60" y1="280" x2="60" y2="30" stroke="#333" stroke-width="1.5" marker-end="url(#arrow-hd)"/>
  <text x="560" y="305" font-size="13" fill="#333">$x_1$</text>
  <text x="35" y="35" font-size="13" fill="#333">$x_2$</text>
  <path d="M 100 80 Q 180 130 240 180 Q 320 230 480 260" fill="none" stroke="#1f77b4" stroke-width="2"/>
  <text x="485" y="255" font-size="12" fill="#1f77b4">$U=u^0$</text>
  <line x1="90" y1="280" x2="430" y2="60" stroke="#888" stroke-width="1.5" stroke-dasharray="4,3"/>
  <text x="395" y="55" font-size="12" fill="#888">$\mathbf{p}^0$</text>
  <line x1="90" y1="280" x2="260" y2="40" stroke="#d62728" stroke-width="1.5"/>
  <text x="220" y="40" font-size="12" fill="#d62728">$\mathbf{p}^1$</text>
  <line x1="155" y1="280" x2="350" y2="20" stroke="#2ca02c" stroke-width="1.5" stroke-dasharray="2,3"/>
  <text x="345" y="20" font-size="12" fill="#2ca02c">compensated $\mathbf{p}^1$</text>
  <circle cx="230" cy="155" r="4" fill="#1f77b4"/>
  <text x="238" y="148" font-size="12" fill="#1f77b4">A = $x(\mathbf{p}^0, m)$</text>
  <circle cx="175" cy="200" r="4" fill="#2ca02c"/>
  <text x="100" y="215" font-size="12" fill="#2ca02c">B = $h(\mathbf{p}^1, u^0)$</text>
  <circle cx="140" cy="180" r="4" fill="#d62728"/>
  <text x="100" y="170" font-size="12" fill="#d62728">C = $x(\mathbf{p}^1, m)$</text>
  <text x="60" y="305" font-size="11" fill="#555">A to B: substitution effect (Hicksian). B to C: income effect.</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">A price rise in good 1 shifts the budget from blue to red. The Hicksian decomposition compensates income to keep utility at $u^0$ (green dashed line), tangent to the original indifference curve at B. The horizontal move A to B is the pure substitution effect.</p>
""",
        "examples": r"""
<ul>
<li><strong>Welfare cost of a tax.</strong> A sales tax on good 1 raises $p_1$. The deadweight loss is the area between the Hicksian demand curve and the new price, not the Marshallian one. Using Marshallian demand overstates DWL when good 1 is normal and understates it when inferior. Atkinson and Stiglitz Ch. 14 build optimal commodity taxation on this exact foundation.</li>
<li><strong>CV and EV for policy appraisal.</strong> UK Treasury Green Book valuations of road pricing, congestion charges, and carbon taxes need a money-metric utility change. CV asks "how much income would the household pay to avoid the policy?", EV asks "how much would they pay to get the policy if not implemented?". Both are line integrals of Hicksian demand.</li>
<li><strong>Demand estimation.</strong> Hausman (1981) shows how to recover the expenditure function from estimated Marshallian demand, then back out exact welfare numbers. This is the workhorse method in modern public economics empirics.</li>
<li><strong>Essay move: explain why Giffen goods are not a counterexample to the law of demand for compensated demand.</strong> The Slutsky substitution matrix is negative semi-definite by construction, so $\partial h_i / \partial p_i \le 0$ always. A Giffen good is purely an income-effect phenomenon in Marshallian demand. Examiners reward students who distinguish the two demand concepts cleanly.</li>
<li><strong>Essay move: link duality to Roy's identity and Shephard's lemma symmetrically.</strong> Roy gives Marshallian demand from the indirect utility, Shephard gives Hicksian demand from expenditure. Recognising the symmetry shows mastery of the UMP and EMP pair.</li>
<li><strong>Limitation.</strong> Hicksian demand is unobservable directly because utility is unobservable. Empirically we observe Marshallian demand and prices, then estimate preferences to recover the compensated object. Measurement error in income can swamp the substitution effect on small samples.</li>
<li><strong>See also</strong> [[Concepts/Slutsky Equation]] and [[Concepts/Expenditure Function]] for the formal machinery.</li>
</ul>
"""
    },
    "cost-benefit-analysis": {
        "math": r"""
<p><strong>Cost-benefit analysis (CBA)</strong> compares the present value of a project's social benefits to its social costs. For a project yielding benefit stream $B_t$ and cost stream $C_t$ over $t = 0, 1, \dots, T$,
$$ NPV = \sum_{t=0}^{T} \frac{B_t - C_t}{(1+r)^t}, $$
where $r$ is the <em>social discount rate</em>. The decision rule is: accept if $NPV > 0$, reject if $NPV < 0$. CBA is the operational embodiment of the <strong>Kaldor-Hicks compensation criterion</strong>: a project is socially desirable if winners <em>could in principle</em> compensate losers and still be better off, even if no actual compensation occurs.</p>

<p>The four ingredients of any CBA (Hindriks and Myles Ch. 13; Micro2025.pdf Topic 2 Lecture 4):</p>

<ol>
<li><strong>Identify the affected parties and welfare change.</strong> Each agent's willingness to pay (WTP) for benefits or willingness to accept (WTA) compensation for costs is the welfare metric. For market goods, prices reveal WTP. For non-market goods, see contingent valuation, hedonic pricing, and travel cost.</li>
<li><strong>Convert physical impacts into monetary equivalents.</strong> Health gains via QALYs and the value of a statistical life; environmental amenities via stated or revealed preference methods; time savings via the value of travel time.</li>
<li><strong>Choose the social discount rate.</strong> Typically derived from the Ramsey equation $r = \rho + \eta g$. The UK Green Book uses a declining rate starting at 3.5 percent.</li>
<li><strong>Sensitivity analysis.</strong> Vary discount rate, value of statistical life, and benefit forecasts to bound $NPV$.</li>
</ol>

<p><strong>Equity weighting.</strong> Pure Kaldor-Hicks ignores who gains and who loses. A welfarist refinement weights costs and benefits accruing to poorer households by a factor reflecting decreasing marginal utility of income:
$$ NPV^{equity} = \sum_t \sum_h \frac{w_h (B_{h,t} - C_{h,t})}{(1+r)^t},\quad w_h = (\bar{y}/y_h)^\eta. $$</p>

<p><strong>Critiques.</strong> CBA monetises incommensurable values, smuggles distributional judgements through the discount rate and weights, and depends on estimates of WTP from individuals who may be uninformed about the good in question. Sen (2000) and Sagoff argue that some choices (basic rights, ecological survival) should not be reduced to a single $NPV$ number.</p>

<p><em>References:</em> Hindriks and Myles, Ch. 13; HM Treasury Green Book (2022); Boardman et al., <em>Cost-Benefit Analysis</em>.</p>
""",
        "widget": r"""
<svg id="widget-cost-benefit-analysis" viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fff">
  <line x1="60" y1="280" x2="560" y2="280" stroke="#333" stroke-width="1.5"/>
  <line x1="60" y1="280" x2="60" y2="30" stroke="#333" stroke-width="1.5"/>
  <text x="290" y="305" font-size="13" fill="#333">Year $t$</text>
  <text x="20" y="155" font-size="13" fill="#333" transform="rotate(-90, 20, 155)">GBP</text>
  <rect x="80" y="200" width="40" height="80" fill="#d62728" opacity="0.75"/>
  <text x="85" y="195" font-size="11" fill="#d62728">$C_0$</text>
  <rect x="135" y="240" width="40" height="40" fill="#d62728" opacity="0.55"/>
  <rect x="190" y="260" width="40" height="20" fill="#d62728" opacity="0.4"/>
  <rect x="245" y="220" width="40" height="60" fill="#2ca02c" opacity="0.8"/>
  <text x="250" y="215" font-size="11" fill="#2ca02c">$B_3$</text>
  <rect x="300" y="180" width="40" height="100" fill="#2ca02c" opacity="0.75"/>
  <rect x="355" y="160" width="40" height="120" fill="#2ca02c" opacity="0.7"/>
  <rect x="410" y="170" width="40" height="110" fill="#2ca02c" opacity="0.6"/>
  <rect x="465" y="190" width="40" height="90" fill="#2ca02c" opacity="0.5"/>
  <path d="M 80 80 Q 200 100 320 130 Q 440 165 540 200" fill="none" stroke="#1f77b4" stroke-width="2" stroke-dasharray="4,2"/>
  <text x="430" y="155" font-size="12" fill="#1f77b4">$1/(1+r)^t$</text>
  <text x="80" y="50" font-size="13" fill="#333" font-weight="bold">NPV = $\sum_t (B_t - C_t)/(1+r)^t$</text>
  <text x="80" y="65" font-size="11" fill="#555">Red = costs (early), green = benefits (later), blue = discount weight.</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Stylised CBA cash-flow diagram. Costs are concentrated up front, benefits arrive later, and the discount factor (blue dashed) shrinks distant flows. A higher $r$ rotates the blue curve down faster and reduces $NPV$.</p>
""",
        "examples": r"""
<ul>
<li><strong>HS2 high-speed rail.</strong> The UK Department for Transport's CBA monetised time savings, agglomeration externalities, and carbon. Critics argued the benefit-cost ratio was sensitive to the assumed value of business travel time and the discount rate. By 2023 cost overruns had pushed the ratio below one.</li>
<li><strong>NICE health technology appraisal.</strong> NICE uses cost per QALY thresholds (typically GBP 20,000 to 30,000) to decide which drugs the NHS reimburses. This is CBA where benefits are denominated in QALYs rather than pounds and the threshold plays the role of the implicit value of a QALY.</li>
<li><strong>Stern Review (2006) on climate change.</strong> Stern adopted $\rho \approx 0.1$ percent (almost zero pure time preference) and got a large $NPV$ for aggressive mitigation. Nordhaus countered with $\rho \approx 1.5$ percent and got much smaller numbers. The disagreement is ethical, not technical: how much weight should we give to future generations?</li>
<li><strong>Essay move: distinguish potential from actual compensation.</strong> Kaldor-Hicks asks only whether winners <em>could</em> compensate losers. Boadway's paradox shows that potential compensation tests can be reversible (project and reverse both pass) when income effects bite. Recognising this gives a tighter answer than reciting the formula.</li>
<li><strong>Essay move: argue that the choice of discount rate is normative not positive.</strong> Doornik rewards students who notice that the Ramsey decomposition $r = \rho + \eta g$ mixes an empirical ($g$) and two ethical ($\rho, \eta$) parameters, and that a positivist appeal to market interest rates dodges the question.</li>
<li><strong>Limitation.</strong> CBA aggregates by summing money, which presupposes that one pound of WTP from a billionaire is worth the same as one pound from a pensioner. Equity weighting is a partial fix but introduces fresh value judgements about $\eta$.</li>
<li><strong>See also</strong> [[Concepts/Kaldor-Hicks Criterion]] and [[Concepts/Social Discount Rate]].</li>
</ul>
"""
    },
    "contingent-valuation": {
        "math": r"""
<p><strong>Contingent valuation (CV)</strong> is a <em>stated preference</em> method for valuing non-market goods. Respondents are presented with a hypothetical scenario (e.g., a programme to preserve a wetland) and asked either their maximum willingness to pay (WTP) or their minimum willingness to accept (WTA) compensation.</p>

<p>Two common elicitation formats:</p>
<ol>
<li><strong>Open-ended:</strong> "What is the most you would pay to preserve the wetland?" Yields a continuous WTP variable but suffers from large non-response and protest zeros.</li>
<li><strong>Dichotomous-choice (referendum):</strong> "Would you vote yes to a one-off tax of GBP $B$ to preserve the wetland?" with $B$ randomised across respondents. The probability of yes is modelled as
$$ \Pr(\text{yes} \mid B) = G\big(\alpha - \beta B + \gamma' x\big), $$
where $G$ is a logit or probit link and $x$ are demographics. Mean WTP is recovered as
$$ \mathbb{E}[WTP] = \int_0^{\infty} \Pr(\text{yes}\mid B)\,dB. $$
This format mirrors a real referendum and is incentive-compatible if respondents believe their vote matters.</li>
</ol>

<p><strong>Total economic value</strong> decomposes as
$$ TEV = \underbrace{UV_{\text{direct}} + UV_{\text{indirect}} + OV}_{\text{use values}} + \underbrace{BV + EV}_{\text{non-use}}, $$
where $UV$ are use values, $OV$ is option value, $BV$ is bequest value, and $EV$ is existence value. CV is the only method that can pick up non-use values like existence value, the satisfaction of knowing blue whales exist even if you never see one.</p>

<p><strong>Biases (Mitchell and Carson, 1989; Micro2025.pdf Topic 2 Lecture 4):</strong></p>
<ol>
<li><strong>Hypothetical bias:</strong> respondents overstate WTP because no real money changes hands. Meta-analyses suggest stated WTP exceeds revealed WTP by a factor of 2 to 3.</li>
<li><strong>Strategic bias:</strong> if respondents think the survey will determine policy and they pay a share, they understate; if they think payment is symbolic, they overstate.</li>
<li><strong>Embedding (scope insensitivity):</strong> WTP for saving 2,000 birds is often statistically indistinguishable from WTP for saving 20,000 (Desvousges et al., 1993).</li>
<li><strong>WTP-WTA divergence:</strong> WTA typically exceeds WTP by a large factor for the same change, inconsistent with standard theory and pointing to loss aversion.</li>
</ol>

<p>The Arrow et al. (1993) NOAA panel laid down best-practice guidelines (in-person interviews, dichotomous choice, conservative design) that became the field standard.</p>

<p><em>References:</em> Hindriks and Myles Ch. 13; Carson (2012, JEP).</p>
""",
        "widget": r"""
<svg id="widget-contingent-valuation" viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fff">
  <line x1="70" y1="270" x2="560" y2="270" stroke="#333" stroke-width="1.5"/>
  <line x1="70" y1="270" x2="70" y2="30" stroke="#333" stroke-width="1.5"/>
  <text x="430" y="295" font-size="13" fill="#333">Bid amount $B$ (GBP)</text>
  <text x="20" y="55" font-size="13" fill="#333">$\Pr(\text{yes})$</text>
  <path d="M 70 60 C 200 70 280 130 320 160 C 380 210 480 255 555 263" fill="none" stroke="#1f77b4" stroke-width="2.5"/>
  <circle cx="120" cy="75" r="4" fill="#1f77b4"/>
  <circle cx="200" cy="100" r="4" fill="#1f77b4"/>
  <circle cx="280" cy="140" r="4" fill="#1f77b4"/>
  <circle cx="360" cy="200" r="4" fill="#1f77b4"/>
  <circle cx="440" cy="240" r="4" fill="#1f77b4"/>
  <circle cx="520" cy="260" r="4" fill="#1f77b4"/>
  <path d="M 70 60 C 200 70 280 130 320 160 C 380 210 480 255 555 263 L 555 270 L 70 270 Z" fill="#1f77b4" opacity="0.12"/>
  <text x="190" y="220" font-size="12" fill="#1f77b4">Mean WTP = $\int_0^\infty \Pr(\text{yes}\mid B)\,dB$</text>
  <line x1="70" y1="60" x2="65" y2="60" stroke="#333"/>
  <text x="40" y="64" font-size="11" fill="#333">1.0</text>
  <line x1="70" y1="165" x2="65" y2="165" stroke="#333"/>
  <text x="40" y="169" font-size="11" fill="#333">0.5</text>
  <line x1="70" y1="270" x2="65" y2="270" stroke="#333"/>
  <text x="40" y="274" font-size="11" fill="#333">0</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Dichotomous-choice CV. As the randomised bid $B$ rises, the share of respondents voting yes falls. Mean WTP is the shaded area under the fitted survival curve.</p>
""",
        "examples": r"""
<ul>
<li><strong>Exxon Valdez (1989).</strong> The NOAA panel was set up partly to assess CV's reliability for natural-resource damage litigation after the spill. Carson et al. (2003) estimated US household WTP at around USD 31, giving total non-use damages near USD 4.9 billion. This study legitimised CV in US courts.</li>
<li><strong>Wetland and biodiversity valuation.</strong> The UK Defra commissioned CV for the National Ecosystem Assessment, valuing peatlands, woodlands, and coastal habitats for cost-benefit appraisal of conservation policy.</li>
<li><strong>Air quality and mortality.</strong> CV elicits WTP for reductions in mortality risk, generating the value of a statistical life used in DEFRA and DfT impact assessments.</li>
<li><strong>Essay move: separate hypothetical bias from scope insensitivity.</strong> Doornik rewards students who note that hypothetical bias affects the <em>level</em> of WTP while scope insensitivity affects the <em>responsiveness</em> of WTP to changes in the good. Different remedies apply: cheap talk scripts for the first, internal scope tests for the second.</li>
<li><strong>Essay move: cite Hausman (2012) versus Carson (2012) in the JEP exchange.</strong> A balanced essay engages with the live methodological debate, not a textbook caricature.</li>
<li><strong>Limitation.</strong> Survey responses are not enforced by budget constraints. Even with best-practice design, stated WTP correlates only modestly with revealed WTP in calibration studies (Murphy et al. 2005 meta-analysis: average ratio 2.6).</li>
<li><strong>See also</strong> [[Concepts/Hedonic Pricing]] for revealed-preference alternatives and [[Concepts/Travel Cost Method]] for behavioural data.</li>
</ul>
"""
    },
    "hedonic-pricing": {
        "math": r"""
<p><strong>Hedonic pricing</strong> is a <em>revealed-preference</em> method that infers the marginal value of a non-market characteristic from the equilibrium price of a differentiated market good. The classic application: house prices regressed on a vector of attributes including a non-market amenity such as air quality or proximity to a park.</p>

<p>A house is a bundle of characteristics $\mathbf{z} = (z_1, z_2, \dots, z_k)$, where $z_1$ is, say, structural size, $z_2$ is local PM2.5 concentration, and so on. In a competitive market with sufficient variation, the equilibrium price function is
$$ P(\mathbf{z}) = P(z_1, \dots, z_k). $$
The household maximises $U(x, \mathbf{z})$ subject to $x + P(\mathbf{z}) = m$, with first-order condition
$$ \frac{\partial U / \partial z_j}{\partial U / \partial x} = \frac{\partial P}{\partial z_j}. $$
The marginal hedonic price $\partial P / \partial z_j$ equals the marginal willingness to pay (MWTP) for attribute $j$ at the consumer's chosen bundle (Rosen, 1974).</p>

<p><strong>Two-stage estimation:</strong></p>
<ol>
<li><strong>Stage 1.</strong> Estimate the hedonic price function by regressing $\ln P$ on attributes:
$$ \ln P_i = \alpha + \sum_j \beta_j z_{ij} + \varepsilon_i. $$
The coefficient $\beta_j$ delivers an implicit price gradient.</li>
<li><strong>Stage 2.</strong> Regress the recovered MWTPs on household characteristics to identify the inverse demand for $z_j$. Identification requires instruments because the household chooses both the bundle and the location.</li>
</ol>

<p><strong>Capitalisation interpretation.</strong> The hedonic gradient captures only <em>local</em> MWTP at the household's chosen bundle, not consumer surplus for large changes. For non-marginal policy changes (e.g., closing all London Underground stations), the gradient gives a first-order approximation that may be badly off.</p>

<p><strong>Identification challenges (Micro2025.pdf Topic 2 Lecture 4):</strong></p>
<ol>
<li><strong>Omitted variables:</strong> neighbourhood amenities correlated with the attribute of interest (good schools near low pollution) bias $\beta_j$.</li>
<li><strong>Sorting:</strong> households with strong tastes for clean air cluster in clean areas, so the cross-sectional gradient mixes preferences and selection.</li>
<li><strong>Spatial autocorrelation:</strong> errors are correlated across nearby houses; standard errors need spatial clustering.</li>
</ol>

<p>Chay and Greenstone (2005) used the Clean Air Act non-attainment designations as a quasi-experiment to identify the capitalisation of PM10 reductions into house prices, a benchmark hedonic study.</p>

<p><em>References:</em> Hindriks and Myles Ch. 13; Rosen (1974, JPE); Chay and Greenstone (2005, JPE).</p>
""",
        "widget": r"""
<svg id="widget-hedonic-pricing" viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fff">
  <line x1="70" y1="270" x2="560" y2="270" stroke="#333" stroke-width="1.5"/>
  <line x1="70" y1="270" x2="70" y2="30" stroke="#333" stroke-width="1.5"/>
  <text x="380" y="295" font-size="13" fill="#333">Air quality $z_j$</text>
  <text x="20" y="55" font-size="13" fill="#333">House price $P$</text>
  <circle cx="120" cy="240" r="3" fill="#1f77b4" opacity="0.7"/>
  <circle cx="140" cy="225" r="3" fill="#1f77b4" opacity="0.7"/>
  <circle cx="170" cy="235" r="3" fill="#1f77b4" opacity="0.7"/>
  <circle cx="200" cy="210" r="3" fill="#1f77b4" opacity="0.7"/>
  <circle cx="225" cy="200" r="3" fill="#1f77b4" opacity="0.7"/>
  <circle cx="260" cy="195" r="3" fill="#1f77b4" opacity="0.7"/>
  <circle cx="290" cy="180" r="3" fill="#1f77b4" opacity="0.7"/>
  <circle cx="320" cy="175" r="3" fill="#1f77b4" opacity="0.7"/>
  <circle cx="355" cy="155" r="3" fill="#1f77b4" opacity="0.7"/>
  <circle cx="385" cy="140" r="3" fill="#1f77b4" opacity="0.7"/>
  <circle cx="415" cy="135" r="3" fill="#1f77b4" opacity="0.7"/>
  <circle cx="445" cy="115" r="3" fill="#1f77b4" opacity="0.7"/>
  <circle cx="475" cy="100" r="3" fill="#1f77b4" opacity="0.7"/>
  <circle cx="505" cy="85" r="3" fill="#1f77b4" opacity="0.7"/>
  <line x1="100" y1="250" x2="540" y2="80" stroke="#d62728" stroke-width="2"/>
  <text x="370" y="105" font-size="12" fill="#d62728">$P(z) = \alpha + \beta z + \dots$</text>
  <circle cx="320" cy="175" r="5" fill="#2ca02c"/>
  <text x="330" y="170" font-size="11" fill="#2ca02c">slope = MWTP</text>
  <line x1="270" y1="190" x2="370" y2="160" stroke="#2ca02c" stroke-width="1.5" stroke-dasharray="3,2"/>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">House prices rise as air quality improves. The slope of the hedonic price function at a household's chosen bundle is its marginal willingness to pay for cleaner air.</p>
""",
        "examples": r"""
<ul>
<li><strong>School quality capitalisation.</strong> Black (1999, QJE) used boundary discontinuities to identify the willingness to pay for school quality, finding that a 5 percent increase in test scores raised house prices by about 2.5 percent. Becomes the template for the boundary discontinuity design.</li>
<li><strong>Airport noise.</strong> Day, Bateman, and Lake (2007) for Birmingham airport regressed prices on decibel exposure to value noise abatement policies.</li>
<li><strong>Pollution damage estimation.</strong> Chay and Greenstone (2005) exploit the Clean Air Act non-attainment status as an instrument: a one-unit drop in PM10 raised house prices by about 0.3 percent, valuing the regulation in the tens of billions.</li>
<li><strong>Essay move: contrast revealed with stated preference cleanly.</strong> Hedonic pricing requires functioning markets and observed sorting, so it cannot pick up pure existence values. CV can pick up existence value but is hypothetical. Doornik rewards students who say which method is appropriate for which good and why.</li>
<li><strong>Essay move: discuss the Rosen second-stage identification problem.</strong> Marginal prices are non-linear in attributes, so the same household trades off a different MWTP at different points. Recovering the inverse demand requires variation across markets or instruments, an open empirical problem (Bishop and Timmins, 2018).</li>
<li><strong>Limitation.</strong> Capitalisation depends on housing-market frictions: with thin markets, search frictions, or zoning constraints, prices may not fully reflect attributes. Renters versus owners face different incentive structures.</li>
<li><strong>See also</strong> [[Concepts/Contingent Valuation]] (stated preference complement) and [[Concepts/Hicksian Demand]] (theoretical welfare basis).</li>
</ul>
"""
    },
    "travel-cost-method": {
        "math": r"""
<p>The <strong>travel cost method</strong> values a recreational site (a national park, beach, museum) by treating the cost of getting there as an implicit price. With no admission fee, travel cost varies across visitors by distance, so a demand curve can be estimated from the relationship between visit frequency and travel cost.</p>

<p>Let $v_i$ be the annual visits by individual $i$ residing at distance $d_i$, with travel cost $TC_i = c d_i + w_i t_i$, where $c$ is the per-mile financial cost, $w_i$ is the wage (opportunity cost of time), and $t_i$ is travel time. The simplest <strong>individual travel-cost model</strong> is
$$ v_i = \alpha - \beta\, TC_i + \gamma' x_i + \varepsilon_i. $$
For visitors with $TC_i = TC^0$, the estimated demand curve gives <strong>consumer surplus</strong>
$$ CS_i = \int_{TC^0}^{TC^{\max}} (\alpha - \beta\, TC + \gamma' x_i)\, dTC = \frac{(\alpha + \gamma' x_i - \beta\, TC^0)^2}{2\beta}, $$
the area under the demand curve above the actual travel cost. Aggregating $CS_i$ across visitors gives total recreational value.</p>

<p><strong>Zonal travel-cost model.</strong> Aggregate visitors into concentric zones of distance from the site. The visit rate (visits per capita) in zone $z$ is regressed on the zone-average travel cost. Coarser but easier when only aggregate visitor counts are available.</p>

<p><strong>Practical issues (Micro2025.pdf Topic 2 Lecture 4; Hindriks and Myles Ch. 13):</strong></p>
<ol>
<li><strong>Value of travel time.</strong> Standard practice values commuting time at 25 to 50 percent of the wage rate. Different conventions can swing the CS estimate by factors of two.</li>
<li><strong>Multi-purpose trips.</strong> If a visitor combines the park with other activities, attributing the entire $TC$ to the park overstates value. Convention: split cost across destinations or focus on dedicated trips.</li>
<li><strong>Truncation and zero observations.</strong> On-site sampling truncates the data to visitors only. Population surveys include zeros from non-visitors, requiring a Tobit or zero-inflated Poisson estimator.</li>
<li><strong>Substitute sites.</strong> Omitting a nearby alternative biases the price coefficient. Random utility models (Train, 2009) extend travel cost to a portfolio of sites.</li>
<li><strong>Use values only.</strong> Travel cost cannot pick up non-use values, since by definition only visitors contribute to the estimate.</li>
</ol>

<p>Clawson and Knetsch (1966) is the canonical original reference. The random utility extension (Bockstael, Hanemann, Kling 1987) is the workhorse in modern environmental economics.</p>

<p><em>References:</em> Hindriks and Myles Ch. 13; Champ, Boyle, Brown <em>A Primer on Nonmarket Valuation</em>.</p>
""",
        "widget": r"""
<svg id="widget-travel-cost-method" viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fff">
  <line x1="70" y1="270" x2="560" y2="270" stroke="#333" stroke-width="1.5"/>
  <line x1="70" y1="270" x2="70" y2="30" stroke="#333" stroke-width="1.5"/>
  <text x="380" y="295" font-size="13" fill="#333">Visits per year $v$</text>
  <text x="20" y="55" font-size="13" fill="#333">Travel cost $TC$</text>
  <line x1="100" y1="60" x2="530" y2="250" stroke="#1f77b4" stroke-width="2.5"/>
  <text x="430" y="200" font-size="12" fill="#1f77b4">demand $v = \alpha - \beta TC$</text>
  <line x1="70" y1="170" x2="350" y2="170" stroke="#888" stroke-dasharray="3,2"/>
  <line x1="350" y1="170" x2="350" y2="270" stroke="#888" stroke-dasharray="3,2"/>
  <text x="50" y="174" font-size="11" fill="#333">$TC^0$</text>
  <text x="345" y="285" font-size="11" fill="#333">$v^*$</text>
  <polygon points="100,60 100,170 350,170" fill="#2ca02c" opacity="0.25"/>
  <text x="160" y="135" font-size="12" fill="#2ca02c" font-weight="bold">Consumer Surplus</text>
  <text x="80" y="50" font-size="13" fill="#333" font-weight="bold">$CS = \tfrac{1}{2}(v^*)(TC^{\max} - TC^0)$</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Estimated demand curve from visit-frequency data. Consumer surplus (green) is the area above the actual travel cost and below the demand curve, aggregated across visitors to give the recreational value of the site.</p>
""",
        "examples": r"""
<ul>
<li><strong>UK National Parks valuation.</strong> Bateman et al. (2003) used travel cost to value visits to the Norfolk Broads, supporting management decisions about boat licence fees and habitat restoration.</li>
<li><strong>Coral reef recreation.</strong> Carr and Mendelsohn (2003) applied travel cost to scuba diving sites on the Great Barrier Reef, generating valuations later used in Australian climate-policy impact assessments.</li>
<li><strong>Museum and heritage valuation.</strong> The British Museum's free-entry policy means revenue understates social value; travel cost using visitor postcodes captures the otherwise invisible consumer surplus.</li>
<li><strong>Essay move: contrast travel cost with hedonic pricing.</strong> Both are revealed-preference methods but at different unit of analysis: travel cost values site visits, hedonics values bundle locations. Doornik rewards students who pick the appropriate method for the good in question.</li>
<li><strong>Essay move: spell out the assumed value of time.</strong> The CS estimate scales linearly in the wage fraction used to monetise travel time. A defensible answer says "I assume 33 percent of the median wage, sensitivity-tested at 25 and 50 percent" rather than reciting the textbook formula.</li>
<li><strong>Limitation.</strong> Travel cost cannot value non-use benefits. Existence value of an unvisited Antarctic ice shelf is invisible in this framework. Combine with CV for total economic value.</li>
<li><strong>See also</strong> [[Concepts/Hedonic Pricing]], [[Concepts/Contingent Valuation]], and [[Concepts/Consumer Surplus]].</li>
</ul>
"""
    },
    "qaly": {
        "math": r"""
<p>The <strong>Quality-Adjusted Life Year (QALY)</strong> is a composite health-outcome measure combining length and quality of life. One QALY equals one year lived in <em>perfect health</em>. A year lived in less than perfect health is weighted by a quality coefficient $q \in [0, 1]$:
$$ \text{QALYs} = \sum_{t=0}^{T} q_t. $$
A patient living 5 years at $q = 0.7$ and then dying contributes $5 \times 0.7 = 3.5$ QALYs.</p>

<p><strong>Cost-effectiveness ratio.</strong> Compare two interventions $A$ and $B$ via the incremental cost-effectiveness ratio (ICER):
$$ ICER_{A \to B} = \frac{C_B - C_A}{\text{QALYs}_B - \text{QALYs}_A}. $$
The decision rule is to fund $B$ over $A$ if $ICER < \lambda$, where $\lambda$ is the threshold cost per QALY (NICE uses GBP 20,000 to 30,000).</p>

<p><strong>Eliciting $q$.</strong> Three standard methods:</p>
<ol>
<li><strong>Standard gamble (SG).</strong> Respondent indifferent between certain health state $h$ and a lottery (perfect health with probability $p$, death with probability $1-p$). Then $q(h) = p$. SG is theoretically grounded in expected utility but conflates risk aversion with quality preferences.</li>
<li><strong>Time trade-off (TTO).</strong> Respondent indifferent between $T$ years in state $h$ and $x$ years in perfect health. Then $q(h) = x/T$. TTO assumes linear preferences over life-years.</li>
<li><strong>Visual analogue scale (VAS).</strong> Respondent rates $h$ on a 0 to 100 scale. Easy but not based on a choice and not directly comparable across people.</li>
</ol>

<p>The EQ-5D instrument (used by NICE) elicits 5 dimensions (mobility, self-care, usual activities, pain, anxiety) at three or five levels each, and maps to $q$ via a UK population tariff (Dolan, 1997).</p>

<p><strong>Theoretical objections (Micro2025.pdf Topic 2 Lecture 5):</strong></p>
<ol>
<li><strong>Constant proportional trade-off.</strong> QALYs assume $q$ is independent of remaining life expectancy. Violated empirically when respondents place special weight on the next few years.</li>
<li><strong>Risk neutrality over years.</strong> Pliskin, Shepard and Weinstein (1980) showed QALY-maximisation under EU requires risk neutrality over life-years given health state, plus an independence axiom.</li>
<li><strong>Distributional issues.</strong> Counting one QALY equally regardless of recipient. The young get larger lifetime gains, biasing decisions against the elderly. NICE's end-of-life premium and the proposed severity modifier are responses.</li>
<li><strong>Age discrimination.</strong> Disability-adjusted life year (DALY) weights have been criticised similarly.</li>
</ol>

<p><em>References:</em> Hindriks and Myles Ch. 13; NICE Methods Guide (2022); Drummond et al., <em>Methods for the Economic Evaluation of Health Care Programmes</em>.</p>
""",
        "widget": r"""
<svg id="widget-qaly" viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fff">
  <line x1="70" y1="270" x2="560" y2="270" stroke="#333" stroke-width="1.5"/>
  <line x1="70" y1="270" x2="70" y2="30" stroke="#333" stroke-width="1.5"/>
  <text x="430" y="295" font-size="13" fill="#333">Years</text>
  <text x="20" y="55" font-size="13" fill="#333">Quality $q$</text>
  <line x1="70" y1="60" x2="65" y2="60" stroke="#333"/>
  <text x="40" y="64" font-size="11" fill="#333">1.0</text>
  <line x1="70" y1="270" x2="65" y2="270" stroke="#333"/>
  <text x="50" y="285" font-size="11" fill="#333">0</text>
  <rect x="80" y="150" width="180" height="120" fill="#d62728" opacity="0.4" stroke="#d62728"/>
  <text x="100" y="145" font-size="11" fill="#d62728">No Tx: 6 yrs at $q=0.5$</text>
  <text x="100" y="170" font-size="13" fill="#d62728" font-weight="bold">QALYs = 3.0</text>
  <rect x="300" y="90" width="240" height="180" fill="#2ca02c" opacity="0.4" stroke="#2ca02c"/>
  <text x="320" y="85" font-size="11" fill="#2ca02c">Tx: 8 yrs at $q=0.75$</text>
  <text x="320" y="120" font-size="13" fill="#2ca02c" font-weight="bold">QALYs = 6.0</text>
  <rect x="80" y="20" width="480" height="22" fill="#fff" stroke="#1f77b4"/>
  <text x="90" y="36" font-size="12" fill="#1f77b4" font-weight="bold">Delta QALYs = 3.0. If Delta cost = GBP 60,000, ICER = GBP 20,000 per QALY.</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">QALYs as area under the survival-quality profile. The treatment extends both length and quality of life. The incremental cost per QALY gained is the decision rule for NICE reimbursement.</p>
""",
        "examples": r"""
<ul>
<li><strong>NICE drug appraisals.</strong> NICE assesses every new NHS-funded medicine on cost per QALY. Trastuzumab (Herceptin) for HER2-positive breast cancer was approved at around GBP 27,000 per QALY in 2006; bevacizumab for bowel cancer was rejected at over GBP 35,000 per QALY in 2010.</li>
<li><strong>QALY league tables.</strong> Williams (1985) ranked interventions: pacemakers around GBP 700 per QALY, kidney dialysis around GBP 14,000, heart transplant around GBP 5,000 (1985 prices). The big methodological point: routinely large differences across interventions imply room for reallocation.</li>
<li><strong>Public-health interventions.</strong> Cancer screening, vaccination programmes, smoking cessation all evaluated on cost per QALY. End-of-life premium (1.2 weight) reflects social preference for treatments extending the lives of the dying.</li>
<li><strong>Essay move: distinguish QALY from value of statistical life.</strong> QALYs are used when the question is "how should we allocate a fixed health budget?", while VSL is used when the question is "how much risk reduction is worth the cost?". Doornik rewards students who get this right.</li>
<li><strong>Essay move: discuss equity weighting and the severity modifier.</strong> NICE's 2022 methods update introduced severity-of-illness multipliers (1.2 to 1.7) to address the concern that pure cost per QALY discriminates against the worst-off. A balanced answer engages with the trade-off between efficiency and equity.</li>
<li><strong>Limitation.</strong> QALY weights are population averages but treatment effects are heterogeneous. Patients with rare diseases or end-of-life conditions often have small QALY gains in absolute terms despite very high individual stakes.</li>
<li><strong>See also</strong> [[Concepts/Cost-Benefit Analysis]] and [[Concepts/Value of Statistical Life]].</li>
</ul>
"""
    },

    "public-goods": {
        "math": r"""
<p>A <em>pure public good</em> is non-rival in consumption and non-excludable in supply. With $G$ the quantity provided and agents $i = 1, \ldots, n$ holding quasi-linear preferences $u_i(x_i, G) = v_i(G) + x_i$ over a numeraire $x_i$ and the public good, every agent simultaneously consumes the same $G$. Production uses the numeraire one-for-one at marginal cost $c$.</p>

<p>The social planner chooses $G$ to maximise $\sum_i v_i(G) - cG$. The first-order condition gives the <strong>Samuelson rule</strong>:</p>

<p>$$\sum_{i=1}^{n} \mathrm{MRS}_{G,x}^{i} = \mathrm{MRT}_{G,x}, \quad \text{equivalently} \quad \sum_{i=1}^{n} v_i'(G^*) = c.$$</p>

<p>The sum of marginal benefits, vertically aggregated rather than horizontally as for private goods, must equal marginal cost. The vertical aggregation reflects that one unit of $G$ benefits every agent at once.</p>

<ol>
<li>Derivation: with $u_i = v_i(G) + x_i$ and resource constraint $\sum_i x_i + cG = \sum_i \omega_i$, substitute and differentiate with respect to $G$. The sum of $v_i'$ minus $c$ vanishes at the optimum.</li>
<li>Compare with private goods, where each agent's MRS equals the price and the planner sets the same MRS for everyone (horizontal aggregation of demand). For public goods every agent gets the same quantity, so demands are stacked vertically.</li>
<li>Decentralisation: a Lindahl equilibrium assigns each agent a personalised price $p_i$ with $\sum_i p_i = c$, and each agent demands the same $G$ at $p_i$. Efficient but requires the planner to know $v_i'(\cdot)$, which agents will not reveal truthfully (see Clarke-Groves).</li>
<li>Under voluntary contribution, agent $i$ equates $v_i'(G)$, not $\sum_j v_j'(G)$, to $c$, so $G^{\text{Nash}} < G^*$.</li>
</ol>

<p>References: Micro2025.pdf Lecture 3.1; Hindriks-Myles Ch. 6.2; Mas-Colell Ch. 11.C.</p>
""",
        "widget": r"""
<svg id="widget-public-goods" viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;font-family:system-ui,sans-serif">
  <rect x="0" y="0" width="600" height="320" fill="var(--bg,#fafafa)"/>
  <line x1="60" y1="280" x2="560" y2="280" stroke="currentColor" stroke-width="1.5"/>
  <line x1="60" y1="20" x2="60" y2="280" stroke="currentColor" stroke-width="1.5"/>
  <text x="560" y="300" font-size="12" text-anchor="end">G</text>
  <text x="50" y="20" font-size="12" text-anchor="end">$/unit</text>
  <line x1="60" y1="220" x2="560" y2="120" stroke="#2a6" stroke-width="1.5" stroke-dasharray="4 3"/>
  <text x="565" y="120" font-size="11" fill="#2a6">MB_1</text>
  <line x1="60" y1="240" x2="560" y2="140" stroke="#26a" stroke-width="1.5" stroke-dasharray="4 3"/>
  <text x="565" y="140" font-size="11" fill="#26a">MB_2</text>
  <line x1="60" y1="160" x2="560" y2="-40" stroke="#a26" stroke-width="2"/>
  <text x="565" y="55" font-size="11" fill="#a26">SMB = MB_1 + MB_2</text>
  <line x1="60" y1="100" x2="560" y2="100" stroke="#444" stroke-width="1.5"/>
  <text x="565" y="100" font-size="11" fill="#444">MC = c</text>
  <circle cx="240" cy="100" r="4" fill="#a26"/>
  <text x="240" y="92" font-size="11" fill="#a26" text-anchor="middle">G*</text>
  <line x1="240" y1="100" x2="240" y2="280" stroke="#a26" stroke-width="0.7" stroke-dasharray="2 2"/>
  <circle cx="125" cy="100" r="4" fill="#2a6"/>
  <text x="125" y="92" font-size="11" fill="#2a6" text-anchor="middle">G_1</text>
  <text x="300" y="40" font-size="13" font-weight="bold">Samuelson rule: vertical sum of MBs = MC</text>
</svg>
<p class="caption" style="font-size:0.85em;color:var(--muted,#666);margin-top:0.4em">Vertical aggregation of marginal benefits gives social MB. The Samuelson level $G^*$ sits where $\sum_i v_i'(G) = c$. Each agent's private optimum $G_i$ where $v_i'(G_i) = c$ is much smaller.</p>
""",
        "examples": r"""
<ol>
<li><strong>National defence.</strong> Each citizen values security but cannot be excluded from it; the Samuelson rule says the optimal defence budget equates aggregate marginal willingness-to-pay to marginal cost. Private contribution would yield almost nothing.</li>
<li><strong>Basic research.</strong> Once a theorem is proved or a vaccine target identified, knowledge is non-rival. Underprovision by private firms justifies public funding (NIH, Wellcome) and patent systems as partial excludability fixes.</li>
<li><strong>Essay move: pin down the public-good label.</strong> Kate Doornik rewards students who specify <em>which</em> non-rivalry and <em>which</em> non-excludability they mean. A lighthouse is non-rival but ships <em>can</em> in principle be excluded, so Coase 1974 famously argued lighthouses are not the textbook example after all.</li>
<li><strong>Essay move: vertical vs horizontal aggregation.</strong> The mark scheme expects an explicit contrast with the private-good demand curve, derived from the consumer's MRS condition, and a sentence on why decentralised provision under Lindahl requires personalised prices.</li>
<li><strong>Essay move: Samuelson rule under heterogeneous preferences.</strong> Strong candidates note that the planner needs to know each $v_i'(G^*)$, which motivates mechanism design (link to [[Concepts/Clarke-Groves Mechanism]]).</li>
<li>Limitation: most real goods are mixed. Education is partly rival (class size), partly excludable (tuition), and partly externality-generating (citizenship). Pure Samuelson logic gives the wrong answer if congestion is present, which motivates club goods.</li>
</ol>
""",
    },
    "free-rider-problem": {
        "math": r"""
<p>Consider $n$ agents with quasi-linear utility $u_i = v_i(G) + x_i$ over a public good $G$ produced one-for-one from the numeraire at marginal cost $c$. Agent $i$ chooses contribution $g_i \geq 0$, total provision $G = \sum_j g_j$, and faces budget $x_i + g_i = \omega_i$.</p>

<p>Agent $i$'s problem, taking $G_{-i} = \sum_{j \neq i} g_j$ as given, is</p>
<p>$$\max_{g_i \geq 0} \ v_i(g_i + G_{-i}) + \omega_i - g_i.$$</p>

<p>If interior, the first-order condition is $v_i'(G) = 1$ (with $c = 1$ normalised). The Samuelson optimum requires $\sum_j v_j'(G^*) = 1$, so $G^{\text{N}} < G^*$ whenever $v_j' > 0$ for $j \neq i$. The gap $G^* - G^{\text{N}}$ is the <strong>free-rider distortion</strong>.</p>

<ol>
<li>If $v_i(G) = \alpha_i \ln G$, the interior Nash condition is $\alpha_i / G = 1$, so only the agent with the largest $\alpha_i$ contributes; all others free-ride. This is the "exploitation of the great by the small" result (Olson 1965).</li>
<li>The <strong>neutrality result</strong>: total $G^{\text{N}}$ is invariant to redistribution of wealth across contributors and, under symmetric preferences, to $n$. Adding agents reduces individual contributions one-for-one; total provision does not rise (Warr 1983; Bergstrom, Blume, Varian 1986).</li>
<li>The free-rider problem grows with $n$ in the sense that the per-capita shortfall does not vanish: $G^{\text{N}} / n \to 0$ while $G^* / n$ stays bounded under standard concavity.</li>
<li>Experimental evidence (Isaac, Walker, Williams 1994): in linear public-good games, contribution starts around 50% of endowment and decays with repetition, falling short of the Nash prediction of zero but well below the optimum.</li>
</ol>

<p>The problem motivates compulsory taxation, mechanism design (Clarke-Groves), and the use of social norms or assurance contracts. References: Micro2025.pdf Lecture 3.1; Hindriks-Myles Ch. 6.3; Mas-Colell Ch. 11.C.</p>
""",
        "widget": r"""
<svg id="widget-free-rider-problem" viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;font-family:system-ui,sans-serif">
  <rect width="600" height="320" fill="var(--bg,#fafafa)"/>
  <line x1="60" y1="280" x2="560" y2="280" stroke="currentColor"/>
  <line x1="60" y1="20" x2="60" y2="280" stroke="currentColor"/>
  <text x="300" y="305" font-size="12" text-anchor="middle">Number of agents n</text>
  <text x="55" y="20" font-size="12" text-anchor="end">G</text>
  <path d="M 80 80 Q 200 95 320 110 T 540 130" stroke="#a26" stroke-width="2" fill="none"/>
  <text x="545" y="125" font-size="11" fill="#a26">G* (Samuelson)</text>
  <path d="M 80 200 Q 200 220 320 232 T 540 240" stroke="#26a" stroke-width="2" fill="none"/>
  <text x="545" y="235" font-size="11" fill="#26a">G^N (Nash, total)</text>
  <path d="M 80 210 Q 200 250 320 265 T 540 275" stroke="#2a6" stroke-width="2" stroke-dasharray="4 3" fill="none"/>
  <text x="545" y="270" font-size="11" fill="#2a6">G^N / n (per capita)</text>
  <text x="300" y="40" font-size="13" font-weight="bold" text-anchor="middle">Free-rider shortfall widens with n</text>
</svg>
<p class="caption" style="font-size:0.85em;color:var(--muted,#666);margin-top:0.4em">Optimal provision $G^*$ rises with $n$ (more beneficiaries). Total Nash provision $G^N$ stays roughly flat (neutrality), so per-capita Nash provision falls toward zero.</p>
""",
        "examples": r"""
<ol>
<li><strong>Public radio pledge drives.</strong> NPR's listener-supported model relies on a fraction of beneficiaries contributing while most listen for free. Donation rates under 10% match the empirical free-rider rate.</li>
<li><strong>Vaccination herd immunity.</strong> Each unvaccinated person free-rides on others' immunity, generating a private equilibrium below the public-health optimum and motivating mandates or subsidies.</li>
<li><strong>Essay move: distinguish strong from weak free riding.</strong> Strong free riding (Nash prediction of zero contribution) almost never holds in experiments; weak free riding (some contribute, but below optimum) does. Examiners reward this nuance.</li>
<li><strong>Essay move: cite the neutrality result.</strong> Bergstrom-Blume-Varian (1986) gives a sharp comparative-static prediction that lump-sum transfers among contributors leave total $G$ unchanged. A confident essay names the result and its interior assumption.</li>
<li><strong>Essay move: link to mechanism design.</strong> Show how Clarke-Groves resolves the truthful-revelation problem at the cost of budget balance (link to [[Concepts/Clarke-Groves Mechanism]]).</li>
<li>Limitation: repeated interaction, reciprocity norms, and warm-glow preferences (Andreoni 1990) can sustain contribution well above the Nash level. Pure free-rider theory predicts under-provision but cannot explain the level of voluntary giving in practice.</li>
</ol>
""",
    },
    "voluntary-contribution-nash": {
        "math": r"""
<p>Set up the canonical voluntary contribution game. Agents $i = 1, \ldots, n$, each with wealth $\omega_i$, choose $g_i \geq 0$ contributing to a public good $G = \sum_j g_j$ at unit cost. Preferences are $u_i(x_i, G) = v_i(G) + x_i$ with $v_i$ strictly increasing and concave, and $x_i = \omega_i - g_i$.</p>

<p>Agent $i$'s best response, conditional on $G_{-i} = \sum_{j \neq i} g_j$, solves</p>
<p>$$\max_{g_i \geq 0} \ v_i(g_i + G_{-i}) - g_i.$$</p>

<p>The Kuhn-Tucker conditions give $v_i'(G) \leq 1$, with equality if $g_i > 0$. Aggregating across interior contributors yields a Nash equilibrium $G^{\text{N}}$ characterised by $v_i'(G^{\text{N}}) = 1$ for each contributor.</p>

<ol>
<li>With symmetric agents and $v(G) = a \ln G$, the symmetric Nash has each agent contributing $g^{\text{N}} = a / n$ and total $G^{\text{N}} = a$. The Samuelson level is $G^* = na$, so $G^{\text{N}} / G^* = 1/n$.</li>
<li><strong>Neutrality (BBV 1986).</strong> Take any interior equilibrium and redistribute wealth among contributors. Each contributor adjusts $g_i$ one-for-one with the transfer, leaving $G^{\text{N}}$ unchanged. Formally, $\partial G^{\text{N}} / \partial \omega_i = 0$ when transferring from contributor to contributor.</li>
<li><strong>Invariance to $n$.</strong> Adding an identical agent: the new agent contributes $a/n$ if interior, but each existing agent reduces by the same amount, so $G$ stays at $a$. With a non-contributor entering, $G$ is exactly unchanged.</li>
<li>Corner case: if $v_i'(0) < 1$ at the equilibrium $G_{-i}$, agent $i$ contributes nothing. Olson's exploitation of the great by the small follows when high-$v_i$ types alone reach the FOC.</li>
</ol>

<p>The equilibrium is inefficient because each agent ignores the marginal benefit conferred on others. The wedge $\sum_j v_j'(G^{\text{N}}) - v_i'(G^{\text{N}}) = n - 1$ in the symmetric log case measures the externality.</p>

<p>References: Micro2025.pdf Lecture 3.1; Hindriks-Myles Ch. 6.3; Bergstrom, Blume, Varian 1986 JPE.</p>
""",
        "widget": r"""
<svg id="widget-voluntary-contribution-nash" viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;font-family:system-ui,sans-serif">
  <rect width="600" height="320" fill="var(--bg,#fafafa)"/>
  <line x1="60" y1="280" x2="560" y2="280" stroke="currentColor"/>
  <line x1="60" y1="20" x2="60" y2="280" stroke="currentColor"/>
  <text x="555" y="300" font-size="12" text-anchor="end">g_1</text>
  <text x="55" y="20" font-size="12" text-anchor="end">g_2</text>
  <line x1="60" y1="80" x2="280" y2="280" stroke="#26a" stroke-width="2"/>
  <text x="285" y="280" font-size="11" fill="#26a">BR_2(g_1)</text>
  <line x1="80" y1="280" x2="280" y2="60" stroke="#a26" stroke-width="2"/>
  <text x="290" y="60" font-size="11" fill="#a26">BR_1(g_2)</text>
  <circle cx="190" cy="190" r="5" fill="#222"/>
  <text x="200" y="195" font-size="11">Nash (g_1^N, g_2^N)</text>
  <line x1="190" y1="280" x2="190" y2="190" stroke="#222" stroke-width="0.6" stroke-dasharray="2 2"/>
  <line x1="60" y1="190" x2="190" y2="190" stroke="#222" stroke-width="0.6" stroke-dasharray="2 2"/>
  <text x="300" y="40" font-size="13" font-weight="bold" text-anchor="middle">Best-response intersection: Nash contributions</text>
</svg>
<p class="caption" style="font-size:0.85em;color:var(--muted,#666);margin-top:0.4em">Each agent's best response is downward sloping: more contribution from the other crowds out one's own. The Nash equilibrium sits where the two best responses intersect; total $G^N = g_1^N + g_2^N$ falls short of the Samuelson level.</p>
""",
        "examples": r"""
<ol>
<li><strong>Charity giving.</strong> Andreoni-Vesterlund evidence shows giving falls when others give more, consistent with the BR-crowd-out logic, but only partially (warm glow attenuates pure neutrality).</li>
<li><strong>International climate negotiations.</strong> Each country chooses abatement taking others' abatement as given; the result is global under-provision relative to the Pareto optimum, the textbook free-rider problem at country level.</li>
<li><strong>Essay move: derive the neutrality result.</strong> A clean derivation of Bergstrom-Blume-Varian (1986) and a statement of the interior assumption distinguishes a 2:1 from a first.</li>
<li><strong>Essay move: contrast Nash and Lindahl.</strong> Both decentralised, but Lindahl uses personalised prices announced by an auctioneer who knows preferences; Nash uses anonymous voluntary contributions and yields under-provision. The role of information is the punchline.</li>
<li><strong>Essay move: invoke quasi-linear assumption.</strong> The neutrality and invariance results require quasi-linearity. Mention that with general preferences (income effects on $G$), redistribution changes total provision.</li>
<li>Limitation: empirically, players in linear public-good games contribute 40-60% of endowment, far above the zero-contribution Nash prediction in the linear case. Theory predicts the wrong level (link to [[Concepts/Free Rider Problem]]).</li>
</ol>
""",
    },
    "clarke-groves-mechanism": {
        "math": r"""
<p>A public-good mechanism asks each agent to report a type (here, a valuation function) and uses reports to choose an allocation and a payment. Let agent $i$ have private valuation $v_i(G)$ over public-good levels $G \in \mathcal{G}$ and quasi-linear utility $u_i = v_i(G) - t_i$ where $t_i$ is the payment.</p>

<p>The <strong>Clarke-Groves (VCG)</strong> mechanism chooses $G^*(\hat v) = \arg\max_G \sum_i \hat v_i(G) - c(G)$ given reports $\hat v$. The payment from agent $i$ is</p>
<p>$$t_i(\hat v) = h_i(\hat v_{-i}) - \sum_{j \neq i} \hat v_j(G^*(\hat v)),$$</p>
<p>where $h_i(\cdot)$ depends only on others' reports. The <strong>Clarke (pivotal) variant</strong> sets $h_i = \sum_{j \neq i} \hat v_j(G^*_{-i})$, where $G^*_{-i}$ is the optimal allocation ignoring $i$. Then</p>
<p>$$t_i^{\text{Clarke}} = \sum_{j \neq i} \hat v_j(G^*_{-i}) - \sum_{j \neq i} \hat v_j(G^*).$$</p>

<p>This is the <em>externality</em> agent $i$ imposes on others by participating: others' total welfare under $G^*_{-i}$ minus their welfare under $G^*$.</p>

<ol>
<li><strong>Dominant-strategy truthfulness.</strong> Agent $i$'s utility under reports $(\hat v_i, \hat v_{-i})$ is $v_i(G^*(\hat v)) + \sum_{j \neq i} \hat v_j(G^*(\hat v)) - h_i(\hat v_{-i})$. The first two terms are exactly the planner's objective evaluated at the chosen $G$. Reporting $\hat v_i = v_i$ aligns the agent with the planner, so truth-telling maximises utility regardless of others' reports.</li>
<li><strong>Efficient allocation.</strong> Because everyone reports truthfully, $G^*(\hat v) = G^*(v)$ is the first-best.</li>
<li><strong>Budget imbalance.</strong> Generically $\sum_i t_i \neq 0$. Green-Laffont (1979) show no dominant-strategy mechanism can be both efficient and budget-balanced for all type profiles. The Clarke tax collects net revenue, which cannot be redistributed without breaking incentives.</li>
<li><strong>Individual rationality.</strong> With $h_i$ chosen as above, $t_i \geq 0$ and $u_i \geq 0$ for any agent who is non-pivotal. Pivotal agents pay positive amounts but still gain (otherwise they would not be pivotal).</li>
</ol>

<p>References: Micro2025.pdf Lecture 3.2; Hindriks-Myles Ch. 7.3; Mas-Colell Ch. 23.C; Clarke 1971; Groves 1973.</p>
""",
        "widget": r"""
<svg id="widget-clarke-groves-mechanism" viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;font-family:system-ui,sans-serif">
  <rect width="600" height="320" fill="var(--bg,#fafafa)"/>
  <text x="300" y="30" font-size="14" font-weight="bold" text-anchor="middle">VCG payment = externality on others</text>
  <rect x="60" y="70" width="220" height="60" fill="#eef" stroke="#26a"/>
  <text x="170" y="95" font-size="12" text-anchor="middle">With agent i</text>
  <text x="170" y="115" font-size="11" text-anchor="middle">Others' welfare = sum v_j(G*)</text>
  <rect x="320" y="70" width="220" height="60" fill="#fee" stroke="#a26"/>
  <text x="430" y="95" font-size="12" text-anchor="middle">Without agent i</text>
  <text x="430" y="115" font-size="11" text-anchor="middle">Others' welfare = sum v_j(G*_minus_i)</text>
  <line x1="280" y1="100" x2="320" y2="100" stroke="#444" stroke-width="1.5"/>
  <rect x="120" y="180" width="360" height="80" fill="#efe" stroke="#2a6"/>
  <text x="300" y="210" font-size="13" text-anchor="middle" font-weight="bold">Clarke tax on i</text>
  <text x="300" y="235" font-size="12" text-anchor="middle">t_i = sum v_j(G*_minus_i) minus sum v_j(G*)</text>
  <text x="300" y="252" font-size="11" text-anchor="middle" fill="#666">= harm i's participation imposes on others</text>
</svg>
<p class="caption" style="font-size:0.85em;color:var(--muted,#666);margin-top:0.4em">The Clarke tax internalises the externality: each agent pays for how their report alters the allocation against others' interests. Truth-telling is a dominant strategy because the agent and planner share the same residual objective.</p>
""",
        "examples": r"""
<ol>
<li><strong>FCC spectrum auctions.</strong> Combinatorial VCG-style auctions allocate radio spectrum licences; bidders bid on packages and pay the externality their winning bid imposes on losers.</li>
<li><strong>Sponsored search.</strong> Google's AdWords uses a generalised second-price auction, closely related to VCG, with each advertiser paying roughly the externality on the next-best advertiser.</li>
<li><strong>Essay move: state the impossibility.</strong> Cite Green-Laffont (1979): no Bayesian-incentive-compatible, efficient, ex-post budget-balanced mechanism exists in general. The Clarke tax achieves the first two but sacrifices the third.</li>
<li><strong>Essay move: contrast with Lindahl.</strong> Lindahl pricing also implements the Samuelson optimum but requires the planner to compute personalised prices using true preferences; VCG works with reports and incentivises truth.</li>
<li><strong>Essay move: connect to Vickrey.</strong> The second-price auction is the single-unit special case (link to [[Concepts/Vickrey Auction]]).</li>
<li>Limitation: the mechanism assumes quasi-linear utility, full rationality, and unlimited wealth; in practice, bidders can fail to bid truthfully under collusion, budget constraints, or risk aversion. Real-world adoption is rare because of the budget-imbalance and complexity issues.</li>
</ol>
""",
    },
    "coase-theorem": {
        "math": r"""
<p>Two parties: a polluter who chooses emissions $q \geq 0$ generating private benefit $B(q)$ with $B' > 0$, $B'' < 0$, and a victim suffering damages $D(q)$ with $D' > 0$, $D'' > 0$. The social optimum solves</p>
<p>$$\max_q \ B(q) - D(q), \quad \Rightarrow \quad B'(q^*) = D'(q^*).$$</p>

<p>The <strong>Coase theorem</strong> (Coase 1960) states: if property rights over $q$ are clearly assigned and transaction costs are zero, the parties bargain to $q^*$ regardless of who holds the right. Distribution of surplus depends on the assignment; allocation does not.</p>

<ol>
<li><strong>Polluter has the right.</strong> Absent bargaining, the polluter chooses $q^P = \arg\max B(q)$. The victim offers payment $P$ to reduce emissions from $q^P$ to $q$, willing to pay up to $D(q^P) - D(q)$. The polluter accepts any $P \geq B(q^P) - B(q)$. Joint surplus is maximised by setting $q = q^*$ where $B' = D'$.</li>
<li><strong>Victim has the right.</strong> Absent bargaining, $q = 0$. The polluter offers payment $P$ to be allowed emissions $q$, willing to pay up to $B(q) - B(0)$. The victim accepts any $P \geq D(q) - D(0)$. Again $q^*$ maximises joint surplus.</li>
<li><strong>Invariance of allocation.</strong> Both regimes solve $\max_q B(q) - D(q)$ once side-payments are possible. Only the lump-sum transfer differs: under polluter rights, victim pays polluter; under victim rights, polluter pays victim.</li>
<li><strong>Caveats.</strong> Multiple polluters or victims raise transaction costs and create free-rider problems within each side; asymmetric information about $B$ or $D$ breaks the theorem (Myerson-Satterthwaite 1983); wealth effects matter if utility is not quasi-linear.</li>
</ol>

<p>The Coase theorem reframes externalities as a property-rights problem rather than a market-failure problem. It complements Pigou: where Pigou says "tax the externality at marginal damage," Coase says "assign the right and let bargaining handle it."</p>

<p>References: Micro2025.pdf Lecture 3.3; Hindriks-Myles Ch. 7.5; Mas-Colell Ch. 11.D; Coase 1960 JLE.</p>
""",
        "widget": r"""
<svg id="widget-coase-theorem" viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;font-family:system-ui,sans-serif">
  <rect width="600" height="320" fill="var(--bg,#fafafa)"/>
  <line x1="60" y1="280" x2="560" y2="280" stroke="currentColor"/>
  <line x1="60" y1="20" x2="60" y2="280" stroke="currentColor"/>
  <text x="555" y="300" font-size="12" text-anchor="end">q (emissions)</text>
  <text x="55" y="20" font-size="12" text-anchor="end">$/unit</text>
  <line x1="60" y1="60" x2="540" y2="260" stroke="#26a" stroke-width="2"/>
  <text x="545" y="265" font-size="11" fill="#26a">D'(q) marginal damage</text>
  <line x1="60" y1="100" x2="540" y2="280" stroke="#a26" stroke-width="2"/>
  <text x="545" y="280" font-size="11" fill="#a26">B'(q) marginal benefit</text>
  <circle cx="285" cy="170" r="5" fill="#222"/>
  <text x="295" y="170" font-size="11">q*: B' = D'</text>
  <line x1="285" y1="170" x2="285" y2="280" stroke="#222" stroke-width="0.6" stroke-dasharray="2 2"/>
  <text x="170" y="50" font-size="12" fill="#444">Same q* under either rights regime</text>
  <text x="170" y="68" font-size="11" fill="#666">(transfers differ; allocation does not)</text>
</svg>
<p class="caption" style="font-size:0.85em;color:var(--muted,#666);margin-top:0.4em">Whoever holds the right, voluntary bargaining drives $q$ to $q^*$ where marginal benefit equals marginal damage. The distribution of surplus shifts with the assignment; the allocation is invariant.</p>
""",
        "examples": r"""
<ol>
<li><strong>Sturges v Bridgman (1879).</strong> Doctor and confectioner share a wall; the confectioner's mortar noise disturbs the doctor's consulting room. Coase's reading: in principle the parties could bargain to the efficient noise level, with the court's role being to assign the right cheaply.</li>
<li><strong>Conservation easements.</strong> Land trusts buy development rights from landowners, internalising the amenity externality. A textbook Coasean exchange where the victim (the public, via the trust) compensates the polluter (the developer) for restraint.</li>
<li><strong>Essay move: name the assumptions.</strong> Coase 1960 lists: well-defined rights, zero transaction costs, full information, no wealth effects. Examiners reward students who tick each off and explain why each fails in practice.</li>
<li><strong>Essay move: invariance vs efficiency.</strong> The theorem has two parts. Efficiency: bargaining reaches the optimum. Invariance: the optimum is the same regardless of assignment. The invariance part is the stronger claim and the one most easily refuted by wealth effects.</li>
<li><strong>Essay move: contrast with Pigou.</strong> Pigouvian tax requires the planner to know $D'(q^*)$; Coase requires only that rights be assigned and bargaining be cheap. Information requirements differ (link to [[Concepts/Externality Internalisation]]).</li>
<li>Limitation: with many parties (climate change, congestion), transaction costs explode and the free-rider problem on the victim side blocks bargaining. The Myerson-Satterthwaite theorem (1983) further rules out efficient bargaining under two-sided private information.</li>
</ol>
""",
    },
    "tragedy-of-the-commons": {
        "math": r"""
<p>An open-access resource (a fishery, a grazing pasture, a congestible road) yields output $F(E)$ given total effort $E = \sum_i e_i$, with $F$ strictly increasing and concave. Each user $i$ chooses effort $e_i \geq 0$ at unit cost $c$ and earns a share $e_i / E$ of total output:</p>
<p>$$\pi_i(e_i; E_{-i}) = \frac{e_i}{e_i + E_{-i}} F(e_i + E_{-i}) - c e_i.$$</p>

<p>The first-order condition for user $i$ is</p>
<p>$$\frac{E_{-i}}{E^2} F(E) + \frac{e_i}{E} F'(E) = c.$$</p>

<p>In the symmetric Nash equilibrium with $n$ identical users, $e_i = E/n$, giving</p>
<p>$$\frac{n - 1}{n} \cdot \frac{F(E)}{E} + \frac{1}{n} F'(E) = c.$$</p>

<p>The <strong>social planner</strong> chooses $E$ to maximise $F(E) - cE$, yielding $F'(E^{\text{SP}}) = c$. Compare: each Nash user equates an average-product weighted condition to $c$, while the planner equates the marginal product.</p>

<ol>
<li>Since average product exceeds marginal product (because $F$ is concave), the Nash condition holds at higher $E$ than the planner's: $E^{\text{N}} > E^{\text{SP}}$. The commons is over-used.</li>
<li>As $n \to \infty$, the Nash condition becomes $F(E)/E = c$: effort is pushed to the point where average product equals marginal cost, dissipating all rent. This is the classic <strong>rent dissipation</strong> result (Gordon 1954).</li>
<li>The deadweight loss is $[F(E^{\text{SP}}) - cE^{\text{SP}}] - [F(E^{\text{N}}) - cE^{\text{N}}] > 0$, the foregone rent.</li>
<li>Solutions: (a) privatise the resource so one owner internalises the externality; (b) regulate quotas to enforce $E^{\text{SP}}$; (c) impose a Pigouvian charge $\tau$ on $e_i$ equal to the marginal congestion externality; (d) Ostrom (1990) shows community norms can substitute when monitoring is cheap.</li>
</ol>

<p>References: Micro2025.pdf Lecture 3.3; Hindriks-Myles Ch. 8.2; Gordon 1954 JPE; Hardin 1968 Science; Ostrom 1990.</p>
""",
        "widget": r"""
<svg id="widget-tragedy-of-the-commons" viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;font-family:system-ui,sans-serif">
  <rect width="600" height="320" fill="var(--bg,#fafafa)"/>
  <line x1="60" y1="280" x2="560" y2="280" stroke="currentColor"/>
  <line x1="60" y1="20" x2="60" y2="280" stroke="currentColor"/>
  <text x="555" y="300" font-size="12" text-anchor="end">E (effort)</text>
  <text x="55" y="20" font-size="12" text-anchor="end">$/unit effort</text>
  <path d="M 80 80 Q 200 100 320 140 T 540 220" stroke="#26a" stroke-width="2" fill="none"/>
  <text x="545" y="220" font-size="11" fill="#26a">F(E)/E (average product)</text>
  <path d="M 80 60 Q 200 130 320 200 T 540 270" stroke="#a26" stroke-width="2" fill="none"/>
  <text x="545" y="270" font-size="11" fill="#a26">F'(E) (marginal product)</text>
  <line x1="60" y1="180" x2="560" y2="180" stroke="#444" stroke-width="1.5"/>
  <text x="545" y="175" font-size="11" fill="#444">c (marginal cost)</text>
  <circle cx="225" cy="180" r="5" fill="#a26"/>
  <text x="235" y="172" font-size="11" fill="#a26">E^SP</text>
  <circle cx="395" cy="180" r="5" fill="#26a"/>
  <text x="405" y="172" font-size="11" fill="#26a">E^N (large n)</text>
  <text x="300" y="40" font-size="13" font-weight="bold" text-anchor="middle">Open access: effort pushed to where AP = c</text>
</svg>
<p class="caption" style="font-size:0.85em;color:var(--muted,#666);margin-top:0.4em">Planner stops at $F'(E) = c$, where marginal product covers marginal cost. Open access pushes effort to where average product equals $c$, dissipating the rent.</p>
""",
        "examples": r"""
<ol>
<li><strong>North Atlantic cod collapse (1992).</strong> Open-access fishing pushed effort beyond sustainable yield; the Canadian government imposed a moratorium that destroyed 35,000 jobs. A textbook commons failure resolved by quota (ITQs in some Atlantic fisheries).</li>
<li><strong>Urban traffic congestion.</strong> Each driver imposes a marginal travel-time externality on others. London's congestion charge (2003) is a Pigouvian fix that internalises the externality; Singapore's ERP is the dynamic version.</li>
<li><strong>Essay move: derive rent dissipation explicitly.</strong> Show that as $n \to \infty$ the Nash FOC collapses to $F(E)/E = c$, and that the difference $F(E^{SP}) - cE^{SP}$ equals the rent dissipated. Examiners reward the algebra.</li>
<li><strong>Essay move: distinguish Hardin from Ostrom.</strong> Hardin (1968) argued the tragedy is inevitable absent privatisation or state control; Ostrom (1990) documented hundreds of self-governed commons sustained by community norms (link to [[Concepts/Common Pool Resources]]).</li>
<li><strong>Essay move: connect to Coase.</strong> The Coase theorem says privatisation should work if rights can be assigned and bargaining is cheap; the commons is the case where the latter fails.</li>
<li>Limitation: the standard model assumes anonymous users and one-shot interaction. Repeated games, kinship networks, and excludable common goods (gated fisheries) all moderate the prediction; pure tragedy is an upper bound on welfare loss, not a forecast.</li>
</ol>
""",
    },
    "rivalry-and-excludability": {
        "math": r"""
<p>Two axes classify goods. A good is <strong>rival</strong> if one agent's consumption reduces what is available to others: $\partial u_j / \partial x_i < 0$ for $j \neq i$, equivalently the resource constraint binds as $\sum_i x_i \leq Q$. A good is <strong>non-rival</strong> if $\partial u_j / \partial x_i = 0$ for $j \neq i$: all agents consume the same $G$ simultaneously.</p>

<p>A good is <strong>excludable</strong> if it is technologically and legally feasible to prevent non-payers from consuming. Excludability is a property of the supply technology and institutional environment, not preferences.</p>

<p>The 2-by-2 classification:</p>
<ol>
<li><strong>Private goods</strong> (rival, excludable): bread, shoes, a taxi ride. Market provision is efficient under standard assumptions; horizontal demand aggregation.</li>
<li><strong>Club goods</strong> (non-rival, excludable): cable TV, a swimming club, a toll road below congestion. Buchanan (1965) shows membership pricing can internalise capacity; the optimal club size trades off congestion against per-member cost.</li>
<li><strong>Common pool resources</strong> (rival, non-excludable): ocean fisheries, groundwater, unmanaged grazing land. Subject to the tragedy of the commons.</li>
<li><strong>Public goods</strong> (non-rival, non-excludable): national defence, clean air, basic research. Samuelson rule applies; voluntary provision yields free-riding.</li>
</ol>

<p>The Samuelson condition for non-rival goods is $\sum_i v_i'(G) = c$ (vertical aggregation); the private-good condition is $v_i'(x_i^*) = p$ for each $i$, with horizontal aggregation $\sum_i x_i^*(p) = S(p)$.</p>

<p>Excludability is a continuum in practice. A patent makes knowledge partially excludable for 20 years; a paywall makes a webpage partially excludable until pirated. Many goods sit on the boundary: roads (congestible), libraries (excludable but typically not priced), public parks (mostly non-rival until crowded). The framework is a starting taxonomy, not a final classification.</p>

<p>References: Micro2025.pdf Lecture 3.1; Hindriks-Myles Ch. 6.1; Mas-Colell Ch. 11.A.</p>
""",
        "widget": r"""
<svg id="widget-rivalry-and-excludability" viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;font-family:system-ui,sans-serif">
  <rect width="600" height="320" fill="var(--bg,#fafafa)"/>
  <text x="300" y="30" font-size="14" font-weight="bold" text-anchor="middle">Classification by rivalry and excludability</text>
  <line x1="180" y1="60" x2="540" y2="60" stroke="currentColor"/>
  <line x1="360" y1="60" x2="360" y2="290" stroke="currentColor"/>
  <line x1="180" y1="175" x2="540" y2="175" stroke="currentColor"/>
  <line x1="180" y1="60" x2="180" y2="290" stroke="currentColor"/>
  <text x="270" y="50" font-size="12" text-anchor="middle" font-weight="bold">Rival</text>
  <text x="450" y="50" font-size="12" text-anchor="middle" font-weight="bold">Non-rival</text>
  <text x="170" y="115" font-size="12" text-anchor="end" font-weight="bold">Excludable</text>
  <text x="170" y="230" font-size="12" text-anchor="end" font-weight="bold">Non-excludable</text>
  <rect x="180" y="60" width="180" height="115" fill="#eef"/>
  <text x="270" y="110" font-size="12" text-anchor="middle">Private goods</text>
  <text x="270" y="130" font-size="10" text-anchor="middle" fill="#666">bread, shoes</text>
  <rect x="360" y="60" width="180" height="115" fill="#fef"/>
  <text x="450" y="110" font-size="12" text-anchor="middle">Club goods</text>
  <text x="450" y="130" font-size="10" text-anchor="middle" fill="#666">cable TV, toll road</text>
  <rect x="180" y="175" width="180" height="115" fill="#fee"/>
  <text x="270" y="225" font-size="12" text-anchor="middle">Common pool</text>
  <text x="270" y="245" font-size="10" text-anchor="middle" fill="#666">fisheries, aquifer</text>
  <rect x="360" y="175" width="180" height="115" fill="#efe"/>
  <text x="450" y="225" font-size="12" text-anchor="middle">Public goods</text>
  <text x="450" y="245" font-size="10" text-anchor="middle" fill="#666">defence, clean air</text>
</svg>
<p class="caption" style="font-size:0.85em;color:var(--muted,#666);margin-top:0.4em">The 2-by-2 classification. Rivalry is a property of consumption; excludability is a property of the supply technology and institutions. Many real goods sit on the boundary.</p>
""",
        "examples": r"""
<ol>
<li><strong>Streaming video.</strong> Netflix is non-rival (one stream does not crowd out another within capacity) and excludable (paywall). A canonical club good with subscription pricing handling the capacity trade-off.</li>
<li><strong>City parks.</strong> Mostly non-rival when uncrowded, partly rival when packed. Mostly non-excludable (fences and admission charges exist but are rarely deployed). The classification shifts with congestion.</li>
<li><strong>Essay move: name the four cells precisely.</strong> A 1st-class answer states each cell with one canonical example and notes the boundary cases. Vague answers blur club goods and public goods.</li>
<li><strong>Essay move: link rivalry to the Samuelson condition.</strong> Non-rivalry is the technical reason the demands stack vertically; spell out the resource-constraint algebra so the marker sees it.</li>
<li><strong>Essay move: discuss endogenous excludability.</strong> Excludability is a technology choice. The lighthouse case (Coase 1974) shows that supposed non-excludable goods can sometimes be excluded if institutions are cleverly designed (link to [[Concepts/Public Goods]]).</li>
<li>Limitation: the classification is a discrete approximation to a continuum. Real goods are often rivalrous only above congestion thresholds and excludable only at a cost. Buchanan club theory handles this for excludable goods; the framework struggles with knowledge goods (partial excludability via patents).</li>
</ol>
""",
    },
    "marginal-private-vs-social-benefit": {
        "math": r"""
<p>Let an activity be carried out at level $q$, generating private benefit $B(q)$ to the decision-maker and external benefit $E(q)$ to third parties (negative if a cost). Marginal private benefit is $\mathrm{MPB}(q) = B'(q)$; marginal external effect is $\mathrm{MEB}(q) = E'(q)$ (negative for a negative externality); marginal social benefit is</p>
<p>$$\mathrm{MSB}(q) = \mathrm{MPB}(q) + \mathrm{MEB}(q).$$</p>

<p>With private cost $C(q)$, the private optimum solves $\mathrm{MPB}(q^P) = \mathrm{MPC}(q^P)$; the social optimum solves $\mathrm{MSB}(q^*) = \mathrm{MSC}(q^*)$. With positive externality and identical costs, $q^* > q^P$; with negative externality, $q^* < q^P$.</p>

<ol>
<li><strong>Pigouvian correction.</strong> A per-unit tax $\tau = -\mathrm{MEB}(q^*)$ (positive for negative externality) shifts the private FOC to $\mathrm{MPB}(q) - \tau = \mathrm{MPC}(q)$, which coincides with $\mathrm{MSB} = \mathrm{MSC}$ at $q = q^*$. A subsidy $s = \mathrm{MEB}(q^*)$ works for positive externalities.</li>
<li><strong>Sign convention.</strong> A negative externality means $E'(q) < 0$, so MSB lies below MPB; private agents over-supply. A positive externality means $E'(q) > 0$, so MSB lies above MPB; private agents under-supply.</li>
<li><strong>Deadweight loss.</strong> The triangle between MSB and MSC over $[q^*, q^P]$ measures the welfare loss from uncorrected externality, $\int_{q^*}^{q^P} [\mathrm{MSC}(q) - \mathrm{MSB}(q)] dq$.</li>
<li><strong>Optimal Pigouvian tax.</strong> Evaluate $\tau$ at the social optimum, not the laissez-faire equilibrium. This is the Baumol-Oates (1971) observation: $\tau = -E'(q^*)$, not $-E'(q^P)$.</li>
</ol>

<p>The MPB-MSB framework is the workhorse for graphical externality analysis at FHS level. The wedge $|\mathrm{MSB} - \mathrm{MPB}|$ measures the size of the market failure; its area between $q^P$ and $q^*$ measures the welfare cost. Coase, Pigou, and tradeable permits are all attempts to close the wedge by different routes.</p>

<p>References: Micro2025.pdf Lecture 3.3; Hindriks-Myles Ch. 7.2; Mas-Colell Ch. 11.B; Pigou 1920; Baumol-Oates 1971.</p>
""",
        "widget": r"""
<svg id="widget-marginal-private-vs-social-benefit" viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;font-family:system-ui,sans-serif">
  <rect width="600" height="320" fill="var(--bg,#fafafa)"/>
  <line x1="60" y1="280" x2="560" y2="280" stroke="currentColor"/>
  <line x1="60" y1="20" x2="60" y2="280" stroke="currentColor"/>
  <text x="555" y="300" font-size="12" text-anchor="end">q</text>
  <text x="55" y="20" font-size="12" text-anchor="end">$/unit</text>
  <line x1="60" y1="100" x2="540" y2="240" stroke="#26a" stroke-width="2"/>
  <text x="545" y="240" font-size="11" fill="#26a">MPB</text>
  <line x1="60" y1="160" x2="540" y2="280" stroke="#a26" stroke-width="2"/>
  <text x="545" y="280" font-size="11" fill="#a26">MSB = MPB minus ext</text>
  <line x1="60" y1="260" x2="540" y2="80" stroke="#444" stroke-width="2"/>
  <text x="545" y="80" font-size="11" fill="#444">MC</text>
  <circle cx="395" cy="175" r="5" fill="#26a"/>
  <text x="405" y="170" font-size="11" fill="#26a">q^P</text>
  <circle cx="305" cy="200" r="5" fill="#a26"/>
  <text x="290" y="195" font-size="11" fill="#a26" text-anchor="end">q*</text>
  <polygon points="305,200 395,175 395,200" fill="#a26" fill-opacity="0.2"/>
  <text x="370" y="215" font-size="10" fill="#a26">DWL</text>
  <text x="300" y="40" font-size="13" font-weight="bold" text-anchor="middle">Negative externality: q^P above q*</text>
</svg>
<p class="caption" style="font-size:0.85em;color:var(--muted,#666);margin-top:0.4em">With a negative externality, MSB lies below MPB. Private equilibrium $q^P$ sits where MPB meets MC; social optimum $q^*$ sits where MSB meets MC. The shaded triangle is the deadweight loss.</p>
""",
        "examples": r"""
<ol>
<li><strong>Carbon emissions.</strong> Burning a tonne of coal benefits the firm by saving fuel costs but inflicts climate damages on the world. MSB is below MPB; the Pigouvian tax (UK CPS, EU ETS price) corrects the wedge.</li>
<li><strong>Vaccination.</strong> Private benefit is own protection; positive externality is herd immunity. MSB exceeds MPB, so private uptake under-supplies the optimum; subsidies and mandates close the gap.</li>
<li><strong>Essay move: state the Baumol-Oates result.</strong> The optimal Pigouvian tax equals the marginal external damage at the social optimum, not at laissez-faire. Many candidates write the tax incorrectly as $-E'(q^P)$ and lose marks.</li>
<li><strong>Essay move: graph the welfare triangle precisely.</strong> Draw MPB, MSB, MC, mark $q^P$ and $q^*$, and shade the triangle between them. The triangle is the DWL; cite this explicitly.</li>
<li><strong>Essay move: distinguish marginal from inframarginal externality.</strong> Pigouvian taxation cares about MSB, not total social benefit. A textbook trap is to confuse total damage with marginal damage (link to [[Concepts/Externality Internalisation]]).</li>
<li>Limitation: the framework assumes the planner knows $E'(q)$, which is rarely true for diffuse externalities (greenhouse gases). Information-constrained policy is the topic of Weitzman (1974).</li>
</ol>
""",
    },

    "cournot-duopoly": {
        "math": r"""
<p><strong>Cournot duopoly</strong> is the canonical model of quantity competition: $n$ firms simultaneously choose outputs $q_i$, and a market-clearing price $p(Q)$ depends on aggregate output $Q = \sum_i q_i$. Firms are sophisticated quantity-setters, but each treats rivals' outputs as fixed when optimising. The model dates from Cournot (1838) and remains the workhorse of industrial organisation (Tirole, <em>Theory of Industrial Organisation</em>, ch. 5; Belleflamme-Peitz, ch. 3).</p>

<p>Take linear inverse demand $p = a - bQ$ and constant marginal cost $c$ (with $a > c$). Firm $i$ chooses $q_i$ to maximise:</p>
<p>$$\pi_i = (a - b(q_i + q_{-i}) - c) q_i.$$</p>
<p>The first-order condition $\partial \pi_i / \partial q_i = 0$ gives the best response:</p>
<p>$$q_i^{BR}(q_{-i}) = \frac{a - c}{2b} - \frac{q_{-i}}{2}.$$</p>
<p>Imposing symmetry $q_i = q^*$ in the $n$-firm case yields the central result:</p>
<p>$$q_i^* = \frac{a - c}{(n+1)b}, \qquad Q^* = \frac{n(a-c)}{(n+1)b}, \qquad p^* = \frac{a + nc}{n+1}.$$</p>

<ol>
<li><strong>Markup.</strong> The Lerner index $(p^* - c)/p^* = 1/(n \varepsilon)$, where $\varepsilon$ is the demand elasticity. Markups fall with $n$.</li>
<li><strong>Monopoly and competition as limits.</strong> $n = 1$ recovers monopoly output $(a-c)/(2b)$; $n \to \infty$ gives $p^* \to c$ and the competitive outcome.</li>
<li><strong>Strategic substitutes.</strong> The best response slopes downward, so $\partial q_i / \partial q_j < 0$: rivals' outputs and own output are substitutes (Bulow, Geanakoplos, Klemperer, 1985).</li>
<li><strong>Welfare.</strong> Deadweight loss is positive but shrinks at rate $1/(n+1)^2$, faster than Cournot output rises, so consumer surplus is increasing and concave in $n$.</li>
</ol>

<p>Cournot equilibrium coincides with the rational-expectations outcome of a Walrasian auctioneer when firms condition on the residual demand they each face (Kreps and Scheinkman, 1983, show capacity-constrained Bertrand yields Cournot). Micro2025 Lecture 12 (IO Foundations) develops the comparative statics. Motta, <em>Competition Policy</em>, ch. 8, uses Cournot to motivate concentration-based merger screens.</p>
""",
        "widget": r"""
<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" id="widget-cournot-duopoly" style="background:#fafafa;border:1px solid #ddd">
  <defs>
    <marker id="arr-cournot" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
      <path d="M0,0 L8,4 L0,8 z" fill="#333"/>
    </marker>
  </defs>
  <line x1="60" y1="280" x2="560" y2="280" stroke="#333" stroke-width="1.5" marker-end="url(#arr-cournot)"/>
  <line x1="60" y1="280" x2="60" y2="30" stroke="#333" stroke-width="1.5" marker-end="url(#arr-cournot)"/>
  <text x="565" y="295" font-size="13" font-family="serif">q2</text>
  <text x="40" y="30" font-size="13" font-family="serif">q1</text>
  <line x1="60" y1="60" x2="460" y2="280" stroke="#1f77b4" stroke-width="2"/>
  <text x="465" y="285" font-size="12" fill="#1f77b4">BR1(q2)</text>
  <line x1="160" y1="280" x2="380" y2="40" stroke="#d62728" stroke-width="2"/>
  <text x="385" y="40" font-size="12" fill="#d62728">BR2(q1)</text>
  <circle cx="240" cy="180" r="5" fill="#000"/>
  <text x="250" y="175" font-size="12">Cournot NE</text>
  <line x1="240" y1="180" x2="240" y2="280" stroke="#999" stroke-dasharray="3,3"/>
  <line x1="60" y1="180" x2="240" y2="180" stroke="#999" stroke-dasharray="3,3"/>
  <text x="232" y="298" font-size="11">q2*</text>
  <text x="42" y="184" font-size="11">q1*</text>
  <text x="180" y="220" font-size="11" fill="#666">slope -1/2</text>
</svg>
<p class="caption" style="font-size:0.85em;color:#555;margin-top:6px">Cournot best-response functions intersect at the symmetric Nash equilibrium $q_1^* = q_2^* = (a-c)/(3b)$. Strategic substitutes give downward-sloping reaction curves.</p>
""",
        "examples": r"""
<ul>
<li><strong>OPEC output coordination.</strong> Crude oil supply is often modelled as a Cournot oligopoly with Saudi Arabia as a residual-demand setter. Quota wars in 2014 and 2020 are interpreted as movements along, not equilibria of, the Cournot reaction curves.</li>
<li><strong>UK mobile networks.</strong> Pre-merger analysis of O2 / Three (CMA 2016) used Cournot calibration to forecast retail price effects, with $n$ falling from four to three predicting roughly a 10 percent ARPU rise.</li>
<li><strong>Compare to Bertrand.</strong> Cournot gives positive markups even with two firms, whereas Bertrand collapses to $p = MC$. Kate Doornik essays expect candidates to motivate the choice between Cournot and Bertrand by reference to capacity constraints (Kreps and Scheinkman, 1983).</li>
<li><strong>Limit of competition.</strong> The result $p \to c$ as $n \to \infty$ underpins the Cournot-Walras convergence theorem and gives a non-trivial micro-foundation for perfect competition.</li>
<li><strong>Evaluation move.</strong> The model treats output as the strategic variable, yet most retail firms actually post prices. Argue why quantity commitment fits commodity sectors with capacity lead times (cement, oil refining) but fares poorly for service industries.</li>
<li><strong>Limitation.</strong> Symmetric-cost Cournot is a special case; with cost asymmetry the lower-cost firm captures a larger share and aggregate welfare rises, complicating the simple HHI link to consumer surplus.</li>
<li>Linked: [[Concepts/Bertrand Duopoly]] and [[Concepts/Stackelberg Leadership]].</li>
</ul>
""",
    },
    "bertrand-duopoly": {
        "math": r"""
<p><strong>Bertrand duopoly</strong> describes price competition between two firms selling a homogeneous good with constant and identical marginal cost $c$. Firms move simultaneously, posting prices $p_1, p_2$. Each consumer buys from whichever firm posts the lower price; ties split demand. The model was formulated by Bertrand (1883) as a critique of Cournot, and is treated in Tirole ch. 5 and Belleflamme-Peitz ch. 3.</p>

<p>Each firm's demand schedule is discontinuous:</p>
<p>$$D_i(p_i, p_j) = \begin{cases} D(p_i) & \text{if } p_i < p_j, \\ \tfrac{1}{2} D(p_i) & \text{if } p_i = p_j, \\ 0 & \text{if } p_i > p_j. \end{cases}$$</p>
<p>Profit $\pi_i = (p_i - c) D_i(p_i, p_j)$ inherits this jump.</p>

<ol>
<li><strong>No pure-strategy equilibrium with $p > c$.</strong> If both post $p > c$, either firm gains by cutting infinitesimally to capture the whole market. Iterated undercutting drives prices toward $c$.</li>
<li><strong>No equilibrium with $p_i < c$.</strong> A firm posting below cost makes losses; deviating to $c$ raises profit to zero.</li>
<li><strong>Equilibrium.</strong> The unique pure-strategy Nash equilibrium has $p_1^* = p_2^* = c$, generating zero profits, total output $D(c)$, and the competitive welfare level.</li>
</ol>

<p>This is the <strong>Bertrand paradox</strong>: with only two firms, the market delivers the competitive outcome. The conclusion is fragile and several routes escape it:</p>
<ol>
<li><strong>Differentiation.</strong> With imperfect substitutes, residual demand is continuous in own price and a positive-markup equilibrium exists (see Differentiated Bertrand).</li>
<li><strong>Capacity constraints.</strong> Edgeworth (1925) showed that capacity-limited Bertrand has no pure-strategy equilibrium; Kreps and Scheinkman (1983) demonstrated that a two-stage capacity-then-price game reproduces Cournot outcomes.</li>
<li><strong>Repeated interaction.</strong> Infinite repetition allows tacit collusion above $c$ for sufficiently patient firms (see Collusion Sustainability).</li>
<li><strong>Asymmetric costs.</strong> If $c_1 < c_2$, the low-cost firm prices just below $c_2$ and earns positive limit profits.</li>
</ol>

<p>Micro2025 Lecture 12 contrasts Bertrand and Cournot to motivate why merger authorities care about the strategic variable. Motta ch. 8 uses Bertrand to argue that the conduct parameter, not just concentration, drives policy.</p>
""",
        "widget": r"""
<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" id="widget-bertrand-duopoly" style="background:#fafafa;border:1px solid #ddd">
  <line x1="60" y1="280" x2="560" y2="280" stroke="#333"/>
  <line x1="60" y1="280" x2="60" y2="30" stroke="#333"/>
  <text x="565" y="295" font-size="13">p_j</text>
  <text x="40" y="30" font-size="13">pi_i</text>
  <line x1="60" y1="220" x2="160" y2="220" stroke="#1f77b4" stroke-width="2"/>
  <text x="100" y="210" font-size="11">p_i &gt; p_j: zero</text>
  <line x1="160" y1="220" x2="160" y2="120" stroke="#1f77b4" stroke-width="2" stroke-dasharray="4,3"/>
  <line x1="160" y1="120" x2="350" y2="60" stroke="#1f77b4" stroke-width="2"/>
  <text x="270" y="100" font-size="11" fill="#1f77b4">p_i &lt; p_j: full demand</text>
  <circle cx="160" cy="170" r="4" fill="#d62728"/>
  <text x="170" y="165" font-size="11" fill="#d62728">tie: half demand</text>
  <line x1="160" y1="280" x2="160" y2="40" stroke="#999" stroke-dasharray="2,2"/>
  <text x="148" y="298" font-size="11">p_j</text>
  <text x="380" y="50" font-size="12" fill="#666">Firm i best response: undercut</text>
  <text x="380" y="68" font-size="12" fill="#666">until p = c.</text>
</svg>
<p class="caption" style="font-size:0.85em;color:#555;margin-top:6px">Profit jump at $p_i = p_j$ drives the undercutting logic; the unique Nash equilibrium is $p_1 = p_2 = c$.</p>
""",
        "examples": r"""
<ul>
<li><strong>Online retail commodities.</strong> Amazon Marketplace listings of identical SKUs (memory cards, generic OTC drugs) approximate Bertrand: shoppers sort by price and the lowest seller captures the buy box, compressing margins toward fulfilment cost.</li>
<li><strong>Wholesale electricity auctions.</strong> Uniform-price pool markets are Bertrand-like in the merit order. Marginal generators set prices close to short-run MC, except when capacity binds (echoing Kreps and Scheinkman).</li>
<li><strong>Resolve the paradox.</strong> A high-mark essay names two or three escape routes (differentiation, capacity, repetition) and links each to an empirical setting. Kate Doornik rewards essays that frame Bertrand as a benchmark, not a prediction.</li>
<li><strong>Compare with Cournot.</strong> Strategic complements vs substitutes generates opposite comparative statics for merger effects (Deneckere and Davidson, 1985): Bertrand mergers raise rivals' prices, Cournot mergers reduce rivals' outputs.</li>
<li><strong>Evaluation move.</strong> Argue that the paradox is a feature, not a bug: it disciplines policy debate by isolating which assumption (homogeneity, no capacity, one-shot) drives high prices.</li>
<li><strong>Limitation.</strong> Mixed-strategy equilibria with capacity constraints have no closed form and are hard to test empirically.</li>
<li>Linked: [[Concepts/Differentiated Bertrand]] and [[Concepts/Collusion Sustainability]].</li>
</ul>
""",
    },
    "differentiated-bertrand": {
        "math": r"""
<p><strong>Differentiated Bertrand</strong> embeds product differentiation in the price-setting game so demand is a smooth function of all prices. The canonical linear specification (Shubik, 1980; Tirole ch. 5) is:</p>
<p>$$q_i = a - b p_i + d p_j, \qquad b > d > 0,$$</p>
<p>with constant marginal cost $c$. The cross-price coefficient $d$ indexes the degree of substitutability: $d \to 0$ gives independent monopolies, $d \to b$ approaches homogeneous Bertrand.</p>

<p>Firm $i$ chooses $p_i$ to maximise:</p>
<p>$$\pi_i = (p_i - c)(a - b p_i + d p_j).$$</p>
<p>FOC gives the best response:</p>
<p>$$p_i^{BR}(p_j) = \frac{a + b c + d p_j}{2b}.$$</p>
<p>Symmetric NE solves $p^* = (a + bc + d p^*) / (2b)$, yielding:</p>
<p>$$p^* = \frac{a + bc}{2b - d}, \qquad p^* - c = \frac{a - (b - d) c}{2b - d}.$$</p>

<ol>
<li><strong>Strategic complements.</strong> $\partial p_i^{BR} / \partial p_j = d / (2b) > 0$: best responses slope upward, opposite to Cournot.</li>
<li><strong>Comparative statics.</strong> Markup falls in $d$ (closer substitutes erode market power) and rises in $a$ (larger market).</li>
<li><strong>Merger effects.</strong> A merger of $i$ and $j$ internalises the cross-price externality and raises both prices (upward pricing pressure). This is the foundation of the UPP test in modern merger analysis (Farrell and Shapiro, 2010).</li>
<li><strong>Welfare.</strong> Consumer surplus is decreasing in markups; with $n$ symmetric firms, total surplus rises in entry but falls in differentiation if the latter is wasteful.</li>
</ol>

<p>Foundations for the linear system come from representative-consumer quadratic utility:</p>
<p>$$U(q_1, q_2) = \alpha(q_1 + q_2) - \tfrac{1}{2}(\beta(q_1^2 + q_2^2) + 2 \gamma q_1 q_2),$$</p>
<p>with $\gamma$ controlling differentiation. Logit demand systems (BLP, 1995) generalise to many products and dominate empirical IO (Belleflamme-Peitz ch. 5). Micro2025 Lecture 12 uses differentiated Bertrand to motivate diversion ratios; Motta ch. 8 ties UPP to Article 102 abuse cases.</p>
""",
        "widget": r"""
<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" id="widget-differentiated-bertrand" style="background:#fafafa;border:1px solid #ddd">
  <line x1="60" y1="280" x2="560" y2="280" stroke="#333"/>
  <line x1="60" y1="280" x2="60" y2="30" stroke="#333"/>
  <text x="565" y="295" font-size="13">p2</text>
  <text x="40" y="30" font-size="13">p1</text>
  <line x1="100" y1="240" x2="500" y2="80" stroke="#1f77b4" stroke-width="2"/>
  <text x="505" y="80" font-size="12" fill="#1f77b4">BR1(p2)</text>
  <line x1="80" y1="200" x2="480" y2="60" stroke="#d62728" stroke-width="2"/>
  <text x="485" y="60" font-size="12" fill="#d62728">BR2(p1)</text>
  <circle cx="320" cy="150" r="5" fill="#000"/>
  <text x="330" y="145" font-size="12">NE (p*, p*)</text>
  <line x1="320" y1="150" x2="320" y2="280" stroke="#999" stroke-dasharray="3,3"/>
  <line x1="60" y1="150" x2="320" y2="150" stroke="#999" stroke-dasharray="3,3"/>
  <text x="315" y="298" font-size="11">p2*</text>
  <text x="42" y="154" font-size="11">p1*</text>
  <text x="140" y="100" font-size="11" fill="#666">upward slopes:</text>
  <text x="140" y="116" font-size="11" fill="#666">strategic complements</text>
</svg>
<p class="caption" style="font-size:0.85em;color:#555;margin-top:6px">With differentiated products, best responses slope upward. The symmetric Nash equilibrium has $p^* = (a + bc)/(2b - d)$, with markup falling as substitution $d$ rises.</p>
""",
        "examples": r"""
<ul>
<li><strong>Ready-to-eat cereal.</strong> Nevo (2001) estimates a logit demand system for Kellogg, General Mills, Post and Quaker; markups average 35 to 45 percent of price, consistent with differentiated Bertrand rather than the homogeneous benchmark.</li>
<li><strong>UK supermarkets.</strong> CMA merger reviews of Asda / Sainsbury's (2019) used diversion ratios drawn from a differentiated Bertrand framework to compute the upward pricing pressure on overlapping product lines.</li>
<li><strong>UPP as policy.</strong> Explain that $\text{UPP} \approx D_{ij} (p_j - c_j)$ is a model-free first-order approximation to merger price effects (Farrell and Shapiro). Kate Doornik rewards essays that link the BLP demand estimates to UPP screens.</li>
<li><strong>Compare to Hotelling.</strong> Linear-quadratic differentiation and spatial differentiation deliver similar comparative statics, but Hotelling adds the endogenous location choice (max differentiation principle).</li>
<li><strong>Evaluation move.</strong> Argue that the linear demand assumption is restrictive: with logit demand, markups also depend on outside good share, which the linear model omits.</li>
<li><strong>Limitation.</strong> Treats differentiation as exogenous; in reality firms invest in branding and R&D to widen $d$, so policy should also consider dynamic incentives.</li>
<li>Linked: [[Concepts/Hotelling Linear City]] and [[Concepts/Merger Analysis]].</li>
</ul>
""",
    },
    "stackelberg-leadership": {
        "math": r"""
<p><strong>Stackelberg leadership</strong> (von Stackelberg, 1934) is the sequential analogue of Cournot. The leader (firm 1) chooses quantity $q_1$ first; the follower (firm 2) observes $q_1$ and best responds with $q_2$. Solve by backward induction (Tirole ch. 8; Belleflamme-Peitz ch. 4).</p>

<p>With linear demand $p = a - b(q_1 + q_2)$ and marginal cost $c$, the follower's problem is:</p>
<p>$$\max_{q_2} (a - b(q_1 + q_2) - c) q_2 \implies q_2^{BR}(q_1) = \frac{a - c - b q_1}{2b}.$$</p>
<p>The leader anticipates this and chooses $q_1$ to maximise:</p>
<p>$$\pi_1(q_1) = (a - b(q_1 + q_2^{BR}(q_1)) - c) q_1 = \left( \tfrac{1}{2}(a - c) - \tfrac{1}{2} b q_1 \right) q_1.$$</p>
<p>FOC gives:</p>
<p>$$q_1^* = \frac{a - c}{2b}, \qquad q_2^* = \frac{a - c}{4b}, \qquad Q^* = \frac{3(a-c)}{4b}, \qquad p^* = \frac{a + 3c}{4}.$$</p>

<ol>
<li><strong>First-mover advantage.</strong> Leader output equals monopoly output and exceeds the Cournot level $(a-c)/(3b)$. Leader profit $(a-c)^2 / (8b)$ exceeds Cournot $(a-c)^2 / (9b)$; follower profit $(a-c)^2 / (16b)$ falls below.</li>
<li><strong>Total output rises.</strong> $3(a-c)/(4b) > 2(a-c)/(3b)$, so consumer surplus is higher under Stackelberg than Cournot.</li>
<li><strong>Commitment matters.</strong> The advantage requires that the leader's quantity be observable and irreversible. Without commitment, the game collapses to simultaneous Cournot.</li>
<li><strong>Credibility.</strong> Capacity investments, long-term supply contracts and irreversible plant expansion serve as commitment devices (Dixit, 1980).</li>
</ol>

<p>The model generalises to $n$ followers and to differentiated-Bertrand leadership, where the leader posts a high price (strategic complements reverse the direction of advantage: in Bertrand-with-leadership the leader earns less than the follower, an example of second-mover advantage; Gal-Or, 1985). Micro2025 Lecture 12 introduces Stackelberg as a benchmark for entry deterrence; Tirole ch. 8 stresses the role of commitment.</p>
""",
        "widget": r"""
<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" id="widget-stackelberg-leadership" style="background:#fafafa;border:1px solid #ddd">
  <line x1="60" y1="280" x2="560" y2="280" stroke="#333"/>
  <line x1="60" y1="280" x2="60" y2="30" stroke="#333"/>
  <text x="565" y="295" font-size="13">q2</text>
  <text x="40" y="30" font-size="13">q1</text>
  <line x1="60" y1="60" x2="460" y2="280" stroke="#1f77b4" stroke-width="2"/>
  <text x="465" y="285" font-size="11" fill="#1f77b4">leader iso-profit</text>
  <line x1="160" y1="280" x2="380" y2="40" stroke="#d62728" stroke-width="2"/>
  <text x="385" y="40" font-size="12" fill="#d62728">BR2(q1)</text>
  <circle cx="240" cy="180" r="5" fill="#666"/>
  <text x="250" y="175" font-size="11" fill="#666">Cournot</text>
  <circle cx="320" cy="140" r="5" fill="#000"/>
  <text x="330" y="135" font-size="12">Stackelberg</text>
  <path d="M 200 240 Q 280 200 360 180" stroke="#999" fill="none" stroke-dasharray="3,3"/>
  <text x="220" y="60" font-size="11" fill="#444">Leader picks tangent point</text>
  <text x="220" y="78" font-size="11" fill="#444">on follower's reaction curve</text>
</svg>
<p class="caption" style="font-size:0.85em;color:#555;margin-top:6px">Leader chooses the point on the follower's reaction curve that is tangent to its own iso-profit locus, giving higher output and profit than the simultaneous Cournot equilibrium.</p>
""",
        "examples": r"""
<ul>
<li><strong>Saudi Aramco in OPEC+.</strong> Saudi Arabia's announced production quotas function as a Stackelberg leader signal; the swing-producer role lets it move first while other members follow on residual demand.</li>
<li><strong>Boeing 747 launch.</strong> The early irreversible commitment to the wide-body airframe deterred McDonnell Douglas DC-10 capacity expansion. Useful applied example of commitment-as-leadership.</li>
<li><strong>Commitment evaluation.</strong> Argue that the advantage requires observable, irreversible quantity. Kate Doornik essays expect candidates to distinguish bluffing from commitment using Dixit's sunk-cost logic.</li>
<li><strong>Reversal under Bertrand.</strong> Note that Stackelberg leadership yields second-mover advantage with strategic complements (Gal-Or, 1985); identify the example as showing why the sign of the externality matters more than the order of moves.</li>
<li><strong>Evaluation move.</strong> Endogenise the leadership role: who becomes leader? Hamilton and Slutsky (1990) show endogenous timing can produce Stackelberg or Cournot depending on cost asymmetry.</li>
<li><strong>Limitation.</strong> The model assumes perfect observability; if the follower mistrusts the leader's announcement, multiple-equilibrium issues arise.</li>
<li>Linked: [[Concepts/Cournot Duopoly]] and [[Concepts/Entry Deterrence]].</li>
</ul>
""",
    },
    "entry-deterrence": {
        "math": r"""
<p><strong>Entry deterrence</strong> covers strategies by which an incumbent shapes pre-entry conditions so a potential entrant chooses to stay out. The canonical Dixit (1980) model embeds Stackelberg-like commitment in a two-stage game (Tirole ch. 8; Belleflamme-Peitz ch. 16).</p>

<p>Stage 1: incumbent (firm 1) installs capacity $k_1$ at unit cost $r$. Stage 2: entrant decides whether to enter (sunk cost $F$); both firms then compete in quantities. Capacity binds production up to $k_1$, but extra units cost $r + w$ where $w$ is variable cost.</p>

<p>Incumbent payoffs depend on whether the entrant enters:</p>
<p>$$\pi_1^{\text{out}} = M(k_1) - r k_1, \qquad \pi_1^{\text{in}}(k_1) = D(k_1) - r k_1.$$</p>
<p>The entrant enters iff post-entry duopoly profit exceeds $F$. The incumbent picks $k_1$ to make entry unprofitable while keeping $\pi_1^{\text{out}}$ high.</p>

<ol>
<li><strong>Excess capacity as commitment.</strong> Installed capacity is sunk, so the incumbent's marginal cost of producing up to $k_1$ falls. The Cournot reaction function shifts outward, lowering the entrant's residual demand.</li>
<li><strong>Three regimes (Dixit, 1980).</strong> Blockaded entry: incumbent's monopoly optimum already deters. Deterred entry: incumbent expands beyond monopoly $k_1$ to push entrant out. Accommodated entry: deterrence costlier than sharing.</li>
<li><strong>Credibility.</strong> The capacity must be observable and sunk before the entry decision. Pure threats (I will flood the market) are not subgame-perfect (Chain Store Paradox; Selten, 1978).</li>
<li><strong>Chain Store resolutions.</strong> Kreps and Wilson (1982) and Milgrom and Roberts (1982) restore deterrence with two-sided incomplete information: a tough incumbent type fights, and the entrant cannot tell types apart, so even a weak incumbent fights to build reputation.</li>
</ol>

<p>Other deterrence channels include advertising as a sunk cost, brand proliferation (Schmalensee, 1978), long-term contracts with buyers (Aghion-Bolton, 1987), and predatory pricing financed by a deep pocket. Motta ch. 7 evaluates how Article 102 abuse cases (e.g., Intel rebates, Google Shopping) frame these as exclusionary conduct. Micro2025 Lecture 12 covers Dixit and the reputation resolution of the Chain Store Paradox.</p>
""",
        "widget": r"""
<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" id="widget-entry-deterrence" style="background:#fafafa;border:1px solid #ddd">
  <text x="40" y="40" font-size="13" fill="#333">Stage 1: Incumbent picks capacity k1</text>
  <text x="40" y="60" font-size="13" fill="#333">Stage 2: Entrant decides; then duopoly</text>
  <circle cx="80" cy="160" r="14" fill="#fff" stroke="#1f77b4" stroke-width="2"/>
  <text x="74" y="165" font-size="13" fill="#1f77b4">I</text>
  <line x1="94" y1="155" x2="200" y2="120" stroke="#333"/>
  <text x="100" y="125" font-size="11">low k1</text>
  <line x1="94" y1="165" x2="200" y2="200" stroke="#333"/>
  <text x="100" y="200" font-size="11">high k1</text>
  <circle cx="220" cy="120" r="14" fill="#fff" stroke="#d62728" stroke-width="2"/>
  <text x="214" y="125" font-size="13" fill="#d62728">E</text>
  <line x1="234" y1="115" x2="340" y2="80" stroke="#333"/>
  <text x="240" y="85" font-size="11">enter</text>
  <line x1="234" y1="125" x2="340" y2="155" stroke="#333"/>
  <text x="240" y="160" font-size="11">stay out</text>
  <circle cx="220" cy="200" r="14" fill="#fff" stroke="#d62728" stroke-width="2"/>
  <text x="214" y="205" font-size="13" fill="#d62728">E</text>
  <line x1="234" y1="195" x2="340" y2="180" stroke="#333"/>
  <text x="240" y="180" font-size="11">enter</text>
  <line x1="234" y1="205" x2="340" y2="240" stroke="#333"/>
  <text x="240" y="245" font-size="11">stay out</text>
  <text x="360" y="85" font-size="11" fill="#666">Duopoly, low capacity</text>
  <text x="360" y="155" font-size="11" fill="#666">Monopoly, low capacity</text>
  <text x="360" y="180" font-size="11" fill="#666">Duopoly, fight</text>
  <rect x="350" y="225" width="200" height="30" fill="#ffe066" stroke="#cc9900"/>
  <text x="360" y="245" font-size="11" fill="#664400">Deterred entry (Dixit outcome)</text>
</svg>
<p class="caption" style="font-size:0.85em;color:#555;margin-top:6px">Two-stage game tree: incumbent commits capacity, then entrant decides. Deterrence is subgame perfect only if the commitment is observable and irreversible.</p>
""",
        "examples": r"""
<ul>
<li><strong>Intel x86 fabs.</strong> Pre-investment in leading-edge process nodes deters AMD and rival x86 manufacturers; the sunk capital plays the role of $k_1$ in Dixit's model.</li>
<li><strong>UK supermarket land banks.</strong> Tesco and Sainsbury's holding undeveloped sites was investigated by the CMA (2008) as a land-banking strategy that deters entry by limiting outlet space.</li>
<li><strong>Reputation as commitment.</strong> Kate Doornik essays reward candidates who explicitly invoke Kreps-Wilson incomplete-information reputation to escape the Chain Store Paradox.</li>
<li><strong>Compare to predation.</strong> Distinguish capacity-based deterrence (lawful unless coupled with abuse) from predatory pricing (illegal under Article 102; see AKZO 1991 with the AVC / ATC test).</li>
<li><strong>Evaluation move.</strong> Argue that deterrence reduces consumer welfare in the short run via higher prices but may raise welfare if it disciplines duplicative entry with fixed cost $F$ (Mankiw and Whinston, 1986, excess entry).</li>
<li><strong>Limitation.</strong> Empirically distinguishing strategic deterrence from efficient scale economies is hard, leaving courts to rely on intent evidence (memos, internal documents).</li>
<li>Linked: [[Concepts/Stackelberg Leadership]] and [[Concepts/UK Competition Act 1998]].</li>
</ul>
""",
    },
    "merger-analysis": {
        "math": r"""
<p><strong>Merger analysis</strong> evaluates the welfare effects of combining two competing firms. The standard framework compares pre-merger and post-merger equilibria, weighing changes in concentration, price, and efficiency. Motta ch. 5 and Belleflamme-Peitz ch. 15 set out the toolkit; Micro2025 Lecture 12 develops the IO theory.</p>

<p>Take symmetric Cournot with $n$ firms, linear demand $p = a - bQ$ and marginal cost $c$. Pre-merger equilibrium gives:</p>
<p>$$q_i = \frac{a - c}{(n+1)b}, \qquad p = \frac{a + nc}{n+1}, \qquad \pi_i = \frac{(a-c)^2}{(n+1)^2 b}.$$</p>

<p>If two firms merge with no cost synergy, the new market has $n - 1$ firms. The merged entity's profit falls below the sum of two pre-merger profits (Salant, Switzer, Reynolds, 1983; merger paradox). The merger is unprofitable unless cost synergies or strategic-complements competition apply.</p>

<ol>
<li><strong>HHI screen.</strong> Pre-merger HHI rises by $2 s_i s_j$ when firms $i, j$ merge with shares $s_i, s_j$. EU and UK thresholds: post-merger HHI > 2000 and $\Delta \text{HHI}$ > 150 triggers a phase 2 review.</li>
<li><strong>Upward pricing pressure (UPP).</strong> Farrell and Shapiro (2010) define $\text{UPP}_i = D_{ij}(p_j - c_j) - e_i$, where $D_{ij}$ is the diversion ratio and $e_i$ is the efficiency offset. Positive UPP signals that the merger raises price absent efficiencies.</li>
<li><strong>Williamson trade-off.</strong> A merger that cuts marginal cost from $c$ to $c'$ and raises price from $p_0$ to $p_1$ improves welfare iff:</li>
</ol>
<p>$$(c - c') \cdot q_1 > \tfrac{1}{2} (p_1 - p_0)(q_0 - q_1).$$</p>
<ol start="4">
<li><strong>Coordinated effects.</strong> A merger may also raise the scope for tacit collusion by reducing the number of firms; the post-merger discount factor threshold $(n-2)/(n-1)$ is easier to meet than $(n-1)/n$.</li>
<li><strong>Failing firm defence.</strong> If the target would exit absent merger, the counterfactual is exit not status quo, weakening the anti-merger case.</li>
</ol>

<p>Modern practice combines structural simulation (BLP-style demand estimation) with reduced-form UPP screens. Motta ch. 5 surveys EU Merger Regulation 139/2004 case law (Volvo / Scania 2000; T-Mobile / Tele2 NL 2018).</p>
""",
        "widget": r"""
<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" id="widget-merger-analysis" style="background:#fafafa;border:1px solid #ddd">
  <line x1="60" y1="280" x2="560" y2="280" stroke="#333"/>
  <line x1="60" y1="280" x2="60" y2="30" stroke="#333"/>
  <text x="565" y="295" font-size="13">Q</text>
  <text x="40" y="30" font-size="13">p</text>
  <line x1="60" y1="60" x2="500" y2="280" stroke="#333" stroke-width="1.5"/>
  <text x="505" y="285" font-size="11">Demand</text>
  <line x1="60" y1="200" x2="500" y2="200" stroke="#1f77b4" stroke-width="1.5"/>
  <text x="510" y="204" font-size="11" fill="#1f77b4">MC pre</text>
  <line x1="60" y1="230" x2="500" y2="230" stroke="#2ca02c" stroke-width="1.5"/>
  <text x="510" y="234" font-size="11" fill="#2ca02c">MC post</text>
  <line x1="280" y1="280" x2="280" y2="160" stroke="#666" stroke-dasharray="3,3"/>
  <text x="270" y="298" font-size="11">Q0</text>
  <text x="42" y="164" font-size="11">p0</text>
  <line x1="60" y1="160" x2="280" y2="160" stroke="#666" stroke-dasharray="3,3"/>
  <line x1="220" y1="280" x2="220" y2="130" stroke="#d62728" stroke-dasharray="3,3"/>
  <text x="210" y="298" font-size="11" fill="#d62728">Q1</text>
  <line x1="60" y1="130" x2="220" y2="130" stroke="#d62728" stroke-dasharray="3,3"/>
  <text x="42" y="134" font-size="11" fill="#d62728">p1</text>
  <polygon points="220,160 280,160 220,130" fill="#ff9999" opacity="0.6"/>
  <text x="290" y="150" font-size="11" fill="#a00">DWL</text>
  <polygon points="60,200 60,230 220,230 220,200" fill="#99ff99" opacity="0.6"/>
  <text x="120" y="222" font-size="11" fill="#0a0">Cost saving</text>
</svg>
<p class="caption" style="font-size:0.85em;color:#555;margin-top:6px">Williamson diagram: green rectangle (cost saving on infra-marginal output) versus pink triangle (deadweight loss). A merger improves welfare iff the rectangle exceeds the triangle.</p>
""",
        "examples": r"""
<ul>
<li><strong>O2 / Three UK (CMA 2016).</strong> The CMA blocked the merger on coordinated and unilateral effects grounds; UPP analysis projected price rises of 10 to 20 percent, with claimed efficiencies deemed insufficient.</li>
<li><strong>Sainsbury's / Asda (CMA 2019).</strong> Diversion-ratio evidence showed close substitution in groceries; the CMA found substantial lessening of competition in 463 local areas plus online.</li>
<li><strong>UPP framing.</strong> A high-mark essay states the diversion ratio formula and links the UPP test back to the differentiated Bertrand model. Kate Doornik rewards explicit links between theory and the consumer-welfare standard.</li>
<li><strong>Efficiency defence.</strong> Note that EU Merger Guidelines require efficiencies to be merger-specific, verifiable, and passed on to consumers; pure cost savings to producers do not qualify under a consumer-surplus standard.</li>
<li><strong>Evaluation move.</strong> Compare consumer-surplus standard (EU, UK) with total-welfare standard (Canada, older Williamson approach). Argue which is theoretically coherent given political-economy concerns about producer rents.</li>
<li><strong>Limitation.</strong> Structural merger simulation rests on demand-system assumptions; misspecification of nests or outside good can swing predicted price effects by 50 percent or more.</li>
<li>Linked: [[Concepts/Williamson Trade-off]] and [[Concepts/HHI Index]].</li>
</ul>
""",
    },
    "williamson-trade-off": {
        "math": r"""
<p>The <strong>Williamson trade-off</strong> (Williamson, 1968) is the foundational welfare condition for merger review under a total-surplus standard. A horizontal merger that raises market power but lowers marginal cost creates two opposing effects: a deadweight-loss triangle from reduced output and a cost-saving rectangle on inframarginal units. Tirole ch. 1 and Motta ch. 5 treat this as the benchmark cost-benefit calculation.</p>

<p>Let pre-merger price be $p_0$ with marginal cost $c$ and output $q_0$. Post-merger price rises to $p_1$, marginal cost falls to $c'$ where $c' < c$, and output falls to $q_1 < q_0$. The change in total surplus is:</p>
<p>$$\Delta W = (c - c') q_1 - \tfrac{1}{2}(p_1 - p_0)(q_0 - q_1).$$</p>

<p>A merger improves welfare iff $\Delta W > 0$, i.e.:</p>
<p>$$\frac{c - c'}{p_1 - p_0} > \frac{q_0 - q_1}{2 q_1}.$$</p>

<ol>
<li><strong>Asymmetric magnitudes.</strong> A small reduction in marginal cost on a large inframarginal output can outweigh a substantial deadweight-loss triangle. Williamson computed that 5 percent cost savings can offset a 20 percent price rise for typical elasticities.</li>
<li><strong>Elasticity matters.</strong> For demand elasticity $\varepsilon$, the change in output is approximately $\Delta q / q_1 \approx \varepsilon \Delta p / p_1$, so a more elastic demand magnifies the DWL triangle.</li>
<li><strong>Consumer-surplus standard reverses sign.</strong> Under a CS standard, any price rise is welfare-reducing regardless of cost savings unless cost savings pass through to lower prices. EU and UK merger control adopt CS, not total surplus, so Williamson's logic is necessary but not sufficient for clearance.</li>
<li><strong>Pass-through.</strong> If a fraction $\rho$ of cost savings is passed through, post-merger price is $p_1 = p_0 - \rho (c - c') + \Delta p^{\text{power}}$. Merger clears CS test iff pass-through exceeds the market-power induced markup increase.</li>
</ol>

<p>The trade-off generalises to multi-product mergers via consumer surplus integrals over the demand system. Modern practice replaces the back-of-envelope rectangle / triangle with structural simulation (Berry, Levinsohn, Pakes, 1995). Motta ch. 5 stresses the limits of Williamson under CS, while Belleflamme-Peitz ch. 15 derives the pass-through condition. Micro2025 Lecture 12 uses this trade-off as the policy-economics anchor.</p>
""",
        "widget": r"""
<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" id="widget-williamson-trade-off" style="background:#fafafa;border:1px solid #ddd">
  <line x1="60" y1="280" x2="560" y2="280" stroke="#333"/>
  <line x1="60" y1="280" x2="60" y2="30" stroke="#333"/>
  <text x="565" y="295" font-size="13">Q</text>
  <text x="40" y="30" font-size="13">p</text>
  <line x1="60" y1="50" x2="480" y2="280" stroke="#333" stroke-width="1.5"/>
  <text x="485" y="285" font-size="11">D</text>
  <line x1="60" y1="210" x2="480" y2="210" stroke="#1f77b4"/>
  <text x="490" y="214" font-size="11" fill="#1f77b4">c pre</text>
  <line x1="60" y1="245" x2="480" y2="245" stroke="#2ca02c"/>
  <text x="490" y="249" font-size="11" fill="#2ca02c">c' post</text>
  <line x1="320" y1="280" x2="320" y2="160" stroke="#999" stroke-dasharray="3,3"/>
  <line x1="60" y1="160" x2="320" y2="160" stroke="#999" stroke-dasharray="3,3"/>
  <text x="312" y="298" font-size="11">q0</text>
  <text x="42" y="164" font-size="11">p0</text>
  <line x1="240" y1="280" x2="240" y2="125" stroke="#d62728" stroke-dasharray="3,3"/>
  <line x1="60" y1="125" x2="240" y2="125" stroke="#d62728" stroke-dasharray="3,3"/>
  <text x="232" y="298" font-size="11" fill="#d62728">q1</text>
  <text x="42" y="129" font-size="11" fill="#d62728">p1</text>
  <polygon points="240,160 320,160 240,125" fill="#ff9999" opacity="0.7"/>
  <text x="265" y="148" font-size="11" fill="#a00">DWL</text>
  <polygon points="60,210 60,245 240,245 240,210" fill="#99ff99" opacity="0.7"/>
  <text x="120" y="232" font-size="11" fill="#0a0">(c-c')*q1</text>
</svg>
<p class="caption" style="font-size:0.85em;color:#555;margin-top:6px">Green rectangle of cost savings on $q_1$ versus pink triangle of deadweight loss. Total-surplus welfare rises iff the rectangle exceeds the triangle.</p>
""",
        "examples": r"""
<ul>
<li><strong>Boeing / McDonnell Douglas 1997.</strong> EU and US clearances appealed to cost synergies in defence and large aircraft production; Williamson-style efficiencies were balanced against a more concentrated airframe market.</li>
<li><strong>Heinz / Beech-Nut 2001 (US blocked).</strong> Court of Appeals rejected the efficiency defence: efficiencies were not merger-specific (could be achieved without merger) and not verifiable, violating Williamson's threshold.</li>
<li><strong>CS vs TS framing.</strong> A strong essay distinguishes Williamson (total surplus) from the EU consumer-surplus standard, then derives the pass-through requirement that makes the CS test stricter. Kate Doornik rewards this comparative move.</li>
<li><strong>Calibration.</strong> For linear demand and 30 percent pass-through, a 10 percent cost saving offsets only a 3 percent unilateral price effect, so efficiency claims usually fail the CS test.</li>
<li><strong>Evaluation move.</strong> Argue that political economy favours CS because producer rents redistribute to shareholders, not workers, in the modern economy: Williamson's TS assumption that a dollar to producers equals a dollar to consumers is normatively contested.</li>
<li><strong>Limitation.</strong> The rectangle / triangle calculus assumes linear demand and constant marginal cost; with non-linear demand the threshold shifts and quantitative claims need full simulation.</li>
<li>Linked: [[Concepts/Merger Analysis]] and [[Concepts/HHI Index]].</li>
</ul>
""",
    },
    "collusion-sustainability": {
        "math": r"""
<p><strong>Collusion sustainability</strong> asks when firms can sustain prices above the static Nash equilibrium through repeated interaction and credible punishments. The infinitely repeated game framework (Friedman, 1971; Abreu, 1986) gives the canonical analysis (Tirole ch. 6; Belleflamme-Peitz ch. 14; Motta ch. 4).</p>

<p>Take $n$ symmetric firms playing Cournot (or Bertrand) every period. The stage-game Nash gives per-firm profit $\pi^N$; the collusive outcome (joint-monopoly) gives $\pi^M / n$ per firm; the one-shot deviation profit is $\pi^D$. Firms discount future profits at rate $\delta \in (0, 1)$.</p>

<p>Under grim-trigger strategies (cooperate while everyone has cooperated; revert to Nash forever after any defection), collusion is incentive compatible iff:</p>
<p>$$\frac{\pi^M / n}{1 - \delta} \geq \pi^D + \frac{\delta \pi^N}{1 - \delta}.$$</p>
<p>Rearranging:</p>
<p>$$\delta \geq \delta^* = \frac{\pi^D - \pi^M / n}{\pi^D - \pi^N}.$$</p>

<p>For Cournot with linear demand and symmetric firms, computation gives:</p>
<p>$$\delta^* = \frac{(n+1)^2}{(n+1)^2 + 4n} \xrightarrow{n \to \infty} 1.$$</p>
<p>For Bertrand with homogeneous goods, the formula simplifies to:</p>
<p>$$\delta^* = \frac{n - 1}{n}.$$</p>

<ol>
<li><strong>Fewer firms ease collusion.</strong> $\delta^*$ rises in $n$: as the cartel grows, the deviation gain (capturing the whole market for one period) outweighs the proportionally smaller share of $\pi^M$.</li>
<li><strong>Stick-and-carrot punishments.</strong> Abreu (1986) shows that optimal punishment paths (a one-shot below-Nash phase before reverting) can sustain collusion for lower $\delta$ than grim trigger.</li>
<li><strong>Facilitating practices.</strong> Multimarket contact (Bernheim-Whinston, 1990), price transparency, frequent interactions, and symmetric costs all reduce $\delta^*$.</li>
<li><strong>Demand cycles.</strong> Rotemberg-Saloner (1986) shows price wars occur in booms (deviation gain high), countercyclical to naive predictions.</li>
</ol>

<p>Implications for merger and conduct policy: anything that lowers $\delta^*$ raises coordinated-effects concerns. Motta ch. 4 surveys the empirical literature; Micro2025 Lecture 13 (Collusion) sets out the model in detail.</p>
""",
        "widget": r"""
<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" id="widget-collusion-sustainability" style="background:#fafafa;border:1px solid #ddd">
  <line x1="60" y1="280" x2="560" y2="280" stroke="#333"/>
  <line x1="60" y1="280" x2="60" y2="30" stroke="#333"/>
  <text x="565" y="295" font-size="13">n</text>
  <text x="40" y="30" font-size="13">delta*</text>
  <text x="32" y="244" font-size="10">0</text>
  <text x="32" y="184" font-size="10">0.5</text>
  <line x1="60" y1="180" x2="63" y2="180" stroke="#333"/>
  <text x="32" y="124" font-size="10">0.8</text>
  <line x1="60" y1="120" x2="63" y2="120" stroke="#333"/>
  <text x="32" y="64" font-size="10">1.0</text>
  <line x1="60" y1="60" x2="63" y2="60" stroke="#333"/>
  <line x1="60" y1="60" x2="560" y2="60" stroke="#999" stroke-dasharray="2,2"/>
  <path d="M 100 240 Q 180 160 280 110 T 540 70" stroke="#1f77b4" stroke-width="2" fill="none"/>
  <text x="350" y="100" font-size="12" fill="#1f77b4">Bertrand: delta* = (n-1)/n</text>
  <path d="M 100 220 Q 200 165 320 130 T 540 90" stroke="#d62728" stroke-width="2" stroke-dasharray="4,3" fill="none"/>
  <text x="350" y="160" font-size="12" fill="#d62728">Cournot: delta* rises in n</text>
  <text x="120" y="270" font-size="11">2</text>
  <text x="220" y="270" font-size="11">4</text>
  <text x="340" y="270" font-size="11">8</text>
  <text x="460" y="270" font-size="11">16</text>
  <text x="100" y="40" font-size="11" fill="#666">Higher n raises delta*:</text>
  <text x="100" y="56" font-size="11" fill="#666">collusion harder.</text>
</svg>
<p class="caption" style="font-size:0.85em;color:#555;margin-top:6px">Critical discount factor $\delta^*$ rises with the number of firms; collusion is incentive compatible only when $\delta$ lies above this curve.</p>
""",
        "examples": r"""
<ul>
<li><strong>Lysine cartel 1992 to 1995.</strong> Five global producers (Ajinomoto, ADM, Kyowa, Cheil, Sewon) sustained price-fixing across continents. Multimarket contact and frequent meetings lowered the effective $\delta^*$.</li>
<li><strong>UK construction bid-rigging 2009.</strong> CMA fined 103 firms a total of GBP 129 million; market transparency in tender procedures made deviations easy to detect, supporting collusion despite many participants.</li>
<li><strong>Bertrand formula.</strong> A high-mark answer derives $\delta^* = (n-1)/n$ from first principles, then uses it to predict that markets with two firms collude more easily than markets with ten. Kate Doornik rewards explicit comparative statics.</li>
<li><strong>Compare Cournot and Bertrand.</strong> Cournot deviation gains are smaller than Bertrand (deviator only captures market via undercutting the residual), so $\delta^*$ is lower for Cournot. This shows why authorities worry more about price-setting than quantity-setting markets.</li>
<li><strong>Evaluation move.</strong> Argue that the model treats $\delta$ as fixed, but interest rates and demand volatility shift effective patience. Booms (Rotemberg-Saloner) and recessions (Haltiwanger-Harrington) make $\delta^*$ time-varying.</li>
<li><strong>Limitation.</strong> Folk theorem multiplicity: any price between $c$ and $p^M$ is sustainable for some $\delta$, so the model cannot pin down the cartel price uniquely.</li>
<li>Linked: [[Concepts/Leniency Programme]] and [[Concepts/HHI Index]].</li>
</ul>
""",
    },
    "hhi-index": {
        "math": r"""
<p>The <strong>Herfindahl-Hirschman Index (HHI)</strong> is a concentration measure equal to the sum of squared market shares. For $n$ firms with shares $s_i \in [0, 100]$ in percent (so $\sum s_i = 100$):</p>
<p>$$\text{HHI} = \sum_{i=1}^n s_i^2.$$</p>
<p>HHI ranges from near 0 (atomistic competition) to $100^2 = 10{,}000$ (monopoly). Antitrust authorities use HHI as a first-stage merger screen (Motta ch. 5; US DOJ / FTC Horizontal Merger Guidelines, 2010).</p>

<ol>
<li><strong>Equivalent number of firms.</strong> $1 / \text{HHI}^*$ in fractions; an HHI of 2500 corresponds to four equal-sized firms (each with share 25 percent, $4 \times 25^2 = 2500$).</li>
<li><strong>Merger change.</strong> If firms $i$ and $j$ merge, $\Delta \text{HHI} = (s_i + s_j)^2 - s_i^2 - s_j^2 = 2 s_i s_j$. Two firms each with 20 percent share contribute $\Delta \text{HHI} = 800$.</li>
<li><strong>EU and UK thresholds.</strong> Post-merger HHI between 1000 and 2000 with $\Delta \text{HHI} < 250$ is unlikely to raise concerns; HHI > 2000 with $\Delta \text{HHI} > 150$ triggers a phase 2 review.</li>
<li><strong>Link to Cournot markup.</strong> Under symmetric Cournot, $\text{HHI} = 10{,}000 / n$ and the Lerner index aggregates as $L = \text{HHI} / (10{,}000 \, \varepsilon)$. Concentration thus maps directly to market power under that conduct.</li>
</ol>

<p>HHI is a structural proxy, not a conduct measure. Two issues qualify its use:</p>
<ol>
<li><strong>Market definition.</strong> HHI is conditional on the candidate market; defining the market too narrowly inflates concentration, too broadly understates it. Hence the SSNIP test precedes HHI computation.</li>
<li><strong>Conduct sensitivity.</strong> The same HHI implies different prices under Cournot, Bertrand, or collusion. HHI is a screen, not a sufficient statistic.</li>
</ol>

<p>Critiques (Schmalensee, 1989; Bresnahan, 1989) note that structure-conduct-performance correlations are weak once market definition and entry barriers are controlled for. Modern practice (Berry, Gaynor, Scott Morton, 2019) prefers direct evidence on diversion and pricing, with HHI retained as a coarse screen. Micro2025 Lecture 12 introduces HHI alongside the Cournot decomposition; Motta ch. 5 surveys the case law.</p>
""",
        "widget": r"""
<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" id="widget-hhi-index" style="background:#fafafa;border:1px solid #ddd">
  <text x="60" y="40" font-size="14" font-weight="bold">HHI by market structure</text>
  <rect x="60" y="60" width="100" height="40" fill="#1f77b4"/>
  <text x="170" y="85" font-size="12">Monopoly: HHI = 10000</text>
  <rect x="60" y="110" width="80" height="40" fill="#1f77b4"/>
  <rect x="140" y="110" width="20" height="40" fill="#aec7e8"/>
  <text x="170" y="135" font-size="12">Dominant plus fringe: 6500</text>
  <rect x="60" y="160" width="40" height="40" fill="#1f77b4"/>
  <rect x="100" y="160" width="40" height="40" fill="#aec7e8"/>
  <rect x="140" y="160" width="20" height="40" fill="#c7e9c0"/>
  <text x="170" y="185" font-size="12">Tight oligopoly: 3300</text>
  <rect x="60" y="210" width="25" height="40" fill="#1f77b4"/>
  <rect x="85" y="210" width="25" height="40" fill="#aec7e8"/>
  <rect x="110" y="210" width="25" height="40" fill="#c7e9c0"/>
  <rect x="135" y="210" width="25" height="40" fill="#fdd49e"/>
  <text x="170" y="235" font-size="12">Symmetric 4 firms: 2500</text>
  <rect x="60" y="260" width="10" height="40" fill="#1f77b4"/>
  <rect x="70" y="260" width="10" height="40" fill="#aec7e8"/>
  <rect x="80" y="260" width="10" height="40" fill="#c7e9c0"/>
  <rect x="90" y="260" width="10" height="40" fill="#fdd49e"/>
  <rect x="100" y="260" width="10" height="40" fill="#cab2d6"/>
  <rect x="110" y="260" width="10" height="40" fill="#fb9a99"/>
  <rect x="120" y="260" width="10" height="40" fill="#fdbf6f"/>
  <rect x="130" y="260" width="10" height="40" fill="#b15928"/>
  <rect x="140" y="260" width="10" height="40" fill="#33a02c"/>
  <rect x="150" y="260" width="10" height="40" fill="#6a3d9a"/>
  <text x="170" y="285" font-size="12">Symmetric 10 firms: 1000</text>
  <line x1="400" y1="60" x2="400" y2="300" stroke="#333" stroke-width="1"/>
  <line x1="395" y1="100" x2="405" y2="100" stroke="#d62728" stroke-width="2"/>
  <text x="410" y="105" font-size="11" fill="#d62728">2500 phase-2 threshold</text>
  <line x1="395" y1="160" x2="405" y2="160" stroke="#fdc26b" stroke-width="2"/>
  <text x="410" y="165" font-size="11" fill="#cc8400">1500 mid-concentration</text>
  <line x1="395" y1="220" x2="405" y2="220" stroke="#2ca02c" stroke-width="2"/>
  <text x="410" y="225" font-size="11" fill="#0a0">1000 unconcentrated</text>
</svg>
<p class="caption" style="font-size:0.85em;color:#555;margin-top:6px">HHI scale and policy thresholds: HHI > 2500 with $\Delta$ > 200 triggers phase 2 review in the US; EU and UK use HHI > 2000 and $\Delta$ > 150.</p>
""",
        "examples": r"""
<ul>
<li><strong>UK retail banking.</strong> The CMA 2016 Retail Banking Investigation reported personal-current-account HHI around 1700 in England, just below the 2000 phase-2 threshold; the remedies focused on conduct (Open Banking) rather than divestiture.</li>
<li><strong>US airline mergers.</strong> The Delta / Northwest 2008 merger raised route-level HHI by 1500 on overlapping city pairs, triggering DOJ scrutiny and divestiture remedies at LaGuardia and Washington National.</li>
<li><strong>Concentration vs conduct.</strong> A high-mark essay states the SCP critique (Schmalensee, Bresnahan): HHI is a structural proxy, but conduct determines outcomes. Kate Doornik rewards candidates who explicitly distinguish structure, conduct, and performance.</li>
<li><strong>Calibration formula.</strong> Show that $\Delta \text{HHI} = 2 s_i s_j$ for an $i, j$ merger; this gives an immediate quantitative anchor for whether a merger crosses the threshold.</li>
<li><strong>Evaluation move.</strong> Argue that HHI is most informative under Cournot conduct (where $L = \text{HHI}/\varepsilon$) and least informative under Bertrand or auction conduct; policy should match the index to the conduct assumption.</li>
<li><strong>Limitation.</strong> HHI is sensitive to market-definition choices; in pharmaceuticals or geographic-locked markets, a 5 percent shift in defined boundaries can move HHI by 1000.</li>
<li>Linked: [[Concepts/SSNIP Test]] and [[Concepts/Merger Analysis]].</li>
</ul>
""",
    },
    "ssnip-test": {
        "math": r"""
<p>The <strong>SSNIP test</strong> (Small but Significant Non-transitory Increase in Price), known as the hypothetical-monopolist test, defines the relevant antitrust market. A candidate set of products is a market iff a hypothetical monopolist over that set could profitably impose a small (typically 5 to 10 percent) non-transitory price increase. The test was formalised in the US 1982 Merger Guidelines and adopted in EU Commission Notice 97/C 372/03 (Motta ch. 3; Belleflamme-Peitz ch. 14).</p>

<p>Formally, consider a candidate market $A$ containing products with current price $p_0$ and quantity $q_0$. A monopolist's profit from a price rise to $p_1 = (1 + x) p_0$ (for $x = 0.05$ to $0.10$) is:</p>
<p>$$\Delta \pi = (p_1 - c) q_1 - (p_0 - c) q_0.$$</p>

<p>Approximating with constant marginal cost $c$ and constant elasticity $\varepsilon$, $q_1 / q_0 \approx (1 + x)^{-\varepsilon}$, giving:</p>
<p>$$\Delta \pi > 0 \iff \varepsilon < \frac{(1 + x) - (p_0 - c)/p_0}{x}.$$</p>

<p>If $\Delta \pi > 0$, the candidate market is the relevant market (substitution out is too weak to discipline monopoly). If $\Delta \pi < 0$, expand the market to include the next-closest substitute and retest.</p>

<ol>
<li><strong>Critical loss analysis.</strong> The actual loss $\Delta q / q$ from a 5 percent price rise must exceed the critical loss $x / (x + L)$, where $L = (p - c)/p$ is the Lerner index. Higher margins shrink the critical loss, making narrow markets easier to define.</li>
<li><strong>Iterative procedure.</strong> Start with a single product, test, then expand by adding the closest substitute until SSNIP becomes unprofitable; the last set for which it is profitable is the relevant market.</li>
<li><strong>Cellophane fallacy.</strong> Applying SSNIP at the prevailing price overstates substitution if the firm is already at the monopoly price (where the constraint binds). For Article 102 dominance assessment, base on competitive prices not actual ones (DuPont, 1956).</li>
<li><strong>Geographic SSNIP.</strong> Analogous test for the geographic dimension: would a hypothetical monopolist in region $R$ find a 5 percent price rise profitable, accounting for cross-region shipping?</li>
</ol>

<p>Modern practice supplements SSNIP with diversion ratios from demand estimation (BLP) and natural experiments (Hausman tests on price correlations). Motta ch. 3 critiques the cellophane trap; Micro2025 Lecture 12 ties SSNIP to HHI computation. EU notice 97/C 372/03 codifies the procedure.</p>
""",
        "widget": r"""
<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" id="widget-ssnip-test" style="background:#fafafa;border:1px solid #ddd">
  <defs>
    <marker id="arrow-ssnip" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
      <path d="M0,0 L8,4 L0,8 z" fill="#333"/>
    </marker>
  </defs>
  <text x="60" y="35" font-size="13" font-weight="bold">SSNIP iterative procedure</text>
  <rect x="60" y="60" width="160" height="60" fill="#fff" stroke="#1f77b4" stroke-width="2" rx="8"/>
  <text x="80" y="85" font-size="12">Candidate market A</text>
  <text x="80" y="105" font-size="12">{product 1}</text>
  <path d="M 220 90 L 280 90" stroke="#333" marker-end="url(#arrow-ssnip)"/>
  <rect x="290" y="60" width="160" height="60" fill="#fff" stroke="#d62728" stroke-width="2" rx="8"/>
  <text x="310" y="85" font-size="12">5% SSNIP</text>
  <text x="310" y="105" font-size="12">profitable?</text>
  <path d="M 450 90 L 510 90" stroke="#333" marker-end="url(#arrow-ssnip)"/>
  <text x="465" y="80" font-size="11" fill="#0a0">Yes</text>
  <rect x="500" y="60" width="80" height="60" fill="#ddffdd" stroke="#0a0" rx="8"/>
  <text x="513" y="95" font-size="12" fill="#0a0">Market</text>
  <path d="M 370 120 L 370 180" stroke="#333" marker-end="url(#arrow-ssnip)"/>
  <text x="380" y="155" font-size="11" fill="#d62728">No</text>
  <rect x="290" y="180" width="160" height="60" fill="#fff" stroke="#1f77b4" stroke-width="2" rx="8"/>
  <text x="305" y="205" font-size="12">Expand to include</text>
  <text x="305" y="225" font-size="12">next substitute</text>
  <path d="M 290 210 L 220 130" stroke="#333" stroke-dasharray="4,3" marker-end="url(#arrow-ssnip)"/>
  <text x="220" y="180" font-size="11" fill="#666">retest</text>
  <text x="60" y="280" font-size="11" fill="#666">Critical loss: x / (x + L). If actual loss exceeds this, monopolist will not raise price.</text>
</svg>
<p class="caption" style="font-size:0.85em;color:#555;margin-top:6px">SSNIP iterates: start narrow, test profitability of a 5 percent price rise, expand until the rise becomes unprofitable. The last profitable set is the relevant market.</p>
""",
        "examples": r"""
<ul>
<li><strong>Coca-Cola / Schweppes 1986.</strong> The Commission applied SSNIP to find that carbonated soft drinks formed a distinct market separate from other beverages; cross-substitution to fruit juice was insufficient to discipline a 5 percent CSD price rise.</li>
<li><strong>BSkyB / Manchester United 1999.</strong> The UK Competition Commission used SSNIP-style reasoning to define pay-TV sports rights as a separate relevant market, blocking the acquisition.</li>
<li><strong>Cellophane fallacy.</strong> A high-mark essay names the DuPont 1956 case where SSNIP applied at monopoly prices wrongly cleared cellophane as part of a wider packaging market. Kate Doornik rewards explicit identification of when the test misfires.</li>
<li><strong>Critical loss formula.</strong> Show $x / (x + L)$ and apply: at $L = 0.5$ and $x = 0.05$, critical loss is 9.1 percent. If observed elasticity gives less than 9.1 percent quantity decline, narrow market is confirmed.</li>
<li><strong>Evaluation move.</strong> Argue that SSNIP is a thought experiment, not data: actual application requires demand estimation, natural experiments, or price-correlation evidence. The test is structurally sound but operationally fragile.</li>
<li><strong>Limitation.</strong> Two-sided platforms (Amazon, Visa) confound SSNIP because raising price on one side can lower demand on the other; standard SSNIP underestimates the welfare cost of platform mergers.</li>
<li>Linked: [[Concepts/HHI Index]] and [[Concepts/Merger Analysis]].</li>
</ul>
""",
    },
    "hotelling-linear-city": {
        "math": r"""
<p>The <strong>Hotelling linear city</strong> (Hotelling, 1929; d'Aspremont-Gabszewicz-Thisse, 1979) is the canonical model of horizontal differentiation. Consumers are uniformly distributed on $[0, 1]$ with density 1. Firm 1 locates at $a$ and firm 2 at $1 - b$ (so $a + b \leq 1$); each consumer $x$ chooses the firm minimising price plus transport cost $t (x - z)^2$ (quadratic transport, ensuring existence).</p>

<p>Take symmetric locations $a = 0, b = 0$ (firms at the endpoints). The marginal consumer indifferent between firms is:</p>
<p>$$x^* = \frac{1}{2} + \frac{p_2 - p_1}{2t}.$$</p>
<p>Demands are $q_1 = x^*$ and $q_2 = 1 - x^*$. With marginal cost $c$ and the FOC $\partial \pi_i / \partial p_i = 0$:</p>
<p>$$p_i^{BR}(p_j) = \frac{p_j + c + t}{2}.$$</p>
<p>Symmetric NE gives the canonical Hotelling pricing result:</p>
<p>$$p_1^* = p_2^* = c + t, \qquad \pi_i^* = \frac{t}{2}.$$</p>

<ol>
<li><strong>Markup equals transport.</strong> The equilibrium markup $t$ measures the strength of differentiation; closer substitutes (lower $t$) erode market power.</li>
<li><strong>Maximum differentiation.</strong> With locations chosen endogenously in a prior stage (and quadratic transport), the unique subgame-perfect equilibrium has firms locating at $0$ and $1$. Differentiation softens price competition, so each firm gains by moving away (d'Aspremont et al., 1979).</li>
<li><strong>Linear transport gives no equilibrium.</strong> With $t |x - z|$ (Hotelling's original assumption), the second-stage pricing game lacks a pure-strategy equilibrium for nearby locations; quadratic transport is the standard fix.</li>
<li><strong>Welfare.</strong> Consumer surplus is decreasing in $t$ (transport waste), but social welfare is maximised at locations $(1/4, 3/4)$, not $(0, 1)$. Firms over-differentiate from a planner's view.</li>
</ol>

<p>Generalisations: circular city (Salop, 1979); two-dimensional product spaces; vertical-plus-horizontal differentiation (Shaked-Sutton, 1982). Hotelling also provides the workhorse model for political competition (median voter) and brand positioning. Belleflamme-Peitz ch. 5 develops the model and welfare; Tirole ch. 7 covers the location stage; Micro2025 Lecture 12 derives the $p = c + t$ result.</p>
""",
        "widget": r"""
<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" id="widget-hotelling-linear-city" style="background:#fafafa;border:1px solid #ddd">
  <line x1="60" y1="200" x2="540" y2="200" stroke="#333" stroke-width="2"/>
  <text x="50" y="240" font-size="11">0</text>
  <text x="525" y="240" font-size="11">1</text>
  <circle cx="60" cy="200" r="10" fill="#1f77b4"/>
  <text x="42" y="180" font-size="12" fill="#1f77b4">Firm 1</text>
  <circle cx="540" cy="200" r="10" fill="#d62728"/>
  <text x="510" y="180" font-size="12" fill="#d62728">Firm 2</text>
  <line x1="300" y1="180" x2="300" y2="220" stroke="#666" stroke-width="1.5" stroke-dasharray="3,3"/>
  <text x="282" y="170" font-size="11" fill="#666">x*</text>
  <rect x="60" y="220" width="240" height="20" fill="#aec7e8" opacity="0.6"/>
  <text x="120" y="234" font-size="11">buys from Firm 1</text>
  <rect x="300" y="220" width="240" height="20" fill="#f4b8b8" opacity="0.6"/>
  <text x="370" y="234" font-size="11">buys from Firm 2</text>
  <text x="60" y="60" font-size="13" font-weight="bold">Linear city: consumer at x pays p_i + t(x - z_i)^2</text>
  <text x="60" y="85" font-size="12">Symmetric NE: p_1 = p_2 = c + t</text>
  <text x="60" y="105" font-size="12">Profit per firm: t/2</text>
  <text x="60" y="125" font-size="12">Higher t raises markup but also waste</text>
  <path d="M 60 200 Q 300 100 540 200" stroke="#2ca02c" stroke-width="1.5" fill="none" opacity="0.5"/>
  <text x="290" y="140" font-size="11" fill="#0a0">Utility from Firm 1</text>
</svg>
<p class="caption" style="font-size:0.85em;color:#555;margin-top:6px">Consumers split at the indifferent point $x^*$; symmetric Nash equilibrium with locations at the endpoints gives $p = c + t$ and per-firm profit $t / 2$.</p>
""",
        "examples": r"""
<ul>
<li><strong>UK supermarket location.</strong> Tesco and Sainsbury's location decisions exhibit empirical clustering closer to (1/4, 3/4) than (0, 1), suggesting that endogenous price competition is muted by other factors (planning regulations, demand density).</li>
<li><strong>Political competition.</strong> The median voter theorem (Hotelling, 1929) applies the same model to two-party democracy: minimum differentiation arises if no price (policy intensity) competition follows. UK Labour and Conservative on economic policy in the 1990s fit this pattern.</li>
<li><strong>Maximum differentiation derivation.</strong> A high-mark essay shows that the location stage with quadratic transport implies firms locate at the endpoints to soften price competition. Kate Doornik rewards candidates who derive both the pricing result and the location result.</li>
<li><strong>Compare to differentiated Bertrand.</strong> Hotelling endogenises the differentiation parameter through location, whereas linear-quadratic Bertrand treats it as exogenous. Argue that the former is theoretically richer but harder to estimate.</li>
<li><strong>Evaluation move.</strong> Note the welfare distortion: firms over-differentiate from a planner's view. This justifies competition policy attention to product-line proliferation as a soft entry deterrence strategy.</li>
<li><strong>Limitation.</strong> The linear-transport version (Hotelling's original) has no pure-strategy equilibrium for nearby locations; the model's tractability depends on quadratic transport, which is a knife-edge assumption.</li>
<li>Linked: [[Concepts/Differentiated Bertrand]] and [[Concepts/Entry Deterrence]].</li>
</ul>
""",
    },
    "price-discrimination": {
        "math": r"""
<p><strong>Price discrimination</strong> is charging different prices for the same good to different consumers, or different prices for different quantities to the same consumer. Pigou (1920) classified it into three degrees (Tirole ch. 3; Belleflamme-Peitz ch. 7 to 10; Motta ch. 7).</p>

<p><strong>First-degree (perfect).</strong> Charge each consumer their reservation value. With inverse demand $P(q)$ and constant marginal cost $c$, monopolist extracts the entire surplus:</p>
<p>$$\Pi^{1st} = \int_0^{q^*} (P(q) - c) dq, \qquad CS = 0,$$</p>
<p>where $q^*$ satisfies $P(q^*) = c$. Output is efficient, but all surplus accrues to the seller.</p>

<p><strong>Second-degree (self-selection).</strong> Offer a menu $(q_L, T_L), (q_H, T_H)$. With consumer types $\theta_L < \theta_H$, optimal menu satisfies the incentive constraints:</p>
<p>$$\theta_L v(q_L) - T_L \geq \theta_L v(q_H) - T_H \quad (\text{IC-L}), \qquad \theta_H v(q_H) - T_H \geq \theta_H v(q_L) - T_L \quad (\text{IC-H}).$$</p>
<p>Optimal contract distorts $q_L$ downward (no distortion at the top): $\theta_H v'(q_H) = c$ but $\theta_L v'(q_L) > c$.</p>

<p><strong>Third-degree.</strong> Charge different prices in separable submarkets $i = 1, 2$. Monopoly sets $MR_i = MC$ in each:</p>
<p>$$p_i \left(1 - \frac{1}{\varepsilon_i}\right) = c \implies \frac{p_1}{p_2} = \frac{1 - 1/\varepsilon_2}{1 - 1/\varepsilon_1}.$$</p>
<p>Higher elasticity gives a lower price.</p>

<ol>
<li><strong>Welfare effects, third-degree.</strong> Output may rise or fall (Schmalensee, 1981); CS may rise if low-elasticity markets get lower prices and the alternative is non-supply.</li>
<li><strong>Required conditions.</strong> Market power, ability to identify or sort consumer types, and prevention of arbitrage.</li>
<li><strong>Output effect (Robinson, 1933).</strong> Under linear demand, third-degree discrimination strictly reduces output relative to uniform monopoly, hence reduces welfare.</li>
<li><strong>Article 102 concern.</strong> EU treats discriminatory pricing as an abuse only if it harms competition between buyers (United Brands 1978) or excludes rivals (margin squeeze).</li>
</ol>

<p>Micro2025 Lecture 12 distinguishes the three degrees; Belleflamme-Peitz ch. 8 develops the self-selection menu with IC-IR constraints.</p>
""",
        "widget": r"""
<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" id="widget-price-discrimination" style="background:#fafafa;border:1px solid #ddd">
  <line x1="60" y1="280" x2="560" y2="280" stroke="#333"/>
  <line x1="60" y1="280" x2="60" y2="30" stroke="#333"/>
  <text x="565" y="295" font-size="13">Q</text>
  <text x="40" y="30" font-size="13">p</text>
  <line x1="60" y1="50" x2="500" y2="280" stroke="#333" stroke-width="1.5"/>
  <text x="505" y="285" font-size="11">D</text>
  <line x1="60" y1="220" x2="500" y2="220" stroke="#1f77b4"/>
  <text x="510" y="224" font-size="11" fill="#1f77b4">MC = c</text>
  <line x1="280" y1="280" x2="280" y2="100" stroke="#666" stroke-dasharray="3,3"/>
  <text x="272" y="298" font-size="11">q*</text>
  <text x="42" y="104" font-size="11">p</text>
  <line x1="60" y1="100" x2="280" y2="100" stroke="#666" stroke-dasharray="3,3"/>
  <polygon points="60,220 60,50 280,220" fill="#99ff99" opacity="0.5"/>
  <text x="120" y="180" font-size="11" fill="#0a0">1st degree:</text>
  <text x="120" y="195" font-size="11" fill="#0a0">all area to firm</text>
  <text x="320" y="60" font-size="12" font-weight="bold">Three degrees</text>
  <text x="320" y="85" font-size="11">1st: extract CS triangle</text>
  <text x="320" y="105" font-size="11">2nd: menu via self-selection</text>
  <text x="320" y="125" font-size="11">3rd: split market by elasticity</text>
  <text x="320" y="155" font-size="11" font-style="italic">p1/p2 = (1 - 1/eps2)/(1 - 1/eps1)</text>
</svg>
<p class="caption" style="font-size:0.85em;color:#555;margin-top:6px">Under first-degree discrimination, the monopolist extracts the entire consumer-surplus triangle; output equals the competitive level but distribution is fully on the producer side.</p>
""",
        "examples": r"""
<ul>
<li><strong>Airline yield management.</strong> Booking-class restrictions (Saturday-night stays, advance purchase) implement second-degree discrimination by self-selection: business travellers buy flexible tickets, leisure travellers accept restrictions for low fares.</li>
<li><strong>Pharmaceutical international pricing.</strong> Pfizer charges different prices for the same drug across countries based on income and health-system buying power. Parallel-trade rules under Article 34 TFEU constrain arbitrage.</li>
<li><strong>Welfare ambiguity.</strong> Kate Doornik rewards candidates who distinguish first-degree (Pareto-efficient but distributionally extreme) from third-degree (output and welfare effects ambiguous; Robinson's linear case gives strictly lower output).</li>
<li><strong>Menu design example.</strong> Set up the two-type screening problem with IC and IR constraints, derive no distortion at the top, downward distortion at the bottom (Mussa-Rosen, 1978; Tirole ch. 3).</li>
<li><strong>Evaluation move.</strong> Argue that price discrimination raises output in markets that would otherwise not be served (e.g., generic drugs in low-income countries), so blanket prohibition under Article 102 would be welfare-reducing.</li>
<li><strong>Limitation.</strong> Behavioural evidence (Gabaix-Laibson, 2006) shows that hidden two-part tariffs and bundling exploit consumer inattention, making simple welfare analysis miss the consumer-protection dimension.</li>
<li>Linked: [[Concepts/Two-Part Tariff]] and [[Concepts/UK Competition Act 1998]].</li>
</ul>
""",
    },
    "two-part-tariff": {
        "math": r"""
<p>A <strong>two-part tariff</strong> charges a fixed fee $A$ plus a per-unit price $p$: total payment $T(q) = A + pq$ for quantity $q$. Tirole ch. 3 and Belleflamme-Peitz ch. 8 treat this as the simplest non-linear pricing scheme; it raises producer surplus above linear pricing while allowing the social planner result $p = MC$.</p>

<p><strong>Single-consumer case.</strong> Inverse demand $P(q)$, marginal cost $c$. Set $p = c$ (efficient quantity $q^*$ with $P(q^*) = c$), then choose $A$ to extract consumer surplus:</p>
<p>$$A^* = CS(c) = \int_0^{q^*} (P(q) - c) dq.$$</p>
<p>Profit $\Pi = A^* = $ entire social surplus. Output is socially efficient; welfare is maximised.</p>

<p><strong>Multiple consumers, identical preferences.</strong> Same logic: $p = c$, $A = CS$ per consumer. With heterogeneous consumers, however, the fixed fee cannot exceed the lowest CS, or low-types exit the market.</p>

<p><strong>Two-type heterogeneity.</strong> Types $\theta_L$ (proportion $\lambda$) and $\theta_H$. Trade-off between:</p>
<ol>
<li>$A = CS_L(p)$: low type pays full surplus, high type stays in; profit per consumer is $A + (p - c) q_H$, weighted by population fractions.</li>
<li>$A = CS_H(p)$: only high types stay in (low types excluded); larger $A$ but smaller customer base.</li>
</ol>

<p>Optimal pricing trades off these:</p>
<p>$$\Pi = \lambda [A + (p - c) q_L] + (1 - \lambda)[A + (p - c) q_H].$$</p>
<p>The optimal per-unit price exceeds $c$ if the population is heterogeneous and the high-type fraction is large; the FOC equates marginal revenue of $p$ across types.</p>

<ol>
<li><strong>Efficiency vs surplus extraction.</strong> Homogeneous demand: two-part tariff is first-best (Coase, 1946). Heterogeneous demand: optimal $p > c$ generates distortion but increases surplus extraction.</li>
<li><strong>Comparison to menu.</strong> A menu of two-part tariffs $(A_1, p_1), (A_2, p_2)$ can implement second-degree discrimination and dominates a single two-part tariff with heterogeneous types.</li>
<li><strong>Application to natural monopoly.</strong> Coase showed that a two-part tariff allows the regulator to support efficient marginal-cost pricing and recover fixed costs via the fee, sidestepping average-cost regulation.</li>
<li><strong>Behavioural friction.</strong> Della Vigna-Malmendier (2006) show gym members systematically overpay through fixed fees they fail to utilise.</li>
</ol>

<p>Micro2025 Lecture 12 derives the homogeneous case; Tirole ch. 3 covers heterogeneity. Motta ch. 7 connects two-part tariffs to loyalty rebates under Article 102 (Intel 2009).</p>
""",
        "widget": r"""
<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" id="widget-two-part-tariff" style="background:#fafafa;border:1px solid #ddd">
  <line x1="60" y1="280" x2="560" y2="280" stroke="#333"/>
  <line x1="60" y1="280" x2="60" y2="30" stroke="#333"/>
  <text x="565" y="295" font-size="13">Q</text>
  <text x="40" y="30" font-size="13">p</text>
  <line x1="60" y1="50" x2="500" y2="280" stroke="#333" stroke-width="1.5"/>
  <text x="505" y="285" font-size="11">D</text>
  <line x1="60" y1="220" x2="500" y2="220" stroke="#1f77b4"/>
  <text x="510" y="224" font-size="11" fill="#1f77b4">MC = c</text>
  <line x1="370" y1="280" x2="370" y2="50" stroke="#666" stroke-dasharray="3,3"/>
  <text x="362" y="298" font-size="11">q*</text>
  <polygon points="60,220 60,50 370,220" fill="#99ff99" opacity="0.55"/>
  <text x="120" y="160" font-size="12" fill="#0a0">CS triangle</text>
  <text x="120" y="178" font-size="12" fill="#0a0">= fixed fee A</text>
  <text x="320" y="60" font-size="13" font-weight="bold">Two-part tariff</text>
  <text x="320" y="85" font-size="12">T(q) = A + pq</text>
  <text x="320" y="105" font-size="12">Set p = c for efficiency</text>
  <text x="320" y="125" font-size="12">Set A = CS to extract surplus</text>
  <text x="320" y="155" font-size="12">Pi = entire welfare triangle</text>
  <text x="320" y="200" font-size="11" font-style="italic" fill="#666">With heterogeneous types,</text>
  <text x="320" y="215" font-size="11" font-style="italic" fill="#666">optimal p &gt; c to extract more from H.</text>
</svg>
<p class="caption" style="font-size:0.85em;color:#555;margin-top:6px">Homogeneous case: set $p = c$ for efficient output and capture the consumer-surplus triangle as the fixed fee $A$, delivering first-best welfare with all surplus to the producer.</p>
""",
        "examples": r"""
<ul>
<li><strong>UK gym memberships.</strong> Joining fee plus monthly charge replicates the two-part tariff. Della Vigna-Malmendier (2006) document overuse of the fixed component by members who project optimistic gym attendance.</li>
<li><strong>Theme parks.</strong> Disney World admission (fixed) plus food / merchandise (per-unit) is a textbook two-part tariff; the price-equal-to-MC logic explains low marginal pricing inside the park.</li>
<li><strong>Coase on natural monopoly.</strong> Kate Doornik rewards candidates who explicitly invoke Coase (1946) to argue that two-part tariffs allow regulated utilities to charge marginal-cost prices while recovering fixed costs, avoiding average-cost distortion.</li>
<li><strong>Heterogeneity result.</strong> Show the optimal $p > c$ trade-off with two types; tie it to the menu of two-part tariffs as second-degree discrimination.</li>
<li><strong>Evaluation move.</strong> Argue that behavioural deviations (overestimation of usage) cause systematic welfare loss for naive consumers; this complicates the standard welfare assessment and motivates consumer-protection regulation.</li>
<li><strong>Limitation.</strong> Two-part tariffs require commitment and non-resale; otherwise arbitrage between consumers undoes the discrimination.</li>
<li>Linked: [[Concepts/Price Discrimination]] and [[Concepts/UK Competition Act 1998]].</li>
</ul>
""",
    },
    "leniency-programme": {
        "math": r"""
<p>A <strong>leniency programme</strong> grants partial or full immunity from antitrust fines to the first cartel member to confess and cooperate with investigators. The aim is to destabilise cartels by raising the probability that one member defects ex post and by lowering the expected payoff from joining ex ante (Motta ch. 4; Belleflamme-Peitz ch. 14).</p>

<p>Stylised model. A cartel of $n$ firms each earns collusive profit $\pi^M / n$ per period. Detection occurs each period with probability $\alpha$ absent leniency, leading to fine $F$. With leniency, an applicant pays fine $\rho F$ where $\rho \in [0, 1]$; the first applicant in a queue pays $\rho_1 = 0$, the second $\rho_2 > 0$, and so on.</p>

<p>The continuation value of cartel membership compared to defection now depends not only on the stage-game deviation profit but also on the probability that another firm applies first. Letting $\sigma$ be the equilibrium probability that any firm applies in a given period, expected cartel payoff is:</p>
<p>$$V = \frac{\pi^M / n - \sigma F (1 - \rho_2) / (n - 1)}{1 - \delta(1 - \sigma n)}.$$</p>

<ol>
<li><strong>Race-to-the-court effect.</strong> Each firm's belief that another might apply raises its own incentive to apply. The threshold discount factor for collusion rises (Motchenkova, 2004; Spagnolo, 2004).</li>
<li><strong>Optimal leniency design.</strong> Full immunity to the first applicant (US Amnesty Plus and EU 2006 Notice) is theoretically optimal: $\rho_1 = 0$ maximises destabilisation. Successive applicants pay $\rho_k > 0$ to maintain incentives in the queue.</li>
<li><strong>Reward vs reduction.</strong> Some authors (Spagnolo, 2005) argue that positive bounties (payments beyond zero fines) would further destabilise cartels but raise concerns about false reporting.</li>
<li><strong>Critical condition.</strong> Leniency destabilises iff expected gain from applying (zero fine plus discounted competitive profit) exceeds expected cartel value. With $\alpha$ small but positive, the threat of being denounced raises $\delta^*$.</li>
</ol>

<p><strong>Empirical evidence.</strong> EU 1996 Notice (revised 2002 and 2006) generated a sharp rise in cartel discoveries: from 1995 to 2010, over 80 percent of EU cartel decisions involved leniency applicants. US DOJ Amnesty Program (revised 1993) tripled cartel detections.</p>

<p>Limits: leniency may also stabilise cartels by helping insiders monitor compliance (Harrington, 2008), but the net effect remains positive in empirical work. Micro2025 Lecture 13 covers the prisoner's-dilemma logic and policy design; Motta ch. 4 surveys cases.</p>
""",
        "widget": r"""
<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" id="widget-leniency-programme" style="background:#fafafa;border:1px solid #ddd">
  <text x="60" y="40" font-size="14" font-weight="bold">Leniency: prisoner's-dilemma payoff matrix</text>
  <line x1="240" y1="60" x2="240" y2="280" stroke="#333"/>
  <line x1="120" y1="120" x2="540" y2="120" stroke="#333"/>
  <text x="280" y="85" font-size="12">Firm 2 stays silent</text>
  <text x="420" y="85" font-size="12">Firm 2 confesses</text>
  <text x="140" y="155" font-size="12">Firm 1 silent</text>
  <text x="140" y="225" font-size="12">Firm 1 confesses</text>
  <rect x="240" y="120" width="150" height="80" fill="#99ff99" opacity="0.3" stroke="#333"/>
  <text x="265" y="155" font-size="12" fill="#0a0">(piM/2, piM/2)</text>
  <text x="275" y="180" font-size="11" fill="#666">cartel survives</text>
  <rect x="390" y="120" width="150" height="80" fill="#fdb462" opacity="0.3" stroke="#333"/>
  <text x="410" y="155" font-size="12" fill="#a06000">(piN - F, piN)</text>
  <text x="415" y="180" font-size="11" fill="#666">firm 2 immune</text>
  <rect x="240" y="200" width="150" height="80" fill="#fdb462" opacity="0.3" stroke="#333"/>
  <text x="260" y="235" font-size="12" fill="#a06000">(piN, piN - F)</text>
  <text x="270" y="260" font-size="11" fill="#666">firm 1 immune</text>
  <rect x="390" y="200" width="150" height="80" fill="#fb9a99" opacity="0.3" stroke="#333"/>
  <text x="410" y="235" font-size="12" fill="#a00">(piN - F/2, piN - F/2)</text>
  <text x="425" y="260" font-size="11" fill="#666">both fined</text>
</svg>
<p class="caption" style="font-size:0.85em;color:#555;margin-top:6px">Leniency converts the cartel game into a prisoner's dilemma: silence is collectively optimal but each firm individually gains by confessing first, destabilising the cartel.</p>
""",
        "examples": r"""
<ul>
<li><strong>EU vitamin cartel 1999.</strong> Roche and BASF confessed under the 1996 EU Leniency Notice; Rhone-Poulenc received full immunity. Cartel uncovered after Hoffmann-La Roche internal review triggered application.</li>
<li><strong>UK construction bid-rigging 2009.</strong> Twenty firms applied for leniency under the 2008 OFT Notice; fines reduced for cooperators. Detection rates rose sharply post-introduction.</li>
<li><strong>Race-to-the-court framing.</strong> A high-mark essay frames leniency as transforming the cartel from a repeated coordination game into a one-shot prisoner's dilemma. Kate Doornik rewards explicit invocation of the destabilisation logic.</li>
<li><strong>Compare to fines without leniency.</strong> Show that fines alone require $\alpha F > \pi^M / n - \pi^N$ for deterrence; leniency raises the effective $\alpha$ endogenously.</li>
<li><strong>Evaluation move.</strong> Argue that leniency may also stabilise cartels by providing a credible enforcement mechanism (Harrington, 2008); the net effect is empirical, and existing evidence (Brenner, 2009) confirms net destabilisation.</li>
<li><strong>Limitation.</strong> Leniency does not address tacit collusion (no explicit agreement, hence nothing to confess), so it is ineffective in concentrated oligopolies sustained by parallel conduct.</li>
<li>Linked: [[Concepts/Collusion Sustainability]] and [[Concepts/UK Competition Act 1998]].</li>
</ul>
""",
    },
    "uk-competition-act": {
        "math": r"""
<p>The <strong>UK Competition Act 1998</strong> and <strong>EU Articles 101 and 102 TFEU</strong> form the statutory framework for competition law in the UK and EU. The 1998 Act was deliberately aligned with EU law via section 60 (now section 60A post-Brexit). Motta ch. 1 and Belleflamme-Peitz ch. 14 set out the institutional structure.</p>

<p><strong>Article 101 / Chapter I.</strong> Prohibits agreements between undertakings that restrict competition. Structure:</p>
<ol>
<li>Article 101(1): prohibition of cartels (price fixing, market sharing, output restrictions, bid rigging).</li>
<li>Article 101(2): such agreements are void.</li>
<li>Article 101(3): exemption if four cumulative conditions are met (efficiency gain, fair share to consumers, no indispensable restriction, no elimination of competition).</li>
</ol>

<p><strong>Article 102 / Chapter II.</strong> Prohibits abuse of a dominant position. Two-stage analysis:</p>
<ol>
<li>Establish dominance: market definition (SSNIP), then assessment of market power (United Brands 1978: ability to behave independently of competitors). Dominance is typically inferred from market share above 40 percent plus barriers.</li>
<li>Establish abuse: exploitative (excessive pricing, discrimination) or exclusionary (predation, rebates, refusal to deal, margin squeeze).</li>
</ol>

<p><strong>Predatory pricing test (AKZO, 1991).</strong> Prices below average variable cost are presumed predatory; prices between AVC and average total cost are predatory if part of a plan to eliminate a competitor.</p>

<p><strong>Enterprise Act 2002.</strong> Adds criminal cartel offence (up to five years imprisonment), modernises merger control (CMA substantial lessening of competition test), and creates director disqualification orders.</p>

<ol>
<li><strong>Burden of proof.</strong> Article 101(1) prohibition: Commission; Article 101(3) exemption: undertaking. Article 102: Commission throughout, with high standards under recent case law (Intel, 2017).</li>
<li><strong>Sanctions.</strong> Fines up to 10 percent of worldwide turnover (EU Regulation 1/2003); leniency reduces fines.</li>
<li><strong>Brexit divergence.</strong> Post-2021, UK Competition Act applies independently; the CMA replaces Commission jurisdiction for UK-only cases. Substantive standards remain similar but case law may diverge.</li>
<li><strong>Welfare standard.</strong> Both EU and UK adopt the consumer-welfare standard (Wouters, 2002; CMA Merger Guidelines, 2021).</li>
</ol>

<p>Motta ch. 1, 4, 7 covers institutional design; Micro2025 Lecture 13 anchors policy analysis in IO theory.</p>
""",
        "widget": r"""
<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" id="widget-uk-competition-act" style="background:#fafafa;border:1px solid #ddd">
  <text x="60" y="40" font-size="14" font-weight="bold">EU and UK competition framework</text>
  <rect x="60" y="60" width="240" height="100" fill="#aec7e8" opacity="0.5" stroke="#1f77b4" rx="6"/>
  <text x="75" y="85" font-size="13" font-weight="bold" fill="#1f77b4">Article 101 / Chapter I</text>
  <text x="75" y="105" font-size="11">Anti-competitive agreements</text>
  <text x="75" y="120" font-size="11">Cartels: price-fixing, bid-rigging</text>
  <text x="75" y="135" font-size="11">Exemption: Art 101(3) four tests</text>
  <text x="75" y="152" font-size="11">Sanction: fines up to 10% turnover</text>
  <rect x="320" y="60" width="240" height="100" fill="#fb9a99" opacity="0.5" stroke="#d62728" rx="6"/>
  <text x="335" y="85" font-size="13" font-weight="bold" fill="#d62728">Article 102 / Chapter II</text>
  <text x="335" y="105" font-size="11">Abuse of dominance</text>
  <text x="335" y="120" font-size="11">Exclusionary: predation, rebates</text>
  <text x="335" y="135" font-size="11">Exploitative: excessive pricing</text>
  <text x="335" y="152" font-size="11">AKZO test: AVC and ATC bands</text>
  <rect x="60" y="180" width="500" height="80" fill="#c7e9c0" opacity="0.5" stroke="#2ca02c" rx="6"/>
  <text x="75" y="205" font-size="13" font-weight="bold" fill="#2ca02c">Enterprise Act 2002 and EUMR 139/2004</text>
  <text x="75" y="225" font-size="11">Merger control: SLC test (UK) / SIEC test (EU)</text>
  <text x="75" y="240" font-size="11">Criminal cartel offence (UK, up to 5 years prison)</text>
  <text x="75" y="255" font-size="11">Leniency, settlement, director disqualification</text>
  <text x="60" y="290" font-size="11" fill="#666">Enforcement: Commission (DG COMP) for EU; CMA for UK; private actions in courts.</text>
</svg>
<p class="caption" style="font-size:0.85em;color:#555;margin-top:6px">Three pillars: anti-cartel rules (101 / Ch I), abuse of dominance (102 / Ch II), and merger control plus criminal sanctions (Enterprise Act 2002, EUMR 139/2004).</p>
""",
        "examples": r"""
<ul>
<li><strong>Microsoft (2004, EU).</strong> Article 102 case: Commission fined EUR 497 million for refusal to supply interoperability information and tying of Media Player. Established the framework for refusal-to-deal abuses under the Bronner test.</li>
<li><strong>UK bakery price-fixing (2010).</strong> OFT (predecessor of CMA) fined three supermarkets and two dairy processors a total of GBP 50 million for an Article 101 / Chapter I cartel on milk, butter, and cheese prices.</li>
<li><strong>AKZO test framing.</strong> Kate Doornik rewards essays that name the two-zone predatory pricing rule: below AVC presumed predatory, AVC-to-ATC predatory if intent shown. Compare with US Brooke Group recoupment requirement.</li>
<li><strong>Article 101(3) exemption.</strong> Show the four conditions (efficiency, consumer share, indispensability, no elimination) and apply to a horizontal R&D agreement (block exemption Regulation 1217/2010).</li>
<li><strong>Evaluation move.</strong> Argue that the EU consumer-welfare standard is a hybrid: it includes consumer surplus and innovation but historically also protects rivals (Form-over-effects critique, Vickers 2005). Post-Intel, the Commission moves toward more effects-based analysis.</li>
<li><strong>Limitation.</strong> Article 102 lacks an explicit efficiency defence; exclusionary practices that yield offsetting consumer benefits are difficult to defend, creating Type II error risk (false positives).</li>
<li>Linked: [[Concepts/Merger Analysis]] and [[Concepts/Leniency Programme]].</li>
</ul>
""",
    },

    "von-neumann-morgenstern-axioms": {
        "math": r"""
<p>Let $\mathcal{L}$ be the set of simple lotteries over a finite outcome set $X$. The vNM theorem (Mas-Colell Ch. 6.B) says that a preference relation $\succsim$ on $\mathcal{L}$ has an expected-utility representation $U(L) = \sum_{x \in X} p_L(x) u(x)$ if and only if it satisfies four axioms.</p>
<ol>
<li><strong>Completeness</strong>: for all $L, L' \in \mathcal{L}$, either $L \succsim L'$ or $L' \succsim L$.</li>
<li><strong>Transitivity</strong>: $L \succsim L'$ and $L' \succsim L''$ imply $L \succsim L''$.</li>
<li><strong>Continuity</strong>: for any $L \succ L' \succ L''$, there exists $\alpha \in (0,1)$ with $\alpha L + (1-\alpha) L'' \sim L'$.</li>
<li><strong>Independence</strong>: for all $L, L', L''$ and $\alpha \in (0,1]$, $L \succsim L'$ iff $\alpha L + (1-\alpha) L'' \succsim \alpha L' + (1-\alpha) L''$.</li>
</ol>
<p>The proof constructs $u$ by fixing a best lottery $\bar L$ and worst lottery $\underline L$, then using continuity to find for each $L$ the unique $\alpha_L$ with $L \sim \alpha_L \bar L + (1 - \alpha_L) \underline L$. Setting $u(L) = \alpha_L$ and applying independence shows linearity in probabilities, giving $U(L) = E_L[u(x)]$.</p>
<p>The representation is unique up to positive affine transformations: if $u$ represents $\succsim$, so does $v(x) = a u(x) + b$ for any $a > 0$. So $u$ is cardinal in differences (concavity is meaningful) but not in levels.</p>
<p>Independence is the load-bearing axiom and the one most often violated empirically (see [[Concepts/Allais Paradox]]). The other three are ordinal axioms that any consistent preference must satisfy.</p>
<p><em>Sources</em>: Micro2025.pdf Topic 6 (FHSMicroWk4) Lecture 1; Mas-Colell Ch. 6.B; Varian Ch. 11.1; Gravelle-Rees Ch. 19.</p>
""",
        "widget": r"""
<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" id="widget-vnm-axioms" role="img" aria-label="vNM axioms schema">
  <style>
    #widget-vnm-axioms text { font-family: Georgia, serif; font-size: 13px; fill: var(--text-primary, #222); }
    #widget-vnm-axioms .box { fill: var(--surface-alt, #f4f1ea); stroke: var(--text-primary, #222); stroke-width: 1.2; }
    #widget-vnm-axioms .arrow { stroke: var(--accent, #884); stroke-width: 1.5; fill: none; marker-end: url(#vnm-arrow); }
    #widget-vnm-axioms .caption { font-size: 11px; fill: var(--text-secondary, #555); }
  </style>
  <defs>
    <marker id="vnm-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M0,0 L10,5 L0,10 z" fill="var(--accent, #884)"/>
    </marker>
  </defs>
  <rect class="box" x="20" y="40" width="110" height="50" rx="6"/>
  <text x="75" y="62" text-anchor="middle">Completeness</text>
  <text x="75" y="80" text-anchor="middle" class="caption">order any pair</text>
  <rect class="box" x="20" y="120" width="110" height="50" rx="6"/>
  <text x="75" y="142" text-anchor="middle">Transitivity</text>
  <text x="75" y="160" text-anchor="middle" class="caption">no cycles</text>
  <rect class="box" x="20" y="200" width="110" height="50" rx="6"/>
  <text x="75" y="222" text-anchor="middle">Continuity</text>
  <text x="75" y="240" text-anchor="middle" class="caption">no lex jumps</text>
  <rect class="box" x="20" y="260" width="110" height="50" rx="6"/>
  <text x="75" y="282" text-anchor="middle">Independence</text>
  <text x="75" y="300" text-anchor="middle" class="caption">linearity in probs</text>
  <path class="arrow" d="M135,170 C220,170 240,170 320,170"/>
  <rect class="box" x="330" y="130" width="240" height="80" rx="8"/>
  <text x="450" y="160" text-anchor="middle" font-weight="bold">vNM Theorem</text>
  <text x="450" y="182" text-anchor="middle">$U(L)=\sum p_L(x)\,u(x)$</text>
  <text x="450" y="202" text-anchor="middle" class="caption">unique up to positive affine</text>
</svg>
<p class="caption">Four axioms collapse preferences over lotteries into a cardinal $u$ on outcomes, with utility of a lottery equal to expected utility of outcomes.</p>
""",
        "examples": r"""
<ul>
<li><strong>Insurance demand.</strong> Whole-of-market insurance pricing presumes households are EU maximisers with concave $u$ over wealth; this is the bedrock assumption behind every life and property cover demand curve.</li>
<li><strong>Asset pricing.</strong> The Lucas tree model and consumption CAPM both require independence to write $E[u'(c_{t+1}) R_{t+1}] = u'(c_t)$ as a separable Euler equation.</li>
<li><strong>Policy CBA.</strong> HM Treasury Green Book values risky outcomes by expected utility with a CRRA $u$; without independence the expected-value calculus loses its justification.</li>
<li><strong>Evaluation move.</strong> Distinguish the normative defence (Dutch books rule out cyclic preferences) from the descriptive critique (Allais and Ellsberg are reproducible); Doornik wants both sides cited.</li>
<li><strong>Evaluation move.</strong> Note that EU is silent on the source of probabilities; objective vs subjective probabilities matter for the [[Concepts/Dutch Book Argument]] formulation.</li>
<li><strong>Limitation.</strong> Independence fails systematically when outcomes interact with reference points (Kahneman and Tversky 1979); prospect theory replaces independence with probability weighting.</li>
</ul>
""",
    },

    "continuity-axiom": {
        "math": r"""
<p>Continuity says that for any three lotteries with $L \succ M \succ N$, there exists $\alpha \in (0,1)$ such that $\alpha L + (1-\alpha) N \sim M$. Equivalently, for any $L \in \mathcal{L}$ the upper contour set $\{L' : L' \succsim L\}$ and lower contour set $\{L' : L \succsim L'\}$ are closed in the probability simplex.</p>
<p>The axiom rules out lexicographic preferences over lotteries. The textbook example (Mas-Colell 6.B.3): if $L = (\text{ }\pounds 1000\text{, sure})$, $M = (\text{ }\pounds 10\text{, sure})$, $N = (\text{death, sure})$ and the agent prefers any positive probability of $\pounds 1000$ over a sure $\pounds 10$ but prefers $\pounds 10$ over any positive probability of death, then no $\alpha \in (0,1)$ satisfies $\alpha L + (1-\alpha) N \sim M$, since $\alpha L + (1-\alpha) N$ has a positive probability of death for every $\alpha < 1$.</p>
<ol>
<li><strong>Topological content</strong>: with the standard topology on the simplex, continuity is equivalent to closedness of the upper and lower contour sets.</li>
<li><strong>Why we need it</strong>: continuity ensures the indifference relation has a well-defined boundary, which the construction of $u$ in the vNM theorem relies on (taking infima of $\alpha$ such that $\alpha \bar L + (1-\alpha) \underline L \succsim L$).</li>
<li><strong>Failures</strong>: safety-first preferences and chance-constrained programming literally violate continuity by placing infinite weight on avoiding a specific outcome.</li>
</ol>
<p>Continuity is rarely violated in laboratory data because the alternatives that violate it (literal infinities in utility) are unusual. The axiom is technical rather than substantive, in contrast to independence.</p>
<p><em>Sources</em>: Micro2025.pdf Topic 6 (FHSMicroWk4) Lecture 1; Mas-Colell Ch. 6.B.3; Gravelle-Rees Ch. 19.2.</p>
""",
        "widget": r"""
<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" id="widget-continuity-axiom" role="img" aria-label="Continuity axiom on the simplex">
  <style>
    #widget-continuity-axiom text { font-family: Georgia, serif; font-size: 12px; fill: var(--text-primary, #222); }
    #widget-continuity-axiom .tri { fill: var(--surface-alt, #f4f1ea); stroke: var(--text-primary, #222); stroke-width: 1.2; }
    #widget-continuity-axiom .iso { stroke: var(--accent, #884); stroke-width: 1.5; fill: none; }
    #widget-continuity-axiom .pt { fill: var(--accent, #884); }
    #widget-continuity-axiom .caption { font-size: 11px; fill: var(--text-secondary, #555); }
  </style>
  <polygon class="tri" points="300,40 100,280 500,280"/>
  <text x="300" y="32" text-anchor="middle">$L$ (best)</text>
  <text x="90" y="295" text-anchor="end">$N$ (worst)</text>
  <text x="510" y="295" text-anchor="start">middle</text>
  <line class="iso" x1="160" y1="208" x2="440" y2="208"/>
  <text x="450" y="205" class="caption">indifference set through $M$</text>
  <circle class="pt" cx="240" cy="208" r="5"/>
  <text x="240" y="200" text-anchor="middle" class="caption">$\alpha L + (1-\alpha) N \sim M$</text>
  <circle class="pt" cx="300" cy="160" r="4"/>
  <text x="320" y="160" class="caption">$M$</text>
  <line class="iso" x1="300" y1="40" x2="240" y2="208" stroke-dasharray="4 3"/>
  <text x="80" y="40">probability mix</text>
  <text x="80" y="58" class="caption">moves along the edge $LN$</text>
</svg>
<p class="caption">Continuity guarantees that a mix $\alpha L + (1-\alpha) N$ on the edge of the simplex hits the indifference set of $M$ at an interior $\alpha$.</p>
""",
        "examples": r"""
<ul>
<li><strong>Driving and small risks.</strong> Every car journey carries a positive probability of fatality, yet people accept these risks for trivial gains; revealed preference is consistent with continuity over standard ranges of probabilities.</li>
<li><strong>Value of statistical life.</strong> The UK VSL of around 2 million pounds is computed by reading off the implicit $\alpha$ at which workers trade wage gains for fatality probabilities, which presumes continuity holds.</li>
<li><strong>Chance-constrained programming.</strong> In operations research and project finance, decisions may include a hard cap such as 'probability of ruin must be below 1 percent', which is a lexicographic preference and violates continuity.</li>
<li><strong>Evaluation move.</strong> Emphasise that continuity is technical, not substantive; the empirical assault on EU lands almost entirely on independence, not on continuity.</li>
<li><strong>Evaluation move.</strong> Point to Hausner (1954) on lexicographic utility for completeness; some safety-critical engineering preferences genuinely require it.</li>
<li><strong>Limitation.</strong> Continuity is hard to verify directly because it concerns behaviour at probability zero or one; see [[Concepts/von Neumann Morgenstern Axioms]] for the broader role.</li>
</ul>
""",
    },

    "reduction-of-compound-lotteries": {
        "math": r"""
<p>A compound lottery is a lottery whose prizes are themselves lotteries. Formally, given simple lotteries $L_1, \ldots, L_K \in \mathcal{L}$ and probabilities $\alpha_1, \ldots, \alpha_K$ summing to one, the compound lottery $(L_1, \ldots, L_K; \alpha_1, \ldots, \alpha_K)$ assigns probability $\alpha_k$ to playing $L_k$.</p>
<p>The reduction axiom (Mas-Colell 6.B.2) says this compound lottery is indifferent to the simple lottery $L = \sum_k \alpha_k L_k$ obtained by multiplying probabilities: if $L_k$ places probability $p_k(x)$ on outcome $x$, then $L$ places probability $\sum_k \alpha_k p_k(x)$ on $x$.</p>
<ol>
<li><strong>Why it matters</strong>: reduction lets us work with the space of simple lotteries only. Without it the choice space explodes and the vNM theorem cannot be stated cleanly.</li>
<li><strong>Reduction vs independence</strong>: under reduction plus independence the expected-utility representation extends to all compound lotteries via $U(\text{compound}) = \sum_k \alpha_k U(L_k)$. Some authors (Segal 1990) drop reduction and keep independence, generating recursive non-expected-utility models.</li>
<li><strong>The role of timing</strong>: reduction implies the agent does not care about when uncertainty resolves, only about the final distribution. Epstein-Zin preferences explicitly break this to separate risk aversion from intertemporal substitution.</li>
</ol>
<p>Empirical violations include the 'common ratio' Allais variant, where subjects treat compound lotteries with a certain stage differently from their reduced simple form, and Tversky-Kahneman's 'isolation effect', where a lottery presented in two stages is valued differently from the equivalent single-stage lottery.</p>
<p>For the FHS exam the standard treatment is to assume reduction holds, then verify that compound lotteries can be evaluated by their simple reductions.</p>
<p><em>Sources</em>: Micro2025.pdf Topic 6 (FHSMicroWk4) Lecture 1; Mas-Colell Ch. 6.B.2; Gravelle-Rees Ch. 19.2.</p>
""",
        "widget": r"""
<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" id="widget-reduction-compound" role="img" aria-label="Reduction of compound lotteries">
  <style>
    #widget-reduction-compound text { font-family: Georgia, serif; font-size: 12px; fill: var(--text-primary, #222); }
    #widget-reduction-compound .node { fill: var(--surface-alt, #f4f1ea); stroke: var(--text-primary, #222); stroke-width: 1.1; }
    #widget-reduction-compound .edge { stroke: var(--text-primary, #222); stroke-width: 1; fill: none; }
    #widget-reduction-compound .accent { fill: var(--accent, #884); }
    #widget-reduction-compound .caption { font-size: 11px; fill: var(--text-secondary, #555); }
  </style>
  <circle class="node" cx="60" cy="160" r="14"/>
  <text x="60" y="164" text-anchor="middle">C</text>
  <line class="edge" x1="74" y1="155" x2="160" y2="100"/>
  <line class="edge" x1="74" y1="165" x2="160" y2="220"/>
  <text x="100" y="120" class="caption">$\alpha$</text>
  <text x="100" y="210" class="caption">$1-\alpha$</text>
  <circle class="node" cx="170" cy="100" r="12"/>
  <text x="170" y="104" text-anchor="middle">$L_1$</text>
  <line class="edge" x1="182" y1="95" x2="240" y2="70"/>
  <line class="edge" x1="182" y1="105" x2="240" y2="130"/>
  <text x="248" y="74" class="caption">$p$: $x$</text>
  <text x="248" y="134" class="caption">$1-p$: $y$</text>
  <circle class="node" cx="170" cy="220" r="12"/>
  <text x="170" y="224" text-anchor="middle">$L_2$</text>
  <line class="edge" x1="182" y1="215" x2="240" y2="190"/>
  <line class="edge" x1="182" y1="225" x2="240" y2="250"/>
  <text x="248" y="194" class="caption">$q$: $x$</text>
  <text x="248" y="254" class="caption">$1-q$: $y$</text>
  <text x="380" y="160" font-weight="bold">$\Rightarrow$</text>
  <circle class="node" cx="450" cy="160" r="14"/>
  <text x="450" y="164" text-anchor="middle">$L$</text>
  <line class="edge" x1="464" y1="155" x2="540" y2="120"/>
  <line class="edge" x1="464" y1="165" x2="540" y2="200"/>
  <text x="548" y="124" class="caption">$\alpha p + (1-\alpha) q$: $x$</text>
  <text x="548" y="204" class="caption">rest: $y$</text>
  <text x="300" y="300" text-anchor="middle" class="caption">compound on the left reduces to simple lottery on the right</text>
</svg>
<p class="caption">Reduction multiplies branch probabilities, collapsing a two-stage tree into a one-stage simple lottery with the same final distribution.</p>
""",
        "examples": r"""
<ul>
<li><strong>National Lottery rollovers.</strong> The reduction axiom says a rollover ticket (which depends on whether the previous draw had a winner) should be valued only on the implied final distribution over jackpot sizes, not on the procedural history.</li>
<li><strong>Insurance with deductibles.</strong> A policy with deductible $D$ and copay $c$ produces a two-stage lottery (claim or not, then haircut); reduction lets the household evaluate it as a single distribution over final wealth.</li>
<li><strong>Casino game design.</strong> Games like Plinko or wheel-of-fortune deliberately stretch the resolution timeline; reduction predicts subjective value should equal the one-shot reduced form, yet observed willingness to play diverges.</li>
<li><strong>Evaluation move.</strong> Cite Segal (1990) and Epstein-Zin (1989) as canonical extensions that drop reduction to capture preference for early or late resolution of uncertainty.</li>
<li><strong>Evaluation move.</strong> Tie violations to procedural fairness considerations: agents in real choice problems care about whether risk was 'chosen' or 'imposed', which reduction blackboxes.</li>
<li><strong>Limitation.</strong> The empirical isolation effect (Tversky-Kahneman 1981) shows people frame each stage separately; see [[Concepts/Allais Paradox]] for the parallel critique of independence.</li>
</ul>
""",
    },

    "risk-aversion": {
        "math": r"""
<p>An expected-utility agent with Bernoulli utility $u$ over wealth is <strong>risk averse</strong> if for every non-degenerate lottery $L$, $u(E[L]) > E[u(L)]$. By Jensen's inequality this is equivalent to $u$ being strictly concave.</p>
<p>The equivalent characterisations (Mas-Colell 6.C.1) are:</p>
<ol>
<li>$u$ is concave: $u(\alpha w_1 + (1-\alpha) w_2) \geq \alpha u(w_1) + (1-\alpha) u(w_2)$ for all $w_1, w_2$, $\alpha \in [0,1]$.</li>
<li>The certainty equivalent satisfies $CE(L) \leq E[L]$ for every $L$ (see [[Concepts/Certainty Equivalent]]).</li>
<li>The risk premium $\pi(L) = E[L] - CE(L) \geq 0$ for every $L$.</li>
<li>If $u$ is twice differentiable, $u''(w) \leq 0$ everywhere.</li>
</ol>
<p>The local Arrow-Pratt approximation gives, for a small risk $\tilde\varepsilon$ with $E[\tilde\varepsilon] = 0$ and $\text{Var}(\tilde\varepsilon) = \sigma^2$:</p>
<p>$$\pi(w; \tilde\varepsilon) \approx \tfrac{1}{2} \sigma^2 \, r_A(w), \quad r_A(w) = -\frac{u''(w)}{u'(w)}.$$</p>
<p>So risk premium scales with variance and with absolute risk aversion. Two agents with the same $u$ up to a positive affine transformation share all risk attitudes.</p>
<p>Comparative risk aversion: agent A is more risk averse than B (Pratt 1964) iff $r_A^A(w) \geq r_A^B(w)$ for all $w$, iff there is a concave $\varphi$ with $u_A = \varphi \circ u_B$, iff $CE_A(L) \leq CE_B(L)$ for every $L$, iff A's risk premium exceeds B's on every lottery.</p>
<p>Risk aversion is the workhorse assumption behind insurance demand, portfolio diversification, and precautionary savings. Without it, the agent prefers fair gambles, which contradicts almost all observed financial behaviour.</p>
<p><em>Sources</em>: Micro2025.pdf Topic 6 (FHSMicroWk4) Lecture 2; Mas-Colell Ch. 6.C; Varian Ch. 11.4; Gravelle-Rees Ch. 19.3.</p>
""",
        "widget": r"""
<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" id="widget-risk-aversion" role="img" aria-label="Concave utility and risk premium">
  <style>
    #widget-risk-aversion text { font-family: Georgia, serif; font-size: 12px; fill: var(--text-primary, #222); }
    #widget-risk-aversion .axis { stroke: var(--text-primary, #222); stroke-width: 1.2; fill: none; }
    #widget-risk-aversion .curve { stroke: var(--accent, #884); stroke-width: 2; fill: none; }
    #widget-risk-aversion .chord { stroke: var(--text-primary, #222); stroke-width: 1; stroke-dasharray: 4 3; fill: none; }
    #widget-risk-aversion .guide { stroke: var(--text-secondary, #777); stroke-width: 0.8; stroke-dasharray: 2 3; }
    #widget-risk-aversion .pt { fill: var(--accent, #884); }
    #widget-risk-aversion .caption { font-size: 11px; fill: var(--text-secondary, #555); }
  </style>
  <line class="axis" x1="60" y1="280" x2="560" y2="280"/>
  <line class="axis" x1="60" y1="280" x2="60" y2="40"/>
  <text x="560" y="295" text-anchor="end">$w$</text>
  <text x="50" y="50" text-anchor="end">$u(w)$</text>
  <path class="curve" d="M 80 270 Q 280 60 540 60"/>
  <line class="chord" x1="120" y1="232" x2="500" y2="76"/>
  <line class="guide" x1="120" y1="280" x2="120" y2="232"/>
  <line class="guide" x1="500" y1="280" x2="500" y2="76"/>
  <line class="guide" x1="310" y1="280" x2="310" y2="154"/>
  <line class="guide" x1="310" y1="154" x2="60" y2="154"/>
  <line class="guide" x1="240" y1="280" x2="240" y2="154"/>
  <line class="guide" x1="240" y1="154" x2="60" y2="154"/>
  <circle class="pt" cx="120" cy="232" r="3.5"/>
  <circle class="pt" cx="500" cy="76" r="3.5"/>
  <circle class="pt" cx="310" cy="154" r="3.5"/>
  <circle class="pt" cx="240" cy="118" r="3.5"/>
  <text x="120" y="295" text-anchor="middle" class="caption">$w_1$</text>
  <text x="500" y="295" text-anchor="middle" class="caption">$w_2$</text>
  <text x="310" y="295" text-anchor="middle" class="caption">$E[w]$</text>
  <text x="240" y="295" text-anchor="middle" class="caption">$CE$</text>
  <text x="55" y="158" text-anchor="end" class="caption">$E[u]$</text>
  <text x="55" y="122" text-anchor="end" class="caption">$u(CE)$</text>
  <text x="320" y="100" class="caption">$\pi = E[w] - CE$</text>
  <path d="M 240 154 L 310 154" stroke="#c00" stroke-width="2.5" fill="none"/>
</svg>
<p class="caption">Concave $u$, with $CE$ below $E[w]$. The horizontal gap is the risk premium $\pi$, scaling as $\tfrac{1}{2}\sigma^2 r_A(w)$ locally.</p>
""",
        "examples": r"""
<ul>
<li><strong>Insurance markets.</strong> Aggregate household demand for life, motor, and home insurance is unintelligible without risk aversion; with linear $u$ no one buys cover at any markup.</li>
<li><strong>Equity premium.</strong> The historical 6 percent excess return on US equities over T-bills is explained as compensation for bearing aggregate risk, with a representative agent of RRA between 2 and 5; see [[Concepts/Arrow-Pratt RRA]].</li>
<li><strong>Precautionary saving.</strong> Under prudent utility ($u''' > 0$, implied by DARA), households accumulate buffer stock wealth when income uncertainty rises; Carroll (1997) calibrates the buffer to UK and US micro data.</li>
<li><strong>Evaluation move.</strong> Distinguish risk aversion (concavity of $u$) from loss aversion (kink at a reference point); empirical magnitudes for loss aversion are far larger than concavity alone delivers.</li>
<li><strong>Evaluation move.</strong> Note Rabin's (2000) calibration theorem: any plausible risk aversion over modest stakes implies absurd risk aversion over large stakes, so expected utility over wealth is itself suspect at the small-stake end.</li>
<li><strong>Limitation.</strong> Concavity of $u$ over wealth predicts that the same agent should also be risk averse over second-order small bets; people are not, suggesting the right state variable is consumption changes, not wealth levels.</li>
</ul>
""",
    },

    "certainty-equivalent": {
        "math": r"""
<p>The <strong>certainty equivalent</strong> $CE(L)$ of a lottery $L$ for an agent with Bernoulli utility $u$ is the sure amount that makes the agent indifferent to the lottery:</p>
<p>$$u(CE(L)) = E_L[u(w)].$$</p>
<p>Since $u$ is strictly increasing this is well-defined: $CE(L) = u^{-1}(E_L[u(w)])$.</p>
<ol>
<li><strong>Relation to $E[L]$</strong>: if $u$ is concave (risk averse), Jensen's inequality gives $u(E[L]) \geq E[u(L)] = u(CE)$, so $CE \leq E[L]$.</li>
<li><strong>Relation to risk premium</strong>: $\pi(L) = E[L] - CE(L) \geq 0$ for a risk-averse agent (see [[Concepts/Risk Premium]]).</li>
<li><strong>Arrow-Pratt approximation</strong>: for a lottery $w + \tilde\varepsilon$ with $E[\tilde\varepsilon] = 0$, $\text{Var}(\tilde\varepsilon) = \sigma^2$, $$CE \approx w - \tfrac{1}{2} \sigma^2 r_A(w),$$ giving a useful local formula linking $CE$, variance, and absolute risk aversion.</li>
<li><strong>CARA closed form</strong>: with $u(w) = -e^{-a w}/a$ and $\tilde\varepsilon \sim N(0, \sigma^2)$, $CE = w + E[\tilde\varepsilon] - \tfrac{a}{2}\sigma^2 = w - \tfrac{a}{2}\sigma^2$ exactly, not just approximately. This is the foundation of [[Concepts/Mean-Variance Utility]].</li>
<li><strong>CRRA closed form</strong>: with $u(w) = w^{1-\gamma}/(1-\gamma)$ and a binary lottery $w \in \{w_H, w_L\}$ with probabilities $p, 1-p$, $$CE = \left( p w_H^{1-\gamma} + (1-p) w_L^{1-\gamma} \right)^{1/(1-\gamma)}.$$</li>
</ol>
<p>The certainty equivalent is the most useful single-number summary of how an agent values a risky prospect, because it is denominated in pounds and directly answers 'what would you accept instead?'. Insurance demand is the budget condition $\pi \leq $ premium charged; portfolio optimisation maximises CE; willingness to pay for risk reduction is $\Delta CE$.</p>
<p>Two agents with the same $u$ up to a positive affine transformation have the same CE for every lottery; CE is the right ranking statistic, not expected utility itself.</p>
<p><em>Sources</em>: Micro2025.pdf Topic 6 (FHSMicroWk4) Lecture 2; Mas-Colell Ch. 6.C.3; Varian Ch. 11.5; Gravelle-Rees Ch. 19.3.</p>
""",
        "widget": r"""
<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" id="widget-certainty-equivalent" role="img" aria-label="Certainty equivalent on concave utility">
  <style>
    #widget-certainty-equivalent text { font-family: Georgia, serif; font-size: 12px; fill: var(--text-primary, #222); }
    #widget-certainty-equivalent .axis { stroke: var(--text-primary, #222); stroke-width: 1.2; fill: none; }
    #widget-certainty-equivalent .curve { stroke: var(--accent, #884); stroke-width: 2; fill: none; }
    #widget-certainty-equivalent .chord { stroke: var(--text-primary, #222); stroke-width: 1; stroke-dasharray: 4 3; fill: none; }
    #widget-certainty-equivalent .guide { stroke: var(--text-secondary, #777); stroke-width: 0.8; stroke-dasharray: 2 3; }
    #widget-certainty-equivalent .pt { fill: var(--accent, #884); }
    #widget-certainty-equivalent .premium { stroke: #c44; stroke-width: 2.5; }
    #widget-certainty-equivalent .caption { font-size: 11px; fill: var(--text-secondary, #555); }
  </style>
  <line class="axis" x1="60" y1="280" x2="560" y2="280"/>
  <line class="axis" x1="60" y1="280" x2="60" y2="40"/>
  <text x="560" y="295" text-anchor="end">wealth $w$</text>
  <text x="50" y="50" text-anchor="end">$u$</text>
  <path class="curve" d="M 80 268 Q 240 80 540 60"/>
  <line class="chord" x1="120" y1="240" x2="480" y2="80"/>
  <line class="guide" x1="120" y1="280" x2="120" y2="240"/>
  <line class="guide" x1="480" y1="280" x2="480" y2="80"/>
  <line class="guide" x1="300" y1="280" x2="300" y2="160"/>
  <line class="guide" x1="300" y1="160" x2="60" y2="160"/>
  <line class="guide" x1="225" y1="280" x2="225" y2="160"/>
  <circle class="pt" cx="120" cy="240" r="3.5"/>
  <circle class="pt" cx="480" cy="80" r="3.5"/>
  <circle class="pt" cx="300" cy="160" r="3.5"/>
  <circle class="pt" cx="225" cy="118" r="4"/>
  <text x="120" y="295" text-anchor="middle" class="caption">$w_L$</text>
  <text x="480" y="295" text-anchor="middle" class="caption">$w_H$</text>
  <text x="300" y="295" text-anchor="middle" class="caption">$E[w]$</text>
  <text x="225" y="295" text-anchor="middle" class="caption">$CE$</text>
  <text x="55" y="163" text-anchor="end" class="caption">$E[u]$</text>
  <line class="premium" x1="225" y1="160" x2="300" y2="160"/>
  <text x="262" y="148" text-anchor="middle" class="caption" fill="#c44">$\pi$</text>
</svg>
<p class="caption">$CE$ is the wealth level that gives utility equal to expected utility; the gap to $E[w]$ is the risk premium $\pi$.</p>
""",
        "examples": r"""
<ul>
<li><strong>Insurance reservation price.</strong> A household with wealth 200k, a 5 percent fire risk of losing 100k, and log utility has $CE \approx 191.6k$, so it would pay up to about 8.4k for full cover, against an expected loss of 5k.</li>
<li><strong>Portfolio choice.</strong> Merton's optimal share in a risky asset is $\theta^* = (\mu - r_f)/(\gamma \sigma^2)$ and is exactly the choice that maximises $CE$ to first order; CE is the right objective in continuous time.</li>
<li><strong>Project evaluation.</strong> For a risky NPV, replacing the random cash flow with its $CE$ and discounting at the risk-free rate is equivalent to discounting expected cash flows at a risk-adjusted rate (Brealey, Myers and Allen).</li>
<li><strong>Evaluation move.</strong> Stress that $CE$ depends only on $u$ up to positive affine transformation, so it is a meaningful pound-denominated welfare statistic where expected utility levels are not.</li>
<li><strong>Evaluation move.</strong> Compare CE under different utility families: CRRA gives a constant proportional discount, CARA a constant pound discount; the empirical evidence (Chiappori et al. 2014) supports CRRA at moderate stakes.</li>
<li><strong>Limitation.</strong> $CE$ is well-defined only under expected utility; under prospect theory or rank-dependent EU the right pound-denominated statistic is the 'utility value' or 'rank-dependent CE', which differs from the EU $CE$.</li>
</ul>
""",
    },

    "risk-premium": {
        "math": r"""
<p>For a lottery $L$ with expected value $E[L]$ and certainty equivalent $CE(L)$, the <strong>risk premium</strong> is</p>
<p>$$\pi(L) = E[L] - CE(L).$$</p>
<p>It is the maximum amount the agent would pay to swap the lottery for its expectation; equivalently the minimum premium reduction the agent would need to abandon insurance.</p>
<p>For a small risk $\tilde\varepsilon$ around wealth $w$ with $E[\tilde\varepsilon] = 0$, $\text{Var}(\tilde\varepsilon) = \sigma^2$, Pratt's (1964) approximation gives</p>
<p>$$\pi(w; \tilde\varepsilon) \approx \tfrac{1}{2} \sigma^2 \, r_A(w),$$</p>
<p>where $r_A(w) = -u''(w)/u'(w)$ is the Arrow-Pratt coefficient of absolute risk aversion. Two consequences follow.</p>
<ol>
<li>Risk premium scales linearly with variance, so the loading needed to compensate for risk is a quadratic of the spread, not the dispersion itself.</li>
<li>Risk premium scales linearly with $r_A(w)$, so a more risk-averse agent (in the Pratt sense) demands a strictly higher premium for any small lottery.</li>
</ol>
<p>Derivation: Taylor expand both sides of $u(w - \pi) = E[u(w + \tilde\varepsilon)]$. Left side: $u(w) - \pi u'(w) + o(\pi)$. Right side: $u(w) + E[\tilde\varepsilon] u'(w) + \tfrac{1}{2} E[\tilde\varepsilon^2] u''(w) + o(\sigma^2)$. With $E[\tilde\varepsilon] = 0$, equating gives $\pi u'(w) \approx -\tfrac{1}{2} \sigma^2 u''(w)$, hence the formula.</p>
<p>For a CARA agent with $u(w) = -e^{-aw}/a$ and Gaussian $\tilde\varepsilon \sim N(0, \sigma^2)$, the approximation is exact: $\pi = \tfrac{a}{2}\sigma^2$. This underlies [[Concepts/Mean-Variance Utility]].</p>
<p>For a CRRA agent with $u(w) = w^{1-\gamma}/(1-\gamma)$ and a proportional gamble $w(1 + \tilde\varepsilon)$ where $E[\tilde\varepsilon] = 0$, $\text{Var}(\tilde\varepsilon) = \sigma_\varepsilon^2$, the premium expressed as a fraction of wealth is $\pi/w \approx \tfrac{1}{2} \gamma \sigma_\varepsilon^2$, the proportional Arrow-Pratt formula with $r_R(w) = \gamma$.</p>
<p><em>Sources</em>: Micro2025.pdf Topic 6 (FHSMicroWk4) Lecture 2; Mas-Colell Ch. 6.C.4; Varian Ch. 11.5; Gravelle-Rees Ch. 19.3.</p>
""",
        "widget": r"""
<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" id="widget-risk-premium" role="img" aria-label="Risk premium and variance">
  <style>
    #widget-risk-premium text { font-family: Georgia, serif; font-size: 12px; fill: var(--text-primary, #222); }
    #widget-risk-premium .axis { stroke: var(--text-primary, #222); stroke-width: 1.2; fill: none; }
    #widget-risk-premium .curve { stroke: var(--accent, #884); stroke-width: 2; fill: none; }
    #widget-risk-premium .curve2 { stroke: #c44; stroke-width: 2; fill: none; }
    #widget-risk-premium .legend-box { fill: var(--surface-alt, #f4f1ea); stroke: var(--text-primary, #222); stroke-width: 0.8; }
    #widget-risk-premium .caption { font-size: 11px; fill: var(--text-secondary, #555); }
  </style>
  <line class="axis" x1="60" y1="280" x2="560" y2="280"/>
  <line class="axis" x1="60" y1="280" x2="60" y2="40"/>
  <text x="560" y="295" text-anchor="end">variance $\sigma^2$</text>
  <text x="50" y="50" text-anchor="end">$\pi$</text>
  <line x1="60" y1="280" x2="540" y2="80" class="curve"/>
  <line x1="60" y1="280" x2="540" y2="160" class="curve2"/>
  <rect class="legend-box" x="380" y="50" width="170" height="50" rx="4"/>
  <line x1="392" y1="65" x2="420" y2="65" stroke="var(--accent, #884)" stroke-width="2"/>
  <text x="428" y="69" class="caption">$r_A = 4$ (high)</text>
  <line x1="392" y1="88" x2="420" y2="88" stroke="#c44" stroke-width="2"/>
  <text x="428" y="92" class="caption">$r_A = 2$ (low)</text>
  <text x="300" y="310" text-anchor="middle" class="caption">slope of $\pi$ vs $\sigma^2$ is $\tfrac{1}{2} r_A$</text>
</svg>
<p class="caption">Risk premium is linear in variance with slope half of Arrow-Pratt absolute risk aversion; more risk-averse agents have steeper lines.</p>
""",
        "examples": r"""
<ul>
<li><strong>Reinsurance loading.</strong> Lloyd's catastrophe reinsurance prices are roughly proportional to expected loss plus a multiple of the standard deviation of loss; the multiple is the syndicate's implicit Arrow-Pratt absolute risk aversion.</li>
<li><strong>Equity risk premium.</strong> A representative agent with CRRA $\gamma = 3$ and consumption growth volatility 2 percent should demand about $\tfrac{1}{2}\cdot 3 \cdot 0.0004 = 0.06$ percent, far below the 6 percent observed; this is Mehra-Prescott's puzzle.</li>
<li><strong>UK fiscal risk pricing.</strong> The Treasury Green Book applies a Social Time Preference Rate of 3.5 percent, decomposed as 1 percent pure time preference plus 2.5 percent for wealth effect on marginal utility under CRRA $\gamma = 1$.</li>
<li><strong>Evaluation move.</strong> Show that the approximation $\pi \approx \tfrac{1}{2}\sigma^2 r_A$ breaks down for large skewed risks (catastrophe insurance) where higher moments matter.</li>
<li><strong>Evaluation move.</strong> Tie the formula to the question of why financial markets exist: pooling reduces $\sigma^2$ per capita, so total welfare cost of risk falls (see [[Concepts/Risk Pooling]]).</li>
<li><strong>Limitation.</strong> Rabin (2000) shows the Pratt approximation extrapolated to large stakes produces absurd predictions for the willingness to accept moderate bets; the formula is local only.</li>
</ul>
""",
    },

    "arrow-pratt-rra": {
        "math": r"""
<p>The <strong>Arrow-Pratt coefficient of relative risk aversion</strong> at wealth $w$ is</p>
<p>$$r_R(w) = -\frac{w \, u''(w)}{u'(w)} = w \cdot r_A(w),$$</p>
<p>where $r_A(w) = -u''(w)/u'(w)$ is the absolute coefficient. $r_R$ measures the local curvature of $u$ with respect to proportional changes in wealth, whereas $r_A$ measures it for pound-denominated changes.</p>
<ol>
<li><strong>Interpretation</strong>: for a proportional gamble $w(1 + \tilde\varepsilon)$ with $E[\tilde\varepsilon] = 0$, $\text{Var}(\tilde\varepsilon) = \sigma_\varepsilon^2$, the proportional risk premium is $\pi/w \approx \tfrac{1}{2} \sigma_\varepsilon^2 \, r_R(w)$.</li>
<li><strong>CRRA family</strong>: $u(w) = w^{1-\gamma}/(1-\gamma)$ for $\gamma \neq 1$, and $u(w) = \log w$ for $\gamma = 1$. Direct calculation gives $r_R(w) = \gamma$ at every $w$. Constant relative risk aversion is a property of the curve, not an assumption added on top.</li>
<li><strong>Empirical estimates</strong>: cross-study reviews (Meyer and Meyer 2005; Outreville 2014) put $\gamma$ in the range 1 to 4 for most consumer choices, rising for narrow gambles and falling for life-cycle savings.</li>
<li><strong>DARA, CARA, IARA</strong>: $r_A$ may decrease, stay constant, or increase in wealth. Empirical evidence (Friend and Blume 1975, Holt and Laury 2002) supports DARA but is consistent with CRRA, since CRRA implies DARA via $r_A = \gamma/w$.</li>
</ol>
<p>Why CRRA is the workhorse: under constant relative risk aversion, choices over proportional gambles are wealth-invariant, which is needed for balanced growth in macro models. Under CRRA the elasticity of intertemporal substitution is $1/\gamma$, tying risk attitude and intertemporal substitution together; the [[Concepts/Mean-Variance Utility]] case (CARA plus Gaussian) breaks this link.</p>
<p>For the FHS exam, the standard tasks are: (i) compute $r_R$ for log, power, exponential, and quadratic utility; (ii) show that CRRA implies wealth-invariance of portfolio shares; (iii) link $r_R$ to the [[Concepts/Risk Premium]] approximation.</p>
<p><em>Sources</em>: Micro2025.pdf Topic 6 (FHSMicroWk4) Lecture 3; Mas-Colell Ch. 6.C.4; Gravelle-Rees Ch. 19.4; Pratt (1964).</p>
""",
        "widget": r"""
<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" id="widget-arrow-pratt-rra" role="img" aria-label="CRRA utility for different gamma">
  <style>
    #widget-arrow-pratt-rra text { font-family: Georgia, serif; font-size: 12px; fill: var(--text-primary, #222); }
    #widget-arrow-pratt-rra .axis { stroke: var(--text-primary, #222); stroke-width: 1.2; fill: none; }
    #widget-arrow-pratt-rra .c1 { stroke: #6a8; stroke-width: 2; fill: none; }
    #widget-arrow-pratt-rra .c2 { stroke: var(--accent, #884); stroke-width: 2; fill: none; }
    #widget-arrow-pratt-rra .c3 { stroke: #c44; stroke-width: 2; fill: none; }
    #widget-arrow-pratt-rra .legend-box { fill: var(--surface-alt, #f4f1ea); stroke: var(--text-primary, #222); stroke-width: 0.8; }
    #widget-arrow-pratt-rra .caption { font-size: 11px; fill: var(--text-secondary, #555); }
  </style>
  <line class="axis" x1="60" y1="280" x2="560" y2="280"/>
  <line class="axis" x1="60" y1="280" x2="60" y2="40"/>
  <text x="560" y="295" text-anchor="end">$w$</text>
  <text x="50" y="50" text-anchor="end">$u$</text>
  <path class="c1" d="M 80 270 Q 200 200 540 110"/>
  <path class="c2" d="M 80 275 Q 180 140 540 80"/>
  <path class="c3" d="M 80 278 Q 140 90 540 60"/>
  <rect class="legend-box" x="380" y="200" width="170" height="80" rx="4"/>
  <line x1="392" y1="218" x2="420" y2="218" stroke="#6a8" stroke-width="2"/>
  <text x="428" y="222" class="caption">$\gamma = 0.5$ (mild)</text>
  <line x1="392" y1="240" x2="420" y2="240" stroke="var(--accent, #884)" stroke-width="2"/>
  <text x="428" y="244" class="caption">$\gamma = 1$ (log)</text>
  <line x1="392" y1="262" x2="420" y2="262" stroke="#c44" stroke-width="2"/>
  <text x="428" y="266" class="caption">$\gamma = 3$ (strong)</text>
</svg>
<p class="caption">Higher $\gamma$ gives a more bowed CRRA utility, with a steeper rise at low wealth and a flatter ceiling; relative risk aversion $r_R(w) = \gamma$ at every $w$.</p>
""",
        "examples": r"""
<ul>
<li><strong>Lifetime portfolio share.</strong> Merton (1969) gives the optimal share in the risky asset as $(\mu - r_f)/(\gamma \sigma^2)$ under CRRA, independent of wealth: a CRRA household with the same $\gamma$ at 25 and at 65 holds the same fraction in equity, abstracting from human capital.</li>
<li><strong>Discount rates.</strong> The Ramsey rule $r = \rho + \gamma g$ uses RRA $\gamma$ as the elasticity of marginal utility of consumption; the Stern Review (2006) chose $\gamma = 1$, Nordhaus prefers $\gamma = 2$, which changes climate damages estimates by a factor of three.</li>
<li><strong>Holt-Laury lottery menus.</strong> Standard FHS undergraduate experiments elicit $\gamma$ via a menu of paired gambles, typically obtaining $\gamma \in [0.3, 1.5]$ for small stakes, well below macro calibrations.</li>
<li><strong>Evaluation move.</strong> Note that CRRA bundles risk aversion ($\gamma$) with elasticity of intertemporal substitution ($1/\gamma$); Epstein-Zin preferences unbundle them, which matters for asset pricing puzzles.</li>
<li><strong>Evaluation move.</strong> Highlight that $\gamma$ estimated from large macro shocks (equity premium puzzle requires $\gamma > 10$) differs from $\gamma$ in micro experiments, pointing to either heterogeneity or preference misspecification.</li>
<li><strong>Limitation.</strong> CRRA cannot accommodate subsistence wealth thresholds; HARA or Stone-Geary utility introduces a lower bound $\bar w$ below which marginal utility diverges; see [[Concepts/Risk Aversion]] for the underlying concept.</li>
</ul>
""",
    },

    "first-order-stochastic-dominance": {
        "math": r"""
<p>For lotteries $L, L'$ on the real line with CDFs $F$ and $F'$, $L$ <strong>first-order stochastically dominates</strong> $L'$ ($L \succeq_{FOSD} L'$) iff</p>
<p>$$F(x) \leq F'(x) \quad \text{for all } x \in \mathbb{R}, \text{ strict somewhere.}$$</p>
<p>Equivalently, the survival function $1 - F$ is everywhere weakly higher under $L$ than under $L'$: $L$ puts more probability mass on every upper tail.</p>
<p>The key result (Mas-Colell 6.D.1, Gravelle-Rees 19.7) is that</p>
<p>$$L \succeq_{FOSD} L' \iff E_L[u(x)] \geq E_{L'}[u(x)] \text{ for every weakly increasing } u.$$</p>
<p>So FOSD is the unanimity ranking among all expected-utility agents who prefer more to less, regardless of risk attitude.</p>
<p>Proof sketch of $\Rightarrow$: integrate by parts. For a bounded $u$ with $u' \geq 0$,</p>
<p>$$E_L[u] - E_{L'}[u] = \int (F'(x) - F(x)) u'(x) dx \geq 0$$</p>
<p>since $F'(x) - F(x) \geq 0$ and $u'(x) \geq 0$. The converse uses indicator utility $u(x) = \mathbf{1}\{x > t\}$ for arbitrary $t$, which forces the CDF inequality.</p>
<ol>
<li><strong>Strength</strong>: FOSD is a strong dominance, holding for every monotone $u$, including linear, concave, and convex. It does not require knowledge of risk attitude.</li>
<li><strong>Detection via random variables</strong>: $L \succeq_{FOSD} L'$ iff there exist coupled random variables $X \sim L$, $X' \sim L'$ on a common probability space with $X \geq X'$ pointwise (a 'comonotonic' coupling).</li>
<li><strong>Stronger than SOSD</strong>: FOSD implies [[Concepts/Second-Order Stochastic Dominance]] but not vice versa. FOSD allows different means; SOSD presumes equal means.</li>
</ol>
<p>For the FHS exam, the standard tasks are: (i) check FOSD by plotting CDFs; (ii) prove the integration-by-parts equivalence; (iii) construct counter-examples where $L$ has higher mean and variance than $L'$ but does not FOSD it.</p>
<p><em>Sources</em>: Micro2025.pdf Topic 6 (FHSMicroWk4) Lecture 3; Mas-Colell Ch. 6.D.1; Gravelle-Rees Ch. 19.7.</p>
""",
        "widget": r"""
<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" id="widget-fosd" role="img" aria-label="First-order stochastic dominance CDFs">
  <style>
    #widget-fosd text { font-family: Georgia, serif; font-size: 12px; fill: var(--text-primary, #222); }
    #widget-fosd .axis { stroke: var(--text-primary, #222); stroke-width: 1.2; fill: none; }
    #widget-fosd .grid { stroke: var(--text-secondary, #aaa); stroke-width: 0.5; stroke-dasharray: 2 3; }
    #widget-fosd .cdf1 { stroke: var(--accent, #884); stroke-width: 2; fill: none; }
    #widget-fosd .cdf2 { stroke: #c44; stroke-width: 2; fill: none; }
    #widget-fosd .legend-box { fill: var(--surface-alt, #f4f1ea); stroke: var(--text-primary, #222); stroke-width: 0.8; }
    #widget-fosd .caption { font-size: 11px; fill: var(--text-secondary, #555); }
  </style>
  <line class="axis" x1="60" y1="280" x2="560" y2="280"/>
  <line class="axis" x1="60" y1="280" x2="60" y2="40"/>
  <line class="grid" x1="60" y1="60" x2="560" y2="60"/>
  <text x="55" y="65" text-anchor="end" class="caption">1</text>
  <text x="55" y="285" text-anchor="end" class="caption">0</text>
  <text x="560" y="295" text-anchor="end">$x$</text>
  <text x="50" y="50" text-anchor="end">$F(x)$</text>
  <path class="cdf1" d="M 60 280 L 200 280 L 200 200 L 360 200 L 360 100 L 500 100 L 500 60 L 560 60"/>
  <path class="cdf2" d="M 60 280 L 140 280 L 140 220 L 280 220 L 280 140 L 420 140 L 420 60 L 560 60"/>
  <rect class="legend-box" x="80" y="50" width="160" height="50" rx="4"/>
  <line x1="92" y1="68" x2="120" y2="68" stroke="var(--accent, #884)" stroke-width="2"/>
  <text x="128" y="72" class="caption">$F_L$ (dominant)</text>
  <line x1="92" y1="90" x2="120" y2="90" stroke="#c44" stroke-width="2"/>
  <text x="128" y="94" class="caption">$F_{L'}$ (dominated)</text>
  <text x="300" y="310" text-anchor="middle" class="caption">$F_L(x) \leq F_{L'}(x)$ for every $x$: $L$ FOSDs $L'$</text>
</svg>
<p class="caption">FOSD: the dominant lottery's CDF lies weakly below the dominated CDF everywhere. Every monotone $u$ prefers $L$.</p>
""",
        "examples": r"""
<ul>
<li><strong>Tax cut analysis.</strong> A proportional tax cut at every income level FOSDs the pre-cut income distribution (CDF strictly lower); every monotone social welfare function prefers it, before deadweight or revenue effects.</li>
<li><strong>R&D investment.</strong> A positive technology shock that adds $\Delta > 0$ to every realisation of output produces a distribution that FOSDs the baseline; the firm value rises for every shareholder utility, not just risk-neutral ones.</li>
<li><strong>Bond ratings.</strong> A senior tranche of a CDO FOSDs the underlying pool's recovery distribution by construction (it pays in every state where the pool pays plus more); this is what 'seniority' formally means.</li>
<li><strong>Evaluation move.</strong> Stress that FOSD is the cleanest comparison because it requires no parametric assumption on $u$; in policy work this is the strongest case you can make.</li>
<li><strong>Evaluation move.</strong> Distinguish FOSD from 'higher mean' clearly: $L = \{0, 100\}$ uniform vs $L' = \{40, 60\}$ uniform have the same mean and neither FOSDs the other, despite different variances; the comparison is [[Concepts/Second-Order Stochastic Dominance]].</li>
<li><strong>Limitation.</strong> FOSD is rarely satisfied between real-world risky distributions because tails almost always cross; SOSD or mean-variance comparisons are more often the binding criterion.</li>
</ul>
""",
    },

    "second-order-stochastic-dominance": {
        "math": r"""
<p>For lotteries $L, L'$ with CDFs $F, F'$ and equal means $E[L] = E[L']$, $L$ <strong>second-order stochastically dominates</strong> $L'$ ($L \succeq_{SOSD} L'$) iff</p>
<p>$$\int_{-\infty}^x F(t) \, dt \leq \int_{-\infty}^x F'(t) \, dt \quad \text{for all } x.$$</p>
<p>So the integrated CDF of $L$ lies weakly below that of $L'$. The standard result (Rothschild-Stiglitz 1970, Mas-Colell 6.D.2) gives</p>
<p>$$L \succeq_{SOSD} L' \iff E_L[u] \geq E_{L'}[u] \text{ for every weakly increasing concave } u.$$</p>
<p>SOSD is the unanimity ranking among all <strong>risk-averse</strong> expected-utility agents.</p>
<p>Three equivalent characterisations (Rothschild-Stiglitz):</p>
<ol>
<li><strong>Integrated-CDF criterion</strong> as above.</li>
<li><strong>Mean-preserving spread</strong>: $L'$ is obtained from $L$ by a sequence of [[Concepts/Mean-Preserving Spread]] operations (transferring probability mass from the centre to the tails while preserving the mean).</li>
<li><strong>Coupling criterion</strong>: there exist random variables $X \sim L$, $X' \sim L'$ on a common space with $X' = X + Z$ where $E[Z \mid X] = 0$ (so $L'$ is $L$ plus mean-zero noise conditional on $L$).</li>
</ol>
<p>Proof sketch of integrated-CDF $\Rightarrow$ EU inequality: integrate by parts twice. For concave $u$ ($u'' \leq 0$) and increasing ($u' \geq 0$),</p>
<p>$$E_L[u] - E_{L'}[u] = -\int \left(\int_{-\infty}^x (F(t) - F'(t)) dt\right) u''(x) \, dx \geq 0$$</p>
<p>since the inner integral is $\leq 0$ and $u'' \leq 0$.</p>
<p>SOSD is less restrictive than FOSD (it does not require monotone CDF dominance, only an integrated condition) and more restrictive than 'any EU agent prefers $L$', because it singles out risk-averse agents.</p>
<p><em>Sources</em>: Micro2025.pdf Topic 6 (FHSMicroWk5) Lecture 4; Mas-Colell Ch. 6.D.2; Rothschild and Stiglitz (1970); Gravelle-Rees Ch. 19.7.</p>
""",
        "widget": r"""
<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" id="widget-sosd" role="img" aria-label="Second-order stochastic dominance via integrated CDFs">
  <style>
    #widget-sosd text { font-family: Georgia, serif; font-size: 12px; fill: var(--text-primary, #222); }
    #widget-sosd .axis { stroke: var(--text-primary, #222); stroke-width: 1.2; fill: none; }
    #widget-sosd .cdf1 { stroke: var(--accent, #884); stroke-width: 2; fill: none; }
    #widget-sosd .cdf2 { stroke: #c44; stroke-width: 2; fill: none; }
    #widget-sosd .legend-box { fill: var(--surface-alt, #f4f1ea); stroke: var(--text-primary, #222); stroke-width: 0.8; }
    #widget-sosd .caption { font-size: 11px; fill: var(--text-secondary, #555); }
    #widget-sosd .label-area { font-size: 11px; fill: var(--text-primary, #222); }
  </style>
  <line class="axis" x1="60" y1="280" x2="560" y2="280"/>
  <line class="axis" x1="60" y1="280" x2="60" y2="40"/>
  <text x="560" y="295" text-anchor="end">$x$</text>
  <text x="50" y="50" text-anchor="end">$F(x)$</text>
  <path class="cdf1" d="M 60 280 L 220 280 L 220 170 L 400 170 L 400 60 L 560 60"/>
  <path class="cdf2" d="M 60 280 L 140 280 L 140 200 L 320 200 L 320 60 L 560 60"/>
  <rect class="legend-box" x="80" y="50" width="170" height="50" rx="4"/>
  <line x1="92" y1="68" x2="120" y2="68" stroke="var(--accent, #884)" stroke-width="2"/>
  <text x="128" y="72" class="caption">$F_L$ (less spread)</text>
  <line x1="92" y1="90" x2="120" y2="90" stroke="#c44" stroke-width="2"/>
  <text x="128" y="94" class="caption">$F_{L'}$ (spread out)</text>
  <text x="180" y="240" class="label-area">CDFs cross, but $\int F_L \leq \int F_{L'}$ everywhere</text>
  <text x="300" y="310" text-anchor="middle" class="caption">same mean, $L$ SOSDs $L'$, every risk-averse agent prefers $L$</text>
</svg>
<p class="caption">CDFs may cross (so FOSD fails), yet $L$ SOSDs $L'$ because $L'$ is a mean-preserving spread of $L$.</p>
""",
        "examples": r"""
<ul>
<li><strong>Diversified vs concentrated portfolio.</strong> A diversified equity portfolio and a single stock with the same expected return: by the Rothschild-Stiglitz characterisation the diversified portfolio SOSDs the single stock if the single stock is a mean-preserving spread.</li>
<li><strong>Income smoothing.</strong> Permanent-income consumption SOSDs raw income with the same lifetime mean; every risk-averse household prefers smoothed consumption.</li>
<li><strong>Climate damages.</strong> A 'fat-tailed' Weitzman-style damage distribution does not SOSD a thin-tailed one with the same mean; risk-averse social planners strictly prefer the thin-tailed regime.</li>
<li><strong>Evaluation move.</strong> Contrast SOSD's mean-preserving spread interpretation with mean-variance ranking; for non-normal distributions the two diverge because higher moments matter for risk-averse but not for mean-variance agents.</li>
<li><strong>Evaluation move.</strong> Note the link to Lorenz dominance: in the income distribution context, SOSD with the same mean is equivalent to Lorenz dominance, the standard concept in welfare analysis (Atkinson 1970).</li>
<li><strong>Limitation.</strong> SOSD presumes equal means; for unequal means use generalised Lorenz dominance or [[Concepts/First-Order Stochastic Dominance]] where possible.</li>
</ul>
""",
    },

    "risk-pooling": {
        "math": r"""
<p><strong>Risk pooling</strong> exploits independence (or low correlation) across many similar risks to reduce per-capita variance. Suppose $n$ agents each face an i.i.d. loss $\tilde L_i$ with mean $\mu$ and variance $\sigma^2$. The pool's total loss is $\tilde S = \sum_{i=1}^n \tilde L_i$, with mean $n\mu$ and variance $n\sigma^2$. Per agent the share is $\tilde L^{pool} = \tilde S/n$ with mean $\mu$ and variance $\sigma^2/n$.</p>
<p>As $n \to \infty$, $\text{Var}(\tilde L^{pool}) \to 0$ by the law of large numbers. The pooled risk has the same mean as the standalone risk but vanishing variance, so for a risk-averse agent the [[Concepts/Risk Premium]] $\pi \approx \tfrac{1}{2} \sigma^2 r_A / n \to 0$.</p>
<ol>
<li><strong>Welfare gain</strong>: each agent's certainty equivalent rises from $\mu - \tfrac{1}{2}\sigma^2 r_A$ to nearly $\mu$ as $n$ grows. The risk premium savings are the social value of insurance.</li>
<li><strong>Vs risk sharing</strong>: risk pooling shrinks aggregate variance through independence; risk sharing redistributes a fixed aggregate risk across more shoulders, which works for systemic risk but does not reduce it.</li>
<li><strong>Correlation kills it</strong>: if losses are positively correlated with coefficient $\rho$, the per-capita variance is $\sigma^2 (1/n + \rho (1 - 1/n)) \to \rho \sigma^2$, not zero. Reinsurance for hurricane or pandemic risk hits this wall.</li>
</ol>
<p>The textbook example (Gravelle-Rees 19.6): two farmers each face a 50 percent chance of a 10k loss, independently. Either alone has $\sigma^2 = 25$ million pounds squared. Pooling halves the variance: each takes half the total loss, so the realised loss is 0, 5k, or 10k with probabilities 0.25, 0.5, 0.25. Variance falls to 12.5 million pounds squared. With CRRA $\gamma = 2$ and initial wealth 100k, the welfare gain in CE terms is about 250 pounds each.</p>
<p>Pooling is the engine of the insurance industry: a million independent motor risks have per-capita variance one millionth of the standalone variance, so the insurer can charge a small loading above expected loss and still leave every customer better off.</p>
<p><em>Sources</em>: Micro2025.pdf Topic 6 (FHSMicroWk5) Lecture 5; Gravelle-Rees Ch. 19.6; Varian Ch. 11.7.</p>
""",
        "widget": r"""
<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" id="widget-risk-pooling" role="img" aria-label="Per-capita variance under risk pooling">
  <style>
    #widget-risk-pooling text { font-family: Georgia, serif; font-size: 12px; fill: var(--text-primary, #222); }
    #widget-risk-pooling .axis { stroke: var(--text-primary, #222); stroke-width: 1.2; fill: none; }
    #widget-risk-pooling .c-indep { stroke: var(--accent, #884); stroke-width: 2; fill: none; }
    #widget-risk-pooling .c-corr { stroke: #c44; stroke-width: 2; fill: none; }
    #widget-risk-pooling .legend-box { fill: var(--surface-alt, #f4f1ea); stroke: var(--text-primary, #222); stroke-width: 0.8; }
    #widget-risk-pooling .caption { font-size: 11px; fill: var(--text-secondary, #555); }
  </style>
  <line class="axis" x1="60" y1="280" x2="560" y2="280"/>
  <line class="axis" x1="60" y1="280" x2="60" y2="40"/>
  <text x="560" y="295" text-anchor="end">$n$ (pool size)</text>
  <text x="50" y="50" text-anchor="end">$\text{Var}/n$</text>
  <path class="c-indep" d="M 90 80 Q 200 250 560 270"/>
  <path class="c-corr" d="M 90 80 Q 200 180 560 165"/>
  <line x1="60" y1="165" x2="560" y2="165" stroke="#c44" stroke-width="0.8" stroke-dasharray="3 3"/>
  <rect class="legend-box" x="320" y="50" width="240" height="60" rx="4"/>
  <line x1="332" y1="68" x2="360" y2="68" stroke="var(--accent, #884)" stroke-width="2"/>
  <text x="368" y="72" class="caption">independent, $\sigma^2/n \to 0$</text>
  <line x1="332" y1="92" x2="360" y2="92" stroke="#c44" stroke-width="2"/>
  <text x="368" y="96" class="caption">$\rho = 0.3$, floor at $\rho \sigma^2$</text>
  <text x="300" y="310" text-anchor="middle" class="caption">pooling kills variance under independence; correlation puts a floor</text>
</svg>
<p class="caption">Per-capita variance falls as $1/n$ under independence and converges to $\rho \sigma^2$ under correlation; correlated catastrophe risks cannot be pooled away.</p>
""",
        "examples": r"""
<ul>
<li><strong>Motor insurance.</strong> Aviva pools millions of independent crash risks; variance per policy falls to near zero, so the loading above expected loss can be 10 to 15 percent (admin, capital, profit) and the customer still finds it worthwhile.</li>
<li><strong>Pandemic uninsurability.</strong> COVID-19 business interruption claims arrived simultaneously across all firms; correlated losses meant pooling failed and insurers exited the line. The pandemic risk had no insurable structure.</li>
<li><strong>Mutual societies.</strong> Friendly societies in 19th century Britain pooled sickness risk among workers in the same trade, but trade-specific downturns produced correlated unemployment that broke the pool, motivating state-level unemployment insurance.</li>
<li><strong>Evaluation move.</strong> Distinguish pooling (independence reduces aggregate variance per capita) from sharing (fixed aggregate risk divided among more agents); systemic risk requires sharing or absorption, not pooling.</li>
<li><strong>Evaluation move.</strong> Tie pooling failures to the case for state-provided insurance: floods, pandemics, and large unemployment shocks are correlated and need taxpayer capital, not private actuarial pooling.</li>
<li><strong>Limitation.</strong> Pooling presumes the joint distribution is known; with parameter uncertainty (climate change altering hurricane frequency), pooled variance is itself uncertain; see [[Concepts/Mean-Preserving Spread]] for how second-moment uncertainty matters.</li>
</ul>
""",
    },

    "state-space-insurance-diagram": {
        "math": r"""
<p>Consider an agent with wealth $w$ facing a possible loss $L$ with probability $\pi$. State 1 is 'no loss' with wealth $w_1 = w$; state 2 is 'loss' with wealth $w_2 = w - L$. Endowment $E = (w, w - L)$ lies below the 45-degree line in the $(w_1, w_2)$ plane.</p>
<p>The agent can buy insurance: pay premium $\alpha q$ to receive payout $\alpha$ if the loss occurs, where $q$ is the price per unit of cover. Then $w_1 = w - \alpha q$ and $w_2 = w - L - \alpha q + \alpha = w - L + \alpha(1-q)$. Eliminating $\alpha$ gives the budget constraint</p>
<p>$$\frac{q}{1-q} (w_1 - w) + (w_2 - (w - L)) = 0,$$</p>
<p>a line through $E$ with slope $-q/(1-q)$ in the $(w_1, w_2)$ plane.</p>
<ol>
<li><strong>Actuarially fair pricing</strong>: $q = \pi$. Slope of budget line is $-\pi/(1-\pi)$, equal to the slope of the indifference curve at the 45-degree line (full insurance point).</li>
<li><strong>Indifference curves</strong>: $V(w_1, w_2) = (1 - \pi) u(w_1) + \pi u(w_2) = \text{const}$. Slope is $$\frac{dw_2}{dw_1}\bigg|_V = -\frac{(1-\pi) u'(w_1)}{\pi u'(w_2)}.$$ At $w_1 = w_2$ (the 45-degree line), this collapses to $-(1-\pi)/\pi$.</li>
<li><strong>Full insurance result</strong>: with fair pricing, tangency of indifference curve and budget line occurs at $w_1 = w_2$, i.e. on the 45-degree line. The agent equates wealth across states.</li>
<li><strong>Unfair pricing</strong>: if $q > \pi$ (insurer loads premium), budget slope $-q/(1-q)$ is steeper than indifference curve slope at 45-degree line, so tangency occurs strictly below the line: partial insurance.</li>
</ol>
<p>Indifference curves are convex iff $u$ is concave (risk averse). The state-space diagram is the workhorse for insurance demand, contingent claims pricing, and the moral hazard / adverse selection extensions (Rothschild and Stiglitz 1976).</p>
<p><em>Sources</em>: Micro2025.pdf Topic 6 (FHSMicroWk5) Lecture 4; Mas-Colell Ch. 6.E; Varian Ch. 11.6; Gravelle-Rees Ch. 19.5.</p>
""",
        "widget": r"""
<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" id="widget-state-space" role="img" aria-label="State-space insurance diagram">
  <style>
    #widget-state-space text { font-family: Georgia, serif; font-size: 12px; fill: var(--text-primary, #222); }
    #widget-state-space .axis { stroke: var(--text-primary, #222); stroke-width: 1.2; fill: none; }
    #widget-state-space .diag { stroke: var(--text-secondary, #777); stroke-width: 1; stroke-dasharray: 4 3; }
    #widget-state-space .budget { stroke: var(--accent, #884); stroke-width: 1.8; }
    #widget-state-space .unfair { stroke: #c44; stroke-width: 1.8; }
    #widget-state-space .indiff { stroke: var(--text-primary, #222); stroke-width: 1.4; fill: none; }
    #widget-state-space .pt { fill: var(--accent, #884); }
    #widget-state-space .pt2 { fill: #c44; }
    #widget-state-space .caption { font-size: 11px; fill: var(--text-secondary, #555); }
  </style>
  <line class="axis" x1="60" y1="280" x2="560" y2="280"/>
  <line class="axis" x1="60" y1="280" x2="60" y2="40"/>
  <text x="560" y="295" text-anchor="end">$w_1$ (no loss)</text>
  <text x="50" y="50" text-anchor="end">$w_2$ (loss)</text>
  <line class="diag" x1="60" y1="280" x2="320" y2="40"/>
  <text x="328" y="44" class="caption">45 degree line, $w_1 = w_2$</text>
  <line class="budget" x1="120" y1="270" x2="440" y2="40"/>
  <line class="unfair" x1="380" y1="270" x2="500" y2="40"/>
  <path class="indiff" d="M 90 220 Q 200 160 320 100 Q 420 70 500 60"/>
  <path class="indiff" d="M 130 260 Q 230 200 350 150 Q 450 120 540 110"/>
  <circle class="pt" cx="420" cy="100" r="5"/>
  <text x="430" y="98" class="caption">$E$ (endowment, $w, w - L$)</text>
  <circle class="pt" cx="245" cy="115" r="5"/>
  <text x="190" y="108" class="caption">full ins (fair)</text>
  <circle class="pt2" cx="410" cy="110" r="5"/>
  <text x="395" y="130" class="caption" fill="#c44">partial (unfair)</text>
</svg>
<p class="caption">Fair-odds budget line through $E$ touches an indifference curve on the 45-degree line: full insurance. Steeper unfair budget gives tangency below 45 degrees: partial insurance.</p>
""",
        "examples": r"""
<ul>
<li><strong>UK motor cover.</strong> Even at typical loadings (25 to 35 percent above expected loss), most drivers choose substantial cover; the state-space diagram predicts partial insurance, matching the universal use of excesses or deductibles.</li>
<li><strong>Health insurance copays.</strong> US ACA marketplace plans price actuarially unfairly due to admin costs; the state-space prediction of underinsurance is exactly what enrolees do, with copays and deductibles producing $w_1 - w_2 > 0$ at the chosen plan.</li>
<li><strong>Catastrophe bonds.</strong> Investors sell hurricane insurance to insurers and earn yields several hundred basis points above Treasuries; the spread is $q - \pi$, the unfair loading from the insurer's side, sustained by the insurer's risk aversion to tail loss.</li>
<li><strong>Evaluation move.</strong> Use the diagram to derive moral hazard: if the agent can reduce $\pi$ by costly effort, full insurance kills the incentive; the optimal contract puts the agent strictly below the 45-degree line.</li>
<li><strong>Evaluation move.</strong> Extend to Rothschild-Stiglitz adverse selection: high and low risks have different indifference curve slopes, so a single contract cannot separate them; menus must satisfy incentive compatibility.</li>
<li><strong>Limitation.</strong> The two-state simplification suppresses the continuous distribution of loss sizes; for catastrophe modelling the full distribution matters, not just $\pi$. See [[Concepts/Fair Premium]] for the actuarial pricing concept.</li>
</ul>
""",
    },

    "fair-premium": {
        "math": r"""
<p>An insurance premium is <strong>actuarially fair</strong> if it equals the expected payout. For a policy paying $\alpha$ in state of loss (probability $\pi$) and zero otherwise, the fair premium is</p>
<p>$$P_{fair} = \pi \alpha,$$</p>
<p>so the price per unit of cover is $q = \pi$. The insurer breaks even in expectation: $E[\text{profit}] = P - \pi \alpha = 0$.</p>
<ol>
<li><strong>Full insurance result.</strong> A risk-averse expected-utility agent facing actuarially fair pricing will fully insure: $\alpha^* = L$, equating wealth across states. The proof is by setting up the FOC. Wealth in no-loss state is $w_1 = w - \pi \alpha$; in loss state $w_2 = w - L + (1 - \pi) \alpha$. Maximise $V = (1-\pi)u(w_1) + \pi u(w_2)$ over $\alpha$: $$\frac{dV}{d\alpha} = -\pi(1-\pi) u'(w_1) + \pi(1-\pi) u'(w_2) = 0,$$ which forces $u'(w_1) = u'(w_2)$, hence $w_1 = w_2$, hence $\alpha = L$.</li>
<li><strong>Why fair pricing is rare.</strong> Insurers face loading costs: admin, capital, commissions, taxes, profit. Empirically these run 20 to 40 percent of expected claims (Cummins and Tennyson 1992). So observed premiums are $q > \pi$, and partial insurance is the rule.</li>
<li><strong>Loading factor.</strong> Define $\lambda = q/\pi - 1$ as the proportional loading. Under partial insurance the agent solves $$\frac{u'(w_1)}{u'(w_2)} = \frac{\pi(1 + \lambda)(1 - q)}{(1-\pi) q} = \frac{(1+\lambda)(1-\pi(1+\lambda))}{(1-\pi)(1+\lambda)} \cdot \frac{1}{(1-\pi)},$$ which simplifies to $u'(w_1) < u'(w_2)$ when $\lambda > 0$, giving $w_1 > w_2$ (partial cover).</li>
<li><strong>Comparative statics.</strong> $d\alpha^*/dL > 0$ (larger losses attract more cover); $d\alpha^*/d\lambda < 0$ (larger loading reduces cover); $d\alpha^*/dr_A > 0$ (more risk-averse agents buy more cover at any positive loading).</li>
</ol>
<p>The fair premium is the welfare benchmark: the social cost of risk is exactly the risk premium $\pi(L) - \pi L \cdot 0 = \tfrac{1}{2} \text{Var}(L) r_A$, the welfare gain a fully insured risk-averse agent enjoys over the uninsured baseline. Government-provided insurance (NHS, unemployment) can be priced fairly because the state does not need a loading for profit; private market loadings reflect rents and costs.</p>
<p><em>Sources</em>: Micro2025.pdf Topic 6 (FHSMicroWk5) Lecture 4; Mas-Colell Ch. 6.E; Varian Ch. 11.6; Gravelle-Rees Ch. 19.5.</p>
""",
        "widget": r"""
<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" id="widget-fair-premium" role="img" aria-label="Fair vs unfair insurance pricing">
  <style>
    #widget-fair-premium text { font-family: Georgia, serif; font-size: 12px; fill: var(--text-primary, #222); }
    #widget-fair-premium .axis { stroke: var(--text-primary, #222); stroke-width: 1.2; fill: none; }
    #widget-fair-premium .diag { stroke: var(--text-secondary, #777); stroke-width: 1; stroke-dasharray: 4 3; }
    #widget-fair-premium .fair { stroke: var(--accent, #884); stroke-width: 1.8; }
    #widget-fair-premium .unfair { stroke: #c44; stroke-width: 1.8; }
    #widget-fair-premium .indiff { stroke: var(--text-primary, #222); stroke-width: 1.4; fill: none; }
    #widget-fair-premium .pt { fill: var(--accent, #884); }
    #widget-fair-premium .pt2 { fill: #c44; }
    #widget-fair-premium .caption { font-size: 11px; fill: var(--text-secondary, #555); }
  </style>
  <line class="axis" x1="60" y1="280" x2="560" y2="280"/>
  <line class="axis" x1="60" y1="280" x2="60" y2="40"/>
  <text x="560" y="295" text-anchor="end">$w_1$</text>
  <text x="50" y="50" text-anchor="end">$w_2$</text>
  <line class="diag" x1="60" y1="280" x2="320" y2="40"/>
  <line class="fair" x1="160" y1="270" x2="460" y2="40"/>
  <line class="unfair" x1="420" y1="270" x2="500" y2="60"/>
  <path class="indiff" d="M 130 220 Q 220 150 320 100 Q 420 70 500 60"/>
  <path class="indiff" d="M 160 260 Q 240 200 350 150 Q 450 120 540 110"/>
  <circle class="pt" cx="420" cy="100" r="5"/>
  <text x="430" y="96" class="caption">endowment</text>
  <circle class="pt" cx="250" cy="105" r="5"/>
  <text x="180" y="100" class="caption">fair price, full ins</text>
  <circle class="pt2" cx="450" cy="113" r="5"/>
  <text x="430" y="135" class="caption" fill="#c44">unfair, partial</text>
</svg>
<p class="caption">Fair budget line (slope $-\pi/(1-\pi)$) hits indifference curve at the 45-degree line; unfair (steeper) budget gives tangency strictly below the line.</p>
""",
        "examples": r"""
<ul>
<li><strong>Lloyd's syndicate pricing.</strong> Catastrophe reinsurance premiums run 200 to 500 percent of expected loss for high layers, reflecting capital costs and tail uncertainty; demand persists because the insurer's risk aversion is even higher than the buyer's.</li>
<li><strong>NHS as social insurance.</strong> Funded by general taxation rather than risk-rated premiums, the NHS implicitly charges close to fair pricing per capita; the state-space prediction (full insurance) matches the universal coverage.</li>
<li><strong>UK annuity market.</strong> Open-market annuity quotes carry roughly 10 percent margin over fair price (Finkelstein and Poterba 2002); the fair-premium benchmark is the lower bound that purely actuarial pricing would deliver.</li>
<li><strong>Evaluation move.</strong> Argue that fair pricing is a useful benchmark but not realistic: every observed market has loadings, so partial insurance is the rule and the full-insurance result is a limit case.</li>
<li><strong>Evaluation move.</strong> Distinguish unfair premiums from optimal premiums: an insurer facing adverse selection may need to load to break even on the pool, so 'unfair' relative to a single agent is 'fair' relative to the equilibrium type mix (Rothschild-Stiglitz 1976).</li>
<li><strong>Limitation.</strong> The fair-premium concept presumes $\pi$ is observable to both parties; under asymmetric information (high vs low risk types), there is no single fair price; see [[Concepts/State-Space Insurance Diagram]] for the geometry.</li>
</ul>
""",
    },

    "allais-paradox": {
        "math": r"""
<p>The <strong>Allais paradox</strong> (Allais 1953) is the most-cited empirical violation of the [[Concepts/von Neumann Morgenstern Axioms]], specifically the independence axiom. The standard pair of choices is over four lotteries:</p>
<ul>
<li>$A$: 1 million pounds with certainty.</li>
<li>$B$: 1 million with probability 0.89; 5 million with probability 0.10; 0 with probability 0.01.</li>
<li>$C$: 1 million with probability 0.11; 0 with probability 0.89.</li>
<li>$D$: 5 million with probability 0.10; 0 with probability 0.90.</li>
</ul>
<p>Most subjects prefer $A$ to $B$ (the 'certainty effect') and $D$ to $C$ (the 'higher expected value' choice). Under expected utility this combination is inconsistent.</p>
<p>Proof. Let $u(0) = 0$, $u(1m) = 1$, $u(5m) = U$. Then $A \succ B$ requires $1 > 0.89 + 0.10 U$, i.e. $U < 1.1$. And $D \succ C$ requires $0.10 U > 0.11$, i.e. $U > 1.1$. Contradiction.</p>
<ol>
<li><strong>Independence violation.</strong> Observe that $A = 0.11 \cdot 1m + 0.89 \cdot 1m$ and $B = 0.10 \cdot 5m + 0.01 \cdot 0 + 0.89 \cdot 1m$. So $A$ and $B$ share an 89 percent chance of $1m$; the difference is in the remaining 11 percent. Similarly $C = 0.11 \cdot 1m + 0.89 \cdot 0$ and $D = 0.10 \cdot 5m + 0.01 \cdot 0 + 0.89 \cdot 0$. Replacing the shared 89 percent of $1m$ (between $A, B$) with 89 percent of $0$ (between $C, D$) flips the preference under independence; in data it does not.</li>
<li><strong>Diagnosis</strong>: subjects over-weight certainty. The 1 percent chance of 0 in lottery $B$ feels much worse than the 90 percent chance of 0 in lottery $D$, because in $B$ it stands between the subject and a sure win.</li>
<li><strong>Resolutions</strong>: prospect theory (Kahneman and Tversky 1979) replaces probabilities with non-linear weights $\omega(p)$ that over-weight small probabilities and under-weight large ones; rank-dependent EU (Quiggin 1982) does the same in a more disciplined way.</li>
</ol>
<p>Standard ripostes from EU defenders: (i) the choices are hypothetical, not incentivised at scale; (ii) framing effects may be at work; (iii) the [[Concepts/Dutch Book Argument]] still applies normatively. But the Allais paradox replicates with real money (Conlisk 1989), so the framing defence is weak.</p>
<p>For the FHS exam, the standard tasks are: (i) write down the four lotteries and prove the contradiction; (ii) explain the violation of independence; (iii) discuss prospect theory as an alternative.</p>
<p><em>Sources</em>: Micro2025.pdf Topic 6 (FHSMicroWk5) Lecture 5; Mas-Colell Ch. 6.B (Example 6.B.4); Allais (1953); Kahneman and Tversky (1979).</p>
""",
        "widget": r"""
<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" id="widget-allais" role="img" aria-label="Allais paradox lottery comparison">
  <style>
    #widget-allais text { font-family: Georgia, serif; font-size: 12px; fill: var(--text-primary, #222); }
    #widget-allais .bar { stroke: var(--text-primary, #222); stroke-width: 0.6; }
    #widget-allais .bg { fill: var(--surface-alt, #f4f1ea); }
    #widget-allais .b1 { fill: var(--accent, #884); }
    #widget-allais .b5 { fill: #c44; }
    #widget-allais .b0 { fill: #444; }
    #widget-allais .caption { font-size: 11px; fill: var(--text-secondary, #555); }
    #widget-allais .label { font-size: 12px; fill: var(--text-primary, #222); font-weight: bold; }
  </style>
  <text x="30" y="60" class="label">$A$:</text>
  <rect class="bar b1" x="80" y="46" width="450" height="22"/>
  <text x="305" y="62" text-anchor="middle" fill="#fff" class="caption">1 million pounds (1.00)</text>
  <text x="30" y="120" class="label">$B$:</text>
  <rect class="bar b5" x="80" y="106" width="45" height="22"/>
  <rect class="bar bg b0" x="125" y="106" width="4.5" height="22"/>
  <rect class="bar b1" x="129.5" y="106" width="400.5" height="22"/>
  <text x="102" y="122" text-anchor="middle" fill="#fff" class="caption">5m (.10)</text>
  <text x="330" y="122" text-anchor="middle" fill="#fff" class="caption">1m (.89), 0 (.01)</text>
  <text x="30" y="200" class="label">$C$:</text>
  <rect class="bar b1" x="80" y="186" width="49.5" height="22"/>
  <rect class="bar b0" x="129.5" y="186" width="400.5" height="22"/>
  <text x="105" y="202" text-anchor="middle" fill="#fff" class="caption">1m (.11)</text>
  <text x="330" y="202" text-anchor="middle" fill="#fff" class="caption">0 (.89)</text>
  <text x="30" y="260" class="label">$D$:</text>
  <rect class="bar b5" x="80" y="246" width="45" height="22"/>
  <rect class="bar b0" x="125" y="246" width="405" height="22"/>
  <text x="102" y="262" text-anchor="middle" fill="#fff" class="caption">5m (.10)</text>
  <text x="327" y="262" text-anchor="middle" fill="#fff" class="caption">0 (.90)</text>
  <text x="300" y="305" text-anchor="middle" class="caption">most pick $A \succ B$ and $D \succ C$, which is inconsistent under expected utility</text>
</svg>
<p class="caption">Lotteries $A, B, C, D$ in the Allais menu; $A$ shares 89 percent of 1m with $B$, replaced by 89 percent of 0 in $C, D$.</p>
""",
        "examples": r"""
<ul>
<li><strong>Lottery design.</strong> National lotteries cap top prizes far below the actuarially optimal; subjects' over-weighting of small probabilities (the prospect-theory counterpart) sustains demand for tickets with negative expected return.</li>
<li><strong>Pension annuity reluctance.</strong> Retirees consistently under-annuitise (Banks and Crawford 2019), preferring lump sums; this looks like a certainty effect on capital sum vs uncertain longevity payments.</li>
<li><strong>Vaccine hesitancy.</strong> Tiny tail risks of vaccine side-effects loom larger than the smoothly distributed disease risk; prospect-theory probability weighting fits the pattern that EU does not.</li>
<li><strong>Evaluation move.</strong> Note Machina's (1982) 'fanning-out' indifference curves on the Marschak-Machina triangle as an EU-relaxation that fits Allais while preserving other properties.</li>
<li><strong>Evaluation move.</strong> Cite Conlisk (1989) for real-money replications and Burke et al. (1996) for cross-cultural replication, undermining the 'hypothetical bias' defence of EU.</li>
<li><strong>Limitation.</strong> Allais shows independence fails on a specific menu but is consistent with EU on most everyday choices; do not over-claim, EU remains a strong first approximation; see [[Concepts/von Neumann Morgenstern Axioms]].</li>
</ul>
""",
    },

    "st-petersburg-paradox": {
        "math": r"""
<p>The <strong>St Petersburg paradox</strong> (Bernoulli 1738) is the historical motivation for expected utility. A fair coin is flipped until the first head; if heads appears on flip $n$, the prize is $2^n$ pounds. The expected prize is</p>
<p>$$E[X] = \sum_{n=1}^\infty \tfrac{1}{2^n} \cdot 2^n = \sum_{n=1}^\infty 1 = \infty.$$</p>
<p>Yet most people would pay only a small finite amount (typically 10 to 25 pounds in experiments) to play. The expected-value criterion is empirically wrong here, and obviously so.</p>
<p>Bernoulli's resolution: replace expected money with expected utility, using a concave $u$. With logarithmic utility $u(x) = \log x$ and initial wealth $w$,</p>
<p>$$E[u(w + X)] = \sum_{n=1}^\infty \tfrac{1}{2^n} \log(w + 2^n).$$</p>
<p>For large $w$ this is approximately $\log w + \sum \tfrac{1}{2^n} \log(1 + 2^n/w) \approx \log w + 1.39$ (the Khinchin-Levy constant for this lottery shifted to log utility), so the certainty equivalent is finite and modest.</p>
<ol>
<li><strong>Why concavity matters</strong>: the doubling prizes are exactly offset by halving probabilities, but the utility of doubling money rises sub-linearly (under concavity), so the series converges.</li>
<li><strong>Karl Menger's reverse</strong>: any unbounded $u$ admits a 'super-St-Petersburg' lottery with infinite expected utility. Resolution: assume $u$ is bounded. CRRA with $\gamma > 1$ has $u$ bounded above, sidestepping the problem.</li>
<li><strong>Empirical price</strong>: laboratory subjects pay 10 to 30 pounds (Cox et al. 2008); under log utility and wealth 50k the formula gives a CE of around 16 pounds, matching the data.</li>
</ol>
<p>The St Petersburg paradox does not show that expected utility fails. It shows that expected money fails, which motivates introducing $u$ in the first place. The historical importance is that this is the cradle of EU: Bernoulli's 1738 paper introduced the entire framework.</p>
<p>Modern variants include the Pasadena game (Nover and Hájek 2004), with a divergent expected utility even under log utility, suggesting bounded $u$ is necessary for a fully general theory.</p>
<p><em>Sources</em>: Micro2025.pdf Topic 6 (FHSMicroWk5) Lecture 5; Mas-Colell Ch. 6.B; Bernoulli (1738); Varian Ch. 11.</p>
""",
        "widget": r"""
<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" id="widget-st-petersburg" role="img" aria-label="St Petersburg payouts and utilities">
  <style>
    #widget-st-petersburg text { font-family: Georgia, serif; font-size: 12px; fill: var(--text-primary, #222); }
    #widget-st-petersburg .axis { stroke: var(--text-primary, #222); stroke-width: 1.2; fill: none; }
    #widget-st-petersburg .bar { fill: var(--accent, #884); stroke: var(--text-primary, #222); stroke-width: 0.5; }
    #widget-st-petersburg .bar2 { fill: #c44; stroke: var(--text-primary, #222); stroke-width: 0.5; }
    #widget-st-petersburg .caption { font-size: 11px; fill: var(--text-secondary, #555); }
    #widget-st-petersburg .legend-box { fill: var(--surface-alt, #f4f1ea); stroke: var(--text-primary, #222); stroke-width: 0.8; }
  </style>
  <line class="axis" x1="60" y1="280" x2="560" y2="280"/>
  <line class="axis" x1="60" y1="280" x2="60" y2="40"/>
  <text x="560" y="295" text-anchor="end">flip $n$ where first head appears</text>
  <text x="50" y="50" text-anchor="end">contribution</text>
  <rect class="bar" x="80" y="60" width="22" height="220"/>
  <rect class="bar" x="125" y="60" width="22" height="220"/>
  <rect class="bar" x="170" y="60" width="22" height="220"/>
  <rect class="bar" x="215" y="60" width="22" height="220"/>
  <rect class="bar" x="260" y="60" width="22" height="220"/>
  <rect class="bar" x="305" y="60" width="22" height="220"/>
  <text x="91" y="295" text-anchor="middle" class="caption">1</text>
  <text x="136" y="295" text-anchor="middle" class="caption">2</text>
  <text x="181" y="295" text-anchor="middle" class="caption">3</text>
  <text x="226" y="295" text-anchor="middle" class="caption">4</text>
  <text x="271" y="295" text-anchor="middle" class="caption">5</text>
  <text x="316" y="295" text-anchor="middle" class="caption">...</text>
  <rect class="bar2" x="380" y="160" width="22" height="120"/>
  <rect class="bar2" x="410" y="200" width="22" height="80"/>
  <rect class="bar2" x="440" y="230" width="22" height="50"/>
  <rect class="bar2" x="470" y="250" width="22" height="30"/>
  <rect class="bar2" x="500" y="262" width="22" height="18"/>
  <rect class="legend-box" x="80" y="50" width="220" height="40" rx="4"/>
  <rect x="92" y="62" width="14" height="14" fill="var(--accent, #884)"/>
  <text x="112" y="74" class="caption">$E[X]$: each term is 1, diverges</text>
  <rect class="legend-box" x="375" y="60" width="170" height="55" rx="4"/>
  <rect x="385" y="72" width="14" height="14" fill="#c44"/>
  <text x="405" y="83" class="caption">$E[\log(w + X)]$: terms</text>
  <text x="405" y="98" class="caption">shrink, sum converges</text>
</svg>
<p class="caption">Each term of $E[X]$ is 1 and the sum is infinite; under log utility the terms decline geometrically and the sum converges to a finite CE.</p>
""",
        "examples": r"""
<ul>
<li><strong>Lottery jackpot caps.</strong> Camelot and competitors cap jackpot rollovers, both for regulatory reasons and because demand would not scale linearly with prize size; people's willingness to pay is governed by utility, not expected value.</li>
<li><strong>Venture capital pricing.</strong> Power-law return distributions (Sanford Bernstein 2017 data) have heavy right tails reminiscent of St Petersburg; VCs price funds at low multiples of expected return because most LPs are risk averse over wealth, not money.</li>
<li><strong>Pascal's mugger.</strong> Pascal-style probability arguments (paying a small sum for an astronomically improbable but astronomically large reward) exploit unbounded $u$; bounded utility (or hyperbolic-discounting of tiny probabilities) defuses them.</li>
<li><strong>Evaluation move.</strong> Distinguish the original paradox (expected money diverges) from Menger's super-St-Petersburg variant (expected utility diverges for unbounded $u$); the latter forces bounded utility, the former just forces concavity.</li>
<li><strong>Evaluation move.</strong> Tie to behavioural anomalies: under prospect theory, small probabilities are over-weighted, which would seem to make people pay more, but the bounded value function caps the willingness to pay.</li>
<li><strong>Limitation.</strong> The paradox is one-shot and finite-population; in repeated play with finite bankroll the relevant criterion is log-optimal (Kelly criterion), not infinite EV; see [[Concepts/Risk Aversion]] for the underlying concept.</li>
</ul>
""",
    },

    "dutch-book-argument": {
        "math": r"""
<p>The <strong>Dutch book argument</strong> (Ramsey 1926, de Finetti 1937) is the standard normative defence of probability axioms and, by extension, expected utility. A 'Dutch book' is a finite sequence of bets that an agent accepts as individually fair (or favourable) at the prices they themselves quote, but that taken together leave the agent sure to lose money in every state.</p>
<p>Formally, suppose an agent quotes a price $p(E)$ for a bet that pays 1 pound if event $E$ occurs and 0 otherwise. Their quoted prices induce a 'probability function' on events. The Dutch book theorem says:</p>
<ol>
<li>If the quoted $p(\cdot)$ violates the probability axioms (non-negativity, normalisation, finite additivity), then there exists a finite portfolio of bets at those prices that delivers a strictly negative payoff in every state.</li>
<li>Conversely, if $p(\cdot)$ obeys the probability axioms, no Dutch book exists: every finite portfolio has at least one state with non-negative payoff.</li>
</ol>
<p>Example: if the agent quotes $p(E) = 0.6$ and $p(E^c) = 0.5$, summing to 1.1. A bookmaker sells the agent a bet on $E$ at 0.6 (paying 1 if $E$) and a bet on $E^c$ at 0.5 (paying 1 if not $E$). The agent pays 1.10 pounds total and receives exactly 1 pound regardless of the state. Sure loss of 0.10 in every state.</p>
<p>The extension to expected utility (Savage 1954) shows that violating the [[Concepts/von Neumann Morgenstern Axioms]] generates a Dutch book in lottery space: an agent with cyclic or non-independent preferences over lotteries can be sold a sequence of lotteries each preferred to its predecessor, ending up worse off than at the start. The result rules out preference cycles as rationally defensible.</p>
<p>Limitations of the argument:</p>
<ol>
<li><strong>Static vs dynamic</strong>: standard Dutch books exploit static violations. Dynamic Dutch books exploit time-inconsistent preferences (hyperbolic discounting), which is a separate matter.</li>
<li><strong>Idealised bookmaker</strong>: presumes the agent will accept every individually-fair bet; in practice agents refuse to engage, especially with strangers.</li>
<li><strong>Probability vs utility</strong>: the original argument concerns subjective probability; for full EU one also needs Savage-style axioms on acts.</li>
</ol>
<p>The Dutch book argument is normatively strong but descriptively unhelpful: it tells us what rational preferences look like, not what observed preferences look like (which is what [[Concepts/Allais Paradox]] is for).</p>
<p><em>Sources</em>: Micro2025.pdf Topic 6 (FHSMicroWk5) Lecture 5; Mas-Colell Ch. 6.F; Ramsey (1926); de Finetti (1937); Savage (1954).</p>
""",
        "widget": r"""
<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" id="widget-dutch-book" role="img" aria-label="Dutch book example">
  <style>
    #widget-dutch-book text { font-family: Georgia, serif; font-size: 12px; fill: var(--text-primary, #222); }
    #widget-dutch-book .box { fill: var(--surface-alt, #f4f1ea); stroke: var(--text-primary, #222); stroke-width: 1.1; }
    #widget-dutch-book .accent { fill: var(--accent, #884); }
    #widget-dutch-book .loss { fill: #c44; }
    #widget-dutch-book .caption { font-size: 11px; fill: var(--text-secondary, #555); }
    #widget-dutch-book .label { font-size: 12px; fill: var(--text-primary, #222); font-weight: bold; }
  </style>
  <text x="60" y="60" class="label">Quoted prices</text>
  <text x="60" y="80" class="caption">$p(E) = 0.60$, $p(E^c) = 0.50$, sum $= 1.10$</text>
  <rect class="box" x="60" y="110" width="220" height="70" rx="6"/>
  <text x="170" y="135" text-anchor="middle" class="label">Bet 1: on $E$</text>
  <text x="170" y="155" text-anchor="middle" class="caption">pay 0.60, get 1 if $E$</text>
  <text x="170" y="172" text-anchor="middle" class="caption">payoff: $E$: $+0.40$, $E^c$: $-0.60$</text>
  <rect class="box" x="320" y="110" width="220" height="70" rx="6"/>
  <text x="430" y="135" text-anchor="middle" class="label">Bet 2: on $E^c$</text>
  <text x="430" y="155" text-anchor="middle" class="caption">pay 0.50, get 1 if not $E$</text>
  <text x="430" y="172" text-anchor="middle" class="caption">payoff: $E$: $-0.50$, $E^c$: $+0.50$</text>
  <rect class="loss" x="160" y="220" width="280" height="60" rx="6"/>
  <text x="300" y="244" text-anchor="middle" fill="#fff" class="label">Both bets together</text>
  <text x="300" y="262" text-anchor="middle" fill="#fff" class="caption">payoff: $E$: $-0.10$, $E^c$: $-0.10$</text>
  <text x="300" y="278" text-anchor="middle" fill="#fff" class="caption">sure loss in every state, Dutch book</text>
</svg>
<p class="caption">Quoted probabilities summing above one let a bookmaker construct a portfolio with guaranteed loss in every state.</p>
""",
        "examples": r"""
<ul>
<li><strong>Sports betting markets.</strong> Bookmakers maintain over-rounds (quoted probabilities sum above one) precisely because the difference funds the spread; a 'Dutch book' is the bookmaker's structural position relative to the bettor.</li>
<li><strong>Prediction market arbitrage.</strong> When PredictIt prices on Yes and No fail to sum to one (commission distortion aside), arbitrageurs construct a riskless trade; the existence of such trades is the formal statement of a Dutch book.</li>
<li><strong>Tax avoidance via cycles.</strong> Closed-loop legal structures (sale and immediate repurchase to crystallise loss) exploit time-inconsistency in tax law that creates a Dutch book against the Exchequer; HMRC's general anti-abuse rule targets these.</li>
<li><strong>Evaluation move.</strong> Argue that the Dutch book argument is normatively decisive but practically irrelevant: real agents refuse the bookmaker rather than satisfy the axioms.</li>
<li><strong>Evaluation move.</strong> Contrast with the [[Concepts/Allais Paradox]] descriptive evidence: Dutch books defend EU normatively, Allais attacks it descriptively, both can be right.</li>
<li><strong>Limitation.</strong> The argument presumes commitment to quoted prices and willingness to accept all small bets; under uncertainty about own preferences (or trust) the conclusion weakens, since refusing is itself rational.</li>
</ul>
""",
    },

    "mean-variance-utility": {
        "math": r"""
<p><strong>Mean-variance utility</strong> represents preferences over risky wealth by a function of the first two moments only:</p>
<p>$$V(w) = E[w] - \tfrac{a}{2} \text{Var}(w),$$</p>
<p>where $a > 0$ is a constant. The agent trades off mean against variance at a constant marginal rate $a/2$.</p>
<p>Mean-variance utility is consistent with EU under either of two conditions (Mas-Colell 6.D.4):</p>
<ol>
<li><strong>CARA plus Gaussian</strong>: if $u(w) = -e^{-aw}/a$ and $w \sim N(\mu, \sigma^2)$, then $E[u(w)] = -e^{-a\mu + a^2 \sigma^2/2}/a$, monotonic in $\mu - \tfrac{a}{2}\sigma^2$. So ranking by mean-variance utility coincides exactly with ranking by EU.</li>
<li><strong>Quadratic utility</strong>: if $u(w) = w - \tfrac{a}{2} w^2$, then $E[u(w)] = E[w] - \tfrac{a}{2}(E[w]^2 + \text{Var}(w))$, which depends only on the first two moments. Drawbacks: $u'$ becomes negative beyond $w = 1/a$, so the agent prefers less wealth at high $w$; risk aversion increases in wealth, opposite of empirical evidence.</li>
</ol>
<p>The Markowitz mean-variance framework underlies modern portfolio theory: with $n$ risky assets with return vector $\mathbf{r} \sim N(\boldsymbol\mu, \Sigma)$ and weights $\mathbf{w}$ summing to 1, the optimal portfolio solves</p>
<p>$$\max_{\mathbf{w}} \mathbf{w}'\boldsymbol\mu - \tfrac{a}{2} \mathbf{w}' \Sigma \mathbf{w},$$</p>
<p>giving $\mathbf{w}^* = (1/a) \Sigma^{-1} \boldsymbol\mu$ (up to a budget constraint). This is the workhorse of portfolio construction.</p>
<p>Limitations:</p>
<ol>
<li><strong>Skewness and tails</strong>: real return distributions are skewed and fat-tailed; mean-variance utility is blind to higher moments, so it under-prices crash risk.</li>
<li><strong>Quadratic flaw</strong>: increasing absolute risk aversion contradicts the empirical decline in $r_A$ with wealth.</li>
<li><strong>Normality requirement</strong>: outside CARA-plus-Gaussian, mean-variance is an approximation, accurate only for small risks (then it coincides with the Arrow-Pratt approximation, see [[Concepts/Risk Premium]]).</li>
</ol>
<p>Mean-variance is the foundation of CAPM, Black-Scholes hedging, and Modern Portfolio Theory; despite its theoretical fragility it remains the industry-standard quantitative framework for portfolio construction.</p>
<p><em>Sources</em>: Micro2025.pdf Topic 6 (FHSMicroWk5) Lecture 6; Mas-Colell Ch. 6.D.4; Markowitz (1952); Varian Ch. 11.</p>
""",
        "widget": r"""
<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" id="widget-mean-variance" role="img" aria-label="Mean-variance indifference curves">
  <style>
    #widget-mean-variance text { font-family: Georgia, serif; font-size: 12px; fill: var(--text-primary, #222); }
    #widget-mean-variance .axis { stroke: var(--text-primary, #222); stroke-width: 1.2; fill: none; }
    #widget-mean-variance .indiff { stroke: var(--accent, #884); stroke-width: 1.6; fill: none; }
    #widget-mean-variance .frontier { stroke: #c44; stroke-width: 2; fill: none; }
    #widget-mean-variance .pt { fill: #c44; }
    #widget-mean-variance .caption { font-size: 11px; fill: var(--text-secondary, #555); }
    #widget-mean-variance .legend-box { fill: var(--surface-alt, #f4f1ea); stroke: var(--text-primary, #222); stroke-width: 0.8; }
  </style>
  <line class="axis" x1="60" y1="280" x2="560" y2="280"/>
  <line class="axis" x1="60" y1="280" x2="60" y2="40"/>
  <text x="560" y="295" text-anchor="end">$\sigma$ (std dev)</text>
  <text x="50" y="50" text-anchor="end">$\mu$ (mean)</text>
  <path class="indiff" d="M 60 230 Q 200 200 540 100"/>
  <path class="indiff" d="M 60 180 Q 200 150 540 50"/>
  <path class="indiff" d="M 60 270 Q 200 240 540 150"/>
  <path class="frontier" d="M 80 250 Q 180 100 540 70"/>
  <circle class="pt" cx="240" cy="155" r="5"/>
  <text x="250" y="150" class="caption" fill="#c44">tangency: optimal portfolio</text>
  <rect class="legend-box" x="80" y="50" width="180" height="50" rx="4"/>
  <line x1="92" y1="68" x2="120" y2="68" stroke="var(--accent, #884)" stroke-width="2"/>
  <text x="128" y="72" class="caption">indifference (slope $a\sigma$)</text>
  <line x1="92" y1="90" x2="120" y2="90" stroke="#c44" stroke-width="2"/>
  <text x="128" y="94" class="caption">efficient frontier</text>
</svg>
<p class="caption">Mean-variance indifference curves rise with risk; tangency with the efficient frontier picks the optimal portfolio. Higher $a$ steepens curves, shifting tangency left.</p>
""",
        "examples": r"""
<ul>
<li><strong>Markowitz portfolio.</strong> A UK pension fund constructs the efficient frontier from the FTSE All-Share, gilts, and corporate bond returns; the tangency portfolio with $a$ around 2 is roughly 60 percent equity, 40 percent bonds.</li>
<li><strong>CAPM.</strong> The Capital Asset Pricing Model takes the market portfolio as the tangency portfolio for the representative investor, giving $E[r_i] - r_f = \beta_i (E[r_m] - r_f)$; an extension of mean-variance utility to equilibrium.</li>
<li><strong>Black-Scholes delta hedging.</strong> Replicating a derivative with a self-financing portfolio is a mean-variance minimisation problem (set variance of replication error to zero), conditional on Gaussian-log returns.</li>
<li><strong>Evaluation move.</strong> Cite the CARA-Gaussian equivalence with EU; this is the strongest theoretical defence, but the Gaussian assumption fails for almost every real return series (Mandelbrot 1963 on fat tails).</li>
<li><strong>Evaluation move.</strong> Highlight that mean-variance ranks portfolios consistently with [[Concepts/Second-Order Stochastic Dominance]] only for the normal family; outside it, two SOSD-ordered portfolios may have different mean-variance rankings (Hadar and Russell 1969).</li>
<li><strong>Limitation.</strong> The quadratic utility case has increasing absolute risk aversion, contradicting cross-sectional evidence; the framework survives only as an approximation, see [[Concepts/Arrow-Pratt RRA]] for the wealth-dependent treatment.</li>
</ul>
""",
    },

    "mean-preserving-spread": {
        "math": r"""
<p>A <strong>mean-preserving spread</strong> (MPS) of a random variable $X$ is a transformation that produces $Y$ with $E[Y] = E[X]$ but more dispersion in a specific sense. Rothschild and Stiglitz (1970) give three equivalent definitions:</p>
<ol>
<li><strong>Integrated CDFs</strong>: $Y$ is an MPS of $X$ iff $E[Y] = E[X]$ and $\int_{-\infty}^t F_Y(s) ds \geq \int_{-\infty}^t F_X(s) ds$ for all $t$, with equality at $+\infty$.</li>
<li><strong>Conditional noise</strong>: there exists a random variable $Z$ on the same probability space as $X$ with $E[Z \mid X] = 0$ and $Y \stackrel{d}{=} X + Z$.</li>
<li><strong>Simple spread</strong>: $Y$ is obtained from $X$ by transferring probability mass from a central point $c$ to two outer points $c - \delta$ and $c + \delta$ (in the right proportions to preserve the mean); any MPS is a finite sequence or limit of simple spreads.</li>
</ol>
<p>The link to [[Concepts/Second-Order Stochastic Dominance]] is direct: $X \succeq_{SOSD} Y$ iff $Y$ is an MPS of $X$. Every risk-averse expected-utility agent prefers $X$ to $Y$.</p>
<p>Proof of conditional-noise $\Rightarrow$ EU inequality: for any concave $u$,</p>
<p>$$E[u(Y)] = E[u(X + Z)] = E[E[u(X+Z) \mid X]] \leq E[u(X + E[Z \mid X])] = E[u(X)]$$</p>
<p>by Jensen's inequality applied conditionally on $X$, using $E[Z \mid X] = 0$.</p>
<p>Example. $X$ takes values 1 and 3 with probability 0.5 each; $E[X] = 2$, $\text{Var}(X) = 1$. $Y$ takes values 0 and 4 with probability 0.5 each; $E[Y] = 2$, $\text{Var}(Y) = 4$. Then $Y$ is an MPS of $X$: probability mass at 1 and 3 has been pushed to 0 and 4, preserving the mean. Every risk-averse agent prefers $X$.</p>
<p>The variance increase is not the defining property; the integrated-CDF condition is. Two distributions can have $\text{Var}(Y) > \text{Var}(X)$ and equal means yet not have $Y$ an MPS of $X$ (the integrated CDFs may cross). The MPS condition is stricter than variance increase.</p>
<p>MPS is used to formalise 'noisier' versus 'cleaner' signals in information economics, the comparative statics of risk in investment problems (Diamond and Stiglitz 1974), and the formalisation of riskier projects in industrial organisation.</p>
<p><em>Sources</em>: Micro2025.pdf Topic 6 (FHSMicroWk5) Lecture 6; Mas-Colell Ch. 6.D.3; Rothschild and Stiglitz (1970, JET); Gravelle-Rees Ch. 19.7.</p>
""",
        "widget": r"""
<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" id="widget-mean-preserving-spread" role="img" aria-label="Mean-preserving spread of a distribution">
  <style>
    #widget-mean-preserving-spread text { font-family: Georgia, serif; font-size: 12px; fill: var(--text-primary, #222); }
    #widget-mean-preserving-spread .axis { stroke: var(--text-primary, #222); stroke-width: 1.2; fill: none; }
    #widget-mean-preserving-spread .bar-x { fill: var(--accent, #884); stroke: var(--text-primary, #222); stroke-width: 0.6; }
    #widget-mean-preserving-spread .bar-y { fill: #c44; stroke: var(--text-primary, #222); stroke-width: 0.6; opacity: 0.7; }
    #widget-mean-preserving-spread .mean { stroke: #444; stroke-width: 1.4; stroke-dasharray: 4 3; }
    #widget-mean-preserving-spread .caption { font-size: 11px; fill: var(--text-secondary, #555); }
    #widget-mean-preserving-spread .legend-box { fill: var(--surface-alt, #f4f1ea); stroke: var(--text-primary, #222); stroke-width: 0.8; }
  </style>
  <line class="axis" x1="60" y1="280" x2="560" y2="280"/>
  <line class="axis" x1="60" y1="280" x2="60" y2="40"/>
  <text x="560" y="295" text-anchor="end">value</text>
  <text x="50" y="50" text-anchor="end">probability</text>
  <rect class="bar-x" x="180" y="160" width="40" height="120"/>
  <rect class="bar-x" x="340" y="160" width="40" height="120"/>
  <rect class="bar-y" x="100" y="160" width="40" height="120"/>
  <rect class="bar-y" x="420" y="160" width="40" height="120"/>
  <line class="mean" x1="280" y1="280" x2="280" y2="60"/>
  <text x="285" y="70" class="caption">mean $= 2$</text>
  <text x="200" y="295" text-anchor="middle" class="caption">1</text>
  <text x="360" y="295" text-anchor="middle" class="caption">3</text>
  <text x="120" y="295" text-anchor="middle" class="caption">0</text>
  <text x="440" y="295" text-anchor="middle" class="caption">4</text>
  <rect class="legend-box" x="80" y="50" width="180" height="50" rx="4"/>
  <rect x="92" y="60" width="16" height="14" fill="var(--accent, #884)"/>
  <text x="116" y="72" class="caption">$X$ on $\{1, 3\}$</text>
  <rect x="92" y="82" width="16" height="14" fill="#c44" opacity="0.7"/>
  <text x="116" y="94" class="caption">$Y$ on $\{0, 4\}$, MPS</text>
</svg>
<p class="caption">$Y$ is a mean-preserving spread of $X$: probability mass at 1 and 3 has shifted outward to 0 and 4, mean unchanged.</p>
""",
        "examples": r"""
<ul>
<li><strong>Noisy signal experiments.</strong> An R&D project producing payoff $X + Z$ where $Z$ is white noise is an MPS of $X$; every risk-averse manager prefers the project with less noise, all else equal (Diamond and Stiglitz 1974).</li>
<li><strong>Income uncertainty and consumption.</strong> Permanent-income consumers facing an MPS of their income stream save more for precautionary reasons (Carroll 1997); the MPS captures 'noisier income' precisely without assuming variance is sufficient.</li>
<li><strong>Stress testing.</strong> Bank of England stress scenarios apply mean-preserving spreads to GDP, unemployment, and house price paths; capital requirements respond to the spread, not just the mean.</li>
<li><strong>Evaluation move.</strong> Distinguish MPS from increased variance: variance is necessary but not sufficient for MPS; two distributions with equal mean and one higher variance need not be MPS-related (CDFs may cross).</li>
<li><strong>Evaluation move.</strong> Tie MPS to information economics: a noisier signal in a Bayesian update is the posterior-mean-preserving spread of a cleaner signal; standard tool in mechanism design (Blackwell 1953).</li>
<li><strong>Limitation.</strong> The MPS concept presumes a complete CDF; for ambiguous distributions (Knightian uncertainty) the framework breaks down; see [[Concepts/Second-Order Stochastic Dominance]] for the SOSD equivalence.</li>
</ul>
""",
    },

    "akerlof-lemons-market": {
        "math": r"""<p><strong>Definition.</strong> Akerlof's lemons market is the canonical adverse-selection environment: sellers privately observe their unit's quality $v \in [\underline{v}, \bar{v}]$ with distribution $F(v)$, buyers see only the asking price $p$. Buyer willingness to pay is $\beta \cdot E[v \mid \text{seller offers at } p]$ with $\beta > 1$ (gains from trade), seller reservation is $v$.</p>
<p><strong>Unravelling derivation.</strong> A seller of type $v$ offers iff $p \ge v$, so the conditional mean of sellers at price $p$ is</p>
<p>$$E[v \mid v \le p] = \frac{\int_{\underline{v}}^{p} v \, dF(v)}{F(p)}.$$</p>
<p>Buyer rationality requires $p = \beta \cdot E[v \mid v \le p]$. The unravelling condition is</p>
<p>$$\beta \cdot E[v \mid v \le p] < p \quad \text{for all } p > \underline{v},$$</p>
<p>which holds when the gain $\beta$ is not large enough to offset the selection effect. With $v \sim U[0,1]$ and $\beta < 2$, the only fixed point is $p = \underline{v} = 0$: no trade occurs.</p>
<ol>
<li>The market failure is informational, not preference-based: at the symmetric-information benchmark every $v$ trades.</li>
<li>Existence of trade requires either $\beta$ above a threshold, a discrete type structure with a sufficiently low-quality bottom, or supplementary instruments (warranties, reimbursement, signals).</li>
<li>The Akerlof result is the foundational example of asymmetric information breaking the first welfare theorem.</li>
</ol>
<p><em>Sources: Micro2025.pdf Topic 7 Lectures (FHSMicroWk6), Akerlof 1970 QJE, Mas-Colell Ch. 13.B, Bolton-Dewatripont Ch. 2.</em></p>""",
        "widget": r"""<svg id="widget-akerlof-lemons-market" viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="background:#fff;font-family:sans-serif;">
<line x1="60" y1="270" x2="560" y2="270" stroke="#333" stroke-width="1.5"/>
<line x1="60" y1="270" x2="60" y2="40" stroke="#333" stroke-width="1.5"/>
<text x="300" y="305" text-anchor="middle" font-size="13">price $p$</text>
<text x="20" y="155" font-size="13" transform="rotate(-90 20 155)">value</text>
<line x1="60" y1="270" x2="560" y2="40" stroke="#888" stroke-dasharray="4 3"/>
<text x="540" y="55" font-size="11" fill="#666">45 line, $p$</text>
<path d="M 60 270 Q 200 230 350 175 T 560 100" stroke="#c0392b" stroke-width="2.5" fill="none"/>
<text x="370" y="195" font-size="11" fill="#c0392b">$\beta E[v|v \le p]$</text>
<circle cx="60" cy="270" r="5" fill="#2c3e50"/>
<text x="70" y="285" font-size="11">only fixed point: no trade</text>
<text x="300" y="25" text-anchor="middle" font-size="13" font-weight="bold">Akerlof unravelling</text>
</svg>
<p style="font-size:12px;color:#555;">The buyer's break-even curve $\beta E[v \mid v \le p]$ lies strictly below the 45 line, so the unique intersection is at the lowest type and the market collapses.</p>""",
        "examples": r"""<ul>
<li><strong>Used cars (Akerlof 1970).</strong> The original example: dealers know which cars are lemons, buyers do not, the average car offered at any price is worse than the average car of that nominal quality, and the market thins to the bottom.</li>
<li><strong>Health insurance pools.</strong> Without mandates, healthy customers exit as premiums rise to cover the sicker remaining pool, the death spiral that the ACA individual mandate was designed to prevent.</li>
<li><strong>Annuities market.</strong> Long-lived individuals self-select into annuities, raising prices, driving out the average lived, an empirically documented selection effect (Finkelstein and Poterba 2004).</li>
<li><strong>Essay move (Doornik likes).</strong> Distinguish the static lemons problem from the dynamic version: with repeat purchases, reputations partially substitute for direct quality observation, so unravelling is less severe in markets with strong brands.</li>
<li><strong>Evaluation move.</strong> Akerlof's prediction of no trade is extreme: real used-car markets are large, suggesting instruments like warranties, certification, and lemon laws restore much of the surplus. The model identifies a mechanism, not a magnitude.</li>
<li><strong>Limitation.</strong> Assumes buyers cannot improve their information at any cost. CarFax, mechanic inspections, and brand reputations all relax this. See [[Concepts/Asymmetric Information]].</li>
</ul>""",
    },
    "full-unravelling": {
        "math": r"""<p><strong>Definition.</strong> Full unravelling is the limiting case of adverse selection in which the only equilibrium has the lowest type trading (or no trade at all). It arises when, for every candidate pooling price, the buyer's conditional valuation falls strictly below that price.</p>
<p><strong>Derivation.</strong> Consider types $\theta \in [0, 1]$ with seller reservation $\theta$ and buyer value $v(\theta)$, $v(\theta) > \theta$ for all $\theta$ (gains from trade everywhere). At pooled price $p$, sellers with $\theta \le p$ offer. The break-even price is</p>
<p>$$p^* = E[v(\theta) \mid \theta \le p^*].$$</p>
<p>If $E[v(\theta) \mid \theta \le p] < p$ for all $p > 0$, iterating the deletion of types whose reservation exceeds the conditional mean shrinks the active set to $\{0\}$. The argument is essentially the elimination of dominated strategies applied to participation.</p>
<ol>
<li>Sufficient condition (Akerlof): $v(\theta) = \beta \theta$ with $\beta < 2$ and $\theta \sim U[0,1]$ yields $E[\beta \theta \mid \theta \le p] = \beta p / 2 < p$.</li>
<li>The unravelling logic is recursive: at each round, the top type exits, the average falls, the price falls, and the new top exits.</li>
<li>Full unravelling is to be contrasted with [[Concepts/Partial Unravelling]], where only types above some cutoff $\theta^*$ exit and a continuing market exists below.</li>
</ol>
<p><strong>Comparative statics.</strong> Raising $\beta$ (gains from trade) shifts the conditional-mean curve up, restoring partial or full participation once $\beta$ exceeds the unravelling threshold. Reducing the variance of $\theta$ also weakens unravelling, since the conditional mean tracks the price more closely.</p>
<p><em>Sources: Micro2025.pdf Topic 7 Lectures (FHSMicroWk6), Akerlof 1970, Mas-Colell Ch. 13.B, Bolton-Dewatripont 2.2.</em></p>""",
        "widget": r"""<svg id="widget-full-unravelling" viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="background:#fff;font-family:sans-serif;">
<line x1="60" y1="270" x2="560" y2="270" stroke="#333" stroke-width="1.5"/>
<line x1="60" y1="270" x2="60" y2="40" stroke="#333" stroke-width="1.5"/>
<text x="300" y="305" text-anchor="middle" font-size="13">price $p$</text>
<text x="20" y="155" font-size="13" transform="rotate(-90 20 155)">conditional mean</text>
<line x1="60" y1="270" x2="500" y2="60" stroke="#888" stroke-dasharray="4 3"/>
<text x="510" y="65" font-size="11" fill="#666">$p$</text>
<line x1="60" y1="270" x2="500" y2="165" stroke="#c0392b" stroke-width="2.5"/>
<text x="510" y="170" font-size="11" fill="#c0392b">$\beta E[\theta|\theta \le p]$, $\beta=1.4$</text>
<circle cx="60" cy="270" r="5" fill="#2c3e50"/>
<text x="80" y="260" font-size="11">unique eqm at $p=0$</text>
<text x="300" y="25" text-anchor="middle" font-size="13" font-weight="bold">Full unravelling: gap closes only at zero</text>
</svg>
<p style="font-size:12px;color:#555;">When the buyer's break-even line is strictly flatter than the 45 line, iteration collapses the market to the bottom type.</p>""",
        "examples": r"""<ul>
<li><strong>Pre-Obamacare individual health market.</strong> Without mandates, premiums chased the worsening risk pool upward, healthier enrollees exited, and several state markets approached full unravelling before the 2014 reforms.</li>
<li><strong>Adverse selection in life annuities.</strong> Voluntary annuity markets in the UK historically priced near full unravelling on mortality, with the longest-lived selecting in (Finkelstein-Poterba 2004).</li>
<li><strong>Essay move.</strong> Distinguish full unravelling (degenerate) from partial unravelling (cutoff equilibrium). Doornik rewards students who identify which condition on $\beta$ or the type density triggers each case.</li>
<li><strong>Essay move.</strong> Discuss policy correctives: mandatory participation (insurance), public certification (CarFax), warranties and reimbursement. Each restores trade by relaxing the informational asymmetry rather than the underlying preferences.</li>
<li><strong>Limitation.</strong> The unravelling result assumes a single price posted to all types. Menu mechanisms (Rothschild-Stiglitz screening) can support partial separation even when pooling unravels. See [[Concepts/Rothschild-Stiglitz Screening]].</li>
</ul>""",
    },
    "spence-signalling": {
        "math": r"""<p><strong>Definition.</strong> Spence's job-market signalling model: workers have type $\theta \in \{\theta_L, \theta_H\}$ with $\theta_H > \theta_L > 0$, prior $\Pr(\theta_H) = \lambda$. Workers choose education $e \ge 0$ before entering a competitive labour market. Education cost is $c(e, \theta) = e / \theta$ (single crossing). Firms observe $e$ but not $\theta$ and pay competitive wage $w(e) = E[\theta \mid e]$.</p>
<p><strong>Separating equilibrium derivation.</strong> In a separating equilibrium, $e_L^* = 0$ and $e_H^* = e^*$. Incentive compatibility for $L$:</p>
<p>$$\theta_L - 0 \ge \theta_H - e^* / \theta_L \quad \Longrightarrow \quad e^* \ge \theta_L (\theta_H - \theta_L).$$</p>
<p>Incentive compatibility for $H$: $\theta_H - e^* / \theta_H \ge \theta_L$, i.e. $e^* \le \theta_H (\theta_H - \theta_L)$. The Riley (least-cost) separating equilibrium picks the lower bound:</p>
<p>$$e^*_{\text{Riley}} = \theta_L (\theta_H - \theta_L).$$</p>
<ol>
<li>Education is purely informational here: $\theta$ is exogenous productivity, not augmented by $e$.</li>
<li>Separation is socially wasteful because $H$ burns $e^* / \theta_H$ of utility purely to be distinguished.</li>
<li>Pooling equilibria at any $e_p \in [0, \theta_L(\theta_H - \theta_L)]$ also exist with wage $w_p = \lambda \theta_H + (1-\lambda)\theta_L$; the [[Concepts/Intuitive Criterion]] eliminates them.</li>
<li>Single crossing $c_{e\theta} = -1/\theta^2 < 0$ ensures $H$'s indifference curves are flatter in $(e, w)$ space, the geometric basis for separation.</li>
</ol>
<p><em>Sources: Micro2025.pdf Topic 7 Lectures (FHSMicroWk6), Spence 1973 QJE, Mas-Colell Ch. 13.C, Bolton-Dewatripont Ch. 3.</em></p>""",
        "widget": r"""<svg id="widget-spence-signalling" viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="background:#fff;font-family:sans-serif;">
<line x1="60" y1="270" x2="560" y2="270" stroke="#333" stroke-width="1.5"/>
<line x1="60" y1="270" x2="60" y2="40" stroke="#333" stroke-width="1.5"/>
<text x="300" y="305" text-anchor="middle" font-size="13">education $e$</text>
<text x="20" y="155" font-size="13" transform="rotate(-90 20 155)">wage $w$</text>
<line x1="60" y1="220" x2="560" y2="220" stroke="#666" stroke-dasharray="3 3"/>
<text x="40" y="225" font-size="11" fill="#666">$\theta_L$</text>
<line x1="60" y1="100" x2="560" y2="100" stroke="#666" stroke-dasharray="3 3"/>
<text x="40" y="105" font-size="11" fill="#666">$\theta_H$</text>
<path d="M 60 220 Q 200 200 280 165 T 500 60" stroke="#3498db" stroke-width="2" fill="none"/>
<text x="430" y="85" font-size="11" fill="#3498db">L IC, slope $1/\theta_L$</text>
<path d="M 60 220 Q 250 215 350 195 T 540 130" stroke="#c0392b" stroke-width="2" fill="none"/>
<text x="430" y="155" font-size="11" fill="#c0392b">H IC, slope $1/\theta_H$</text>
<circle cx="60" cy="220" r="5" fill="#3498db"/>
<text x="68" y="240" font-size="11">$e_L=0$</text>
<circle cx="280" cy="100" r="5" fill="#c0392b"/>
<text x="240" y="90" font-size="11">$e^* = \theta_L(\theta_H-\theta_L)$</text>
<text x="300" y="25" text-anchor="middle" font-size="13" font-weight="bold">Spence separating equilibrium</text>
</svg>
<p style="font-size:12px;color:#555;">Single crossing puts L's indifference curve through $(0,\theta_L)$ above H's. The Riley point is where L is just indifferent.</p>""",
        "examples": r"""<ul>
<li><strong>Education credentials.</strong> The empirical sheepskin effect (large wage jumps at degree completion rather than smooth in years of study) is consistent with signalling over pure human-capital accumulation.</li>
<li><strong>MBA programmes.</strong> Two-year top MBAs cost 200k plus foregone income; the signal value is plausibly large relative to the marginal management content, especially for career switchers.</li>
<li><strong>Peacock tails.</strong> Zahavi's handicap principle in biology is mathematically a Spence model: only fit peacocks can afford the cost of large tails. See [[Concepts/Conspicuous Consumption]].</li>
<li><strong>Essay move (Doornik likes).</strong> Compare signalling against human-capital and screening interpretations of the education wage premium. Empirically, separating these is hard; instrumental variables on compulsory schooling laws (Card 1999) suggest both forces operate.</li>
<li><strong>Evaluation move.</strong> Welfare: in the pure signalling model education is socially wasteful, so a tax on $e$ could improve outcomes if the planner could identify it. But education has joint productivity content, complicating the policy lesson.</li>
<li><strong>Limitation.</strong> The model assumes single-shot interaction with anonymous firms. In repeated employment, on-the-job performance gradually reveals $\theta$, reducing reliance on the entry signal.</li>
</ul>""",
    },
    "single-crossing-property": {
        "math": r"""<p><strong>Definition.</strong> The single crossing property (SCP) states that the indifference curves of any two types in $(s, w)$ space (signal, reward) cross at most once. Formally, for utility $U(s, w, \theta)$ with $U_w > 0$ and $U_s < 0$ (signal costly), SCP holds iff the marginal rate of substitution</p>
<p>$$\text{MRS}(s, w, \theta) = -\frac{U_s(s, w, \theta)}{U_w(s, w, \theta)}$$</p>
<p>is monotone in $\theta$. Equivalently, $\partial^2 U / \partial s \partial \theta$ has constant sign.</p>
<p><strong>Why SCP matters.</strong> Order types by $\theta$ so that high types have the lower MRS. Then any contract $(s, w)$ that gives $L$ exactly its outside option lies strictly below $H$'s indifference curve through the same point, so $H$ can be offered a higher-signal higher-wage bundle without attracting $L$. This is the geometric content of incentive compatibility in signalling and screening.</p>
<ol>
<li>Spence model: $U = w - s / \theta$, $\text{MRS} = 1/\theta$ is monotone in $\theta$, SCP holds.</li>
<li>Mirrlees taxation: SCP in skills $\theta$ ensures the optimal income schedule is monotone.</li>
<li>R-S insurance: SCP in loss probability $\pi$ ensures the high-risk type prefers more insurance at any premium, which makes the separating menu implementable.</li>
<li>SCP plus continuity is sufficient for the existence of separating equilibria; without SCP, separating menus can fail to be incentive compatible globally.</li>
</ol>
<p><strong>Spence-Mirrlees condition.</strong> When the type space is continuous, SCP is the Spence-Mirrlees condition $\partial \text{MRS} / \partial \theta < 0$, the canonical regularity assumption in mechanism design.</p>
<p><em>Sources: Micro2025.pdf Topic 7 Lectures (FHSMicroWk6), Mas-Colell Ch. 13.C and Ch. 14, Bolton-Dewatripont Ch. 2.3 and 3.2, Milgrom-Shannon 1994.</em></p>""",
        "widget": r"""<svg id="widget-single-crossing-property" viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="background:#fff;font-family:sans-serif;">
<line x1="60" y1="270" x2="560" y2="270" stroke="#333" stroke-width="1.5"/>
<line x1="60" y1="270" x2="60" y2="40" stroke="#333" stroke-width="1.5"/>
<text x="300" y="305" text-anchor="middle" font-size="13">signal $s$</text>
<text x="20" y="155" font-size="13" transform="rotate(-90 20 155)">wage $w$</text>
<line x1="60" y1="240" x2="540" y2="60" stroke="#3498db" stroke-width="2"/>
<text x="450" y="100" font-size="11" fill="#3498db">L: steep, MRS$=1/\theta_L$</text>
<line x1="60" y1="240" x2="540" y2="160" stroke="#c0392b" stroke-width="2"/>
<text x="450" y="180" font-size="11" fill="#c0392b">H: flat, MRS$=1/\theta_H$</text>
<circle cx="60" cy="240" r="5" fill="#2c3e50"/>
<text x="68" y="258" font-size="11">single crossing point</text>
<text x="300" y="25" text-anchor="middle" font-size="13" font-weight="bold">Single crossing in signalling</text>
</svg>
<p style="font-size:12px;color:#555;">$H$'s indifference curve through any point is flatter than $L$'s, so the curves cross only once. This is the geometric basis for separating contracts.</p>""",
        "examples": r"""<ul>
<li><strong>Education signalling.</strong> A more able worker has lower marginal cost of education effort, so their indifference curve in $(e, w)$ space is flatter, the textbook Spence setup.</li>
<li><strong>Optimal income tax (Mirrlees).</strong> Higher-skilled workers have lower disutility of labour at any income, so their indifference curves in $(y, c)$ space are flatter, single crossing is the standing assumption.</li>
<li><strong>Nonlinear pricing.</strong> High-demand consumers have a lower MRS of price for quantity, justifying quantity discounts as a screening device.</li>
<li><strong>Essay move (Doornik likes).</strong> Make SCP explicit when deriving any separating equilibrium. Show the implied ordering of MRS and check whether the model's parameterisation actually satisfies it: many candidate setups fail SCP and admit no separating equilibrium.</li>
<li><strong>Essay move.</strong> Connect SCP to the Spence-Mirrlees condition in mechanism design: a single, transparent regularity assumption with wide reach across signalling, screening, and taxation. See [[Concepts/Separating vs Pooling Equilibrium]].</li>
<li><strong>Limitation.</strong> Many real environments have multidimensional types (ability and ambition; risk and risk aversion), where SCP is a strong restriction and the analysis becomes much harder.</li>
</ul>""",
    },
    "separating-vs-pooling": {
        "math": r"""<p><strong>Definitions.</strong> In a signalling game with types $\theta \in \Theta$ and signals $s$, a strategy profile is <em>separating</em> if the signal map $s(\theta)$ is injective on the support of types, so the receiver infers $\theta$ from $s$. It is <em>pooling</em> if $s(\theta)$ is constant. <em>Semi-separating</em> (or partially pooling) profiles mix the two.</p>
<p><strong>Equilibrium characterisation in Spence.</strong> Types $\{\theta_L, \theta_H\}$, education cost $s/\theta$, competitive wage $w(s) = E[\theta \mid s]$.</p>
<ol>
<li><strong>Separating PBE.</strong> $s_L = 0$, $s_H \in [\theta_L(\theta_H - \theta_L), \theta_H(\theta_H - \theta_L)]$, $w(s_L) = \theta_L$, $w(s_H) = \theta_H$. Off-path beliefs assign $\theta_L$ to any unexpected $s$.</li>
<li><strong>Pooling PBE.</strong> All types choose the same $s_p$. Wage $w(s_p) = \lambda \theta_H + (1-\lambda)\theta_L \equiv \bar{\theta}$. Sustained by beliefs that any deviation $s \ne s_p$ comes from $L$.</li>
</ol>
<p><strong>Welfare comparison.</strong> Pooling at $s_p = 0$ Pareto-dominates separating when $\bar{\theta}$ is close to $\theta_H$ (i.e., $\lambda$ near 1): $L$ gains, $H$ loses by less than the saved signalling cost. Separating dominates when $\lambda$ is low (so pooled wage is far below $\theta_H$).</p>
<p><strong>Multiplicity and refinement.</strong> The signalling game has a continuum of equilibria. The [[Concepts/Intuitive Criterion]] eliminates pooling (whenever $H$ has a credible deviation to a separating signal) and selects the [[Concepts/Riley Outcome]] within the separating set.</p>
<p><em>Sources: Micro2025.pdf Topic 7 Lectures (FHSMicroWk6), Spence 1973, Cho-Kreps 1987 QJE, Mas-Colell Ch. 13.C, Bolton-Dewatripont Ch. 3.</em></p>""",
        "widget": r"""<svg id="widget-separating-vs-pooling" viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="background:#fff;font-family:sans-serif;">
<line x1="60" y1="270" x2="560" y2="270" stroke="#333" stroke-width="1.5"/>
<line x1="60" y1="270" x2="60" y2="40" stroke="#333" stroke-width="1.5"/>
<text x="300" y="305" text-anchor="middle" font-size="13">signal $s$</text>
<text x="20" y="155" font-size="13" transform="rotate(-90 20 155)">wage $w$</text>
<line x1="60" y1="220" x2="560" y2="220" stroke="#888" stroke-dasharray="3 3"/>
<text x="35" y="225" font-size="11">$\theta_L$</text>
<line x1="60" y1="160" x2="560" y2="160" stroke="#888" stroke-dasharray="3 3"/>
<text x="35" y="165" font-size="11">$\bar\theta$</text>
<line x1="60" y1="100" x2="560" y2="100" stroke="#888" stroke-dasharray="3 3"/>
<text x="35" y="105" font-size="11">$\theta_H$</text>
<circle cx="60" cy="220" r="6" fill="#3498db"/>
<text x="70" y="240" font-size="11">separating: $L$ at $(0,\theta_L)$</text>
<circle cx="260" cy="100" r="6" fill="#c0392b"/>
<text x="180" y="90" font-size="11">separating: $H$ at $(e^*,\theta_H)$</text>
<circle cx="160" cy="160" r="6" fill="#27ae60"/>
<text x="170" y="155" font-size="11">pooling: both at $(s_p, \bar\theta)$</text>
<text x="300" y="25" text-anchor="middle" font-size="13" font-weight="bold">Separating vs pooling equilibria</text>
</svg>
<p style="font-size:12px;color:#555;">Both equilibrium types coexist; refinements select among them.</p>""",
        "examples": r"""<ul>
<li><strong>Hiring without degree requirement.</strong> If firms drop degree requirements, the labour market moves from a separating to a pooling equilibrium: average productivity drops, high-types are worse off, low-types better off.</li>
<li><strong>Health insurance group rating.</strong> Group-rated employer health plans pool risks within a firm. They are a deliberate institutional move toward pooling, sustainable because employment is exogenous to health risk.</li>
<li><strong>Used-car certification.</strong> Certified pre-owned programmes create a separating equilibrium with two segments (certified, sold) rather than a pooled market.</li>
<li><strong>Essay move (Doornik likes).</strong> Always state both equilibrium types and their off-path beliefs explicitly. Distinguish equilibrium multiplicity (a feature of the game) from refinement-selected outcomes.</li>
<li><strong>Essay move.</strong> Compare welfare across equilibria: pooling is not always inferior, and the welfare ordering depends on the type prior $\lambda$. See [[Concepts/Pooling Equilibrium]].</li>
<li><strong>Limitation.</strong> The static signalling game ignores reputation, repeated interaction, and partial information acquisition. Realistic markets often display semi-separating outcomes that neither extreme captures.</li>
</ul>""",
    },
    "intuitive-criterion": {
        "math": r"""<p><strong>Definition.</strong> The intuitive criterion (Cho and Kreps 1987) is an equilibrium refinement for signalling games. Given a putative PBE with equilibrium payoffs $U^*(\theta)$, define for each off-path signal $s$ the set</p>
<p>$$D(s) = \{\theta : U^*(\theta) > \max_{a} U(s, a, \theta)\},$$</p>
<p>the types for whom $s$ is equilibrium-dominated (no receiver response can make $s$ better than $U^*(\theta)$). The intuitive criterion requires the receiver, on observing $s$, to place zero probability on $\theta \in D(s)$ when forming beliefs.</p>
<p><strong>Application to Spence.</strong> Consider a pooling PBE at $s_p < e^*_{\text{Riley}} = \theta_L(\theta_H - \theta_L)$ with wage $\bar{\theta}$. Take $s' \in (s_p, e^*_{\text{Riley}})$. For $L$: $U_L^* = \bar{\theta} - s_p / \theta_L$ versus max attainable at $s'$ is $\theta_H - s'/\theta_L$. The inequality $\bar{\theta} - s_p/\theta_L > \theta_H - s'/\theta_L$ is equivalent to $s' > s_p + \theta_L(\theta_H - \bar{\theta})$. For $s'$ slightly above this threshold but below the Riley level, $L$ is equilibrium-dominated and $H$ is not. The receiver must then believe $\theta_H$, but $H$ then strictly prefers $s'$ to $s_p$, breaking the pooling equilibrium.</p>
<ol>
<li>The intuitive criterion eliminates all pooling equilibria in the two-type Spence model.</li>
<li>It selects the least-cost (Riley) separating equilibrium uniquely.</li>
<li>With three or more types, the intuitive criterion can leave multiple equilibria. Stronger refinements (D1, divinity) are sometimes needed.</li>
<li>The logic is: forward induction over off-path beliefs.</li>
</ol>
<p><em>Sources: Micro2025.pdf Topic 7 Lectures (FHSMicroWk6), Cho-Kreps 1987 QJE, Mas-Colell Ch. 13.C, Bolton-Dewatripont Ch. 3.4.</em></p>""",
        "widget": r"""<svg id="widget-intuitive-criterion" viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="background:#fff;font-family:sans-serif;">
<line x1="60" y1="270" x2="560" y2="270" stroke="#333" stroke-width="1.5"/>
<line x1="60" y1="270" x2="60" y2="40" stroke="#333" stroke-width="1.5"/>
<text x="300" y="305" text-anchor="middle" font-size="13">signal $s$</text>
<text x="20" y="155" font-size="13" transform="rotate(-90 20 155)">wage $w$</text>
<line x1="60" y1="160" x2="560" y2="160" stroke="#888" stroke-dasharray="3 3"/>
<text x="35" y="165" font-size="11">$\bar\theta$</text>
<line x1="60" y1="100" x2="560" y2="100" stroke="#888" stroke-dasharray="3 3"/>
<text x="35" y="105" font-size="11">$\theta_H$</text>
<circle cx="180" cy="160" r="6" fill="#27ae60"/>
<text x="120" y="180" font-size="11">pooling $s_p$</text>
<path d="M 180 160 L 360 100" stroke="#c0392b" stroke-width="2" stroke-dasharray="5 3"/>
<text x="280" y="135" font-size="11" fill="#c0392b">$H$'s profitable deviation $s'$</text>
<rect x="200" y="60" width="120" height="100" fill="#c0392b" fill-opacity="0.1" stroke="#c0392b" stroke-dasharray="3 2"/>
<text x="260" y="55" text-anchor="middle" font-size="11" fill="#c0392b">credible-$H$ region</text>
<text x="300" y="25" text-anchor="middle" font-size="13" font-weight="bold">Intuitive criterion breaks pooling</text>
</svg>
<p style="font-size:12px;color:#555;">In the shaded region, deviation is dominated for $L$ but not for $H$; rational beliefs assign $\theta_H$, and $H$ then prefers $s'$.</p>""",
        "examples": r"""<ul>
<li><strong>Education signalling.</strong> Predicts the unique selected outcome is the least-cost separating equilibrium, the Riley point, not any of the multiple pooling equilibria.</li>
<li><strong>Limit pricing (Milgrom-Roberts 1982).</strong> Incumbent firms signal low cost via low prices. The intuitive criterion picks the separating equilibrium where only low-cost incumbents limit price.</li>
<li><strong>Corporate finance.</strong> Myers-Majluf signalling through underpricing of equity; the intuitive criterion is used to argue that pooling outcomes are not robust.</li>
<li><strong>Essay move (Doornik likes).</strong> Spell out the equilibrium-dominance test concretely: identify the off-path signal and the types for whom it cannot improve on the equilibrium payoff. Sloppy invocation of the criterion is a common essay weakness.</li>
<li><strong>Essay move.</strong> Distinguish the intuitive criterion from stronger refinements (D1) which restrict beliefs further. State which one is sufficient for your selection claim.</li>
<li><strong>Limitation.</strong> The criterion is a particular forward-induction story among many. It is not derived from primitive rationality axioms, and its predictions can change discontinuously with the type space. See [[Concepts/Riley Outcome]].</li>
</ul>""",
    },
    "rothschild-stiglitz-screening": {
        "math": r"""<p><strong>Setup.</strong> Two risk types, $H$ (loss probability $\pi_H$) and $L$ (loss probability $\pi_L$), with $\pi_H > \pi_L$. Population shares $\lambda$ and $1-\lambda$. Initial wealth $W$, loss $D$. A contract is a pair $(p, q)$, premium $p$ and payout $q$ in the loss state. State-contingent consumption $(c_1, c_2) = (W - p, W - D + q - p)$. Insurers are risk-neutral and competitive.</p>
<p><strong>Separating equilibrium.</strong> R-S show that if an equilibrium exists, it must be separating with:</p>
<ol>
<li>$H$ gets full insurance at fair premium: $c_{1H} = c_{2H} = W - \pi_H D$.</li>
<li>$L$ gets partial coverage on $L$'s fair-odds line, set so that $H$ is exactly indifferent between the two contracts (binding IC):</li>
</ol>
<p>$$U_H(c_{1L}, c_{2L}) = U_H(c_{1H}, c_{2H}).$$</p>
<p>The $L$ contract is strictly below $L$'s first-best (full insurance at $L$'s fair premium), so $L$ bears the cost of asymmetric information.</p>
<p><strong>Existence problem.</strong> The candidate separating menu is broken by any pooling contract that lies above $L$'s indifference curve at $L$'s contract and above the pooled fair-odds line. This happens precisely when $\lambda$ is small (mostly low-risks). When this holds, no PBE exists in pure strategies.</p>
<p><strong>Key contrast with Spence.</strong> In R-S, no pooling equilibrium can survive because competitive insurers can cream-skim. In Spence, pooling exists but is eliminated only by refinement.</p>
<p><em>Sources: Micro2025.pdf Topic 7 Lectures (FHSMicroWk6), Rothschild-Stiglitz 1976 QJE, Mas-Colell Ch. 13.D, Bolton-Dewatripont Ch. 2.4.</em></p>""",
        "widget": r"""<svg id="widget-rothschild-stiglitz-screening" viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="background:#fff;font-family:sans-serif;">
<line x1="60" y1="270" x2="560" y2="270" stroke="#333" stroke-width="1.5"/>
<line x1="60" y1="270" x2="60" y2="40" stroke="#333" stroke-width="1.5"/>
<text x="300" y="305" text-anchor="middle" font-size="13">$c_1$ (no-loss)</text>
<text x="20" y="155" font-size="13" transform="rotate(-90 20 155)">$c_2$ (loss)</text>
<line x1="60" y1="270" x2="560" y2="40" stroke="#888" stroke-dasharray="3 3"/>
<text x="540" y="55" font-size="11" fill="#666">45 line</text>
<circle cx="480" cy="240" r="6" fill="#2c3e50"/>
<text x="490" y="255" font-size="11">$E$ endowment</text>
<line x1="480" y1="240" x2="200" y2="80" stroke="#c0392b" stroke-width="1.5"/>
<text x="190" y="75" font-size="11" fill="#c0392b">$H$ fair odds (steep)</text>
<line x1="480" y1="240" x2="100" y2="180" stroke="#3498db" stroke-width="1.5"/>
<text x="90" y="175" font-size="11" fill="#3498db">$L$ fair odds (flat)</text>
<circle cx="310" cy="160" r="6" fill="#c0392b"/>
<text x="315" y="175" font-size="11" fill="#c0392b">$H^*$: full insurance</text>
<circle cx="350" cy="200" r="6" fill="#3498db"/>
<text x="295" y="220" font-size="11" fill="#3498db">$L^*$: partial</text>
<text x="300" y="25" text-anchor="middle" font-size="13" font-weight="bold">R-S separating menu</text>
</svg>
<p style="font-size:12px;color:#555;">$H$ on full-insurance point of its fair-odds line; $L$ on its fair-odds line at the point that just makes $H$ indifferent.</p>""",
        "examples": r"""<ul>
<li><strong>Auto insurance menus.</strong> Real insurers offer high-deductible and full-coverage options; the menu structure is recognisably Rothschild-Stiglitz in spirit.</li>
<li><strong>Annuity tiers.</strong> Single-life vs joint-life annuities and varying guarantee periods screen by mortality expectation.</li>
<li><strong>Health insurance pre-ACA.</strong> Plans with high deductibles attracted low-risk enrollees; high coverage attracted high-risks. This is also the source of the non-existence problem for pooled plans.</li>
<li><strong>Essay move (Doornik likes).</strong> Draw the state-space diagram explicitly with both fair-odds lines and the binding $H$ indifference curve at $L$'s contract. The geometry is mark-bearing.</li>
<li><strong>Essay move.</strong> Discuss the existence pathology and its resolution: [[Concepts/Wilson Equilibrium Refinement]], Riley reactive equilibrium, or Miyazaki-Spence cross-subsidisation. Show awareness that the simple R-S model has a known limitation.</li>
<li><strong>Limitation.</strong> The model assumes risk-neutral competitive insurers and unobservable types with single-dimensional risk. Multidimensional heterogeneity (risk and risk aversion) can reverse predictions, see Chiappori-Salanie 2000.</li>
</ul>""",
    },
    "state-space-rothschild-stiglitz": {
        "math": r"""<p><strong>Construction.</strong> Plot consumption in state 1 (no loss) on the horizontal axis and state 2 (loss) on the vertical axis. The endowment without insurance is $E = (W, W - D)$, which lies below the 45 line. Full insurance lies on the 45 line.</p>
<p><strong>Fair-odds lines.</strong> A contract $(p, q)$ is type-$i$-fair iff $p = \pi_i q$. The locus of fair contracts in state-space is a line through $E$ with slope $-(1 - \pi_i) / \pi_i$. Higher $\pi_i$ implies a steeper line, so $H$'s fair-odds line is steeper than $L$'s.</p>
<p><strong>Indifference curves.</strong> Expected utility $\pi_i u(c_2) + (1 - \pi_i) u(c_1)$ has slope (MRS in state-space) at any point</p>
<p>$$\left| \frac{dc_2}{dc_1} \right| = \frac{(1 - \pi_i) u'(c_1)}{\pi_i u'(c_2)}.$$</p>
<p>At any common point, $L$'s indifference curve is steeper than $H$'s (single crossing). On the 45 line, the MRS equals $(1 - \pi_i)/\pi_i$, which matches the fair-odds slope: each type fully insures at its own fair odds.</p>
<p><strong>Separating equilibrium geometry.</strong></p>
<ol>
<li>$H$'s contract $\alpha_H$: intersection of 45 line with $H$'s fair-odds line.</li>
<li>$L$'s contract $\alpha_L$: intersection of $L$'s fair-odds line with $H$'s indifference curve through $\alpha_H$ (binding IC).</li>
<li>The shaded region above $L$'s indifference curve through $\alpha_L$ and above the pooled fair-odds line is where a cream-skimming pooling contract would lie. Non-emptiness is the source of the existence problem.</li>
</ol>
<p><em>Sources: Micro2025.pdf Topic 7 Lectures (FHSMicroWk6), Rothschild-Stiglitz 1976, Mas-Colell Ch. 13.D, Bolton-Dewatripont 2.4.</em></p>""",
        "widget": r"""<svg id="widget-state-space-rothschild-stiglitz" viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="background:#fff;font-family:sans-serif;">
<line x1="60" y1="270" x2="560" y2="270" stroke="#333" stroke-width="1.5"/>
<line x1="60" y1="270" x2="60" y2="40" stroke="#333" stroke-width="1.5"/>
<text x="300" y="305" text-anchor="middle" font-size="13">$c_1$ (no-loss)</text>
<text x="20" y="155" font-size="13" transform="rotate(-90 20 155)">$c_2$ (loss)</text>
<line x1="60" y1="270" x2="500" y2="50" stroke="#888" stroke-dasharray="3 3"/>
<text x="510" y="55" font-size="11" fill="#666">45 line</text>
<circle cx="480" cy="240" r="6" fill="#2c3e50"/>
<text x="490" y="258" font-size="11">$E$</text>
<line x1="480" y1="240" x2="220" y2="90" stroke="#c0392b" stroke-width="1.5"/>
<text x="200" y="85" font-size="11" fill="#c0392b">$H$ fair odds</text>
<line x1="480" y1="240" x2="120" y2="190" stroke="#3498db" stroke-width="1.5"/>
<text x="80" y="195" font-size="11" fill="#3498db">$L$ fair odds</text>
<circle cx="320" cy="150" r="6" fill="#c0392b"/>
<text x="330" y="145" font-size="11" fill="#c0392b">$\alpha_H$ full</text>
<path d="M 200 100 Q 320 150 460 230" stroke="#c0392b" stroke-width="1" fill="none" stroke-dasharray="2 2"/>
<text x="380" y="195" font-size="10" fill="#c0392b">$U_H$ through $\alpha_H$</text>
<circle cx="370" cy="215" r="6" fill="#3498db"/>
<text x="380" y="210" font-size="11" fill="#3498db">$\alpha_L$ partial</text>
<text x="300" y="25" text-anchor="middle" font-size="13" font-weight="bold">R-S state-space diagram</text>
</svg>
<p style="font-size:12px;color:#555;">$\alpha_H$ at full insurance on $H$'s fair odds; $\alpha_L$ on $L$'s fair odds where $H$'s indifference curve through $\alpha_H$ crosses.</p>""",
        "examples": r"""<ul>
<li><strong>Standard FHS exam diagram.</strong> Doornik routinely asks for the R-S diagram with both fair-odds lines, the endowment, the binding IC, and the two equilibrium contracts. Producing this cleanly is a high-value mark grab.</li>
<li><strong>Welfare reading.</strong> The diagram shows the $L$ type strictly worse off than under full information (point on $L$'s fair odds but below the 45 line). Quantify the welfare loss as the certainty equivalent gap.</li>
<li><strong>Non-existence illustration.</strong> Add the pooled fair-odds line (slope $-(1-\bar\pi)/\bar\pi$ where $\bar\pi = \lambda \pi_H + (1-\lambda)\pi_L$). Show the cream-skimming region when $\lambda$ is small.</li>
<li><strong>Essay move (Doornik likes).</strong> Always label endowment, both fair-odds lines, binding IC, and indicate which type is at full vs partial insurance. A correctly labelled diagram often substitutes for paragraphs of prose.</li>
<li><strong>Essay move.</strong> Use the diagram to motivate the cross-subsidisation refinement: the Miyazaki-Spence equilibrium gives $L$ a contract on a steeper-than-$L$-fair line.</li>
<li><strong>Limitation.</strong> Two-state diagrams assume binary loss outcomes. Continuous loss distributions complicate the geometry but the qualitative results carry through. See [[Concepts/Fair Odds Line]].</li>
</ul>""",
    },
    "fair-odds-line": {
        "math": r"""<p><strong>Definition.</strong> In state-space $(c_1, c_2)$ with loss probability $\pi$, a fair-odds line is the locus of contracts that break even for a risk-neutral insurer when the customer has loss probability $\pi$. Each contract $(p, q)$ moves the agent from endowment $E = (W, W - D)$ to $(W - p, W - D + q - p)$, with the insurer's profit $p - \pi q = 0$.</p>
<p><strong>Equation.</strong> Eliminating $(p, q)$ and rearranging:</p>
<p>$$c_1 - W = -\frac{1 - \pi}{\pi} \, (c_2 - (W - D)),$$</p>
<p>so the fair-odds line through $E$ has slope $-(1 - \pi)/\pi$ in $(c_1, c_2)$ space. Steeper slopes correspond to higher loss probabilities.</p>
<ol>
<li>The full-insurance point on a type's fair-odds line is the intersection with the 45 line: $c_1 = c_2 = W - \pi D$.</li>
<li>An agent with expected utility $\pi u(c_2) + (1 - \pi) u(c_1)$ has MRS $(1-\pi)u'(c_1)/(\pi u'(c_2))$, which on the 45 line equals $(1-\pi)/\pi$, the slope of the fair-odds line. Hence first-best is full insurance at the own-fair odds.</li>
<li>The pooled fair-odds line has slope $-(1 - \bar{\pi})/\bar{\pi}$ with $\bar{\pi} = \lambda \pi_H + (1-\lambda) \pi_L$; it lies between the two type-specific lines.</li>
<li>Iso-profit lines for the insurer are parallel to the fair-odds line.</li>
</ol>
<p><strong>Geometric content.</strong> The fair-odds line is simultaneously the budget set (under fair pricing) and the zero-profit locus for the insurer. Competitive equilibrium contracts lie on a fair-odds line of some pricing pool; cross-subsidising contracts lie off the type-specific line and on the pooled line.</p>
<p><em>Sources: Micro2025.pdf Topic 7 Lectures (FHSMicroWk6), Rothschild-Stiglitz 1976, Mas-Colell Ch. 13.D, Bolton-Dewatripont Ch. 2.4.</em></p>""",
        "widget": r"""<svg id="widget-fair-odds-line" viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="background:#fff;font-family:sans-serif;">
<line x1="60" y1="270" x2="560" y2="270" stroke="#333" stroke-width="1.5"/>
<line x1="60" y1="270" x2="60" y2="40" stroke="#333" stroke-width="1.5"/>
<text x="300" y="305" text-anchor="middle" font-size="13">$c_1$</text>
<text x="20" y="155" font-size="13" transform="rotate(-90 20 155)">$c_2$</text>
<line x1="60" y1="270" x2="500" y2="50" stroke="#888" stroke-dasharray="3 3"/>
<text x="510" y="55" font-size="11" fill="#666">45 line</text>
<circle cx="480" cy="240" r="6" fill="#2c3e50"/>
<text x="490" y="258" font-size="11">$E=(W,W-D)$</text>
<line x1="480" y1="240" x2="220" y2="90" stroke="#c0392b" stroke-width="2"/>
<text x="200" y="85" font-size="11" fill="#c0392b">slope $-(1-\pi_H)/\pi_H$</text>
<line x1="480" y1="240" x2="140" y2="200" stroke="#3498db" stroke-width="2"/>
<text x="60" y="200" font-size="11" fill="#3498db">slope $-(1-\pi_L)/\pi_L$</text>
<circle cx="335" cy="155" r="5" fill="#c0392b"/>
<text x="340" y="150" font-size="10" fill="#c0392b">$H$ full</text>
<text x="300" y="25" text-anchor="middle" font-size="13" font-weight="bold">Fair-odds lines through endowment</text>
</svg>
<p style="font-size:12px;color:#555;">Both lines pass through $E$. Higher $\pi$ means steeper line; full insurance lies on the 45 line.</p>""",
        "examples": r"""<ul>
<li><strong>Insurance pricing.</strong> A risk-neutral monopolist insurer prices on the customer's fair-odds line and captures all surplus; a competitive market prices contracts on the zero-profit fair-odds line.</li>
<li><strong>Underwriting categories.</strong> Smokers and non-smokers have different fair-odds lines; observable categorisation moves the market closer to first-best.</li>
<li><strong>Reinsurance.</strong> Catastrophe bonds price tail risk on a fair-odds line for the underlying loss distribution.</li>
<li><strong>Essay move (Doornik likes).</strong> Derive the slope from the zero-profit condition explicitly in your answer. Most students draw the line without showing where the slope comes from.</li>
<li><strong>Essay move.</strong> Relate slope to MRS: the equivalence at the 45 line is why first-best is full insurance, a one-line argument that captures the textbook result.</li>
<li><strong>Limitation.</strong> Assumes risk-neutral insurers. Capital constraints, deadweight costs of capital, and load factors push real premiums off the fair-odds line, see [[Concepts/State-Space Diagram (Rothschild-Stiglitz)]].</li>
</ul>""",
    },
    "reimbursement-contracts": {
        "math": r"""<p><strong>Definition.</strong> A reimbursement contract pays a partial refund to the buyer if the good turns out to be defective ex post. In a lemons setting where quality $v$ is observed only after purchase (with verifiability), the contract restores some efficiency by transferring risk back to the seller.</p>
<p><strong>Setup.</strong> Seller of type $v$, buyer value $\beta v$ with $\beta > 1$, price $p$, reimbursement $r$ paid by the seller if $v$ is verified to be below some threshold $\hat{v}$ (a defect). Seller participation: $p - r \cdot \Pr(\text{defect} \mid v) \ge v$.</p>
<p><strong>Effect on adverse selection.</strong> A high-$v$ seller has low defect probability, so the expected cost of the reimbursement is small; a low-$v$ seller faces a large expected payout. Reimbursement therefore acts as a signal: only high types willingly accept large $r$. The contract space expands from one dimension ($p$) to two ($p, r$), letting the market support a separating menu.</p>
<p><strong>FHS exam example (2018 Q4).</strong> Used bicycle, quality $v \sim U[0, 100]$, $\beta = 1.5$. Without reimbursement, only the bottom trades. Offering $r = 50$ if buyer dissatisfied gives sellers below some cutoff $v_c$ a payoff $p - 50 \cdot \Pr(\text{dissat} \mid v)$ that is increasing in $v$, separating the market.</p>
<ol>
<li>Reimbursement is one of several instruments that can restore trade in lemons markets, alongside warranties, certification, and signalling investments.</li>
<li>Effectiveness depends on verifiability of defects (else seller liability is unenforceable).</li>
<li>Equivalent to a money-back guarantee in retail; equivalent to a put option on quality in finance.</li>
</ol>
<p><em>Sources: Micro2025.pdf Topic 7 Lectures (FHSMicroWk6), Mas-Colell Ch. 13.B, Bolton-Dewatripont Ch. 2.5, FHS 2018 Q4.</em></p>""",
        "widget": r"""<svg id="widget-reimbursement-contracts" viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="background:#fff;font-family:sans-serif;">
<line x1="60" y1="270" x2="560" y2="270" stroke="#333" stroke-width="1.5"/>
<line x1="60" y1="270" x2="60" y2="40" stroke="#333" stroke-width="1.5"/>
<text x="300" y="305" text-anchor="middle" font-size="13">quality $v$</text>
<text x="20" y="155" font-size="13" transform="rotate(-90 20 155)">seller payoff</text>
<line x1="60" y1="220" x2="560" y2="100" stroke="#3498db" stroke-width="2"/>
<text x="430" y="125" font-size="11" fill="#3498db">no reimbursement</text>
<line x1="60" y1="260" x2="560" y2="60" stroke="#c0392b" stroke-width="2"/>
<text x="430" y="85" font-size="11" fill="#c0392b">with $r=50$</text>
<circle cx="200" cy="190" r="5" fill="#2c3e50"/>
<text x="210" y="205" font-size="11">cutoff without $r$</text>
<circle cx="340" cy="140" r="5" fill="#c0392b"/>
<text x="340" y="130" font-size="11" fill="#c0392b">cutoff shifts right</text>
<text x="300" y="25" text-anchor="middle" font-size="13" font-weight="bold">Reimbursement steepens the schedule</text>
</svg>
<p style="font-size:12px;color:#555;">Reimbursement penalises low types disproportionately, extending the active market to higher cutoff.</p>""",
        "examples": r"""<ul>
<li><strong>Consumer money-back guarantees.</strong> Online retailers (Amazon, Zappos) offer free returns. The cost to the retailer is low because most goods are not defective; the signal value to consumers is large.</li>
<li><strong>Used-car warranties.</strong> CPO programmes bundle limited warranties into the price, an explicit reimbursement contract that separates the certified segment.</li>
<li><strong>Software service-level agreements.</strong> SaaS providers refund a fraction of fees for downtime; this signals confidence in uptime and reassures risk-averse enterprise buyers.</li>
<li><strong>Essay move (Doornik likes).</strong> Quote the 2018 Q4 setup if relevant; show explicitly how $r$ enters the seller's IR constraint and shifts the cutoff $v_c$.</li>
<li><strong>Essay move.</strong> Compare reimbursement, warranties, and reputation as efficiency-restoring instruments. The choice depends on verifiability, time horizons, and contract enforcement costs.</li>
<li><strong>Limitation.</strong> Requires verifiable defects and enforceable contracts. In informal markets these are weak, which is why such markets often rely on reputation. See [[Concepts/Akerlof Lemons Market]].</li>
</ul>""",
    },
    "asymmetric-information": {
        "math": r"""<p><strong>Definition.</strong> Asymmetric information is a market environment in which one party to a transaction has information relevant to the contract terms that the other party cannot observe. The textbook taxonomy splits it into:</p>
<ol>
<li><strong>Hidden information (adverse selection).</strong> Type $\theta$ is private before contracting. Examples: insurance applicants know their health, used-car sellers know quality, workers know productivity.</li>
<li><strong>Hidden action (moral hazard).</strong> Effort or care $e$ is private after contracting. Examples: insured drivers' caution, managers' effort, doctors' diligence.</li>
</ol>
<p><strong>Welfare consequences.</strong> Asymmetric information breaks the first welfare theorem. The competitive equilibrium fails to internalise the informational externality the informed party exerts on the uninformed party.</p>
<p><strong>Standard formal devices.</strong> Both adverse selection and moral hazard are studied through principal-agent models, where the principal chooses a mechanism (a menu of contracts $\{(p_i, q_i)\}_i$) to maximise its objective subject to the agent's incentive compatibility (IC) and individual rationality (IR) constraints.</p>
<p>For adverse selection with two types: $\text{IR}_i: U_i(p_i, q_i) \ge \bar{U}_i$; $\text{IC}_i: U_i(p_i, q_i) \ge U_i(p_j, q_j)$ for $j \ne i$. The standard solution has IR binding on the low type, IC binding on the high type. This is the no-distortion-at-top and downward-distortion-elsewhere pattern.</p>
<p><strong>Empirical detection.</strong> The Chiappori-Salanie 2000 positive-correlation test: under asymmetric information, observable claim frequency should be positively correlated with coverage choice, conditional on observable risk factors. Mixed empirical evidence across markets.</p>
<p><em>Sources: Micro2025.pdf Topic 7 Lectures (FHSMicroWk6), Mas-Colell Ch. 13 and 14, Bolton-Dewatripont Ch. 1 and 2, Akerlof 1970, Rothschild-Stiglitz 1976.</em></p>""",
        "widget": r"""<svg id="widget-asymmetric-information" viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="background:#fff;font-family:sans-serif;">
<rect x="60" y="60" width="220" height="100" fill="#3498db" fill-opacity="0.15" stroke="#3498db" stroke-width="1.5"/>
<text x="170" y="90" text-anchor="middle" font-size="13" font-weight="bold">Hidden Information</text>
<text x="170" y="110" text-anchor="middle" font-size="11">(Adverse Selection)</text>
<text x="170" y="130" text-anchor="middle" font-size="11">pre-contracting</text>
<text x="170" y="148" text-anchor="middle" font-size="11">screening, signalling</text>
<rect x="320" y="60" width="220" height="100" fill="#c0392b" fill-opacity="0.15" stroke="#c0392b" stroke-width="1.5"/>
<text x="430" y="90" text-anchor="middle" font-size="13" font-weight="bold">Hidden Action</text>
<text x="430" y="110" text-anchor="middle" font-size="11">(Moral Hazard)</text>
<text x="430" y="130" text-anchor="middle" font-size="11">post-contracting</text>
<text x="430" y="148" text-anchor="middle" font-size="11">incentive contracts</text>
<rect x="180" y="200" width="240" height="80" fill="#27ae60" fill-opacity="0.15" stroke="#27ae60" stroke-width="1.5"/>
<text x="300" y="225" text-anchor="middle" font-size="12" font-weight="bold">Asymmetric Information</text>
<text x="300" y="245" text-anchor="middle" font-size="11">breaks 1st welfare theorem</text>
<text x="300" y="263" text-anchor="middle" font-size="11">IR + IC constraints bind</text>
<line x1="170" y1="160" x2="240" y2="200" stroke="#666" stroke-dasharray="3 3"/>
<line x1="430" y1="160" x2="360" y2="200" stroke="#666" stroke-dasharray="3 3"/>
<text x="300" y="35" text-anchor="middle" font-size="13" font-weight="bold">Asymmetric information taxonomy</text>
</svg>
<p style="font-size:12px;color:#555;">The two pure forms of asymmetric information differ in the timing of the unobserved variable.</p>""",
        "examples": r"""<ul>
<li><strong>Credit markets.</strong> Lenders know less than borrowers about repayment likelihood (adverse selection) and post-loan effort (moral hazard). Credit rationing (Stiglitz-Weiss 1981) is the canonical consequence.</li>
<li><strong>Health insurance.</strong> Pre-existing condition asymmetry is hidden information; failure to exercise after enrolment is hidden action. Both are present and partially separated by plan choice and copays.</li>
<li><strong>Corporate finance.</strong> Managers know more about project quality than investors (adverse selection: Myers-Majluf) and more about effort (moral hazard: Jensen-Meckling).</li>
<li><strong>Essay move (Doornik likes).</strong> Specify which form of asymmetric information your question concerns and define $\theta$ vs $e$ explicitly. A common student error is to conflate the two.</li>
<li><strong>Essay move.</strong> Use the positive-correlation test as an empirical anchor. Where it fails (e.g. long-term care insurance, Finkelstein-McGarry 2006), multidimensional heterogeneity is the suspect.</li>
<li><strong>Limitation.</strong> The clean two-type theory misses common real-world features: learning, repeated interaction, partial verifiability. See [[Concepts/Hidden Information vs Hidden Action]].</li>
</ul>""",
    },

    "first-best-contract": {
        "math": r"""<p>The <strong>first-best contract</strong> is the optimal risk-sharing arrangement when the agent's effort $e$ is verifiable by the principal (or output reveals it perfectly). With effort contractible, the principal directly stipulates the efficient effort level $e^*$ and chooses the wage schedule $w(x)$ to maximise expected profit subject only to the agent's participation constraint (IR).</p>
        <p>The problem is:</p>
        <p>$\max_{w(\cdot), e} \; E[x - w(x) \mid e]$ subject to $E[u(w(x)) \mid e] - c(e) \geq \bar u$.</p>
        <ol>
        <li>Form the Lagrangian with multiplier $\lambda$ on IR. The first-order condition on $w(x)$ at each output state gives $f(x \mid e) = \lambda u'(w(x)) f(x \mid e)$, hence $u'(w(x)) = 1/\lambda$, a constant.</li>
        <li>Constant marginal utility implies a constant wage $w^*$. The risk-averse agent is <strong>fully insured</strong> and the risk-neutral principal bears all output risk. This is the Borch rule for efficient risk sharing.</li>
        <li>The wage $w^*$ is pinned down by IR holding with equality: $u(w^*) = \bar u + c(e^*)$, so $w^* = u^{-1}(\bar u + c(e^*))$.</li>
        <li>Optimal effort $e^*$ solves $E[x_e \mid e] = c'(e)$, equating marginal expected output to marginal effort cost. This is the surplus-maximising effort, the same level a social planner would choose.</li>
        </ol>
        <p>The first-best is unattainable when effort is hidden because a flat wage gives the agent no reason to exert costly effort: the IC constraint fails. The first-best serves as the welfare benchmark against which the <strong>agency cost</strong> of the second-best is measured. Two knife-edge cases recover it: a risk-neutral agent (sell the firm to the agent) and a perfectly informative output signal (set a forcing contract).</p>
        <p>References: Micro2025.pdf Topic 8 Lectures (FHSMicroWk7), Bolton and Dewatripont Ch. 4.1, Mas-Colell, Whinston and Green Ch. 14.B, Holmstrom 1979 Section 2.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" id="widget-first-best-contract" role="img" aria-label="First-best full insurance diagram">
          <defs>
            <marker id="fb-arr" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L6,4 L0,8 z" fill="#333"/></marker>
          </defs>
          <rect x="0" y="0" width="600" height="320" fill="white"/>
          <text x="300" y="22" text-anchor="middle" font-size="14" font-weight="bold">First-Best: Flat Wage in Output Space</text>
          <line x1="60" y1="270" x2="560" y2="270" stroke="#333" stroke-width="1.5" marker-end="url(#fb-arr)"/>
          <line x1="60" y1="270" x2="60" y2="50" stroke="#333" stroke-width="1.5" marker-end="url(#fb-arr)"/>
          <text x="565" y="285" font-size="12">output $x$</text>
          <text x="30" y="55" font-size="12">wage</text>
          <line x1="60" y1="170" x2="560" y2="170" stroke="#1f77b4" stroke-width="2.5"/>
          <text x="470" y="160" font-size="12" fill="#1f77b4">$w^* = u^{-1}(\bar u + c(e^*))$</text>
          <line x1="60" y1="220" x2="560" y2="120" stroke="#d62728" stroke-width="2" stroke-dasharray="5,4"/>
          <text x="470" y="115" font-size="12" fill="#d62728">second-best slope</text>
          <line x1="60" y1="170" x2="60" y2="270" stroke="#888" stroke-dasharray="2,2"/>
          <text x="65" y="220" font-size="11" fill="#555">agent fully insured</text>
          <circle cx="200" cy="170" r="4" fill="#1f77b4"/>
          <circle cx="400" cy="170" r="4" fill="#1f77b4"/>
          <text x="300" y="305" text-anchor="middle" font-size="11" fill="#555">Caption: under observable effort the principal pays a constant wage; the dashed line shows the second-best for contrast.</text>
        </svg>""",
        "examples": r"""<ul>
        <li><strong>Salaried civil servants.</strong> Where output is hard to attribute to individuals and effort is roughly observable through supervision, fixed salary contracts approximate the first-best risk-sharing rule.</li>
        <li><strong>Piecework with monitored quality.</strong> A factory with cameras over the line can verify effort directly, allowing a flat wage tied to attendance rather than output. Closer to first-best than commission pay.</li>
        <li><strong>Evaluation move (Doornik).</strong> The first-best is a useful benchmark, not a policy target. Showing the gap between first-best and second-best surplus quantifies the welfare cost of asymmetric information and motivates why second-best contracts look strange (steep, risky).</li>
        <li><strong>Evaluation move.</strong> The two knife-edge cases (risk neutrality, perfect signal) restore the first-best and clarify which feature, hidden action or risk aversion, is doing the work in the agency model.</li>
        <li><strong>Evaluation move.</strong> Empirically, executive pay rarely looks first-best even when effort seems observable. Bertrand and Mullainathan (2001) "Are CEOs rewarded for luck?" suggests the principal-agent benchmark misses governance frictions.</li>
        <li><strong>Limitation.</strong> The first-best ignores wealth constraints and limited liability. With $w \geq 0$ even an observable-effort contract may not implement $e^*$ because the principal cannot extract enough surplus upfront.</li>
        <li>See [[Concepts/Second-Best Contract]] for the contract that obtains when effort is hidden.</li>
        </ul>""",
    },
    "second-best-contract": {
        "math": r"""<p>The <strong>second-best contract</strong> solves the principal-agent problem when effort $e$ is the agent's private action. The principal designs $w(x)$ to maximise expected profit subject to participation (IR) and incentive compatibility (IC), where IC says the agent prefers the targeted effort $e_H$ to any alternative.</p>
        <p>Using the first-order approach with two effort levels and densities $f(x \mid e_H), f(x \mid e_L)$, the problem is:</p>
        <p>$\max_{w(\cdot)} \; \int (x - w(x)) f(x \mid e_H) dx$ subject to $\int u(w(x)) f(x \mid e_H) dx - c(e_H) \geq \bar u$ (IR) and $\int u(w(x))[f(x \mid e_H) - f(x \mid e_L)] dx \geq c(e_H) - c(e_L)$ (IC).</p>
        <ol>
        <li>Let $\lambda \geq 0$ be the IR multiplier and $\mu \geq 0$ the IC multiplier. Pointwise optimisation yields the <strong>Mirrlees-Holmstrom</strong> condition:</li>
        <li>$\dfrac{1}{u'(w(x))} = \lambda + \mu \dfrac{f(x \mid e_H) - f(x \mid e_L)}{f(x \mid e_H)} = \lambda + \mu \left(1 - \dfrac{f_L}{f_H}\right)$.</li>
        <li>The ratio $f_e/f = (f_H - f_L)/f_H$ is the <strong>likelihood ratio</strong>: outputs more informative of high effort raise $w(x)$. Both IR and IC bind in the interior solution.</li>
        <li>The wage schedule is not monotone in $x$ in general; it is monotone in the likelihood ratio. If MLRP holds, the two coincide and $w(x)$ rises with $x$.</li>
        <li>The agent's expected utility equals $\bar u$ (IR binds) but they bear output risk, so the principal pays a <strong>risk premium</strong>. The expected wage exceeds the first-best constant wage by an amount called the <strong>agency cost</strong>.</li>
        </ol>
        <p>The agency cost rises with the agent's risk aversion $r$, the noisiness of output $\sigma^2$, and the curvature of effort cost $c''$. It falls when the signal becomes more informative about effort (steeper likelihood ratio).</p>
        <p>References: Micro2025.pdf Topic 8 Lectures (FHSMicroWk7), Bolton and Dewatripont Ch. 4.2 to 4.4, Holmstrom 1979 "Moral Hazard and Observability", Mas-Colell Ch. 14.B.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" id="widget-second-best-contract" role="img" aria-label="Agency cost decomposition">
          <rect x="0" y="0" width="600" height="320" fill="white"/>
          <text x="300" y="22" text-anchor="middle" font-size="14" font-weight="bold">Agency Cost = Second-Best Wage Bill minus First-Best</text>
          <rect x="80" y="80" width="160" height="180" fill="#1f77b4" opacity="0.7" stroke="#1f77b4"/>
          <text x="160" y="290" text-anchor="middle" font-size="12">First-best $E[w^*]$</text>
          <text x="160" y="170" text-anchor="middle" font-size="11" fill="white">surplus to principal</text>
          <rect x="280" y="80" width="160" height="180" fill="#1f77b4" opacity="0.7" stroke="#1f77b4"/>
          <rect x="280" y="50" width="160" height="30" fill="#d62728" opacity="0.8" stroke="#d62728"/>
          <text x="360" y="290" text-anchor="middle" font-size="12">Second-best $E[w(x)]$</text>
          <text x="360" y="68" text-anchor="middle" font-size="11" fill="white">risk premium</text>
          <line x1="450" y1="50" x2="500" y2="50" stroke="#d62728" stroke-width="2"/>
          <line x1="450" y1="80" x2="500" y2="80" stroke="#d62728" stroke-width="2"/>
          <text x="510" y="70" font-size="12" fill="#d62728">agency cost</text>
          <text x="510" y="84" font-size="11" fill="#d62728">$= \mu c'(e_H)$ (approx.)</text>
          <text x="300" y="310" text-anchor="middle" font-size="11" fill="#555">Caption: hidden effort forces the principal to pay a premium for bearing output risk.</text>
        </svg>""",
        "examples": r"""<ul>
        <li><strong>Sales commission with quota.</strong> A bonus paid only above a target quota approximates a step function in $w(x)$. Optimal when the likelihood ratio jumps at the quota threshold (good salespeople almost surely beat it).</li>
        <li><strong>Equity grants and stock options for executives.</strong> Pay schedules convex in firm value reflect the increasing likelihood ratio of high-effort states at the top of the distribution. Murphy (1999) handbook chapter documents the rise of convex CEO pay.</li>
        <li><strong>Evaluation move (Doornik).</strong> The first-order approach (FOA) used to derive the Holmstrom condition is not generally valid. Mirrlees (1999) and Rogerson (1985) show MLRP plus CDFC (convexity of the distribution function condition) is needed for the FOA to be justified.</li>
        <li><strong>Evaluation move.</strong> Compare second-best to "selling the firm" benchmark to isolate the role of risk aversion versus risk neutrality. With risk-neutral agent the second-best equals the first-best and agency cost is zero.</li>
        <li><strong>Evaluation move.</strong> The model assumes only two effort levels in many textbook presentations. Grossman and Hart (1983) generalise to continuous effort; the structure of $w(x)$ depends on monotonicity assumptions on the family of densities.</li>
        <li><strong>Limitation.</strong> The static one-shot framing misses career concerns and reputation, which Holmstrom (1999) shows can substitute for explicit incentives over time. See [[Concepts/Repeated Moral Hazard]].</li>
        </ul>""",
    },
    "linear-contracts": {
        "math": r"""<p>A <strong>linear contract</strong> pays the agent $w(x) = t + s x$, where $t$ is a base salary and $s \in [0, 1]$ is the slope or incentive intensity. Although usually a restrictive functional form, Holmstrom and Milgrom (1987) show that linear contracts are <strong>fully optimal</strong> in a continuous-time setting with CARA utility, Brownian output, and effort affecting drift.</p>
        <p>Static CARA-normal version. Output $x = e + \varepsilon$ with $\varepsilon \sim N(0, \sigma^2)$; agent has CARA utility $u(w) = -e^{-r w}$; cost $c(e) = \tfrac{1}{2} c e^2$.</p>
        <ol>
        <li>Given $w = t + s x$, the agent's certainty-equivalent income is $\mathrm{CE}(e) = t + s e - \tfrac{1}{2} r s^2 \sigma^2 - \tfrac{1}{2} c e^2$.</li>
        <li>Maximising over $e$ gives the IC: $e(s) = s/c$. The agent's effort is proportional to incentive intensity.</li>
        <li>The principal chooses $s$ and $t$ to maximise expected surplus $E[x - w] = (1 - s) e(s) + (\mathrm{CE} - \bar u)$ subject to IR ($\mathrm{CE} = \bar u$). Substituting $e(s) = s/c$:</li>
        <li>Total surplus $= s/c - \tfrac{1}{2}(s/c)^2 c - \tfrac{1}{2} r s^2 \sigma^2 = s/c - \tfrac{1}{2} s^2 (1/c + r \sigma^2)$.</li>
        <li>FOC in $s$: $1/c = s (1/c + r \sigma^2)$, giving the central Holmstrom-Milgrom formula $s^* = \dfrac{1}{1 + r \sigma^2 c}$.</li>
        </ol>
        <p>The slope $s^*$ trades off incentives against insurance. As $r \to 0$ (risk neutrality), $s^* \to 1$: sell the firm. As $\sigma^2 \to 0$ (no noise) or $c \to 0$ (linear cost), $s^* \to 1$ again. Higher $r, \sigma^2, c$ all shrink $s^*$, flattening pay and protecting the agent.</p>
        <p>The base salary $t$ adjusts to satisfy IR: $t = \bar u - s e(s) + \tfrac{1}{2} r s^2 \sigma^2 + \tfrac{1}{2} c e(s)^2$. The agent earns zero rents in this CARA-normal world (IR binds without limited liability).</p>
        <p>References: Micro2025.pdf Topic 8 Lectures (FHSMicroWk7), Holmstrom and Milgrom 1987 Econometrica, Bolton and Dewatripont Ch. 4.6, Mas-Colell Ch. 14.B.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" id="widget-linear-contracts" role="img" aria-label="Optimal incentive intensity as function of noise">
          <defs><marker id="lc-arr" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L6,4 L0,8 z" fill="#333"/></marker></defs>
          <rect x="0" y="0" width="600" height="320" fill="white"/>
          <text x="300" y="22" text-anchor="middle" font-size="14" font-weight="bold">Optimal slope $s^* = 1/(1+r\sigma^2 c)$</text>
          <line x1="70" y1="270" x2="560" y2="270" stroke="#333" stroke-width="1.5" marker-end="url(#lc-arr)"/>
          <line x1="70" y1="270" x2="70" y2="50" stroke="#333" stroke-width="1.5" marker-end="url(#lc-arr)"/>
          <text x="565" y="285" font-size="12">noise $\sigma^2$</text>
          <text x="30" y="55" font-size="12">$s^*$</text>
          <text x="40" y="75" font-size="11">1</text>
          <line x1="65" y1="70" x2="75" y2="70" stroke="#333"/>
          <path d="M 70 70 Q 200 90 350 170 T 560 240" stroke="#1f77b4" stroke-width="2.5" fill="none"/>
          <line x1="70" y1="70" x2="100" y2="70" stroke="#d62728" stroke-dasharray="4,3"/>
          <text x="105" y="75" font-size="11" fill="#d62728">risk-neutral limit $s^*=1$</text>
          <text x="380" y="265" font-size="11" fill="#1f77b4">incentives weaken as noise rises</text>
          <text x="300" y="305" text-anchor="middle" font-size="11" fill="#555">Caption: the slope falls in $r, \sigma^2$ and $c$; insurance dominates incentives when any factor is large.</text>
        </svg>""",
        "examples": r"""<ul>
        <li><strong>Sharecropping.</strong> A 50:50 crop split between landlord and tenant is the canonical linear contract. Stiglitz (1974) modelled it as the second-best response to weather risk and unobservable farmer effort.</li>
        <li><strong>Sales commission.</strong> Real estate agents earning roughly 3 percent of sale price approximate $s^* < 1$, with the listing brokerage absorbing risk and overhead through the base.</li>
        <li><strong>Evaluation move (Doornik).</strong> Linearity is exact only in the Holmstrom-Milgrom (1987) continuous-time setup. In the static problem, linearity is generally suboptimal; the Mirrlees-Holmstrom schedule depends on the likelihood ratio.</li>
        <li><strong>Evaluation move.</strong> Linearity has the practical virtue of robustness to gaming: nonlinear schedules invite manipulation around kinks (Oyer 1998 on quarterly sales spikes near bonus thresholds).</li>
        <li><strong>Evaluation move.</strong> The CARA-normal benchmark assumes no wealth effects. With DARA or limited liability, the linear form breaks; see [[Concepts/Wage Bounds Limited Liability]].</li>
        <li><strong>Limitation.</strong> Multitasking (Holmstrom and Milgrom 1991) shows that linear contracts on the measurable task can distort effort away from unmeasured tasks. The simple slope formula does not generalise.</li>
        </ul>""",
    },
    "revenue-sharing": {
        "math": r"""<p><strong>Revenue sharing</strong> is a linear contract with no base wage: $w(x) = s x$, where $s \in (0, 1)$ is the agent's share of gross revenue (output) $x$. It is a special case of the linear contract family and appears widely in sharecropping, sales commissions, real estate, publishing royalties, and franchising.</p>
        <p>Setup. Risk-averse agent with utility $u(w) - c(e)$, output $x = e + \varepsilon$ with mean $e$ and variance $\sigma^2$, and a competitive outside option giving $\bar u$. The principal posts $s$; the agent picks effort.</p>
        <ol>
        <li>Given share $s$, the agent solves $\max_e E[u(s x)] - c(e)$. With CARA and normal noise, IC gives $e(s) = s/c$.</li>
        <li>IR requires $s E[x] - \tfrac{1}{2} r s^2 \sigma^2 - c(e(s)) \geq \bar u$. Without a base $t$, IR may fail when $s$ is small; the principal must raise $s$ enough to clear $\bar u$, distorting incentives away from the unconstrained second-best.</li>
        <li>If IR is slack at the unconstrained optimum $s^*_{\text{linear}} = 1/(1 + r \sigma^2 c)$, revenue sharing replicates the linear contract. Otherwise the share is set by IR binding: $s_{\text{RS}} > s^*_{\text{linear}}$, giving the agent a rent.</li>
        <li>Revenue sharing is <strong>strictly suboptimal</strong> relative to the general linear contract when IR is non-binding, because the principal cannot extract the rent without negative wages.</li>
        </ol>
        <p>The classic application is sharecropping. Cheung (1969) argued share contracts are efficient given monitoring costs; Stiglitz (1974) formalised it as a second-best to risk-sharing with hidden effort. Sharing protects the tenant from weather shocks while preserving some incentive to work, at the cost of underprovision of effort relative to fixed rent (which would implement first-best for a risk-neutral tenant).</p>
        <p>Real estate brokerage at roughly 5 to 6 percent split between buyer and seller agents, music streaming royalties at 70 percent to rights holders, and book royalties at 10 to 15 percent of list price all fit this template, though the precise $s$ reflects bargaining and industry convention as much as moral hazard theory.</p>
        <p>References: Micro2025.pdf Topic 8 Lectures (FHSMicroWk7), Bolton and Dewatripont Ch. 4.6, Stiglitz 1974 "Incentives and Risk Sharing in Sharecropping", Cheung 1969 "Theory of Share Tenancy".</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" id="widget-revenue-sharing" role="img" aria-label="Revenue sharing payoff lines">
          <defs><marker id="rs-arr" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L6,4 L0,8 z" fill="#333"/></marker></defs>
          <rect x="0" y="0" width="600" height="320" fill="white"/>
          <text x="300" y="22" text-anchor="middle" font-size="14" font-weight="bold">Revenue Sharing Splits Output</text>
          <line x1="70" y1="270" x2="560" y2="270" stroke="#333" stroke-width="1.5" marker-end="url(#rs-arr)"/>
          <line x1="70" y1="270" x2="70" y2="50" stroke="#333" stroke-width="1.5" marker-end="url(#rs-arr)"/>
          <text x="565" y="285" font-size="12">output $x$</text>
          <text x="30" y="55" font-size="12">pay</text>
          <line x1="70" y1="270" x2="540" y2="60" stroke="#999" stroke-dasharray="3,3"/>
          <text x="495" y="55" font-size="11" fill="#666">$x$ (45-degree)</text>
          <line x1="70" y1="270" x2="540" y2="165" stroke="#1f77b4" stroke-width="2.5"/>
          <text x="510" y="155" font-size="12" fill="#1f77b4">$sx$, $s=0.5$</text>
          <line x1="70" y1="270" x2="540" y2="200" stroke="#2ca02c" stroke-width="2.5"/>
          <text x="510" y="215" font-size="12" fill="#2ca02c">$sx$, $s=0.3$</text>
          <text x="200" y="160" font-size="11" fill="#555">principal keeps $(1-s)x$</text>
          <text x="300" y="305" text-anchor="middle" font-size="11" fill="#555">Caption: zero intercept distinguishes revenue sharing from a general linear contract with base wage $t$.</text>
        </svg>""",
        "examples": r"""<ul>
        <li><strong>Sharecropping in pre-industrial agriculture.</strong> Tenant pays landlord 50 percent of crop. Allen (1992) on English open fields and Otsuka, Chuma and Hayami (1992) on Asian rice document how the share varies with weather risk and monitoring intensity.</li>
        <li><strong>Spotify and streaming royalties.</strong> Approximately 70 percent of net revenue flows to rights holders, with no fixed advance for most artists. A pure revenue share fits the high-noise, hard-to-monitor production setting.</li>
        <li><strong>Evaluation move (Doornik).</strong> A general linear contract with $t < 0$ (the agent pays an upfront franchise fee) strictly dominates pure revenue sharing because it allows the principal to extract rents while keeping incentives optimal. McDonald's franchise model approximates this.</li>
        <li><strong>Evaluation move.</strong> Revenue sharing is robust to renegotiation: with $t = 0$ no party has an incentive to walk away ex post. Hart and Moore (1988) on incomplete contracts suggests this matters when courts cannot verify $t$.</li>
        <li><strong>Evaluation move.</strong> Empirical share contracts cluster at simple fractions (50:50, 1/3:2/3). Young and Burke (2001) attribute this to learning and fairness norms rather than fine optimisation. The friction sits outside the textbook model.</li>
        <li><strong>Limitation.</strong> Revenue sharing on gross output distorts input choices when the agent supplies cost-bearing inputs. See [[Concepts/Linear Contracts]] for the general two-parameter family.</li>
        </ul>""",
    },
    "risk-vs-insurance-tradeoff": {
        "math": r"""<p>The <strong>risk versus insurance trade-off</strong> is the central tension of the principal-agent problem. Steeper wage schedules sharpen incentives by making the agent's pay sensitive to output, but they push output risk onto a risk-averse agent who must be compensated through a higher expected wage (the risk premium). Flatter schedules insure the agent but blunt incentives, lowering effort.</p>
        <p>Formal statement in the CARA-normal model. Let the agent's certainty equivalent under linear contract $w = t + sx$ be $\mathrm{CE}(s) = t + s e(s) - \tfrac{1}{2} r s^2 \sigma^2 - c(e(s))$, where $e(s) = s/c$.</p>
        <ol>
        <li>Marginal incentive benefit of higher $s$: induces extra effort $de/ds = 1/c$, raising output by $de/ds = 1/c$ at unit value. Net gain to principal $= (1-s)/c$.</li>
        <li>Marginal insurance cost of higher $s$: imposes risk $r \sigma^2 s$ on the agent, who demands wage compensation. Net cost $= r \sigma^2 s$.</li>
        <li>Optimal $s^*$ equates marginal benefit and cost. With $c \cdot s$ as the effort cost contribution, the balance yields $s^* = 1/(1 + r \sigma^2 c)$.</li>
        <li>Two corner cases collapse the trade-off:
          <ul>
            <li><em>Risk-neutral agent</em> ($r = 0$): no insurance motive, set $s = 1$ and "sell the firm". First-best is attained.</li>
            <li><em>Perfect signal</em> ($\sigma^2 = 0$): output reveals effort, set a forcing contract paying $\bar u + c(e^*)$ if $x = e^*$ and $-\infty$ otherwise. First-best again.</li>
          </ul>
        </li>
        <li>For interior cases, the agent bears <em>some</em> risk and the principal pays a risk premium. Total surplus falls short of the first-best by the <strong>agency cost</strong> $= \tfrac{1}{2} r (s^*)^2 \sigma^2 / (1 + r \sigma^2 c)$.</li>
        </ol>
        <p>The trade-off is more general than the linear contract. In the Mirrlees-Holmstrom condition $1/u'(w(x)) = \lambda + \mu f_e/f$, the slope of $w(x)$ in the likelihood ratio captures the incentive side; the curvature of $u$ captures the insurance side. Higher $r = -u''/u'$ pulls $w(x)$ closer to flat.</p>
        <p>References: Micro2025.pdf Topic 8 Lectures (FHSMicroWk7), Bolton and Dewatripont Ch. 4.3 to 4.6, Holmstrom 1979, Mas-Colell Ch. 14.B.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" id="widget-risk-vs-insurance-tradeoff" role="img" aria-label="Marginal benefit and cost of incentive intensity">
          <defs><marker id="ri-arr" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L6,4 L0,8 z" fill="#333"/></marker></defs>
          <rect x="0" y="0" width="600" height="320" fill="white"/>
          <text x="300" y="22" text-anchor="middle" font-size="14" font-weight="bold">Trade-off: Incentive Benefit vs Insurance Cost</text>
          <line x1="70" y1="270" x2="560" y2="270" stroke="#333" stroke-width="1.5" marker-end="url(#ri-arr)"/>
          <line x1="70" y1="270" x2="70" y2="50" stroke="#333" stroke-width="1.5" marker-end="url(#ri-arr)"/>
          <text x="565" y="285" font-size="12">slope $s$</text>
          <text x="30" y="55" font-size="12">marginal</text>
          <line x1="70" y1="90" x2="560" y2="230" stroke="#1f77b4" stroke-width="2.5"/>
          <text x="475" y="220" font-size="12" fill="#1f77b4">MB $= (1-s)/c$</text>
          <line x1="70" y1="265" x2="560" y2="100" stroke="#d62728" stroke-width="2.5"/>
          <text x="475" y="115" font-size="12" fill="#d62728">MC $= r\sigma^2 s$</text>
          <circle cx="290" cy="180" r="6" fill="#2ca02c"/>
          <text x="295" y="175" font-size="12" fill="#2ca02c">$s^*$</text>
          <line x1="290" y1="180" x2="290" y2="270" stroke="#2ca02c" stroke-dasharray="3,3"/>
          <text x="300" y="305" text-anchor="middle" font-size="11" fill="#555">Caption: optimum where marginal incentive benefit meets marginal insurance cost.</text>
        </svg>""",
        "examples": r"""<ul>
        <li><strong>CEO equity compensation.</strong> Executives hold roughly 1 to 5 percent of firm equity, far below 100 percent. Jensen and Murphy (1990) document the small slope of CEO pay against firm value, consistent with high $r$ or high $\sigma^2$ shrinking $s^*$.</li>
        <li><strong>Taxi medallions vs Uber drivers.</strong> Salaried taxi drivers (flat $s$) versus self-employed Uber drivers ($s$ close to 1) sit at different ends of the trade-off. Hall and Krueger (2018) on Uber driver heterogeneity suggests sorting by risk tolerance.</li>
        <li><strong>Evaluation move (Doornik).</strong> The trade-off is not absolute. Better monitoring technology (cameras, GPS, software analytics) raises the informativeness of signals and shifts $s^*$ towards lower-powered contracts without sacrificing effort.</li>
        <li><strong>Evaluation move.</strong> The CARA-normal model treats the trade-off as a smooth, unique interior optimum. With limited liability or DARA, the trade-off can produce corner solutions (agent rents, no participation).</li>
        <li><strong>Evaluation move.</strong> Behavioural agents (loss-averse, intrinsically motivated) complicate the calculus. Benabou and Tirole (2003) show high-powered incentives can crowd out intrinsic motivation, flipping the sign of the trade-off.</li>
        <li><strong>Limitation.</strong> The trade-off is a comparative-static claim about a fixed-information environment. Once signals are endogenous (the agent chooses what to disclose), see [[Concepts/Multitasking]] for distortions across measurable and unmeasurable activities.</li>
        </ul>""",
    },
    "wage-bounds-limited-liability": {
        "math": r"""<p><strong>Limited liability</strong> imposes a floor $w(x) \geq \underline w$ on wages, often $\underline w = 0$ (no negative wages) or $\underline w = -W$ where $W$ is the agent's wealth. The constraint binds in second-best problems with risky output: the principal would like to punish bad outcomes more severely than the floor allows.</p>
        <p>Risk-neutral agent with limited liability. Two output levels $x_L < x_H$, two efforts $e_L < e_H$. Let $p_H = \Pr(x_H \mid e_H), p_L = \Pr(x_H \mid e_L)$ with $p_H > p_L$. The principal picks $w_L, w_H \geq 0$ to implement $e_H$.</p>
        <ol>
        <li>IC: $p_H w_H + (1 - p_H) w_L - c \geq p_L w_H + (1 - p_L) w_L$, simplifying to $(p_H - p_L)(w_H - w_L) \geq c$.</li>
        <li>IR: $p_H w_H + (1 - p_H) w_L - c \geq 0$.</li>
        <li>Limited liability (LL): $w_L \geq 0, w_H \geq 0$.</li>
        <li>Without LL, the principal sets $w_L < 0$ to extract surplus, IR binds, agent gets $\bar u$. With LL, $w_L = 0$ binds (the cheapest way to satisfy LL), and IC then forces $w_H = c/(p_H - p_L)$.</li>
        <li>Agent's expected utility $= p_H \cdot c/(p_H - p_L) - c = c \cdot p_L/(p_H - p_L) > 0$, strictly above the outside option. The agent earns a <strong>limited liability rent</strong>.</li>
        </ol>
        <p>Implications. (1) IR becomes slack and IC binds; the binding constraint switches when LL is introduced. (2) The agent earns rents the principal cannot extract through a negative base wage. (3) The principal may prefer to implement low effort $e_L$ at zero wages rather than pay the rent for $e_H$; LL can shut down high-effort contracting altogether.</p>
        <p>With a risk-averse agent and LL, both effects compound: the risk premium for output risk plus the LL rent. The agency cost rises further. Innes (1990) and Sappington (1983) characterise LL contracts; debt-like (call option) wage structures with $w(x) = \max(0, x - K)$ often emerge.</p>
        <p>References: Micro2025.pdf Topic 8 Lectures (FHSMicroWk7), Bolton and Dewatripont Ch. 4.5, Sappington 1983 "Limited Liability Contracts between Principal and Agent", Innes 1990 "Limited Liability and Incentive Contracting".</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" id="widget-wage-bounds-limited-liability" role="img" aria-label="Wage schedule with limited liability floor">
          <defs><marker id="ll-arr" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L6,4 L0,8 z" fill="#333"/></marker></defs>
          <rect x="0" y="0" width="600" height="320" fill="white"/>
          <text x="300" y="22" text-anchor="middle" font-size="14" font-weight="bold">Limited Liability Truncates Wage Schedule</text>
          <line x1="70" y1="240" x2="560" y2="240" stroke="#333" stroke-width="1.5" marker-end="url(#ll-arr)"/>
          <line x1="70" y1="290" x2="70" y2="50" stroke="#333" stroke-width="1.5" marker-end="url(#ll-arr)"/>
          <text x="565" y="255" font-size="12">output $x$</text>
          <text x="30" y="55" font-size="12">wage $w$</text>
          <line x1="70" y1="280" x2="200" y2="240" stroke="#1f77b4" stroke-width="2" stroke-dasharray="5,4"/>
          <text x="100" y="295" font-size="11" fill="#1f77b4">would-be $w<0$</text>
          <line x1="70" y1="240" x2="200" y2="240" stroke="#2ca02c" stroke-width="3"/>
          <line x1="200" y1="240" x2="560" y2="100" stroke="#2ca02c" stroke-width="3"/>
          <text x="430" y="105" font-size="12" fill="#2ca02c">LL contract</text>
          <line x1="70" y1="240" x2="560" y2="240" stroke="#d62728" stroke-dasharray="3,3"/>
          <text x="400" y="235" font-size="11" fill="#d62728">floor $w = 0$</text>
          <text x="300" y="310" text-anchor="middle" font-size="11" fill="#555">Caption: principal cannot punish below the floor, so the agent collects a rent at low outputs.</text>
        </svg>""",
        "examples": r"""<ul>
        <li><strong>Debt contracts and entrepreneurship.</strong> Innes (1990) shows that the optimal LL contract between an outside investor and an entrepreneur with hidden effort takes the form of risky debt: pay $\min(x, R)$ to investor, residual to entrepreneur, mimicking standard debt.</li>
        <li><strong>Minimum wage as a limited liability floor.</strong> A statutory floor on hourly wages binds the second-best problem; firms substitute towards effort norms, monitoring, and bonus structures rather than negative pay.</li>
        <li><strong>Evaluation move (Doornik).</strong> LL converts the problem from risk-sharing to rent extraction. The agent earns positive rents even with risk neutrality, contradicting the textbook result that risk-neutral agents always reach the first-best.</li>
        <li><strong>Evaluation move.</strong> The interaction of LL with risk aversion is non-trivial: LL alone gives rents to a risk-neutral agent; risk aversion alone gives no rents but imposes risk premia. Together they raise agency cost super-additively.</li>
        <li><strong>Evaluation move.</strong> Limited liability rationalises why low-output workers are not fired or fined heavily: the threat is non-credible under bankruptcy law. Levin (2003) on relational contracts builds on this.</li>
        <li><strong>Limitation.</strong> The basic model abstracts from collateral and signalling, which can relax LL by letting the agent post bonds. See [[Concepts/Second-Best Contract]] for the unconstrained benchmark.</li>
        </ul>""",
    },
    "monotone-likelihood-ratio": {
        "math": r"""<p>The <strong>monotone likelihood ratio property (MLRP)</strong> is a structural condition on the family of output densities $\{f(x \mid e)\}_e$ that guarantees the optimal second-best wage schedule $w(x)$ is monotonically increasing in output $x$. Without MLRP, $w(x)$ can be non-monotone even when higher effort raises mean output.</p>
        <p>Definition. The family $f(x \mid e)$ satisfies MLRP if for any $e_H > e_L$, the likelihood ratio</p>
        <p>$\mathrm{LR}(x) = \dfrac{f(x \mid e_H)}{f(x \mid e_L)}$</p>
        <p>is non-decreasing in $x$. Equivalently, high outputs are relatively more likely under high effort than under low effort.</p>
        <ol>
        <li>From the Mirrlees-Holmstrom FOC: $\dfrac{1}{u'(w(x))} = \lambda + \mu \left(1 - \dfrac{f(x \mid e_L)}{f(x \mid e_H)}\right) = \lambda + \mu \left(1 - \dfrac{1}{\mathrm{LR}(x)}\right)$.</li>
        <li>The right-hand side is increasing in $x$ iff $\mathrm{LR}(x)$ is increasing in $x$, that is, iff MLRP holds.</li>
        <li>Since $u$ is concave, $1/u'$ is increasing in $w$, so $w(x)$ is increasing in $x$ when MLRP holds.</li>
        <li>Examples of MLRP families: normal $N(e, \sigma^2)$ with $e$ shifting mean; exponential with rate $\lambda(e)$ decreasing in $e$; Poisson with mean $e$; many one-parameter exponential families.</li>
        <li>Counterexample: bimodal output distribution where very high $x$ is consistent only with luck, not effort. The likelihood ratio peaks then falls; the wage schedule would optimally pay <em>less</em> at the very top, which is counter-intuitive and operationally awkward.</li>
        </ol>
        <p>MLRP is closely linked to <strong>first-order stochastic dominance (FOSD)</strong>: MLRP implies FOSD, but not vice versa. FOSD ensures higher effort raises mean output; MLRP ensures the wage schedule is well-behaved.</p>
        <p>Importance for the first-order approach. Mirrlees (1999) and Rogerson (1985) show that MLRP plus the <strong>convexity of distribution function condition (CDFC)</strong> jointly justify replacing the agent's IC constraint by its first-order condition. Without these conditions, the FOA can yield non-incentive-compatible contracts; the wage schedule must be re-derived using the full IC set.</p>
        <p>References: Micro2025.pdf Topic 8 Lectures (FHSMicroWk7), Milgrom 1981 "Good News and Bad News", Bolton and Dewatripont Ch. 4.4, Rogerson 1985 "The First-Order Approach to Principal-Agent Problems".</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" id="widget-monotone-likelihood-ratio" role="img" aria-label="Increasing likelihood ratio and monotone wage schedule">
          <defs><marker id="ml-arr" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L6,4 L0,8 z" fill="#333"/></marker></defs>
          <rect x="0" y="0" width="600" height="320" fill="white"/>
          <text x="300" y="22" text-anchor="middle" font-size="14" font-weight="bold">MLRP: $f_H/f_L$ Increasing in $x$ implies $w'(x) > 0$</text>
          <line x1="60" y1="270" x2="290" y2="270" stroke="#333" stroke-width="1.2" marker-end="url(#ml-arr)"/>
          <line x1="60" y1="270" x2="60" y2="50" stroke="#333" stroke-width="1.2" marker-end="url(#ml-arr)"/>
          <text x="295" y="285" font-size="11">$x$</text>
          <text x="35" y="55" font-size="11">$f_H/f_L$</text>
          <path d="M 60 230 Q 150 200 200 130 T 285 60" stroke="#1f77b4" stroke-width="2.5" fill="none"/>
          <text x="170" y="100" font-size="11" fill="#1f77b4">increasing LR</text>
          <line x1="320" y1="270" x2="560" y2="270" stroke="#333" stroke-width="1.2" marker-end="url(#ml-arr)"/>
          <line x1="320" y1="270" x2="320" y2="50" stroke="#333" stroke-width="1.2" marker-end="url(#ml-arr)"/>
          <text x="565" y="285" font-size="11">$x$</text>
          <text x="295" y="55" font-size="11">$w(x)$</text>
          <path d="M 320 240 Q 410 220 460 150 T 555 70" stroke="#2ca02c" stroke-width="2.5" fill="none"/>
          <text x="420" y="110" font-size="11" fill="#2ca02c">monotone wage</text>
          <text x="300" y="305" text-anchor="middle" font-size="11" fill="#555">Caption: MLRP delivers the natural-looking pay schedule; without it the wage may dip at high $x$.</text>
        </svg>""",
        "examples": r"""<ul>
        <li><strong>Sales bonus schemes.</strong> Most commission structures are monotone in sales: higher sales pay more. MLRP-style intuition rationalises this as the optimal contract when output is normally distributed around effort.</li>
        <li><strong>Production line piecework.</strong> Pay per unit produced rises with units. MLRP is plausible when defects are rare and each unit reflects independent attention from the worker.</li>
        <li><strong>Evaluation move (Doornik).</strong> MLRP is sufficient for monotone wages but not necessary. Some non-MLRP densities still yield monotone optimal wages when combined with risk-averse preferences; the result depends on the joint structure.</li>
        <li><strong>Evaluation move.</strong> Milgrom (1981) "Good News and Bad News" frames MLRP as Bayesian: outputs are good news about high effort. The framing connects principal-agent to information design and statistical inference.</li>
        <li><strong>Evaluation move.</strong> MLRP can fail in tournaments and ranking contests where extreme outputs (winning by a huge margin) are noise-driven, not effort-driven. Lazear and Rosen (1981) tournament theory allows for this.</li>
        <li><strong>Limitation.</strong> MLRP is a primitive assumption with no direct empirical test. Many output processes (multimodal sales, project finance binary outcomes) violate it, requiring case-by-case analysis. See [[Concepts/Second-Best Contract]] for the underlying optimisation.</li>
        </ul>""",
    },
    "peltzman-effect": {
        "math": r"""<p>The <strong>Peltzman effect</strong> is the behavioural offset to safety regulation: when a dangerous activity is made safer through mandated equipment or rules, agents respond by acting more recklessly. The total risk reduction is less than the engineering reduction, and may even be reversed.</p>
        <p>Model. Agent chooses risky action $a$ (driving speed, exertion in sport) yielding utility $u(a) = b(a) - p(a, \theta) L$, where $b(a)$ is private benefit, $p(a, \theta)$ is accident probability decreasing in safety regulation $\theta$, and $L$ is loss size. Safety improves the regulation: $\partial p / \partial \theta < 0$.</p>
        <ol>
        <li>FOC for risky activity: $b'(a) = p_a(a, \theta) L$, where $p_a > 0$ (more recklessness raises accident probability).</li>
        <li>Comparative statics on $\theta$. Implicit differentiation: $\dfrac{da}{d\theta} = -\dfrac{p_{a\theta} L}{b''(a) - p_{aa} L}$. The denominator is negative (SOC for a max).</li>
        <li>The sign of $da/d\theta$ depends on $p_{a\theta}$. If $p_{a\theta} < 0$ (safety regulation reduces the marginal cost of recklessness more than the average), then $da/d\theta > 0$: agents take more risks when regulation increases.</li>
        <li>The total effect on accidents $\dfrac{dp}{d\theta} = p_\theta + p_a \cdot da/d\theta$. The first term is the direct safety effect (negative); the second is the behavioural offset (positive). Net effect can be small, zero, or even positive.</li>
        </ol>
        <p>The classic example is mandatory seatbelt laws (Peltzman 1975). Seatbelts make accidents less fatal for drivers, lowering the marginal cost of fast driving. Drivers respond by driving faster, raising accident frequency. Pedestrian fatalities can rise even if driver fatalities fall. Peltzman estimated that the safety regulation produced little net change in total fatalities, with the gain to drivers offset by losses to pedestrians and cyclists.</p>
        <p>Mechanism. The Peltzman effect is a special case of <strong>moral hazard</strong>: lower private cost of risky action induces more risky action. It differs from insurance moral hazard in that the "insurance" is provided by technology rather than a contract. The lesson generalises to football helmets (Pop Warner concussion data), ABS brakes, and ski helmets.</p>
        <p>Empirical status: contested. Peltzman's 1975 study has been challenged (Robertson 1977 dispute, more recent meta-analyses). The effect appears to exist but is typically smaller than the engineering safety gain, so net safety improves but by less than projected.</p>
        <p>References: Micro2025.pdf Topic 8 Lectures (FHSMicroWk7), Peltzman 1975 JPE "The Effects of Automobile Safety Regulation", Mas-Colell Ch. 14.B for the general moral hazard framework.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" id="widget-peltzman-effect" role="img" aria-label="Peltzman effect: behavioural offset to safety regulation">
          <defs><marker id="pe-arr" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L6,4 L0,8 z" fill="#333"/></marker></defs>
          <rect x="0" y="0" width="600" height="320" fill="white"/>
          <text x="300" y="22" text-anchor="middle" font-size="14" font-weight="bold">Peltzman: Behavioural Offset to Safety Gain</text>
          <line x1="70" y1="270" x2="560" y2="270" stroke="#333" stroke-width="1.5" marker-end="url(#pe-arr)"/>
          <line x1="70" y1="270" x2="70" y2="50" stroke="#333" stroke-width="1.5" marker-end="url(#pe-arr)"/>
          <text x="565" y="285" font-size="12">safety regulation $\theta$</text>
          <text x="30" y="55" font-size="12">total risk</text>
          <line x1="70" y1="80" x2="560" y2="240" stroke="#1f77b4" stroke-width="2.5"/>
          <text x="440" y="232" font-size="12" fill="#1f77b4">engineering effect alone</text>
          <path d="M 70 80 Q 200 150 350 160 T 560 190" stroke="#d62728" stroke-width="2.5" fill="none"/>
          <text x="380" y="195" font-size="12" fill="#d62728">actual: behavioural offset</text>
          <line x1="300" y1="160" x2="300" y2="200" stroke="#666" stroke-dasharray="3,3"/>
          <text x="305" y="180" font-size="11" fill="#666">offset gap</text>
          <text x="300" y="305" text-anchor="middle" font-size="11" fill="#555">Caption: safer cars yield smaller actual risk reduction than the engineering calculation predicts.</text>
        </svg>""",
        "examples": r"""<ul>
        <li><strong>Seatbelt mandates and driving speed.</strong> Peltzman (1975) and later replications find drivers speed up modestly after seatbelt adoption. Pedestrian fatalities rose in some samples, consistent with the behavioural offset.</li>
        <li><strong>Anti-lock brakes and following distance.</strong> Sagberg et al. (1997) on taxi drivers in Oslo find drivers with ABS follow other cars more closely, offsetting part of the safety improvement.</li>
        <li><strong>Evaluation move (Doornik).</strong> The Peltzman effect is a partial-equilibrium prediction. General-equilibrium reasoning suggests that safer cars lower the cost of driving, raising total miles driven; this congestion effect can dominate the speed effect on aggregate fatalities.</li>
        <li><strong>Evaluation move.</strong> Welfare analysis is ambiguous: drivers may rationally prefer faster, riskier driving once protected. The Peltzman offset is not a market failure; it is the optimal response to changed prices.</li>
        <li><strong>Evaluation move.</strong> Empirical magnitudes vary. Cohen and Einav (2003) on seatbelt laws find essentially zero offset for the driver; the engineering effect dominates. The size of the offset depends on the activity and population.</li>
        <li><strong>Limitation.</strong> The effect requires that agents perceive and respond to the safety change. Unobserved risks (asbestos, radiation) do not generate Peltzman offsets. Linked to [[Concepts/Moral Hazard in Insurance]] as a non-contractual analogue.</li>
        </ul>""",
    },
    "holmstrom-milgrom-model": {
        "math": r"""<p>The <strong>Holmstrom-Milgrom (1987) model</strong> shows that linear pay-for-performance contracts are <em>exactly optimal</em> in a continuous-time agency setting with CARA utility, Brownian noise, and the agent controlling the drift of output. The result rationalises the linear contracts seen in practice and underlies the standard $s^* = 1/(1 + r \sigma^2 c)$ formula.</p>
        <p>Setup. Time $t \in [0, 1]$. Output $X_t$ follows $dX_t = e_t \, dt + \sigma \, dB_t$, where $e_t$ is the agent's effort process and $B_t$ is standard Brownian motion. The agent has CARA utility $u(w) = -\exp(-r w)$ and effort cost flow $c(e_t) = \tfrac{1}{2} c \, e_t^2$, additively separable across time.</p>
        <ol>
        <li>The agent observes the path of $X_t$ continuously and chooses $e_t$ dynamically. The principal designs a contract $w$ as a function of the realised path $\{X_s\}_{s \in [0, 1]}$ paid at $t = 1$.</li>
        <li>Holmstrom and Milgrom prove: the optimal contract is <em>linear</em> in the terminal output $X_1$, namely $w = t + s X_1$, with $s^* = 1/(1 + r \sigma^2 c)$ (where $\sigma^2$ now denotes the total variance of $X_1$).</li>
        <li>Intuition: the linearity is the unique contract robust to the agent's freedom to adjust effort dynamically in response to interim outcomes. Any nonlinear contract gives the agent the option to game the schedule (raise effort when behind, slack when ahead); the optimum eliminates this option value.</li>
        <li>The agent's optimal effort is constant in time: $e_t^* = s^*/c$. Effort does not depend on the realised path because CARA preferences are wealth-independent.</li>
        <li>Implementation: pay the agent $t + s^* X_1$ at $t = 1$, where $t$ is set by IR: $t = \bar u - s^* e^* + \tfrac{1}{2} r (s^*)^2 \sigma^2 + \tfrac{1}{2} c (e^*)^2$.</li>
        </ol>
        <p>Why linearity is special. In static models with two effort levels and discrete output, the optimal contract is generally nonlinear (the Mirrlees-Holmstrom schedule). HM 1987 closes a gap between theory (nonlinear) and practice (linear) by showing that adding dynamic effort choice plus CARA-normal structure forces linearity.</p>
        <p>The 1991 extension. Holmstrom and Milgrom (1991) "Multitask Principal-Agent" extends to vector effort and multiple output signals, deriving the multitask linear contract $w = t + s' x$ with $s = (\mathrm{Cov}^{-1} \cdot ...)$. The single-task case nests in.</p>
        <p>References: Micro2025.pdf Topic 8 Lectures (FHSMicroWk7), Holmstrom and Milgrom 1987 Econometrica "Aggregation and Linearity in the Provision of Intertemporal Incentives", Holmstrom and Milgrom 1991 JLEO "Multitask Principal-Agent", Bolton and Dewatripont Ch. 4.6.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" id="widget-holmstrom-milgrom-model" role="img" aria-label="Holmstrom-Milgrom Brownian output and linear contract">
          <defs><marker id="hm-arr" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L6,4 L0,8 z" fill="#333"/></marker></defs>
          <rect x="0" y="0" width="600" height="320" fill="white"/>
          <text x="300" y="22" text-anchor="middle" font-size="14" font-weight="bold">Brownian Output, Linear Contract on Terminal Value</text>
          <line x1="70" y1="270" x2="560" y2="270" stroke="#333" stroke-width="1.5" marker-end="url(#hm-arr)"/>
          <line x1="70" y1="270" x2="70" y2="50" stroke="#333" stroke-width="1.5" marker-end="url(#hm-arr)"/>
          <text x="565" y="285" font-size="12">time $t$</text>
          <text x="30" y="55" font-size="12">$X_t$</text>
          <path d="M 70 250 L 100 230 L 130 235 L 170 215 L 210 220 L 250 195 L 290 200 L 330 175 L 370 185 L 410 160 L 450 155 L 490 130 L 530 140 L 560 110" stroke="#1f77b4" stroke-width="1.8" fill="none"/>
          <line x1="70" y1="270" x2="560" y2="160" stroke="#999" stroke-dasharray="3,3"/>
          <text x="500" y="155" font-size="11" fill="#666">drift $e \cdot t$</text>
          <circle cx="560" cy="110" r="5" fill="#d62728"/>
          <text x="500" y="100" font-size="11" fill="#d62728">$X_1$ realised</text>
          <text x="120" y="100" font-size="12" fill="#1f77b4">$dX_t = e\,dt + \sigma\,dB_t$</text>
          <text x="120" y="120" font-size="12" fill="#2ca02c">$w = t + s^* X_1$, linear</text>
          <text x="300" y="305" text-anchor="middle" font-size="11" fill="#555">Caption: payment depends only on the terminal value of the diffusion process.</text>
        </svg>""",
        "examples": r"""<ul>
        <li><strong>Investment manager fee structures.</strong> Hedge fund "2 and 20" (2 percent base, 20 percent of profit above high water mark) approximates a linear share of terminal value, consistent with HM 1987 logic in a Brownian asset price setting.</li>
        <li><strong>Sales bonuses on year-end totals.</strong> Linear commission on full-year sales rather than monthly thresholds avoids the gaming problem HM identify: workers cannot smooth effort to exploit kinks.</li>
        <li><strong>Evaluation move (Doornik).</strong> The HM result is fragile to deviations from the CARA-normal structure. With wealth effects (DARA), risk aversion, or non-Gaussian noise, the linear contract is only an approximation.</li>
        <li><strong>Evaluation move.</strong> The model treats time horizon as exogenous. Endogenous horizon (project completion, retirement) breaks the simple linearity result; see Sannikov (2008) on continuous-time agency with stochastic horizons.</li>
        <li><strong>Evaluation move.</strong> HM rationalises linearity from a single mechanism, but empirically linear pay reflects many factors: gaming resistance, transparency, fairness, regulatory simplicity. Murphy (1999) compensation handbook surveys.</li>
        <li><strong>Limitation.</strong> The result assumes a single risk-neutral principal and observable terminal output. With renegotiation, multiple principals, or multitasking, linearity can be suboptimal. See [[Concepts/Multitasking]].</li>
        </ul>""",
    },

    "nash-equilibrium": {
        "math": r"""<p>A <strong>Nash equilibrium</strong> in a strategic-form game $G = (N, (S_i)_{i \in N}, (u_i)_{i \in N})$ is a strategy profile $s^* = (s_1^*, \dots, s_n^*)$ such that for every player $i$ and every alternative $s_i \in S_i$, $u_i(s_i^*, s_{-i}^*) \geq u_i(s_i, s_{-i}^*)$. No player can strictly improve by a unilateral deviation.</p>

<p>Equivalent definition via best responses: $s^*$ is Nash iff $s_i^* \in BR_i(s_{-i}^*)$ for every $i$, where $BR_i(s_{-i}) = \arg\max_{s_i} u_i(s_i, s_{-i})$. Equilibria are fixed points of the joint best-response correspondence.</p>

<ol>
<li>Construct the best-response function for each player. In Cournot with linear inverse demand $P = a - bQ$ and constant marginal cost $c$, firm $i$'s best response is $q_i = (a - c - b q_{-i})/(2b)$.</li>
<li>Impose symmetry $q_1 = q_2 = q^*$ and solve: $q^* = (a-c)/(3b)$, equilibrium price $p^* = (a + 2c)/3$.</li>
<li>Verify the equilibrium by checking no player wants to deviate: $\partial u_i / \partial s_i$ at $s^*$ equals zero and the second-order condition holds.</li>
</ol>

<p>Existence: Nash (1950) shows that every finite game admits a (possibly mixed) Nash equilibrium. The proof uses Kakutani's fixed-point theorem on the best-response correspondence, which is upper-hemicontinuous, non-empty, convex-valued.</p>

<p>Reference: Micro2025.pdf Topic 4 Lecture 1; Gibbons Ch. 1; Mas-Colell Ch. 8; Osborne and Rubinstein Ch. 2.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <line x1="60" y1="280" x2="540" y2="280" stroke="#333" stroke-width="2"/>
  <line x1="60" y1="280" x2="60" y2="40" stroke="#333" stroke-width="2"/>
  <text x="520" y="300" font-size="13">$q_2$</text>
  <text x="40" y="50" font-size="13">$q_1$</text>
  <line x1="60" y1="100" x2="380" y2="280" stroke="#1f77b4" stroke-width="2"/>
  <text x="100" y="95" font-size="12" fill="#1f77b4">$BR_1(q_2)$</text>
  <line x1="180" y1="280" x2="540" y2="80" stroke="#d62728" stroke-width="2"/>
  <text x="400" y="100" font-size="12" fill="#d62728">$BR_2(q_1)$</text>
  <circle cx="240" cy="200" r="6" fill="#2ca02c"/>
  <text x="250" y="195" font-size="13" fill="#2ca02c">Nash $E^*$</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Cournot best-response functions intersect at the Nash equilibrium where neither firm wants to deviate.</p>""",
        "examples": r"""<ul>
<li><strong>Cournot output competition.</strong> Two firms simultaneously choose quantities. The Nash equilibrium has both producing $(a-c)/(3b)$, total industry output $2(a-c)/(3b)$, higher than monopoly and lower than perfect competition.</li>
<li><strong>Bertrand price competition.</strong> With homogeneous goods and constant marginal cost, the unique Nash equilibrium is $p_1 = p_2 = c$, zero profit. The Bertrand paradox: just two firms suffice for the competitive outcome.</li>
<li><strong>Penalty shootouts.</strong> Chiappori, Levitt, and Groseclose (2002) show that professional footballers play (approximately) mixed-strategy Nash equilibria in kick direction, with shooting frequencies matched to goalkeeper responses.</li>
<li><strong>Essay move.</strong> Nash is a positive solution concept, not a normative one. Equilibria can be Pareto-inefficient (Prisoner's Dilemma), inequitable, or socially harmful. Doornik rewards explicit attention to multiplicity and refinement.</li>
<li><strong>Essay move.</strong> Distinguish pure-strategy from mixed-strategy Nash. Matching Pennies has no pure-strategy NE but a unique mixed NE. The Battle of the Sexes has two pure-strategy NE and one mixed NE.</li>
<li><strong>Limitation.</strong> Nash equilibrium assumes common knowledge of rationality and the game's payoffs. In games with incomplete information, the right concept is Bayes-Nash equilibrium; with sequential structure, subgame-perfect equilibrium.</li>
<li>See also [[Concepts/Subgame Perfect Equilibrium]], [[Concepts/Best Response Functions]], and [[Concepts/Mixed Strategy Equilibrium]].</li>
</ul>""",
    },
    "mixed-strategy-equilibrium": {
        "math": r"""<p>A <strong>mixed strategy</strong> for player $i$ is a probability distribution $\sigma_i \in \Delta(S_i)$ over pure strategies. Expected utility is $u_i(\sigma) = \sum_{s \in S} \prod_j \sigma_j(s_j) \cdot u_i(s)$. A <strong>mixed-strategy Nash equilibrium</strong> is a profile $\sigma^*$ such that for each $i$, $\sigma_i^*$ is a best response to $\sigma_{-i}^*$ in the expanded strategy set $\Delta(S_i)$.</p>

<p>The key characterisation: player $i$ randomises over a set of pure strategies only if all those strategies yield the same expected payoff against $\sigma_{-i}^*$. This is the <strong>indifference condition</strong> and it pins down mixing probabilities.</p>

<ol>
<li>In Matching Pennies with payoffs $(1, -1)$ for matches and $(-1, 1)$ for mismatches, let player 1 mix $H$ with probability $p$ and player 2 mix $H$ with probability $q$.</li>
<li>Player 1's expected payoff to $H$ is $q - (1-q) = 2q - 1$; to $T$ is $(1-q) - q = 1 - 2q$. Indifference gives $q^* = 1/2$.</li>
<li>Symmetrically $p^* = 1/2$. The unique mixed-strategy Nash equilibrium is $(\sigma_1, \sigma_2) = ((1/2, 1/2), (1/2, 1/2))$ with expected payoff 0 to both.</li>
</ol>

<p>Existence (Nash 1950): every finite game has at least one mixed Nash equilibrium. The proof uses Brouwer or Kakutani applied to the best-response correspondence $BR: \Delta(S) \to \Delta(S)$.</p>

<p>Interpretation: mixed strategies can be read as deliberate randomisation, as beliefs about opponents in a population, or as the steady state of a learning process. The population interpretation (Harsanyi 1973) is often the cleanest.</p>

<p>Reference: Micro2025.pdf Topic 4 Lecture 2; Gibbons Ch. 1.3; Osborne-Rubinstein Ch. 3.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <line x1="60" y1="280" x2="540" y2="280" stroke="#333" stroke-width="2"/>
  <line x1="60" y1="280" x2="60" y2="40" stroke="#333" stroke-width="2"/>
  <text x="520" y="300" font-size="13">$q$ (player 2 mixes H)</text>
  <text x="40" y="50" font-size="13">$p$ (player 1 mixes H)</text>
  <line x1="300" y1="40" x2="300" y2="280" stroke="#1f77b4" stroke-width="2"/>
  <text x="305" y="60" font-size="12" fill="#1f77b4">$BR_1$: $p$ free if $q=1/2$</text>
  <line x1="60" y1="160" x2="540" y2="160" stroke="#d62728" stroke-width="2"/>
  <text x="65" y="155" font-size="12" fill="#d62728">$BR_2$: $q$ free if $p=1/2$</text>
  <circle cx="300" cy="160" r="6" fill="#2ca02c"/>
  <text x="310" y="155" font-size="13" fill="#2ca02c">$(1/2, 1/2)$</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Matching Pennies: best responses intersect at the unique mixed equilibrium $(1/2, 1/2)$, the only profile satisfying mutual indifference.</p>""",
        "examples": r"""<ul>
<li><strong>Penalty kicks.</strong> Empirical work (Palacios-Huerta 2003) finds that elite footballers' kick directions are statistically indistinguishable from the mixed equilibrium prediction, even though most players cannot articulate the logic.</li>
<li><strong>Tax audits.</strong> A revenue authority cannot audit everyone, so it commits to auditing a fraction $q$ of returns. Honest reporting requires $q$ large enough that the expected penalty exceeds the gain from cheating, a mixed-strategy equilibrium between auditors and filers.</li>
<li><strong>Market entry timing.</strong> When two firms consider entering a market that can only sustain one entrant, the mixed equilibrium has each entering with the probability that leaves the other indifferent.</li>
<li><strong>Essay move.</strong> The indifference condition implies that mixing probabilities depend on the opponent's payoffs, not the player's own. This is the counterintuitive part: changing my own payoffs changes the opponent's randomisation, not mine.</li>
<li><strong>Essay move.</strong> Mixed strategies are necessary for existence (Nash 1950). In Matching Pennies, no pure profile is an equilibrium, but $(1/2, 1/2)$ is. Doornik rewards explicit invocation of Nash's existence proof.</li>
<li><strong>Limitation.</strong> Mixed equilibria are often unstable to learning dynamics and to small perturbations of the payoffs. Purification (Harsanyi 1973) helps: a mixed equilibrium in a complete-information game is the limit of pure-strategy Bayes-Nash equilibria in nearby incomplete-information games.</li>
<li>See also [[Concepts/Matching Pennies]], [[Concepts/Nash Existence Theorem]], [[Concepts/Best Response Functions]].</li>
</ul>""",
    },
    "dominance": {
        "math": r"""<p>Strategy $s_i$ <strong>strictly dominates</strong> $s_i'$ for player $i$ if $u_i(s_i, s_{-i}) > u_i(s_i', s_{-i})$ for every $s_{-i} \in S_{-i}$. A rational player never plays a strictly dominated strategy. <strong>Weak dominance</strong> replaces the strict inequality with $\geq$, with strict inequality for at least one $s_{-i}$.</p>

<p>A strategy $s_i$ is <strong>strictly dominated</strong> if some other strategy strictly dominates it. By extension, $s_i$ is strictly dominated by a mixed strategy $\sigma_i$ if $u_i(\sigma_i, s_{-i}) > u_i(s_i, s_{-i})$ for every $s_{-i}$.</p>

<ol>
<li>Identify pure-strategy dominance by comparing rows (or columns) of the payoff matrix entry by entry.</li>
<li>Check mixed-strategy dominance: a pure strategy can be strictly dominated by a mix of other strategies even when no single pure strategy dominates it.</li>
<li>Iterate: after eliminating strictly dominated strategies, recheck the reduced game.</li>
</ol>

<p>Result (Pearce 1984, Bernheim 1984): the set of <strong>rationalisable</strong> strategies is the largest set $R_i \subseteq S_i$ for each player such that every $s_i \in R_i$ is a best response to some belief over $R_{-i}$. Rationalisable strategies survive iterated elimination of strictly dominated strategies (IESDS).</p>

<p>Order of elimination does not matter for strict dominance: the IESDS limit is unique. For weak dominance, order matters and the answer depends on the elimination path.</p>

<p>Reference: Micro2025.pdf Topic 4 Lecture 1; Gibbons Ch. 1.1.B; Mas-Colell Ch. 8.B.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <text x="200" y="40" font-size="14" font-weight="bold">Prisoner's Dilemma</text>
  <line x1="160" y1="60" x2="160" y2="260" stroke="#333"/>
  <line x1="60" y1="160" x2="460" y2="160" stroke="#333"/>
  <text x="200" y="85" font-size="13">Cooperate</text>
  <text x="340" y="85" font-size="13">Defect</text>
  <text x="80" y="120" font-size="13">Cooperate</text>
  <text x="80" y="220" font-size="13">Defect</text>
  <text x="200" y="125" font-size="13">3, 3</text>
  <text x="340" y="125" font-size="13">0, 4</text>
  <text x="200" y="225" font-size="13">4, 0</text>
  <text x="340" y="225" font-size="13" fill="#d62728" font-weight="bold">1, 1</text>
  <text x="480" y="200" font-size="12" fill="#d62728">Defect strictly</text>
  <text x="480" y="218" font-size="12" fill="#d62728">dominates Cooperate</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Defect strictly dominates Cooperate for both players, yet (D, D) is Pareto-inferior to (C, C).</p>""",
        "examples": r"""<ul>
<li><strong>Prisoner's Dilemma.</strong> Defect strictly dominates Cooperate for each prisoner. IESDS predicts (D, D), which is Pareto-inferior to (C, C). The canonical illustration that dominance is not normative.</li>
<li><strong>Second-price auctions.</strong> Bidding your true valuation $v_i$ is a weakly dominant strategy: you never benefit from misreporting. The Vickrey auction owes its incentive-compatibility to weak dominance.</li>
<li><strong>Cournot duopoly with capacity ceilings.</strong> Quantities above $(a-c)/b$ are strictly dominated, since they always yield negative profit. After two rounds of IESDS, the strategy set shrinks to the rationalisable interval.</li>
<li><strong>Essay move.</strong> Distinguish strict from weak dominance. Strict allows unique IESDS; weak does not. This matters when comparing the BNE of a second-price auction (multiple equilibria, only one in weakly undominated strategies) to the dominant-strategy version.</li>
<li><strong>Essay move.</strong> Rationalisability is weaker than Nash. Every Nash equilibrium is rationalisable, but not conversely. In the Beauty Contest game, only "guess 0" is rationalisable.</li>
<li><strong>Limitation.</strong> Dominance arguments are sensitive to the cardinal payoff representation in non-vNM contexts. They are also weak when very few or no strategies are dominated, as in Battle of the Sexes.</li>
<li>See also [[Concepts/Iterated Elimination of Strictly Dominated Strategies]], [[Concepts/Strict vs Weak Dominance]].</li>
</ul>""",
    },
    "subgame-perfect-equilibrium": {
        "math": r"""<p>An extensive-form game $\Gamma$ has a <strong>subgame</strong> at every information set that is a singleton and is reached with positive probability under any strategy. A <strong>subgame perfect equilibrium</strong> (SPE) is a strategy profile $\sigma^*$ such that the restriction of $\sigma^*$ to every subgame is a Nash equilibrium of that subgame.</p>

<p>SPE refines Nash by eliminating equilibria that rely on non-credible threats off the equilibrium path. The standard solution algorithm for finite games of perfect information is <strong>backward induction</strong>: solve the game from the terminal nodes back to the root.</p>

<ol>
<li>Start at each terminal subgame (decision node closest to a leaf). Pick the action that maximises the active player's payoff.</li>
<li>Replace each terminal subgame with its solved continuation value.</li>
<li>Move up one level and repeat until the root is reached. The collection of optimal actions is the unique SPE (Zermelo 1913, Kuhn 1953).</li>
</ol>

<p>Example: Stackelberg duopoly with leader $L$ choosing $q_L$ first, follower $F$ observing and choosing $q_F$. The follower's best response is $q_F(q_L) = (a - c - b q_L)/(2b)$. The leader maximises $(a - b q_L - b q_F(q_L) - c) q_L$, giving $q_L^* = (a-c)/(2b)$ and $q_F^* = (a-c)/(4b)$. Leader profit is twice the symmetric Cournot profit.</p>

<p>For games with simultaneous moves within a stage or imperfect information, SPE may not be the right refinement. The correct concept is <strong>perfect Bayesian equilibrium</strong> (PBE), which adds belief consistency conditions on information sets.</p>

<p>Reference: Micro2025.pdf Topic 4 Lecture 2; Gibbons Ch. 2; Fudenberg-Tirole Ch. 3.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <circle cx="300" cy="50" r="8" fill="#333"/>
  <text x="310" y="55" font-size="12">Entrant</text>
  <line x1="300" y1="58" x2="180" y2="140" stroke="#333" stroke-width="2"/>
  <line x1="300" y1="58" x2="420" y2="140" stroke="#333" stroke-width="2"/>
  <text x="220" y="100" font-size="12">Stay out</text>
  <text x="360" y="100" font-size="12">Enter</text>
  <text x="160" y="170" font-size="12">(0, 10)</text>
  <circle cx="420" cy="150" r="8" fill="#1f77b4"/>
  <text x="430" y="155" font-size="12">Incumbent</text>
  <line x1="420" y1="158" x2="340" y2="240" stroke="#333" stroke-width="2"/>
  <line x1="420" y1="158" x2="500" y2="240" stroke="#333" stroke-width="2"/>
  <text x="350" y="200" font-size="12">Fight</text>
  <text x="460" y="200" font-size="12">Accommodate</text>
  <text x="310" y="270" font-size="12">(-2, -2)</text>
  <text x="480" y="270" font-size="12" fill="#2ca02c">(2, 4)</text>
  <text x="60" y="300" font-size="12" fill="#555">SPE: Entrant enters, Incumbent accommodates (fighting is not credible).</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Entry deterrence game. The threat to fight is not credible, so SPE predicts entry and accommodation.</p>""",
        "examples": r"""<ul>
<li><strong>Entry deterrence.</strong> An incumbent threatens to flood the market if a rival enters. If fighting is strictly worse than accommodating, the threat is empty: SPE predicts entry. Selten (1965) introduced SPE precisely to handle this case.</li>
<li><strong>Wage bargaining.</strong> In Rubinstein's alternating-offers model, the unique SPE has the first proposer get $1/(1+\delta)$ and the responder $\delta/(1+\delta)$. Equilibrium agreement is immediate, no delay.</li>
<li><strong>Tax compliance.</strong> A tax authority commits to audit probability $p$. Filers' SPE response is honest reporting iff the audit penalty exceeds the expected gain from cheating.</li>
<li><strong>Essay move.</strong> SPE rules out Nash equilibria supported by non-credible threats. The standard Doornik essay invokes the chain-store paradox to show that SPE can be too restrictive in long-horizon games (Selten 1978).</li>
<li><strong>Essay move.</strong> Backward induction requires common knowledge of rationality at every stage. Experimental evidence (centipede game) shows that subjects routinely deviate, suggesting bounded rationality or other-regarding preferences.</li>
<li><strong>Limitation.</strong> In games with infinite horizons or continuous time, backward induction can fail because there is no last node. Folk theorems rescue cooperation in repeated games by relaxing SPE's bite.</li>
<li>See also [[Concepts/Backward Induction]], [[Concepts/Credible Threat]], [[Concepts/Entry Deterrence]].</li>
</ul>""",
    },
    "backward-induction": {
        "math": r"""<p><strong>Backward induction</strong> is the algorithm for solving finite games of perfect information. Starting from the terminal nodes, at each decision node assign the action that maximises the active player's payoff, taking the continuation as given. The collection of optimal actions is the unique subgame-perfect equilibrium (Zermelo 1913, Kuhn 1953).</p>

<p>Formally: let $H$ denote the set of histories of length up to the maximum depth $T$. Define $V_T(h) = u(h)$ at terminal histories. Recursively for $t < T$ and history $h$ at depth $t$, let player $i(h)$ choose:</p>

$$a^*(h) = \arg\max_{a \in A(h)} V_{t+1}(h, a),$$

<p>where $V_{t+1}(h, a) = V_t(h')$ for the successor history $h' = (h, a)$. The SPE strategy $\sigma_i$ for each $i$ plays $a^*(h)$ at every history where $i$ moves.</p>

<ol>
<li>Identify all terminal nodes and their payoffs.</li>
<li>Work back one level: at each node whose successors are all terminal, the active player picks the action with the highest payoff. Record the resulting payoff vector.</li>
<li>Continue iterating, replacing solved subtrees with their continuation values, until the root is reached.</li>
</ol>

<p>Kuhn's theorem guarantees that a unique SPE exists in every finite extensive-form game of perfect information, and backward induction finds it. When information is imperfect (simultaneous moves, hidden actions), the procedure must be generalised to backward induction on subgames combined with belief consistency.</p>

<p>The centipede game illustrates a tension: backward induction predicts immediate stopping, but in laboratory experiments most players continue. This has motivated extensive work on epistemic foundations (Aumann 1995, Stalnaker 1998) and on bounded rationality.</p>

<p>Reference: Micro2025.pdf Topic 4 Lecture 2; Gibbons Ch. 2.1; Osborne-Rubinstein Ch. 6.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <circle cx="80" cy="160" r="8" fill="#333"/>
  <text x="80" y="145" font-size="12" text-anchor="middle">P1</text>
  <circle cx="200" cy="160" r="8" fill="#1f77b4"/>
  <text x="200" y="145" font-size="12" text-anchor="middle">P2</text>
  <circle cx="320" cy="160" r="8" fill="#333"/>
  <text x="320" y="145" font-size="12" text-anchor="middle">P1</text>
  <circle cx="440" cy="160" r="8" fill="#1f77b4"/>
  <text x="440" y="145" font-size="12" text-anchor="middle">P2</text>
  <line x1="88" y1="160" x2="192" y2="160" stroke="#333"/>
  <line x1="208" y1="160" x2="312" y2="160" stroke="#333"/>
  <line x1="328" y1="160" x2="432" y2="160" stroke="#333"/>
  <line x1="80" y1="168" x2="80" y2="220" stroke="#333"/>
  <line x1="200" y1="168" x2="200" y2="220" stroke="#333"/>
  <line x1="320" y1="168" x2="320" y2="220" stroke="#333"/>
  <line x1="440" y1="168" x2="440" y2="220" stroke="#333"/>
  <text x="80" y="240" font-size="12" text-anchor="middle">(1, 1)</text>
  <text x="200" y="240" font-size="12" text-anchor="middle">(0, 3)</text>
  <text x="320" y="240" font-size="12" text-anchor="middle">(2, 2)</text>
  <text x="440" y="240" font-size="12" text-anchor="middle">(1, 4)</text>
  <text x="500" y="160" font-size="12">(3, 3)</text>
  <line x1="448" y1="160" x2="490" y2="160" stroke="#333"/>
  <text x="80" y="280" font-size="12" fill="#d62728">SPE: stop at root</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Centipede game: backward induction unravels cooperation. Each player prefers to stop one move earlier than the opponent would, all the way back to the root.</p>""",
        "examples": r"""<ul>
<li><strong>Chess endgame analysis.</strong> When few pieces remain, backward induction from checkmate yields optimal play. Tablebases for 7-piece endgames have been computed exhaustively.</li>
<li><strong>Sequential bargaining.</strong> Rubinstein-Stahl alternating offers with discount factor $\delta$: backward induction from the last round (in finite-horizon versions) pins down the unique SPE, which has immediate agreement.</li>
<li><strong>Voting agendas.</strong> McKelvey (1979) shows that with a clever agenda, backward induction on a series of pairwise votes can produce any outcome the agenda-setter prefers, even one preferred by no majority over the status quo.</li>
<li><strong>Essay move.</strong> Backward induction depends on common knowledge of rationality at every node. The centipede game is the standard counterexample: experimental subjects continue much further than the SPE prediction.</li>
<li><strong>Essay move.</strong> Backward induction yields existence and uniqueness in finite perfect-information games (Kuhn). In games with simultaneous stages or chance moves, it generalises to backward induction on subgames combined with Bayes' rule.</li>
<li><strong>Limitation.</strong> The procedure fails in infinite-horizon games with no last node. It also requires strict preferences at each node, otherwise tie-breaking conventions matter.</li>
<li>See also [[Concepts/Subgame Perfect Equilibrium]], [[Concepts/Folk Theorem]].</li>
</ul>""",
    },
    "infinitely-repeated-games": {
        "math": r"""<p>An <strong>infinitely repeated game</strong> with stage game $G$, discount factor $\delta \in (0, 1)$, and players observing past actions perfectly is denoted $G^\infty(\delta)$. A strategy is a sequence of action plans, possibly conditioning on the entire history. Player $i$'s payoff is the discounted sum:</p>

$$U_i = (1 - \delta) \sum_{t = 0}^{\infty} \delta^t u_i(a^t).$$

<p>The $(1 - \delta)$ factor normalises so that average payoffs are directly comparable to one-shot payoffs.</p>

<p>The fundamental observation: cooperation can be sustained in $G^\infty$ by punishment strategies, even when it is impossible in the one-shot game. The simplest example is <strong>grim trigger</strong>: cooperate until any deviation, then play the stage Nash equilibrium forever. If the stage game is the Prisoner's Dilemma with cooperation payoff $c$, defection payoff $d > c$, and Nash payoff $n < c$, the grim trigger sustains cooperation iff:</p>

$$\frac{c}{1 - \delta} \geq d + \frac{\delta n}{1 - \delta} \quad \Longleftrightarrow \quad \delta \geq \delta^* = \frac{d - c}{d - n}.$$

<ol>
<li>Specify the stage game and identify Nash and cooperative payoffs.</li>
<li>Specify the trigger strategy and the punishment phase.</li>
<li>Compute the critical discount factor $\delta^*$ from the no-deviation condition.</li>
<li>Apply the one-shot deviation principle to verify subgame perfection.</li>
</ol>

<p>The <strong>folk theorem</strong> (Friedman 1971, Fudenberg-Maskin 1986) states that any payoff vector that is individually rational and feasible can be supported as a subgame-perfect equilibrium for $\delta$ close enough to 1. The set of equilibrium payoffs is generically large.</p>

<p>Reference: Micro2025.pdf Topic 4 Lecture 3; Gibbons Ch. 2.3; Mailath-Samuelson "Repeated Games and Reputations".</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <line x1="60" y1="280" x2="540" y2="280" stroke="#333" stroke-width="2"/>
  <line x1="60" y1="280" x2="60" y2="40" stroke="#333" stroke-width="2"/>
  <text x="540" y="300" font-size="13">$\delta$</text>
  <text x="40" y="50" font-size="13">payoff</text>
  <line x1="60" y1="200" x2="540" y2="200" stroke="#1f77b4" stroke-width="2" stroke-dasharray="4 2"/>
  <text x="80" y="195" font-size="12" fill="#1f77b4">defect payoff $d/(1-\delta) - \delta(d-n)/(1-\delta)$</text>
  <path d="M 60 240 Q 200 220 540 80" fill="none" stroke="#2ca02c" stroke-width="2"/>
  <text x="350" y="160" font-size="12" fill="#2ca02c">cooperate payoff $c/(1-\delta)$</text>
  <line x1="300" y1="40" x2="300" y2="280" stroke="#d62728" stroke-width="1" stroke-dasharray="3 3"/>
  <text x="305" y="60" font-size="12" fill="#d62728">$\delta^* = (d-c)/(d-n)$</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Cooperation sustains for $\delta \geq \delta^*$. The critical discount factor depends only on stage-game payoffs.</p>""",
        "examples": r"""<ul>
<li><strong>OPEC quotas.</strong> Sustaining cartel discipline requires that the future gains from continued cooperation exceed the one-shot deviation gain. Empirical estimates of OPEC discount factors are near or below the critical threshold, explaining frequent compliance failures.</li>
<li><strong>Cournot collusion.</strong> Two firms can sustain monopoly output via grim trigger if $\delta \geq (n - 1)/n$ for symmetric $n$-firm cases. Larger industries require higher discount factors, the standard explanation for why concentration aids collusion.</li>
<li><strong>Bilateral trade reputation.</strong> Klein and Leffler (1981) show that price premia and brand investments are mechanisms to sustain quality provision in repeated exchange.</li>
<li><strong>Essay move.</strong> Use the one-shot deviation principle when checking subgame perfection. The principle works in infinite-horizon games iff payoffs are continuous at infinity, which is automatic with discounting.</li>
<li><strong>Essay move.</strong> Distinguish trigger strategies (permanent punishment) from finite-period punishments (Abreu's stick-and-carrot). Doornik rewards essays that note these reduce the critical $\delta$.</li>
<li><strong>Limitation.</strong> The standard folk theorem assumes perfect observability. With imperfect monitoring (Green-Porter 1984), cooperation is harder and equilibrium prices fluctuate between phases of cooperation and punishment.</li>
<li>See also [[Concepts/Grim Trigger Strategy]], [[Concepts/Critical Discount Factor]], [[Concepts/Folk Theorem]].</li>
</ul>""",
    },
    "grim-trigger-strategy": {
        "math": r"""<p>The <strong>grim trigger strategy</strong> in an infinitely repeated game prescribes: cooperate in period 0; in period $t \geq 1$, cooperate iff all players cooperated in every previous period, otherwise play the stage Nash equilibrium forever. The punishment is permanent and triggered by any deviation.</p>

<p>Consider a symmetric stage game with cooperative payoff $c$, one-shot deviation payoff $d > c$, and stage Nash payoff $n < c$. Discount factor $\delta \in (0, 1)$. Both players play grim trigger. We check that no profitable deviation exists.</p>

<ol>
<li><strong>On the equilibrium path</strong> (no past deviation): cooperate. Payoff from continuing is $c + \delta c + \delta^2 c + \dots = c / (1 - \delta)$.</li>
<li><strong>Deviation payoff:</strong> defect once to gain $d$, trigger permanent punishment $n$ forever after: $d + \delta n / (1 - \delta)$.</li>
<li><strong>Incentive compatibility:</strong> $c/(1-\delta) \geq d + \delta n/(1 - \delta)$, which simplifies to $\delta \geq (d - c)/(d - n) \equiv \delta^*$.</li>
<li><strong>Off the equilibrium path</strong> (someone has deviated): play stage Nash. This is automatically a best response since $n$ is a Nash equilibrium of the stage game.</li>
</ol>

<p>The strategy profile is therefore a subgame-perfect equilibrium iff $\delta \geq \delta^*$.</p>

<p>Grim trigger gives the simplest folk theorem proof but has two drawbacks: punishments are infinitely costly to the punisher off path (renegotiation-proofness fails), and a single mistake destroys cooperation forever. Abreu (1986) shows that the most severe credible punishments can be achieved by finite "stick and carrot" schemes that are renegotiation-proof.</p>

<p>Reference: Micro2025.pdf Topic 4 Lecture 3; Friedman 1971; Mailath-Samuelson Ch. 2-3.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <text x="40" y="40" font-size="13" font-weight="bold">Grim trigger phase diagram</text>
  <rect x="60" y="80" width="160" height="80" fill="#a7f3d0" stroke="#10b981"/>
  <text x="140" y="125" font-size="13" text-anchor="middle">Cooperation</text>
  <rect x="380" y="80" width="160" height="80" fill="#fecaca" stroke="#dc2626"/>
  <text x="460" y="125" font-size="13" text-anchor="middle">Punishment</text>
  <line x1="220" y1="120" x2="380" y2="120" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  <text x="300" y="110" font-size="12" text-anchor="middle">Any defection</text>
  <path d="M 460 160 Q 460 200 460 160" fill="none" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  <text x="460" y="200" font-size="12" text-anchor="middle">Absorbing</text>
  <defs>
    <marker id="arrow" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
      <path d="M0,0 L8,4 L0,8 z" fill="#333"/>
    </marker>
  </defs>
  <text x="60" y="240" font-size="12" fill="#555">No path back to cooperation: punishment is absorbing.</text>
  <text x="60" y="270" font-size="12" fill="#555">Sustains cooperation iff $\delta \geq (d-c)/(d-n)$.</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Grim trigger has two phases: cooperation on the equilibrium path, permanent Nash punishment off path. The latter is absorbing.</p>""",
        "examples": r"""<ul>
<li><strong>Diamond cartels.</strong> De Beers (1888 to 2000s) used long-term contracts and threats of supply flooding to punish defectors. The system collapsed only when new entrants made the discount factor implicit in the punishment less credible.</li>
<li><strong>International trade agreements.</strong> WTO retaliation rules approximate grim trigger: a country violating obligations faces authorised tariffs from injured trading partners.</li>
<li><strong>Repeated work relationships.</strong> Long-term implicit contracts between employers and workers (efficiency wages, deferred compensation) use the threat of firing to sustain effort.</li>
<li><strong>Essay move.</strong> Grim trigger is the simplest folk-theorem strategy. It gives the lowest critical discount factor among permanent-punishment strategies because it imposes the worst credible punishment, the stage Nash payoff.</li>
<li><strong>Essay move.</strong> Doornik often asks whether grim trigger is renegotiation-proof. The answer is no: in the punishment phase, both players prefer to return to cooperation, so the punishment is not subgame stable to renegotiation. Farrell-Maskin (1989) addresses this.</li>
<li><strong>Limitation.</strong> A single observation error triggers permanent punishment. Under imperfect monitoring (Green-Porter 1984), trigger strategies generate occasional punishment phases on the equilibrium path. Real cartels need forgiving strategies.</li>
<li>See also [[Concepts/Tit-for-Tat Strategy]], [[Concepts/Critical Discount Factor]], [[Concepts/Nash Reversion Strategy]].</li>
</ul>""",
    },
    "critical-discount-factor": {
        "math": r"""<p>The <strong>critical discount factor</strong> $\delta^*$ is the threshold above which a given cooperative outcome is sustainable as a subgame-perfect equilibrium of an infinitely repeated game under a specified punishment strategy. For grim trigger in a symmetric stage game with cooperative payoff $c$, deviation payoff $d$, and Nash punishment payoff $n$:</p>

$$\delta^* = \frac{d - c}{d - n}.$$

<p>The derivation comes from the incentive constraint $c/(1 - \delta) \geq d + \delta n/(1 - \delta)$. Rearranging: $c \geq (1 - \delta) d + \delta n$, hence $\delta(d - n) \geq d - c$, giving $\delta \geq (d - c)/(d - n)$.</p>

<ol>
<li><strong>Symmetric Cournot collusion with $n$ firms.</strong> Cooperation = monopoly output split, deviation = optimal one-shot defection, Nash = $n$-firm Cournot. The critical $\delta^*$ rises with $n$: more firms means a larger one-shot gain and a smaller cooperative share each.</li>
<li><strong>Bertrand with homogeneous goods.</strong> Cooperation = monopoly price, Nash punishment = $p = c$, deviation = undercut by epsilon. The critical factor is $\delta^* = 1 - 1/n$ for $n$ symmetric firms.</li>
<li><strong>Two-firm Prisoner's Dilemma with $c = 3, d = 4, n = 1$:</strong> $\delta^* = (4-3)/(4-1) = 1/3$.</li>
</ol>

<p>The critical $\delta^*$ measures how patient players need to be. It rises in the temptation to deviate $(d - c)$ and falls in the harshness of punishment $(c - n)$. Real-world inferences about industry collusion often hinge on whether observed discount factors plausibly exceed $\delta^*$.</p>

<p>Reference: Micro2025.pdf Topic 4 Lecture 3, Topic 5 Lecture on Collusion; Tirole Ch. 6; Motta Ch. 4.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <line x1="60" y1="280" x2="540" y2="280" stroke="#333" stroke-width="2"/>
  <line x1="60" y1="280" x2="60" y2="40" stroke="#333" stroke-width="2"/>
  <text x="540" y="300" font-size="13">$n$ (firms)</text>
  <text x="40" y="50" font-size="13">$\delta^*$</text>
  <path d="M 100 240 Q 200 180 300 130 Q 400 90 540 60" fill="none" stroke="#1f77b4" stroke-width="2"/>
  <text x="200" y="160" font-size="12" fill="#1f77b4">$\delta^* = 1 - 1/n$</text>
  <line x1="60" y1="80" x2="540" y2="80" stroke="#d62728" stroke-width="1" stroke-dasharray="4 2"/>
  <text x="70" y="75" font-size="11" fill="#d62728">$\delta = 1$ (perfect patience)</text>
  <text x="60" y="300" font-size="12" fill="#555">More firms raise the patience threshold for cartel sustainability.</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">The critical discount factor for Bertrand cartelisation rises with the number of firms, approaching 1.</p>""",
        "examples": r"""<ul>
<li><strong>Cement industry.</strong> Average industry discount factors estimated from interest rates and write-off periods sit around 0.85 to 0.95. With 4 to 5 regional rivals, $\delta^* \approx 0.75$ for Bertrand collusion, so cartels are sustainable, consistent with frequent EU antitrust actions.</li>
<li><strong>OPEC discount factors.</strong> The political horizon of producer regimes is short, especially for low-reserves countries. Saudi compliance is greater than Venezuelan, consistent with differential $\delta$.</li>
<li><strong>Currency interventions.</strong> Central bank cooperation (Plaza Accord) requires that the future gains of joint action exceed the one-shot deviation gain from free-riding.</li>
<li><strong>Essay move.</strong> Show $\delta^*$ varies with the stage-game parameters. Doornik rewards explicit derivation of the comparative statics in $n$ (number of firms), price elasticity, and market growth rate.</li>
<li><strong>Essay move.</strong> Compare grim trigger to optimal punishment (Abreu 1986). The stick-and-carrot scheme delivers the same $\delta^*$ but is renegotiation-proof.</li>
<li><strong>Limitation.</strong> Real cartels face capacity constraints, demand uncertainty, and entry, all of which alter $\delta^*$. Empirical cartel research (Levenstein-Suslow 2006) finds cartels are more fragile than the textbook model suggests.</li>
<li>See also [[Concepts/Grim Trigger Strategy]], [[Concepts/Collusion Sustainability]].</li>
</ul>""",
    },
    "folk-theorem": {
        "math": r"""<p>The <strong>folk theorem</strong> characterises the set of payoffs achievable as subgame-perfect equilibria of an infinitely repeated game. Define the set of feasible payoff vectors as the convex hull $F$ of the stage payoffs, and the minmax payoff for player $i$ as $\underline{v}_i = \min_{a_{-i}} \max_{a_i} u_i(a_i, a_{-i})$. A payoff $v$ is <strong>individually rational</strong> if $v_i > \underline{v}_i$ for all $i$.</p>

<p>Folk theorem (Friedman 1971 for Nash punishments, Fudenberg-Maskin 1986 for subgame perfection): for any individually rational payoff $v \in F$ with $v_i > \underline{v}_i$ strict for all $i$, there exists $\bar\delta < 1$ such that for $\delta \in (\bar\delta, 1)$, $v$ is the average payoff of a subgame-perfect equilibrium of the discounted repeated game.</p>

<ol>
<li>Choose any target payoff $v$ that is feasible and strictly above all minmax payoffs.</li>
<li>Construct a path of action profiles whose average discounted payoff is $v$. Convex combinations of stage profiles approximate continuous payoffs via public randomisation or alternating phases.</li>
<li>Specify a punishment strategy that holds deviators to their minmax payoff for long enough to wipe out any one-shot gain.</li>
<li>Verify that the punishment is itself credible (subgame-perfect). Fudenberg-Maskin require dimensionality: the set of feasible payoffs must have full dimension, otherwise punishment cannot reward the punisher.</li>
</ol>

<p>Implication: the set of equilibrium payoffs is generically vast. Almost anything individually rational can be sustained, including monopoly profits, exact equality, and even Pareto-dominated outcomes.</p>

<p>For Nash-reversion punishments (Friedman), replace minmax with stage Nash payoff. The set of achievable equilibria is smaller but still typically large.</p>

<p>Reference: Micro2025.pdf Topic 4 Lecture 3; Fudenberg-Maskin 1986 Econometrica; Mailath-Samuelson Ch. 3.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <line x1="60" y1="280" x2="540" y2="280" stroke="#333" stroke-width="2"/>
  <line x1="60" y1="280" x2="60" y2="40" stroke="#333" stroke-width="2"/>
  <text x="520" y="300" font-size="13">$u_1$</text>
  <text x="40" y="50" font-size="13">$u_2$</text>
  <polygon points="100,260 460,260 460,80 100,80" fill="none" stroke="#1f77b4" stroke-width="2" stroke-dasharray="5 3"/>
  <text x="130" y="100" font-size="12" fill="#1f77b4">Feasible payoffs $F$</text>
  <polygon points="200,200 460,200 460,80 200,80" fill="#a7f3d0" fill-opacity="0.5" stroke="#10b981" stroke-width="2"/>
  <text x="320" y="150" font-size="13" fill="#065f46">Folk-theorem set</text>
  <line x1="200" y1="40" x2="200" y2="280" stroke="#d62728" stroke-width="1" stroke-dasharray="3 3"/>
  <text x="120" y="290" font-size="12" fill="#d62728">$\underline{v}_1$</text>
  <line x1="60" y1="200" x2="540" y2="200" stroke="#d62728" stroke-width="1" stroke-dasharray="3 3"/>
  <text x="40" y="208" font-size="12" fill="#d62728">$\underline{v}_2$</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Folk-theorem set: feasible payoffs strictly above both players' minmax values, all sustainable as SPE for $\delta$ near 1.</p>""",
        "examples": r"""<ul>
<li><strong>Cartel pricing.</strong> The folk theorem implies that any price between marginal cost and monopoly is sustainable in repeated Bertrand. Empirically observed cartel margins reflect bargaining and detection risk rather than uniqueness.</li>
<li><strong>Cooperation in evolutionary biology.</strong> Reciprocal altruism among long-lived animals (Trivers 1971) is the folk-theorem mechanism: long horizons make cooperation individually rational despite short-run temptations.</li>
<li><strong>International environmental agreements.</strong> The Montreal Protocol on ozone-depleting substances is sustained by trade sanctions, an explicit punishment scheme that delivers the cooperative outcome via folk-theorem logic.</li>
<li><strong>Essay move.</strong> The folk theorem is a curse and a blessing. It shows cooperation is sustainable but also shows that almost anything else is, undermining the predictive power of repeated-game theory. Doornik rewards explicit reflection on this multiplicity problem.</li>
<li><strong>Essay move.</strong> The dimensionality condition matters in symmetric games. In a two-player zero-sum game (no surplus to share), the folk theorem collapses to the value of the stage game.</li>
<li><strong>Limitation.</strong> The theorem assumes perfect monitoring and time-invariant payoffs. With imperfect monitoring (Green-Porter), only a smaller set of equilibrium payoffs is sustainable, and equilibrium prices may oscillate.</li>
<li>See also [[Concepts/Infinitely Repeated Games]], [[Concepts/Grim Trigger Strategy]], [[Concepts/Critical Discount Factor]].</li>
</ul>""",
    },
    "best-response-functions": {
        "math": r"""<p>Player $i$'s <strong>best response function</strong> (or correspondence) maps any profile of opponents' strategies $s_{-i}$ to the set of strategies that maximise $i$'s payoff: $BR_i(s_{-i}) = \arg\max_{s_i \in S_i} u_i(s_i, s_{-i})$. When the payoff is strictly concave and continuous in $s_i$, $BR_i$ is single-valued and continuous.</p>

<p>A Nash equilibrium is a fixed point of the joint best-response correspondence $BR: S \to S$ defined by $BR(s) = \prod_i BR_i(s_{-i})$. Existence of equilibrium amounts to existence of a fixed point.</p>

<ol>
<li>For each player, derive the first-order condition from $u_i(s_i, s_{-i})$ and solve for $s_i$ as a function of $s_{-i}$.</li>
<li>In Cournot with $P(Q) = a - bQ$ and constant marginal cost $c$, firm $i$ solves $\max (a - b(q_i + q_{-i}) - c) q_i$. FOC: $a - 2b q_i - b q_{-i} - c = 0$, giving $BR_i(q_{-i}) = (a - c - b q_{-i})/(2b)$.</li>
<li>In Bertrand with differentiated products $D_i(p_i, p_{-i})$, the best response is the price that maximises $(p_i - c) D_i(p_i, p_{-i})$.</li>
<li>Intersect best responses to find Nash equilibria.</li>
</ol>

<p>The slope of $BR$ classifies strategic interaction. If $\partial BR_i / \partial s_{-i} > 0$, strategies are <strong>strategic complements</strong> (Bertrand prices, R&D investment under positive spillovers). If $\partial BR_i / \partial s_{-i} < 0$, they are <strong>strategic substitutes</strong> (Cournot quantities, public good contributions). The sign matters for comparative statics: with complements, equilibrium responses to a shock amplify; with substitutes, they dampen.</p>

<p>Reference: Micro2025.pdf Topic 4 Lecture 1; Bulow-Geanakoplos-Klemperer 1985 JPE; Tirole Ch. 8.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <line x1="60" y1="280" x2="540" y2="280" stroke="#333" stroke-width="2"/>
  <line x1="60" y1="280" x2="60" y2="40" stroke="#333" stroke-width="2"/>
  <text x="540" y="300" font-size="13">$q_2$</text>
  <text x="40" y="50" font-size="13">$q_1$</text>
  <line x1="60" y1="100" x2="380" y2="280" stroke="#1f77b4" stroke-width="2"/>
  <text x="80" y="95" font-size="12" fill="#1f77b4">$BR_1(q_2)$ (Cournot, substitutes)</text>
  <line x1="180" y1="280" x2="540" y2="100" stroke="#d62728" stroke-width="2"/>
  <text x="420" y="120" font-size="12" fill="#d62728">$BR_2(q_1)$</text>
  <circle cx="280" cy="200" r="6" fill="#2ca02c"/>
  <text x="290" y="195" font-size="13" fill="#2ca02c">Nash</text>
  <text x="60" y="305" font-size="12" fill="#555">Downward slope indicates strategic substitutes.</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Cournot best responses have negative slope (substitutes). Bertrand best responses with differentiated goods have positive slope (complements).</p>""",
        "examples": r"""<ul>
<li><strong>Cournot duopoly.</strong> Quantities are strategic substitutes. A productivity shock that lowers firm 1's marginal cost raises $q_1$, lowers $q_2$ via the downward-sloping $BR$.</li>
<li><strong>R&D races with positive spillovers.</strong> If my research benefits my rival, our R&D efforts are strategic complements. Hall-Mairesse-Mohnen surveys document this empirically across industries.</li>
<li><strong>Currency speculation.</strong> Speculators' attack decisions are strategic complements: more attackers make a successful attack more likely, raising my best response intensity (Obstfeld 1996).</li>
<li><strong>Essay move.</strong> Use the Bulow-Geanakoplos-Klemperer (1985) taxonomy. The four cases (substitutes vs complements, strategic vs technological) yield different comparative statics. Doornik likes students who place a model in this 2x2.</li>
<li><strong>Essay move.</strong> Stability of equilibrium depends on the slope of best responses. In Cournot, stability requires the BR slope to be less than 1 in absolute value, which is automatic with strict concavity.</li>
<li><strong>Limitation.</strong> Best-response functions may not exist if payoffs are not quasi-concave in own strategy. They may also be multi-valued, in which case selection becomes a substantive issue.</li>
<li>See also [[Concepts/Nash Equilibrium]], [[Concepts/Strategic Substitutes vs Complements]], [[Concepts/Cournot Duopoly]].</li>
</ul>""",
    },
    "affine-utility-normalisation": {
        "math": r"""<p>A vNM utility function $u: X \to \mathbb{R}$ representing preferences over lotteries is unique only up to <strong>positive affine transformations</strong>: $u$ and $\tilde u = a u + b$ with $a > 0$ represent the same preferences. The class of affine transformations preserves expected utility comparisons.</p>

<p>Implication: in any analysis based on expected utility, we can choose units to make algebra cleaner. Standard normalisations:</p>

<ol>
<li><strong>Best-worst:</strong> set $u(\text{best outcome}) = 1$ and $u(\text{worst outcome}) = 0$. Then $u(L)$ is the probability of the best in the equivalent lottery that mixes only best and worst. This is the constructive content of the vNM theorem.</li>
<li><strong>Reference outcome:</strong> set $u(\text{status quo}) = 0$. Welfare changes are measured in net units.</li>
<li><strong>Quadratic CARA:</strong> for CARA utility $u(w) = -e^{-\rho w}$, normalise the constant out to compare risk premia.</li>
</ol>

<p>The affine class is the largest that preserves expected utility orderings. Any nonlinear transform $\phi(u)$ with $\phi'' \neq 0$ changes risk attitudes. For example, if $u$ is risk-neutral and $\phi$ is concave, $\phi \circ u$ is risk-averse.</p>

<p>Cardinality matters in game theory and welfare economics. In games, players' payoffs are individually unique up to affine transformations, but interpersonal comparisons require additional structure. In welfare economics, the inability to compare utilities across people without an ethical assumption is the formal content of Arrow's theorem.</p>

<p>Affine normalisation is used routinely in textbook proofs: write Arrow-Pratt $r_A = -u''/u'$ without worrying about scale, set vNM utilities at 0 and 1 for the binary alternatives, etc.</p>

<p>Reference: Micro2025.pdf Topic 4 Lecture 1; Mas-Colell Ch. 6.B; Kreps "Notes on the Theory of Choice" Ch. 5.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <line x1="60" y1="280" x2="540" y2="280" stroke="#333" stroke-width="2"/>
  <line x1="60" y1="280" x2="60" y2="40" stroke="#333" stroke-width="2"/>
  <text x="540" y="300" font-size="13">$w$</text>
  <text x="40" y="50" font-size="13">$u(w)$</text>
  <path d="M 80 240 Q 200 160 540 80" fill="none" stroke="#1f77b4" stroke-width="2"/>
  <text x="200" y="155" font-size="12" fill="#1f77b4">$u(w) = \log w$</text>
  <path d="M 80 200 Q 200 100 540 40" fill="none" stroke="#d62728" stroke-width="2" stroke-dasharray="4 3"/>
  <text x="200" y="80" font-size="12" fill="#d62728">$\tilde u = 2u + 5$ (same preferences)</text>
  <text x="60" y="305" font-size="12" fill="#555">Both functions induce the same ranking over lotteries.</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Affine transformations of a vNM utility leave preferences over lotteries unchanged: the curves are equivalent.</p>""",
        "examples": r"""<ul>
<li><strong>Lab experiments.</strong> Money outcomes are typically normalised in experiments by subtracting a baseline (show-up fee) so that 0 corresponds to the status quo. This is an affine transformation and does not affect inferences about risk attitudes.</li>
<li><strong>Welfare comparisons within a household.</strong> Becker's (1974) model of family altruism uses a transferable utility frame. Affine normalisation across spouses is fine for predicting allocation; making interpersonal welfare claims requires extra assumptions.</li>
<li><strong>Survey-based well-being.</strong> Cantril ladder scales (0-10) and life-satisfaction scales are affine transforms of underlying ordinal preferences. They preserve ordering within individual but interpersonal comparisons depend on the framing.</li>
<li><strong>Essay move.</strong> The vNM theorem gives expected-utility representation unique up to positive affine transformations. This is weaker than full cardinality but stronger than ordinality. Doornik rewards essays that clarify this distinction.</li>
<li><strong>Essay move.</strong> Use affine normalisation as a derivation shortcut. In signalling games, set $u(\theta_L) = 0$ and $u(\theta_H) = 1$ when checking single-crossing without loss of generality.</li>
<li><strong>Limitation.</strong> Interpersonal utility comparisons cannot be derived from affine vNM utilities alone. Sen, Roberts, and others develop the framework of cardinal full comparability needed for utilitarian aggregation.</li>
<li>See also [[Concepts/von Neumann Morgenstern Axioms]], [[Concepts/Social Welfare Functions]].</li>
</ul>""",
    },
    "strategic-form-game": {
        "math": r"""<p>A <strong>strategic-form game</strong> (also called a normal-form game) is a triple $G = (N, (S_i)_{i \in N}, (u_i)_{i \in N})$ where $N = \{1, \dots, n\}$ is the player set, $S_i$ is player $i$'s strategy space, and $u_i: S \to \mathbb{R}$ is player $i$'s payoff over the joint strategy space $S = \prod_i S_i$.</p>

<p>The representation is "static": every player simultaneously chooses a strategy without observing others' choices. A strategy can be a single action (in a one-shot game) or a complete contingent plan (the normal-form reduction of an extensive-form game).</p>

<ol>
<li>Identify the player set $N$ and each player's strategy set $S_i$.</li>
<li>Specify the payoff function $u_i: S \to \mathbb{R}$, often via a payoff matrix when strategy sets are finite.</li>
<li>Define solution concepts on the strategic form: Nash equilibrium, dominance, rationalisability.</li>
</ol>

<p>For two-player finite games, the strategic form is a payoff matrix with rows for player 1 and columns for player 2. For three or more players, multiple matrices indexed by other players' choices are needed.</p>

<p>A given extensive-form game has a unique strategic-form reduction (by enumerating contingent plans), but the converse fails: many extensive forms can yield the same strategic form. This is why SPE distinguishes equilibria that normal-form Nash cannot.</p>

<p>Existence of Nash equilibrium in strategic-form games: Nash (1950) proves existence in mixed strategies for any finite game. For infinite strategy sets, existence requires continuity and quasi-concavity of payoffs (Glicksberg, Debreu-Fan-Glicksberg).</p>

<p>Reference: Micro2025.pdf Topic 4 Lecture 1; Mas-Colell Ch. 7.B; Gibbons Ch. 1.1.A.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <text x="60" y="40" font-size="14" font-weight="bold">Normal form: Battle of the Sexes</text>
  <line x1="160" y1="80" x2="160" y2="240" stroke="#333"/>
  <line x1="60" y1="160" x2="460" y2="160" stroke="#333"/>
  <text x="220" y="100" font-size="13">Opera</text>
  <text x="360" y="100" font-size="13">Football</text>
  <text x="80" y="125" font-size="13">Opera</text>
  <text x="80" y="225" font-size="13">Football</text>
  <text x="220" y="125" font-size="13" fill="#2ca02c">2, 1</text>
  <text x="360" y="125" font-size="13">0, 0</text>
  <text x="220" y="225" font-size="13">0, 0</text>
  <text x="360" y="225" font-size="13" fill="#2ca02c">1, 2</text>
  <text x="480" y="200" font-size="12" fill="#555">Two pure NE,</text>
  <text x="480" y="218" font-size="12" fill="#555">one mixed NE.</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Strategic-form representation of Battle of the Sexes. Each cell is a (row, column) payoff pair.</p>""",
        "examples": r"""<ul>
<li><strong>Sealed-bid auctions.</strong> First-price auctions have a strategic-form representation: bidders simultaneously submit bids, highest wins, pays own bid. Bayes-Nash equilibrium derives from this primitive.</li>
<li><strong>Voting.</strong> Plurality voting with strategic voters is a strategic-form game: each voter chooses one candidate, payoffs depend on the winning vote count.</li>
<li><strong>Spectrum auctions.</strong> Modern FCC auctions are complex strategic-form games over bidding schedules.</li>
<li><strong>Essay move.</strong> Distinguish strategic form from extensive form. Doornik rewards students who note that subgame-perfect equilibria can be lost in the normal-form reduction (the chain-store paradox is the standard example).</li>
<li><strong>Essay move.</strong> Strategic form makes Nash existence and dominance arguments clean, but it loses temporal structure. For sequential games, always check the extensive form for incredible threats.</li>
<li><strong>Limitation.</strong> Large or continuous strategy spaces make the strategic form unwieldy. Cournot has continuous strategy sets; we use calculus rather than payoff matrices.</li>
<li>See also [[Concepts/Extensive Form Game]], [[Concepts/Nash Equilibrium]].</li>
</ul>""",
    },
    "extensive-form-game": {
        "math": r"""<p>An <strong>extensive-form game</strong> is a tuple $\Gamma = (N, T, P, A, H, u)$ where $T$ is a game tree (directed graph with a unique root and no cycles), $P$ assigns each non-terminal node to a player or chance, $A$ specifies the action set at each node, $H$ partitions decision nodes into information sets (nodes within an information set are indistinguishable to the active player), and $u$ assigns payoff vectors to terminal nodes.</p>

<p>The extensive form makes timing and information explicit. A <strong>strategy</strong> for player $i$ specifies an action at every information set where $i$ moves. A behavioural strategy specifies a probability distribution over actions at each information set.</p>

<ol>
<li><strong>Perfect information:</strong> every information set is a singleton, so every player observes all past actions. Chess, sequential bargaining.</li>
<li><strong>Imperfect information:</strong> some information sets contain multiple nodes. Simultaneous moves can be represented by collapsing multiple nodes into a single information set.</li>
<li><strong>Perfect recall:</strong> standard assumption that no player forgets past actions or information. Kuhn's theorem links behavioural strategies and mixed strategies under perfect recall.</li>
</ol>

<p>Kuhn (1953) shows that any extensive-form game with perfect recall has a strategic-form reduction with the same equilibria. But the extensive form is needed for solution concepts that exploit sequential structure: SPE, PBE, sequential equilibrium.</p>

<p>Drawing convention: hollow circles for chance nodes, filled circles for player nodes, dashed ovals around nodes in the same information set, payoff vectors at the leaves.</p>

<p>Reference: Micro2025.pdf Topic 4 Lecture 2; Mas-Colell Ch. 7.D; Osborne-Rubinstein Ch. 6.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <circle cx="300" cy="50" r="8" fill="#333"/>
  <text x="310" y="45" font-size="12">P1</text>
  <line x1="300" y1="58" x2="180" y2="130" stroke="#333" stroke-width="2"/>
  <line x1="300" y1="58" x2="420" y2="130" stroke="#333" stroke-width="2"/>
  <text x="220" y="100" font-size="12">L</text>
  <text x="370" y="100" font-size="12">R</text>
  <circle cx="180" cy="140" r="8" fill="#1f77b4"/>
  <circle cx="420" cy="140" r="8" fill="#1f77b4"/>
  <ellipse cx="300" cy="140" rx="160" ry="20" fill="none" stroke="#888" stroke-dasharray="4 2"/>
  <text x="500" y="145" font-size="12" fill="#888">P2 info set</text>
  <line x1="180" y1="148" x2="120" y2="230" stroke="#333"/>
  <line x1="180" y1="148" x2="240" y2="230" stroke="#333"/>
  <line x1="420" y1="148" x2="360" y2="230" stroke="#333"/>
  <line x1="420" y1="148" x2="480" y2="230" stroke="#333"/>
  <text x="100" y="260" font-size="12">(2, 1)</text>
  <text x="220" y="260" font-size="12">(0, 0)</text>
  <text x="340" y="260" font-size="12">(0, 0)</text>
  <text x="460" y="260" font-size="12">(1, 2)</text>
  <text x="60" y="300" font-size="12" fill="#555">P2 moves without observing P1's choice.</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Extensive-form representation. The dashed oval marks P2's information set: P2 cannot distinguish the two nodes within.</p>""",
        "examples": r"""<ul>
<li><strong>Sequential bargaining.</strong> Rubinstein's alternating-offers protocol is naturally represented in extensive form, with offer and accept/reject nodes alternating between players.</li>
<li><strong>Auctions with multiple stages.</strong> English auctions, Dutch auctions, and FCC clock auctions all use the extensive form to encode the temporal protocol that pins down the equilibrium.</li>
<li><strong>Centipede game.</strong> A canonical pedagogical example: each player can either continue (passing larger stakes) or stop (taking the current pot). The extensive form makes the backward-induction unravelling visible.</li>
<li><strong>Essay move.</strong> Doornik rewards students who switch between strategic and extensive forms fluently. Use the extensive form for credibility arguments, the strategic form for dominance arguments.</li>
<li><strong>Essay move.</strong> Information sets capture imperfect information. Drawing them correctly is crucial: a common student error is to omit the connecting ovals and inadvertently assume perfect monitoring.</li>
<li><strong>Limitation.</strong> Extensive forms grow exponentially with the number of stages. Compact game-tree representations (game logics, automata) are needed for analysis of long-horizon games.</li>
<li>See also [[Concepts/Information Set]], [[Concepts/Subgame Perfect Equilibrium]], [[Concepts/Strategic Form Game]].</li>
</ul>""",
    },
    "information-set": {
        "math": r"""<p>An <strong>information set</strong> $h$ in an extensive-form game is a non-empty subset of decision nodes that are indistinguishable to the active player at the time of decision. The active player at $h$ chooses an action $a \in A(h)$ knowing only that play has reached some node within $h$, not which one.</p>

<p>Formally, information sets partition the set of decision nodes. Two nodes belong to the same information set only if (i) the same player moves at both and (ii) the action sets at both nodes are identical.</p>

<ol>
<li><strong>Perfect information:</strong> every information set is a singleton. The active player always knows the exact history.</li>
<li><strong>Imperfect information:</strong> some information sets contain multiple nodes, capturing either simultaneous moves or hidden past actions.</li>
<li><strong>Perfect recall:</strong> no player forgets information once known. Formally, if two nodes are in the same information set and a player took action $a$ at an earlier node, that action's effect must be the same at both current nodes.</li>
</ol>

<p>Strategies on extensive-form games specify actions at information sets, not at individual nodes. A behavioural strategy assigns a probability distribution $\beta_i(\cdot | h)$ over $A(h)$ at every information set $h$ where $i$ moves.</p>

<p>Beliefs on information sets: in perfect Bayesian equilibrium, each player has a probability distribution $\mu(\cdot | h)$ over the nodes within their information sets. Consistency of $\mu$ with the strategy profile (via Bayes' rule on path, freely chosen off path) is the central requirement.</p>

<p>Common information-set diagrams use dashed ovals around the nodes belonging to a single information set. The number of nodes determines the "size" of the imperfection.</p>

<p>Reference: Micro2025.pdf Topic 4 Lecture 2; Mas-Colell Ch. 7.D; Fudenberg-Tirole Ch. 8.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <text x="60" y="40" font-size="14" font-weight="bold">Signalling: sender chooses, receiver acts</text>
  <circle cx="120" cy="100" r="8" fill="#333"/>
  <text x="120" y="85" font-size="12" text-anchor="middle">Nature</text>
  <line x1="120" y1="108" x2="80" y2="160" stroke="#333"/>
  <line x1="120" y1="108" x2="160" y2="160" stroke="#333"/>
  <text x="70" y="140" font-size="11">$\theta_L$</text>
  <text x="160" y="140" font-size="11">$\theta_H$</text>
  <circle cx="80" cy="170" r="8" fill="#1f77b4"/>
  <circle cx="160" cy="170" r="8" fill="#1f77b4"/>
  <line x1="80" y1="178" x2="40" y2="230" stroke="#333"/>
  <line x1="80" y1="178" x2="120" y2="230" stroke="#333"/>
  <line x1="160" y1="178" x2="200" y2="230" stroke="#333"/>
  <line x1="160" y1="178" x2="240" y2="230" stroke="#333"/>
  <text x="30" y="245" font-size="11">$s_0$</text>
  <text x="120" y="245" font-size="11">$s_1$</text>
  <text x="200" y="245" font-size="11">$s_0$</text>
  <text x="240" y="245" font-size="11">$s_1$</text>
  <circle cx="40" cy="245" r="5" fill="#d62728"/>
  <circle cx="240" cy="245" r="5" fill="#d62728"/>
  <ellipse cx="40" cy="270" rx="40" ry="15" fill="none" stroke="#888" stroke-dasharray="3 2"/>
  <ellipse cx="240" cy="270" rx="40" ry="15" fill="none" stroke="#888" stroke-dasharray="3 2"/>
  <text x="300" y="180" font-size="12" fill="#555">Receiver sees signal $s$,</text>
  <text x="300" y="200" font-size="12" fill="#555">not type $\theta$. Receiver's</text>
  <text x="300" y="220" font-size="12" fill="#555">information sets group nodes</text>
  <text x="300" y="240" font-size="12" fill="#555">by signal.</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">In a signalling game, the receiver's information sets group sender's type nodes by observed signal.</p>""",
        "examples": r"""<ul>
<li><strong>Job market signalling.</strong> A firm observes the worker's education but not their ability. The firm's information set groups (high-ability, high-education) and (low-ability, high-education) nodes. Spence (1973) is the canonical analysis.</li>
<li><strong>Insurance markets.</strong> An insurer cannot observe the applicant's risk type, so the contract menu must be designed for an information set that pools all types.</li>
<li><strong>Imperfect monitoring in cartels.</strong> When firms observe only an aggregate market signal, not individual cheating, each firm's continuation strategy depends on an information set that bundles many underlying histories.</li>
<li><strong>Essay move.</strong> Distinguish hidden action (the action taken, not the type, is unobserved) from hidden information (the type, not action, is unobserved). The information-set structure differs.</li>
<li><strong>Essay move.</strong> Doornik rewards explicit treatment of belief consistency. PBE requires Bayes' rule on the equilibrium path. Off path, beliefs are free, and refinements like the intuitive criterion restrict them.</li>
<li><strong>Limitation.</strong> Information sets and beliefs over them grow combinatorially with game depth. Computational PBE search is hard for large games.</li>
<li>See also [[Concepts/Extensive Form Game]], [[Concepts/Hidden Information vs Hidden Action]].</li>
</ul>""",
    },
    "matching-pennies": {
        "math": r"""<p><strong>Matching Pennies</strong> is the canonical two-player zero-sum game with no pure-strategy Nash equilibrium. Each player simultaneously plays Heads (H) or Tails (T). Player 1 wins if both choose the same; Player 2 wins if they choose differently. Payoffs:</p>

<p>$u_1(H, H) = u_1(T, T) = 1$, $u_1(H, T) = u_1(T, H) = -1$, and $u_2 = -u_1$.</p>

<p>No pure strategy profile is Nash. From $(H, H)$, player 2 prefers $T$; from $(H, T)$, player 1 prefers $T$; and so on around the cycle. The game has a unique <strong>mixed-strategy Nash equilibrium</strong> in which each player randomises with probability $1/2$.</p>

<ol>
<li>Suppose player 1 plays $H$ with probability $p$ and $T$ with $1 - p$. Player 2's expected payoff to $H$ is $-p + (1 - p) = 1 - 2p$ and to $T$ is $p - (1-p) = 2p - 1$.</li>
<li>Player 2 randomises iff indifferent: $1 - 2p = 2p - 1$, so $p = 1/2$.</li>
<li>By symmetry, player 2 must play $q = 1/2$.</li>
<li>Verify: at $(p, q) = (1/2, 1/2)$, both players have expected payoff 0 regardless of their own choice. Mutual best responses, so Nash.</li>
</ol>

<p>The value of the game is 0 (by zero-sum and symmetry). Matching Pennies is the prototype for any zero-sum game with a unique mixed-strategy equilibrium: tax evasion vs. audit, attack vs. defend in security, exploration vs. exploitation in adversarial settings.</p>

<p>The game is the simplest illustration of the indifference principle: in a mixed-strategy equilibrium, each player must be indifferent across the strategies they randomise over, and the mixing probabilities are pinned down by the opponent's payoffs.</p>

<p>Reference: Micro2025.pdf Topic 4 Lecture 2; Gibbons Ch. 1.3; von Neumann-Morgenstern original minimax theorem.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <text x="200" y="40" font-size="14" font-weight="bold">Matching Pennies</text>
  <line x1="200" y1="60" x2="200" y2="240" stroke="#333"/>
  <line x1="100" y1="150" x2="400" y2="150" stroke="#333"/>
  <text x="260" y="80" font-size="13">H</text>
  <text x="340" y="80" font-size="13">T</text>
  <text x="160" y="110" font-size="13">H</text>
  <text x="160" y="200" font-size="13">T</text>
  <text x="260" y="115" font-size="13">1, -1</text>
  <text x="340" y="115" font-size="13">-1, 1</text>
  <text x="260" y="205" font-size="13">-1, 1</text>
  <text x="340" y="205" font-size="13">1, -1</text>
  <text x="430" y="150" font-size="13" fill="#2ca02c">Mixed NE: (1/2, 1/2)</text>
  <text x="60" y="290" font-size="12" fill="#555">No pure NE: each player's best response cycles round the matrix.</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Matching Pennies has no pure Nash equilibrium and a unique mixed equilibrium with each player randomising 50-50.</p>""",
        "examples": r"""<ul>
<li><strong>Penalty shootouts.</strong> Kicker vs goalkeeper is a Matching Pennies analogue. Chiappori-Levitt-Groseclose (2002) confirm professional shootouts are statistically consistent with mixed Nash play.</li>
<li><strong>Auditing.</strong> Tax authorities cannot audit everyone; taxpayers cannot perfectly hide. The equilibrium mix between truthful reporting and audit intensity is a Matching Pennies game.</li>
<li><strong>Sports tactics.</strong> Tennis serve direction (Walker-Wooders 2001), baseball pitch type (Kovash-Levitt 2009), and rugby kicking direction all empirically approximate Matching Pennies equilibria.</li>
<li><strong>Essay move.</strong> Use Matching Pennies as the leading example of a game without pure Nash equilibrium. The existence theorem (Nash 1950) rescues equilibrium prediction by allowing mixed strategies.</li>
<li><strong>Essay move.</strong> Doornik likes the observation that mixing probabilities depend only on the opponent's payoffs, not on one's own. Changing my own payoffs from $(1, -1)$ to $(2, -2)$ does not change my equilibrium mix.</li>
<li><strong>Limitation.</strong> Mixed strategies are sometimes interpreted as deliberate randomisation; experimental subjects struggle with this. The population (Harsanyi) interpretation is cleaner.</li>
<li>See also [[Concepts/Mixed Strategy Equilibrium]], [[Concepts/Nash Existence Theorem]].</li>
</ul>""",
    },
    "battle-of-the-sexes": {
        "math": r"""<p><strong>Battle of the Sexes</strong> is the canonical two-player coordination game with conflicting preferences. Both players prefer to coordinate on the same activity, but each prefers a different activity. Standard payoffs:</p>

<p>$u_1(O, O) = 2, u_2(O, O) = 1$, $u_1(F, F) = 1, u_2(F, F) = 2$, $u_1(O, F) = u_1(F, O) = u_2(O, F) = u_2(F, O) = 0$.</p>

<p>The game has three Nash equilibria: two in pure strategies, $(O, O)$ and $(F, F)$, and one in mixed strategies.</p>

<ol>
<li>For the mixed equilibrium, let player 1 play $O$ with probability $p$ and player 2 play $O$ with probability $q$. Player 1's expected utility from $O$ is $2q$ and from $F$ is $(1)(1 - q) = 1 - q$. Indifference: $2q = 1 - q$, so $q = 1/3$.</li>
<li>By analogous calculation for player 2's indifference: $p = 2/3$.</li>
<li>Mixed equilibrium: player 1 plays $O$ with probability $2/3$, player 2 plays $O$ with probability $1/3$. Expected payoff to each player is $2 \cdot 1/3 = 2/3$.</li>
</ol>

<p>The mixed equilibrium is Pareto-inferior to both pure equilibria, illustrating that coordination failure carries a welfare cost. The two pure equilibria are Pareto-efficient relative to the mixed one but asymmetric: each favours one player.</p>

<p>Battle of the Sexes is the prototype for coordination problems in standards setting (HD-DVD vs Blu-ray), platform competition (mobile OS), and meeting points without communication. Schelling (1960) emphasised the role of focal points in selecting among multiple equilibria.</p>

<p>Reference: Micro2025.pdf Topic 4 Lecture 1; Schelling, "The Strategy of Conflict"; Mas-Colell Ch. 8.D.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <text x="160" y="40" font-size="14" font-weight="bold">Battle of the Sexes</text>
  <line x1="200" y1="60" x2="200" y2="240" stroke="#333"/>
  <line x1="100" y1="150" x2="400" y2="150" stroke="#333"/>
  <text x="260" y="80" font-size="13">Opera</text>
  <text x="340" y="80" font-size="13">Football</text>
  <text x="140" y="115" font-size="13">Opera</text>
  <text x="140" y="205" font-size="13">Football</text>
  <text x="260" y="115" font-size="13" fill="#2ca02c">2, 1</text>
  <text x="340" y="115" font-size="13">0, 0</text>
  <text x="260" y="205" font-size="13">0, 0</text>
  <text x="340" y="205" font-size="13" fill="#2ca02c">1, 2</text>
  <text x="430" y="120" font-size="12" fill="#2ca02c">Pure NE 1: (O,O)</text>
  <text x="430" y="210" font-size="12" fill="#2ca02c">Pure NE 2: (F,F)</text>
  <text x="60" y="290" font-size="12" fill="#555">Plus mixed NE: p=2/3, q=1/3, expected payoff 2/3 each.</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Two asymmetric pure Nash equilibria plus a Pareto-inferior mixed equilibrium.</p>""",
        "examples": r"""<ul>
<li><strong>Format standards.</strong> HD-DVD vs Blu-ray (2006 to 2008) was a Battle of the Sexes between Toshiba and Sony with each preferring their format. Blu-ray won when major studios coordinated on it as a focal point.</li>
<li><strong>Power couple geography.</strong> Two-career couples deciding where to live face Battle of the Sexes: both want to be together, each prefers their career city.</li>
<li><strong>Mobile platforms.</strong> The Android-iOS duopoly has elements of Battle of the Sexes for app developers, who prefer to coordinate on one platform but disagree on which.</li>
<li><strong>Essay move.</strong> Battle of the Sexes shows the welfare cost of multiple equilibria. The mixed equilibrium is Pareto-inferior. Doornik rewards explicit comparison of equilibrium payoffs.</li>
<li><strong>Essay move.</strong> Use Schelling's focal-point logic to argue equilibrium selection. Historical precedent, salience, and pre-game communication can resolve coordination problems that pure equilibrium analysis cannot.</li>
<li><strong>Limitation.</strong> Without communication or focal points, the theory does not predict which equilibrium will be played. Repeated play and learning can break ties via convention.</li>
<li>See also [[Concepts/Nash Equilibrium]], [[Concepts/Mixed Strategy Equilibrium]].</li>
</ul>""",
    },
    "hawk-dove-game": {
        "math": r"""<p>The <strong>Hawk-Dove (Chicken) game</strong> is a two-player anti-coordination game. Each player chooses Hawk (aggressive) or Dove (passive). The worst outcome for both is mutual Hawk; both prefer to be the lone Hawk; if both play Dove, they get a moderate payoff.</p>

<p>Standard payoffs with value $V$ and cost of conflict $C > V$:</p>

<p>$u(H, H) = (V - C)/2$, $u(H, D) = V$, $u(D, H) = 0$, $u(D, D) = V/2$.</p>

<p>The game has two pure-strategy Nash equilibria, $(H, D)$ and $(D, H)$, and one symmetric mixed equilibrium.</p>

<ol>
<li>For the mixed equilibrium, let each player play H with probability $p$. Expected payoff to H: $p(V-C)/2 + (1-p)V = V - p(V+C)/2$.</li>
<li>Expected payoff to D: $p \cdot 0 + (1-p) V/2 = (1-p) V/2$.</li>
<li>Indifference: $V - p(V+C)/2 = (1-p) V/2$. Solving: $p^* = V/C$.</li>
<li>Symmetric mixed equilibrium has each player playing Hawk with probability $V/C$. Higher costs of conflict reduce the equilibrium hawk fraction.</li>
</ol>

<p>The expected payoff per player at the mixed equilibrium is $V(1 - V/C)/2$, lower than $V/2$ (mutual Dove), illustrating again that mixed equilibria can be Pareto-dominated.</p>

<p>Hawk-Dove is central in evolutionary game theory (Maynard Smith 1973). The mixed equilibrium corresponds to an <strong>evolutionarily stable strategy</strong> (ESS) when interpreted as the fraction of hawks in a population. The ESS condition delivers the same proportion $V/C$.</p>

<p>Reference: Micro2025.pdf Topic 4 Lecture 1; Maynard Smith, "Evolution and the Theory of Games"; Osborne-Rubinstein Ch. 13.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <text x="200" y="40" font-size="14" font-weight="bold">Hawk-Dove (V=2, C=4)</text>
  <line x1="200" y1="60" x2="200" y2="240" stroke="#333"/>
  <line x1="100" y1="150" x2="400" y2="150" stroke="#333"/>
  <text x="260" y="80" font-size="13">Hawk</text>
  <text x="340" y="80" font-size="13">Dove</text>
  <text x="150" y="115" font-size="13">Hawk</text>
  <text x="150" y="205" font-size="13">Dove</text>
  <text x="260" y="115" font-size="13" fill="#d62728">-1, -1</text>
  <text x="340" y="115" font-size="13" fill="#2ca02c">2, 0</text>
  <text x="260" y="205" font-size="13" fill="#2ca02c">0, 2</text>
  <text x="340" y="205" font-size="13">1, 1</text>
  <text x="430" y="120" font-size="12" fill="#2ca02c">Pure NE: (H, D), (D, H)</text>
  <text x="430" y="200" font-size="12" fill="#555">Mixed: p* = V/C = 1/2</text>
  <text x="60" y="290" font-size="12" fill="#555">Mutual Hawk is worst; asymmetric NE pure; symmetric NE mixed.</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Anti-coordination: each prefers to be the Hawk if the other is Dove, but mutual Hawk is a disaster.</p>""",
        "examples": r"""<ul>
<li><strong>Resource conflicts.</strong> Animal contests over territory (Maynard Smith and Price 1973) match Hawk-Dove exactly. The equilibrium fraction of aggressive types depends on the value of the resource versus the cost of fighting.</li>
<li><strong>Brinkmanship.</strong> Cuban Missile Crisis and other nuclear-era standoffs are textbook Chicken. The threat is credible only because both sides know that mutual H is catastrophic.</li>
<li><strong>Traffic at intersections.</strong> When two cars approach an unmarked intersection, each prefers to yield iff the other goes first. The pure equilibria correspond to whoever signals first.</li>
<li><strong>Essay move.</strong> Hawk-Dove illustrates that asymmetric equilibria can arise endogenously in symmetric games. Doornik rewards essays that link this to the evolutionary stability concept.</li>
<li><strong>Essay move.</strong> The mixed equilibrium is Pareto-dominated by mutual Dove. Cooperation requires institutions (rules of the road, property rights) to coordinate on one of the pure equilibria.</li>
<li><strong>Limitation.</strong> The two-by-two structure abstracts from gradient strategies. With continuous aggression levels, the strategic structure can change qualitatively.</li>
<li>See also [[Concepts/Battle of the Sexes]], [[Concepts/Mixed Strategy Equilibrium]].</li>
</ul>""",
    },
    "iterated-elimination-strictly-dominated": {
        "math": r"""<p><strong>Iterated elimination of strictly dominated strategies (IESDS)</strong> is the procedure: start with the full strategy set; remove every strictly dominated strategy (possibly dominated by a mixed strategy); on the reduced game, re-check dominance and remove again; repeat until no further removals.</p>

<p>The limit of the process is the set of <strong>rationalisable</strong> strategies (Pearce 1984, Bernheim 1984). Every Nash equilibrium consists of rationalisable strategies, but rationalisable sets can be much larger than Nash sets.</p>

<ol>
<li>For each player, check whether any pure strategy $s_i$ is strictly dominated by another pure or mixed strategy $\sigma_i$: $u_i(\sigma_i, s_{-i}) > u_i(s_i, s_{-i})$ for all $s_{-i}$ remaining in the reduced game.</li>
<li>Remove all dominated strategies simultaneously.</li>
<li>Repeat on the reduced game. The order of elimination does not matter for strict dominance: the limit is unique.</li>
</ol>

<p><strong>Beauty Contest game</strong> (Nagel 1995): players choose integers from 0 to 100; the winner is whoever picks closest to $2/3$ of the average. IESDS argument:</p>

<p>Round 1: any pick above 67 is strictly dominated (since $2/3 \cdot 100 = 67$). Remove all $s > 67$.</p>

<p>Round 2: with new max 67, any pick above $2/3 \cdot 67 = 44$ is dominated.</p>

<p>Iterating, the unique rationalisable pick is 0. Experimentally, subjects typically need 1 to 4 rounds of iteration, suggesting bounded depth of strategic reasoning.</p>

<p>For weak dominance, the order of elimination matters. IESDS is well-defined and order-independent only for strict dominance.</p>

<p>Reference: Micro2025.pdf Topic 4 Lecture 1; Gibbons Ch. 1.1.B; Pearce 1984 Econometrica.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <text x="60" y="40" font-size="14" font-weight="bold">Beauty Contest IESDS</text>
  <rect x="60" y="60" width="480" height="30" fill="#fee2e2" stroke="#dc2626"/>
  <text x="70" y="80" font-size="12">Round 0: choices in [0, 100]</text>
  <rect x="60" y="100" width="320" height="30" fill="#fed7aa" stroke="#ea580c"/>
  <text x="70" y="120" font-size="12">Round 1: [0, 67] (strictly dominate >67)</text>
  <rect x="60" y="140" width="215" height="30" fill="#fef3c7" stroke="#ca8a04"/>
  <text x="70" y="160" font-size="12">Round 2: [0, 44]</text>
  <rect x="60" y="180" width="144" height="30" fill="#dcfce7" stroke="#65a30d"/>
  <text x="70" y="200" font-size="12">Round 3: [0, 30]</text>
  <rect x="60" y="220" width="40" height="30" fill="#bfdbfe" stroke="#2563eb"/>
  <text x="120" y="240" font-size="12">Limit: {0}</text>
  <text x="60" y="290" font-size="12" fill="#555">Repeated IESDS leaves only the Nash equilibrium {0}.</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Beauty Contest: each round of IESDS removes the top third of remaining choices. The limit is the unique rationalisable strategy 0.</p>""",
        "examples": r"""<ul>
<li><strong>Beauty contest experiments.</strong> Nagel (1995) and Camerer-Ho-Chong show that real subjects iterate between 1 and 3 rounds, predicting modal guesses around 33, 22, or 15, not 0. Bounded rationality literature uses this to estimate levels of reasoning.</li>
<li><strong>Cournot oligopoly.</strong> Quantities above the monopoly output are strictly dominated. After enough rounds of IESDS, the remaining quantities lie in a narrow interval around the Nash equilibrium.</li>
<li><strong>Auctions with private values.</strong> In a first-price sealed-bid auction, bidding above your valuation is strictly dominated, so the rationalisable bid range is bounded above.</li>
<li><strong>Essay move.</strong> Distinguish strict from weak dominance. Doornik rewards students who note that IESDS with weak dominance is order-dependent: different elimination orders give different surviving sets.</li>
<li><strong>Essay move.</strong> Every Nash equilibrium consists of rationalisable strategies, but the converse may fail. Use the IESDS hierarchy: dominance solvable, rationalisable, Nash, refinements.</li>
<li><strong>Limitation.</strong> IESDS requires common knowledge of rationality. Empirical evidence shows that 2 to 4 levels is the typical depth observed, suggesting cognitive limits on iterated reasoning.</li>
<li>See also [[Concepts/Dominance]], [[Concepts/Strict vs Weak Dominance]].</li>
</ul>""",
    },
    "strict-vs-weak-dominance": {
        "math": r"""<p>Strategy $s_i$ <strong>strictly dominates</strong> $s_i'$ for player $i$ if $u_i(s_i, s_{-i}) > u_i(s_i', s_{-i})$ for every $s_{-i}$. Strategy $s_i$ <strong>weakly dominates</strong> $s_i'$ if $u_i(s_i, s_{-i}) \geq u_i(s_i', s_{-i})$ for every $s_{-i}$, with strict inequality for at least one $s_{-i}$.</p>

<p>The distinction has sharp consequences for solution concepts.</p>

<ol>
<li><strong>IESDS with strict dominance</strong> is order-independent: the limit set is unique. This is because eliminating a strictly dominated strategy never depends on whether other dominated strategies were eliminated first.</li>
<li><strong>IESDS with weak dominance</strong> is order-dependent: different elimination paths produce different survivor sets. Samuelson (1992) gives a 3x3 example where two distinct elimination orders give different SPE.</li>
<li>A rational player <strong>never plays a strictly dominated strategy</strong>. A rational player <em>may</em> play a weakly dominated strategy (it could be a best response if the dominant alternative ties on the relevant contingencies).</li>
</ol>

<p>Implications for refinements:</p>

<p>Trembling-hand perfect equilibrium (Selten 1975) requires Nash equilibrium robust to small probability of opponents' mistakes. Trembling-hand perfection implies that no player uses a weakly dominated strategy.</p>

<p>Second-price (Vickrey) auctions: bidding your true valuation is weakly dominant. Other Bayes-Nash equilibria exist (e.g. bid zero, lose), but they involve weakly dominated bids. Trembling-hand perfection selects truth-telling.</p>

<p>Reference: Micro2025.pdf Topic 4 Lecture 1; Mas-Colell Ch. 8.B; Fudenberg-Tirole Ch. 1.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <text x="60" y="40" font-size="14" font-weight="bold">Weak vs Strict Dominance</text>
  <line x1="220" y1="60" x2="220" y2="280" stroke="#333"/>
  <line x1="80" y1="140" x2="480" y2="140" stroke="#333"/>
  <text x="280" y="80" font-size="13">L</text>
  <text x="380" y="80" font-size="13">R</text>
  <text x="80" y="100" font-size="13">U</text>
  <text x="80" y="200" font-size="13">D</text>
  <text x="280" y="110" font-size="13">2, 0</text>
  <text x="380" y="110" font-size="13">1, 0</text>
  <text x="280" y="210" font-size="13" fill="#2563eb">1, 0</text>
  <text x="380" y="210" font-size="13" fill="#2563eb">1, 0</text>
  <text x="60" y="260" font-size="12">U weakly dominates D (2 > 1, 1 = 1).</text>
  <text x="60" y="280" font-size="12">No strict dominance.</text>
  <text x="60" y="300" font-size="12" fill="#555">If we eliminate D first, then R can be weakly dominated by L.</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">U weakly dominates D. Iteration order matters with weak dominance.</p>""",
        "examples": r"""<ul>
<li><strong>Vickrey auctions.</strong> Truthful bidding $b_i = v_i$ weakly dominates other bids. Other Bayes-Nash equilibria exist in dominated strategies, but trembling-hand perfection selects truth-telling.</li>
<li><strong>Voting.</strong> Voting for your favourite candidate weakly dominates other strategies if your vote is never decisive. Under uncertainty over pivot probability, the weak-dominance argument typically does not bind.</li>
<li><strong>Median voter.</strong> The median strategy weakly dominates other Condorcet-winning strategies in single-peaked preferences (Black 1948).</li>
<li><strong>Essay move.</strong> Doornik often asks why economists use Bayes-Nash equilibrium instead of dominance solvability. The answer is that weak dominance leaves selection unresolved and strong dominance is rare outside special games.</li>
<li><strong>Essay move.</strong> Use the Vickrey auction comparison: strict dominance gives uniqueness in dominant-strategy equilibrium; weak dominance allows multiple BNE, requiring refinements.</li>
<li><strong>Limitation.</strong> Many real games (Cournot, Bertrand) have no dominance relations at all, so dominance arguments are not useful selection tools.</li>
<li>See also [[Concepts/Dominance]], [[Concepts/Iterated Elimination of Strictly Dominated Strategies]].</li>
</ul>""",
    },
    "tit-for-tat": {
        "math": r"""<p><strong>Tit-for-tat (TFT)</strong> is a simple history-dependent strategy for repeated games: cooperate in period 0; in period $t \geq 1$, play whatever the opponent played in period $t - 1$. The strategy is reactive (one-period memory), forgiving (resumes cooperation if opponent cooperates), and retaliatory (punishes defection once).</p>

<p>In the infinitely repeated Prisoner's Dilemma with stage payoffs $c > n$ (mutual cooperation > mutual Nash), $d > c$ (one-shot defection), and $s < n$ (sucker payoff $< $ Nash), tit-for-tat sustains cooperation iff $\delta$ exceeds a critical threshold.</p>

<ol>
<li><strong>On-path payoff:</strong> mutual cooperation forever, $c/(1-\delta)$.</li>
<li><strong>One-shot deviation by player 1 in period 0:</strong> $d$ in period 0, then opponent plays D in period 1, so player 1's best response in period 1 is to defect too (or any subsequent strategy). The most informative deviation alternates D, C, D, C, ... (alternating ploy), or single defection then return to C.</li>
<li><strong>Alternating ploy DC DC DC...:</strong> payoff $(d + \delta s + \delta^2 d + \delta^3 s + \dots)/(1) = (d + \delta s)/(1 - \delta^2)$.</li>
<li>Incentive condition: $c/(1-\delta) \geq (d + \delta s)/(1 - \delta^2)$, giving $\delta \geq (d - c)/(c - s)$.</li>
</ol>

<p>TFT is not subgame-perfect in the strict sense: after a deviation, the punishment phase is sub-optimal for the punisher. Friedman's grim trigger gives an SPE; TFT requires a renegotiation-proof or evolutionary stability argument.</p>

<p>Axelrod (1984) ran computer tournaments where TFT consistently outperformed more complex strategies, popularising the reputation that "nice, forgiving, retaliatory" strategies do well in heterogeneous populations.</p>

<p>Reference: Micro2025.pdf Topic 4 Lecture 3; Axelrod "The Evolution of Cooperation"; Mailath-Samuelson Ch. 2.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <text x="60" y="40" font-size="14" font-weight="bold">Tit-for-Tat Phase Diagram</text>
  <circle cx="150" cy="160" r="40" fill="#a7f3d0" stroke="#10b981" stroke-width="2"/>
  <text x="150" y="165" font-size="14" text-anchor="middle">C</text>
  <circle cx="400" cy="160" r="40" fill="#fecaca" stroke="#dc2626" stroke-width="2"/>
  <text x="400" y="165" font-size="14" text-anchor="middle">D</text>
  <path d="M 190 145 Q 275 100 360 145" fill="none" stroke="#333" stroke-width="2" marker-end="url(#a1)"/>
  <text x="270" y="100" font-size="12">opponent D</text>
  <path d="M 360 175 Q 275 220 190 175" fill="none" stroke="#333" stroke-width="2" marker-end="url(#a1)"/>
  <text x="270" y="240" font-size="12">opponent C</text>
  <defs>
    <marker id="a1" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
      <path d="M0,0 L8,4 L0,8 z" fill="#333"/>
    </marker>
  </defs>
  <text x="60" y="290" font-size="12" fill="#555">Reactive, forgiving, one-period memory. Punishes once and resumes cooperation.</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Tit-for-tat: cooperate after C, defect after D. One-period memory, forgiving punishment.</p>""",
        "examples": r"""<ul>
<li><strong>Tournament results (Axelrod 1984).</strong> Round-robin contests of repeated PD strategies. TFT won both tournaments, despite being one of the simplest entrants.</li>
<li><strong>Trench warfare (Live and Let Live, WWI).</strong> Ashworth (1980) documents how soldiers on opposing fronts developed implicit TFT norms: shoot to miss unless attacked, then retaliate.</li>
<li><strong>Currency reserve agreements.</strong> Central bank cooperation episodes show TFT features: small deviations are reciprocated proportionally, with willingness to return to cooperation.</li>
<li><strong>Essay move.</strong> TFT is one strategy among many in the folk-theorem set. Doornik rewards explicit comparison with grim trigger (TFT is less harsh, more forgiving, but not subgame-perfect).</li>
<li><strong>Essay move.</strong> TFT is evolutionarily robust but not strictly stable: it can be invaded by ALLD if signal noise is high. Generous-TFT (Nowak-Sigmund 1992) is more robust.</li>
<li><strong>Limitation.</strong> Under imperfect monitoring, TFT amplifies errors. A single misread defection triggers a chain of mutual punishments. Pavlov (win-stay, lose-shift) is more error-tolerant.</li>
<li>See also [[Concepts/Grim Trigger Strategy]], [[Concepts/Infinitely Repeated Games]].</li>
</ul>""",
    },
    "nash-reversion": {
        "math": r"""<p>A <strong>Nash reversion strategy</strong> (Friedman 1971) prescribes that following any deviation from a cooperative path, players play the static (one-shot) Nash equilibrium of the stage game forever. Unlike grim trigger applied to non-Nash punishments, Nash reversion uses the credible threat of returning to stage Nash, which is automatically a subgame-perfect punishment.</p>

<p>For a symmetric stage game with cooperative payoff $c$, stage Nash payoff $n < c$, and one-shot deviation payoff $d > c$:</p>

$$\delta^*_{NR} = \frac{d - c}{d - n}.$$

<p>The derivation is identical to grim trigger because the punishment payoff is the same: stage Nash.</p>

<ol>
<li>Cooperative phase: both play the cooperative action. Payoff $c/(1-\delta)$.</li>
<li>Any deviation triggers permanent reversion to stage Nash. Payoff of deviator: $d + \delta n/(1-\delta)$.</li>
<li>Incentive constraint: $c/(1-\delta) \geq d + \delta n/(1-\delta)$.</li>
<li>Verify subgame perfection: the punishment phase is stage Nash forever, which is trivially an SPE of the continuation game.</li>
</ol>

<p>Friedman's contribution was to show that Nash reversion is automatically subgame-perfect (no need to worry about whether the punishment is credible). The cost is that it gives a possibly suboptimal range of sustainable cooperative outcomes: stage Nash is not always the worst credible punishment.</p>

<p>Abreu (1986) shows that the most severe credible punishment is generally not stage Nash but an asymmetric "stick and carrot" scheme. This delivers a lower critical discount factor than Friedman's.</p>

<p>Nash reversion is the default folk-theorem result quoted in most textbook applications, especially in IO. The cartel sustainability condition $\delta \geq (n-1)/n$ for Bertrand collusion is a Nash reversion result.</p>

<p>Reference: Micro2025.pdf Topic 4 Lecture 3; Friedman 1971 REStud; Abreu 1986 JET.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <text x="60" y="40" font-size="14" font-weight="bold">Nash Reversion vs Optimal Punishment</text>
  <line x1="60" y1="280" x2="540" y2="280" stroke="#333"/>
  <line x1="60" y1="280" x2="60" y2="60" stroke="#333"/>
  <text x="540" y="300" font-size="13">time</text>
  <text x="40" y="60" font-size="13">payoff</text>
  <line x1="80" y1="100" x2="280" y2="100" stroke="#10b981" stroke-width="2"/>
  <text x="90" y="90" font-size="11" fill="#10b981">Cooperate $c$</text>
  <line x1="280" y1="220" x2="540" y2="220" stroke="#dc2626" stroke-width="2"/>
  <text x="290" y="245" font-size="11" fill="#dc2626">Stage Nash $n$ forever</text>
  <circle cx="280" cy="220" r="4" fill="#000"/>
  <text x="270" y="245" font-size="11" fill="#555">deviation</text>
  <text x="60" y="300" font-size="12" fill="#555">Permanent punishment at stage Nash, automatically credible.</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Nash reversion: deviation triggers permanent stage Nash, which is automatically subgame-perfect.</p>""",
        "examples": r"""<ul>
<li><strong>Cournot collusion.</strong> Two firms sustain monopoly output via reversion to Cournot Nash. Sustainable for $\delta \geq (d-c)/(d-n)$ with stage Cournot as punishment.</li>
<li><strong>Bertrand cartels.</strong> Reversion to $p = c$ sustains $p = p^M$ for $\delta \geq (n-1)/n$ where $n$ is the number of firms.</li>
<li><strong>OPEC.</strong> Threat of return to competitive pricing is the standard punishment device for sustaining quotas. Empirically, the threat is credible because the static Nash is competitive.</li>
<li><strong>Essay move.</strong> Friedman's Nash-reversion folk theorem is sufficient for showing cooperation can be sustained. Doornik rewards explicit invocation of credibility: stage Nash is automatically a continuation equilibrium.</li>
<li><strong>Essay move.</strong> Compare to Abreu (1986) optimal punishments. Nash reversion is conservative but transparent; optimal punishments deliver lower $\delta^*$ but require complex stick-and-carrot schemes.</li>
<li><strong>Limitation.</strong> Stage Nash is sometimes not the worst credible punishment. For games where the stage game has multiple Nash equilibria, asymmetric punishment can achieve a wider folk-theorem set.</li>
<li>See also [[Concepts/Grim Trigger Strategy]], [[Concepts/Folk Theorem]].</li>
</ul>""",
    },
    "strategic-substitutes-complements": {
        "math": r"""<p>Strategies $s_i$ and $s_j$ are <strong>strategic complements</strong> if $\partial^2 u_i / \partial s_i \partial s_j > 0$, equivalently if best-response functions are upward-sloping: $BR_i'(s_j) > 0$. They are <strong>strategic substitutes</strong> if $\partial^2 u_i / \partial s_i \partial s_j < 0$, equivalently $BR_i'(s_j) < 0$.</p>

<p>Bulow, Geanakoplos, and Klemperer (1985) classify oligopoly games by this taxonomy. Cournot quantities are substitutes; Bertrand prices with differentiated goods are complements; advertising and R&D can be either.</p>

<ol>
<li>For Cournot with $P = a - bQ$ and constant MC: $\partial^2 \pi_i / \partial q_i \partial q_j = -b < 0$. Substitutes.</li>
<li>For Bertrand with differentiated demand $q_i = a - b p_i + c p_j$ ($c > 0$): $\partial^2 \pi_i / \partial p_i \partial p_j = c > 0$. Complements.</li>
<li>The slope of the best response is determined by the sign of the cross-partial divided by the negative own second derivative: $BR_i'(s_j) = -(\partial^2 u_i / \partial s_i \partial s_j) / (\partial^2 u_i / \partial s_i^2)$.</li>
</ol>

<p>Comparative statics consequence: with substitutes, a positive shock to one firm reduces the others' equilibrium choices (dampening). With complements, it raises them (amplification).</p>

<p>Tournament implications: under strategic complements, taxation that lowers one firm's incentive lowers everyone's via the upward-sloping reaction function. This is the Topkis-Milgrom-Roberts theorem on monotone comparative statics in games with complementarities.</p>

<p>Empirical: Cooper-Haltiwanger-Power (1999) document strategic complementarities in plant-level investment timing; pricing in retail (Eichenbaum-Jaimovich-Rebelo 2011) exhibits complementarities consistent with Bertrand.</p>

<p>Reference: Micro2025.pdf Topic 4 Lecture 1; Bulow-Geanakoplos-Klemperer 1985 JPE; Milgrom-Roberts 1990 Econometrica.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <line x1="80" y1="260" x2="280" y2="260" stroke="#333"/>
  <line x1="80" y1="260" x2="80" y2="80" stroke="#333"/>
  <text x="200" y="280" font-size="13">$s_j$</text>
  <text x="60" y="90" font-size="13">$s_i$</text>
  <line x1="80" y1="120" x2="280" y2="240" stroke="#1f77b4" stroke-width="2"/>
  <text x="100" y="115" font-size="12" fill="#1f77b4">Substitutes (Cournot)</text>
  <line x1="320" y1="260" x2="520" y2="260" stroke="#333"/>
  <line x1="320" y1="260" x2="320" y2="80" stroke="#333"/>
  <text x="440" y="280" font-size="13">$s_j$</text>
  <text x="300" y="90" font-size="13">$s_i$</text>
  <line x1="320" y1="240" x2="520" y2="100" stroke="#d62728" stroke-width="2"/>
  <text x="340" y="115" font-size="12" fill="#d62728">Complements (Bertrand)</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Strategic substitutes: BR slopes down. Strategic complements: BR slopes up.</p>""",
        "examples": r"""<ul>
<li><strong>Currency attack on a peg.</strong> Speculators' attack intensities are strategic complements: more attackers raise the probability of devaluation, so my best-response intensity rises. Obstfeld (1996) shows this creates multiple equilibria.</li>
<li><strong>Bank runs.</strong> Diamond-Dybvig (1983) liquidity decisions are complements: if I expect others to withdraw, I withdraw too. The result is a fragile equilibrium with possible bank runs.</li>
<li><strong>Bertrand price competition.</strong> With differentiated goods, prices are complements. A merger softens competition through the upward-sloping reaction function: post-merger, prices rise.</li>
<li><strong>Essay move.</strong> Doornik rewards explicit derivation of comparative-static signs via the BGK taxonomy. A productivity shock has opposite signs on equilibrium quantities depending on whether competition is in quantities (substitutes) or prices (complements).</li>
<li><strong>Essay move.</strong> Topkis-Milgrom-Roberts monotone comparative statics work for complements without strict differentiability. Used in macro models with coordination failures.</li>
<li><strong>Limitation.</strong> The classification ignores third-order effects. In oligopoly with R&D, the same product market can exhibit complements in one stage and substitutes in another.</li>
<li>See also [[Concepts/Best Response Functions]], [[Concepts/Cournot Duopoly]], [[Concepts/Bertrand Duopoly]].</li>
</ul>""",
    },
    "first-mover-advantage": {
        "math": r"""<p>The <strong>first-mover advantage</strong> arises in sequential games when the player who commits first earns a higher payoff than under simultaneous play. The leading example is the Stackelberg duopoly.</p>

<p>With linear inverse demand $P = a - bQ$ and constant marginal cost $c$, the simultaneous-move (Cournot) Nash equilibrium gives each firm output $(a-c)/(3b)$ and profit $(a-c)^2/(9b)$. Under Stackelberg leadership:</p>

<ol>
<li><strong>Follower's problem:</strong> $\max_{q_F} (a - b(q_L + q_F) - c) q_F$. FOC gives $q_F(q_L) = (a - c - b q_L)/(2b)$.</li>
<li><strong>Leader's problem:</strong> $\max_{q_L} (a - b(q_L + q_F(q_L)) - c) q_L$. Substituting the follower's reaction function: $\max_{q_L} ((a - c)/2 - b q_L/2) q_L$.</li>
<li><strong>FOC for leader:</strong> $q_L^* = (a - c)/(2b)$, $q_F^* = (a - c)/(4b)$.</li>
<li><strong>Profits:</strong> $\pi_L = (a-c)^2/(8b)$, $\pi_F = (a-c)^2/(16b)$. Leader profit is twice the follower's and 12.5\% higher than Cournot.</li>
</ol>

<p>The mechanism: by committing to a high quantity, the leader exploits the substitutes structure to push the follower down its reaction function. The follower's optimal response reduces its own output, leaving the leader with a larger share of total output.</p>

<p>The first-mover advantage requires (a) strategic substitutes; (b) credible commitment by the leader; (c) the follower observing the leader's choice. Under strategic complements (Bertrand differentiated), the first mover may suffer a <strong>second-mover advantage</strong> because committing to a low price gives the follower an opportunity to undercut even further.</p>

<p>Dixit (1980), Schelling (1960) emphasised the role of commitment. Empirical first-mover advantages are mixed: market-share leadership often persists but profitability advantages erode (Lieberman-Montgomery 1988).</p>

<p>Reference: Micro2025.pdf Topic 4 Lecture 2 and Topic 5; Tirole Ch. 8; Stackelberg (1934).</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <line x1="80" y1="280" x2="540" y2="280" stroke="#333"/>
  <line x1="80" y1="280" x2="80" y2="40" stroke="#333"/>
  <text x="540" y="300" font-size="13">$q_F$</text>
  <text x="60" y="50" font-size="13">$q_L$</text>
  <line x1="80" y1="100" x2="380" y2="280" stroke="#1f77b4" stroke-width="2"/>
  <text x="100" y="95" font-size="12" fill="#1f77b4">$BR_L$ (Cournot)</text>
  <line x1="180" y1="280" x2="540" y2="100" stroke="#d62728" stroke-width="2"/>
  <text x="420" y="115" font-size="12" fill="#d62728">$BR_F$</text>
  <circle cx="280" cy="200" r="5" fill="#2ca02c"/>
  <text x="290" y="195" font-size="12" fill="#2ca02c">Cournot</text>
  <circle cx="180" cy="140" r="5" fill="#9467bd"/>
  <text x="190" y="135" font-size="12" fill="#9467bd">Stackelberg leader</text>
  <path d="M 290 195 L 195 140" stroke="#888" stroke-width="1" stroke-dasharray="4 2" marker-end="url(#a2)"/>
  <defs><marker id="a2" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#888"/></marker></defs>
  <text x="60" y="305" font-size="12" fill="#555">Leader moves to a higher $q$, pushing follower down its BR.</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Stackelberg leader commits to a higher quantity, exploiting the downward-sloping follower BR.</p>""",
        "examples": r"""<ul>
<li><strong>Stackelberg quantity leadership.</strong> Saudi Arabia in OPEC plays the leader role, setting quotas first and letting other producers adjust.</li>
<li><strong>Platform launches.</strong> Apple's iPhone preempted the smartphone market in 2007. Lieberman-Montgomery (1988) document mixed first-mover outcomes across industries.</li>
<li><strong>Capacity preemption.</strong> Building excess capacity ahead of rivals (Spence 1977, Dixit 1980) commits to high output. Real applications include cement, oil refining, and chemicals.</li>
<li><strong>Essay move.</strong> Distinguish first-mover advantage (Stackelberg) from second-mover advantage (Bertrand differentiated). Doornik rewards explicit appeal to strategic substitutes vs complements.</li>
<li><strong>Essay move.</strong> Commitment must be credible. Dixit (1980) shows that irreversible capacity investments are commitment devices; verbal threats are not.</li>
<li><strong>Limitation.</strong> Empirical evidence on persistent first-mover advantages is mixed. Network effects can lock in early advantage (Facebook, Microsoft Office), but late movers can also win with better products (Google after AltaVista).</li>
<li>See also [[Concepts/Stackelberg Leadership]], [[Concepts/Credible Threat]], [[Concepts/Entry Deterrence]].</li>
</ul>""",
    },
    "credible-threat": {
        "math": r"""<p>A <strong>credible threat</strong> in an extensive-form game is one that the threatener would actually carry out if called upon. Non-credible threats can support Nash equilibria but not subgame-perfect equilibria. The credibility distinction is the conceptual heart of Selten's (1965) SPE.</p>

<p>Formally: a threat is credible iff carrying it out is a continuation equilibrium of the subgame following the action that would trigger it. Equivalently, the threat is part of a subgame-perfect strategy profile.</p>

<ol>
<li><strong>Entry deterrence example.</strong> Incumbent threatens to flood the market if entry occurs. Entry payoffs: enter and accommodate $(2, 4)$, enter and fight $(-2, -2)$. The threat to fight is not credible because fighting is worse for the incumbent.</li>
<li><strong>SPE prediction:</strong> entrant enters, incumbent accommodates. The Nash equilibrium "entrant stays out, incumbent threatens to fight" is not subgame-perfect.</li>
<li><strong>Restoring credibility through commitment.</strong> The incumbent can build excess capacity at cost $K$ so that fighting becomes the optimal continuation play. If $K$ is sunk, the threat becomes credible (Dixit 1980).</li>
</ol>

<p>Commitment devices that turn non-credible threats into credible ones:</p>

<p>Burning bridges (Schelling 1960): destroy the option to retreat, so that the only remaining response is the threat.</p>

<p>Delegation: hire an agent whose payoffs make the threat credible. Used in international diplomacy and corporate finance.</p>

<p>Repeated interaction: in infinitely repeated games, threats backed by trigger strategies are credible because the punishment is subgame Nash. Folk theorem applies.</p>

<p>Audience costs: politicians' threats become credible when public commitment raises the cost of backing down (Fearon 1994).</p>

<p>Reference: Micro2025.pdf Topic 4 Lecture 2; Selten 1965; Schelling, "The Strategy of Conflict" Ch. 2-3; Dixit 1980.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <circle cx="200" cy="50" r="8" fill="#333"/>
  <text x="60" y="55" font-size="12">Entrant</text>
  <line x1="200" y1="58" x2="100" y2="140" stroke="#333" stroke-width="2"/>
  <line x1="200" y1="58" x2="300" y2="140" stroke="#333" stroke-width="2"/>
  <text x="120" y="110" font-size="12">Stay out</text>
  <text x="260" y="110" font-size="12">Enter</text>
  <text x="80" y="160" font-size="12">(0, 10)</text>
  <circle cx="300" cy="150" r="8" fill="#1f77b4"/>
  <text x="316" y="155" font-size="12">Incumbent</text>
  <line x1="300" y1="158" x2="240" y2="240" stroke="#333"/>
  <line x1="300" y1="158" x2="360" y2="240" stroke="#333"/>
  <text x="240" y="200" font-size="12">Fight</text>
  <text x="360" y="200" font-size="12">Accommodate</text>
  <text x="220" y="260" font-size="12" fill="#d62728">(-2, -2)</text>
  <text x="340" y="260" font-size="12" fill="#2ca02c">(2, 4)</text>
  <text x="60" y="290" font-size="12" fill="#d62728">Fight is not credible: incumbent strictly prefers Accommodate.</text>
  <text x="60" y="308" font-size="12" fill="#2ca02c">SPE: Entrant enters, Incumbent accommodates.</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Threat to fight is not credible: SPE eliminates Nash equilibria sustained by non-credible threats.</p>""",
        "examples": r"""<ul>
<li><strong>Cuban Missile Crisis.</strong> Kennedy's threat of naval blockade and possible nuclear response was credible because the alternative (allowing missiles in Cuba) was politically and strategically worse.</li>
<li><strong>Industrial entry deterrence.</strong> Schmalensee (1981) shows that excess capacity in cement and chemicals industries is consistent with credible threats to fight entrants.</li>
<li><strong>Sovereign debt restructuring.</strong> A government's threat to default is credible only if default costs are lower than continued debt service. Sturzenegger-Zettelmeyer (2006) catalogue cases.</li>
<li><strong>Essay move.</strong> Doornik rewards explicit checks of credibility in any game where threats are mentioned. The standard trap is to accept the threat at face value, ignoring its incentive compatibility off path.</li>
<li><strong>Essay move.</strong> Commitment devices (sunk investments, delegation, public statements) turn non-credible threats into credible ones. Dixit (1980) is the canonical reference.</li>
<li><strong>Limitation.</strong> Trembling-hand perfection (Selten 1975) requires threats credible even under small probabilities of mistakes. Some SPE strategies fail this stronger test.</li>
<li>See also [[Concepts/Subgame Perfect Equilibrium]], [[Concepts/Entry Deterrence]], [[Concepts/First-Mover Advantage]].</li>
</ul>""",
    },
    "nash-existence-theorem": {
        "math": r"""<p>The <strong>Nash existence theorem</strong> (Nash 1950) states: every finite game has at least one (possibly mixed) Nash equilibrium. The proof uses Kakutani's fixed-point theorem applied to the best-response correspondence.</p>

<p>Let $G = (N, (S_i), (u_i))$ be a finite strategic-form game. Define mixed strategies $\Sigma_i = \Delta(S_i)$ and the expected payoff $u_i(\sigma)$. The best-response correspondence $BR_i: \Sigma_{-i} \rightrightarrows \Sigma_i$ assigns $BR_i(\sigma_{-i}) = \arg\max_{\sigma_i \in \Sigma_i} u_i(\sigma_i, \sigma_{-i})$.</p>

<ol>
<li>Each $\Sigma_i$ is a compact convex subset of Euclidean space (a simplex).</li>
<li>$u_i$ is continuous in $\sigma$ (multilinear, hence continuous on the compact domain).</li>
<li>$BR_i(\sigma_{-i})$ is non-empty (Weierstrass: continuous function on compact set attains its maximum).</li>
<li>$BR_i(\sigma_{-i})$ is convex (because $u_i$ is linear in $\sigma_i$ holding $\sigma_{-i}$ fixed: the set of maximisers is a face of the simplex).</li>
<li>$BR_i$ is upper-hemicontinuous (closed-graph; follows from continuity of $u_i$).</li>
</ol>

<p>The joint best-response correspondence $BR = \prod_i BR_i: \Sigma \rightrightarrows \Sigma$ satisfies all four Kakutani conditions: compact convex domain, non-empty values, convex values, upper-hemicontinuous. Kakutani's theorem then guarantees a fixed point $\sigma^*$ with $\sigma^* \in BR(\sigma^*)$, which is a Nash equilibrium.</p>

<p>Extensions:</p>

<p>Infinite strategy sets: Glicksberg (1952), Debreu-Fan-Glicksberg require continuity and quasi-concavity of $u_i$ in own strategy.</p>

<p>Discontinuous payoffs: Reny (1999) gives a "better-reply security" condition that ensures existence even with payoff discontinuities (applies to auctions).</p>

<p>The proof is non-constructive. Finding equilibria computationally is PPAD-complete (Daskalakis-Goldberg-Papadimitriou 2009), a hardness result that does not contradict existence.</p>

<p>Reference: Micro2025.pdf Topic 4 Lecture 1; Nash 1950 PNAS; Mas-Colell Ch. 8.D; Kakutani 1941.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <line x1="80" y1="260" x2="500" y2="260" stroke="#333"/>
  <line x1="80" y1="260" x2="80" y2="40" stroke="#333"/>
  <text x="500" y="280" font-size="13">$\sigma_2$</text>
  <text x="60" y="50" font-size="13">$\sigma_1$</text>
  <line x1="80" y1="80" x2="80" y2="160" stroke="#1f77b4" stroke-width="3"/>
  <line x1="80" y1="160" x2="280" y2="160" stroke="#1f77b4" stroke-width="3"/>
  <line x1="280" y1="160" x2="280" y2="260" stroke="#1f77b4" stroke-width="3"/>
  <text x="100" y="100" font-size="12" fill="#1f77b4">$BR_1$</text>
  <line x1="200" y1="260" x2="200" y2="200" stroke="#d62728" stroke-width="3"/>
  <line x1="200" y1="200" x2="500" y2="200" stroke="#d62728" stroke-width="3"/>
  <text x="380" y="190" font-size="12" fill="#d62728">$BR_2$</text>
  <circle cx="280" cy="200" r="6" fill="#2ca02c"/>
  <text x="290" y="195" font-size="12" fill="#2ca02c">Nash fixed point</text>
  <text x="60" y="300" font-size="12" fill="#555">Joint BR is UHC convex-valued; Kakutani gives a fixed point.</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">The best-response correspondence satisfies Kakutani's conditions, guaranteeing a fixed point that is a Nash equilibrium.</p>""",
        "examples": r"""<ul>
<li><strong>Matching Pennies.</strong> No pure-strategy Nash equilibrium, but Nash's theorem guarantees a mixed equilibrium. We find $(1/2, 1/2)$ by indifference.</li>
<li><strong>Cournot oligopoly with $n$ firms.</strong> Existence follows from Debreu-Fan-Glicksberg: strategy sets compact and convex, profit continuous and concave in own quantity. The interior equilibrium exists.</li>
<li><strong>First-price auctions.</strong> Discontinuous payoffs at ties prevent direct application of Glicksberg. Reny's better-reply security delivers existence (Athey 2001).</li>
<li><strong>Essay move.</strong> Doornik rewards essays that distinguish Nash's existence (finite games, mixed equilibrium) from Debreu-Fan-Glicksberg (infinite strategy sets, continuous payoffs, pure equilibrium).</li>
<li><strong>Essay move.</strong> Existence is non-constructive: Nash's proof guarantees an equilibrium without giving an algorithm to compute it. PPAD-hardness shows computational difficulty.</li>
<li><strong>Limitation.</strong> Existence does not imply uniqueness. Many games have multiple equilibria, raising the selection problem (focal points, refinements, learning dynamics).</li>
<li>See also [[Concepts/Nash Equilibrium]], [[Concepts/Mixed Strategy Equilibrium]], [[Concepts/Best Response Functions]].</li>
</ul>""",
    },

    "multitasking": {
        "math": r"""<p>The <strong>multitasking problem</strong> (Holmstrom-Milgrom 1991) arises when the agent allocates effort across multiple tasks $e = (e_1, e_2, \dots, e_n)$ but the principal can contract only on a noisy aggregate signal. The agent's cost of effort is $C(e)$, with cross-derivatives $\partial^2 C / \partial e_i \partial e_j \neq 0$ creating substitutability or complementarity across tasks.</p>

<p>The principal observes signals $y_i = e_i + \epsilon_i$ with measurement noise $\epsilon_i \sim N(0, \sigma_i^2)$. A linear contract pays $w = \alpha + \sum_i \beta_i y_i$. Optimal incentive intensities satisfy:</p>

$$\beta_i^* = \frac{V_i(e)}{1 + r \sigma_i^2 C''(e)},$$

<p>where $V_i$ is the principal's marginal value of task $i$. The intensity on each task depends on the noise in <strong>all</strong> signals through the cost cross-derivative.</p>

<ol>
<li>If task 1 is measurable (low $\sigma_1$) and task 2 is not (high $\sigma_2$), the principal may need to reduce $\beta_1$ to avoid distorting effort away from task 2.</li>
<li>Optimal incentives can be muted on the measurable task. In the extreme, $\beta_1 = 0$ even though $y_1$ is observable: low-powered fixed-wage contracts.</li>
<li>The result rationalises why public school teachers, government bureaucrats, and academic researchers face flat compensation: their multiple tasks (some unmeasurable) make high-powered incentives counterproductive.</li>
</ol>

<p>Multitasking explains <strong>gaming</strong>: agents shift effort to measured tasks (test scores) at the expense of unmeasured tasks (deeper learning). Campbell's law: the more an indicator is used for decisions, the more it gets distorted (Goodhart 1975).</p>

<p>Holmstrom-Milgrom show that linear contracts with low $\beta_i$ on all tasks may dominate a high-powered contract on one task. This rationalises bundled task assignments: pay the same low rate across the entire bundle to discourage substitution.</p>

<p>Reference: Micro2025.pdf Topic 8 Lecture on Multitasking; Holmstrom-Milgrom 1991 JLEO; Bolton-Dewatripont Ch. 4.5.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <text x="60" y="40" font-size="14" font-weight="bold">Multitasking: gaming on measured task</text>
  <line x1="80" y1="280" x2="540" y2="280" stroke="#333"/>
  <line x1="80" y1="280" x2="80" y2="60" stroke="#333"/>
  <text x="540" y="300" font-size="13">$\beta_1$ (incentive on task 1)</text>
  <text x="60" y="70" font-size="13">effort</text>
  <line x1="80" y1="240" x2="540" y2="80" stroke="#1f77b4" stroke-width="2"/>
  <text x="100" y="220" font-size="12" fill="#1f77b4">$e_1$ (measured)</text>
  <line x1="80" y1="160" x2="540" y2="240" stroke="#d62728" stroke-width="2"/>
  <text x="450" y="230" font-size="12" fill="#d62728">$e_2$ (hidden)</text>
  <text x="60" y="305" font-size="12" fill="#555">Raising $\beta_1$ crowds out unmeasured task 2.</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Stronger incentive on measured task pulls effort away from unmeasured task.</p>""",
        "examples": r"""<ul>
<li><strong>Teacher pay-for-performance.</strong> US states tying teacher pay to test scores documented gaming: teaching to the test, neglect of non-tested skills, even outright cheating (Atlanta 2009).</li>
<li><strong>Targets in health care.</strong> UK NHS waiting-time targets reduced waits but distorted clinical priorities (Propper-Sutton-Whitnall 2008).</li>
<li><strong>Sales-force pay.</strong> Commission-only pay encourages volume over customer relationships, often eroding long-run revenue.</li>
<li><strong>Essay move.</strong> Multitasking explains why high-powered incentives are unusual outside salesforce or capital markets. Doornik likes essays that link this to bureaucracy.</li>
<li><strong>Essay move.</strong> Compare to single-task moral hazard. With one task, optimal $\beta$ is positive. With multitasking, optimal $\beta$ on a measurable task can be zero.</li>
<li><strong>Limitation.</strong> The linear contract is exogenously imposed. Optimal nonlinear contracts can sometimes restore high-powered incentives while controlling substitution (Baker 2002).</li>
<li>See also [[Concepts/Holmstrom-Milgrom Linear Contracts Model]], [[Concepts/Linear Contracts]].</li>
</ul>""",
    },
    "selling-the-firm": {
        "math": r"""<p><strong>Selling the firm to the agent</strong> is the canonical first-best solution when the principal is risk-neutral, the agent is risk-neutral, and effort is unobservable. The principal "sells" the firm by setting the agent's wage equal to output minus a fixed transfer: $w(q) = q - T$ where $T$ is the rental fee.</p>

<p>The agent then bears all risk and chooses effort to maximise $E[q | e] - T - C(e)$. Since the agent is the residual claimant, effort is socially optimal: $\partial E[q]/\partial e = C'(e)$, exactly the first-best condition.</p>

<ol>
<li>Risk-neutral agent, IC binds at $e^{FB}$.</li>
<li>Principal sets $T = E[q | e^{FB}] - C(e^{FB}) - \bar u$ to extract all surplus down to the participant's outside option $\bar u$. The agent earns $\bar u$ in expectation; the principal earns $T$, the entire net surplus.</li>
<li>Verify IR: $E[q | e^{FB}] - T - C(e^{FB}) = \bar u$. Satisfied with equality.</li>
<li>Verify IC: the agent's marginal incentive to raise $e$ is $\partial E[q]/\partial e - C'(e) = 0$ at $e^{FB}$.</li>
</ol>

<p>The result generalises: any risk-neutral agent who fully internalises output can achieve first best. Real-world franchising (McDonalds, Domino's), share-cropping with risk-neutral tenants (rare), and management buyouts approximate this.</p>

<p>The result <strong>fails</strong> when:</p>

<p>(i) The agent is risk-averse: full risk-bearing carries a risk premium that outweighs the effort gain. Linear contracts with $\beta < 1$ are then optimal (Holmstrom-Milgrom).</p>

<p>(ii) Limited liability binds: the agent's worst-case output is $-\infty$, but the agent cannot lose more than current wealth. The transfer $T$ must be bounded, sacrificing efficiency.</p>

<p>(iii) Wealth constraints prevent paying $T$ up front. The agent cannot finance the buyout.</p>

<p>Reference: Micro2025.pdf Topic 8 Lecture 2; Bolton-Dewatripont Ch. 4.2; Mas-Colell Ch. 14.B.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <text x="60" y="40" font-size="14" font-weight="bold">Selling the firm: agent as residual claimant</text>
  <line x1="80" y1="260" x2="540" y2="260" stroke="#333"/>
  <line x1="80" y1="260" x2="80" y2="60" stroke="#333"/>
  <text x="540" y="280" font-size="13">$q$</text>
  <text x="60" y="70" font-size="13">$w$</text>
  <line x1="80" y1="220" x2="540" y2="80" stroke="#1f77b4" stroke-width="2"/>
  <text x="200" y="120" font-size="12" fill="#1f77b4">$w(q) = q - T$ (slope 1)</text>
  <line x1="80" y1="190" x2="540" y2="190" stroke="#d62728" stroke-width="2" stroke-dasharray="4 2"/>
  <text x="100" y="185" font-size="12" fill="#d62728">Risk-averse agent: $w = \alpha + \beta q, \beta < 1$</text>
  <text x="60" y="305" font-size="12" fill="#555">Full slope contract gives first-best effort; rare in practice.</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Selling the firm: agent's marginal pay equals marginal output, restoring first-best effort.</p>""",
        "examples": r"""<ul>
<li><strong>Franchising.</strong> McDonalds and Subway franchisees pay a royalty and keep the residual. Brickley-Dark (1987) and Lafontaine-Slade survey the empirical evidence that this aligns franchisee effort.</li>
<li><strong>Sharecropping with risk-neutral tenants.</strong> Rare empirically: most tenants are risk-averse and capital-constrained, so 50-50 sharing or fixed rents dominate (Stiglitz 1974).</li>
<li><strong>Management buyouts and LBOs.</strong> Jensen (1989) argues that LBO incentives approximate selling the firm to management.</li>
<li><strong>Essay move.</strong> Selling the firm is the analytical benchmark for the risk-versus-insurance trade-off. Doornik rewards explicit recognition that it works only under risk neutrality and unlimited liability.</li>
<li><strong>Essay move.</strong> Compare to linear contracts. Selling the firm is the $\beta = 1$ case; risk-averse agents prefer $\beta < 1$ for risk sharing.</li>
<li><strong>Limitation.</strong> Wealth constraints prevent paying the up-front transfer $T$. Real franchisees borrow to fund the fee; agency persists at the financial level.</li>
<li>See also [[Concepts/First-Best Contract]], [[Concepts/Risk vs Insurance Trade-off]].</li>
</ul>""",
    },
    "insurance-moral-hazard": {
        "math": r"""<p><strong>Moral hazard in insurance</strong> arises when the insured's care-taking effort is unobservable. The insurer cannot condition the premium on effort, so insurance reduces the incentive to avoid losses. Pauly (1968) gave the first formal treatment.</p>

<p>Let an individual with wealth $w$ face a loss $L$ with probability $p(e)$ where $e \geq 0$ is unobservable care. Without insurance, $\max_e E[u] = (1 - p(e)) u(w) + p(e) u(w - L) - c(e)$, FOC: $-p'(e) [u(w) - u(w - L)] = c'(e)$.</p>

<p>With full insurance at fair premium $p L$, the insured's wealth in both states equals $w - p L$. Effort cost $c(e)$ remains but provides no benefit: optimal effort is zero. The insurer's expected payment rises, the actuarially fair premium must adjust upward.</p>

<ol>
<li><strong>Full insurance result:</strong> with observable effort, the first-best solution is full insurance plus a contract that requires the efficient effort level. With unobservable effort, full insurance gives $e = 0$.</li>
<li><strong>Partial insurance solution:</strong> the insured must bear some risk (deductible, co-insurance). The optimal contract has coverage less than 100%, balancing risk-sharing against moral hazard incentives.</li>
<li><strong>Co-insurance rate $\alpha$:</strong> the insured pays $\alpha L$ in the loss state and the insurer pays $(1 - \alpha) L$. The premium is $\pi = (1 - \alpha) p(e^*) L$, where $e^*$ is the effort the insured chooses under coverage $\alpha$.</li>
</ol>

<p>The standard empirical evidence: Manning et al. (1987) RAND Health Insurance Experiment found that subjects with higher cost-sharing spent 30% less on healthcare with no major detrimental health effects. Finkelstein (2007) shows the introduction of Medicare in 1965 raised hospital spending sharply, consistent with moral-hazard demand effects.</p>

<p>Distinguish <strong>ex-ante moral hazard</strong> (care-taking effort, e.g. exercise) from <strong>ex-post moral hazard</strong> (utilisation given loss, e.g. medical treatment intensity). The former is the textbook framework; the latter dominates many empirical studies.</p>

<p>Reference: Micro2025.pdf Topic 8 Lecture on Insurance Moral Hazard; Pauly 1968 AER; Arrow 1963 AER; Einav-Finkelstein 2018 ARE.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <text x="60" y="40" font-size="14" font-weight="bold">Insurance and effort: trade-off</text>
  <line x1="80" y1="280" x2="540" y2="280" stroke="#333"/>
  <line x1="80" y1="280" x2="80" y2="60" stroke="#333"/>
  <text x="540" y="300" font-size="13">coverage $1-\alpha$</text>
  <text x="60" y="70" font-size="13">effort $e^*$</text>
  <line x1="80" y1="80" x2="540" y2="240" stroke="#1f77b4" stroke-width="2"/>
  <text x="100" y="100" font-size="12" fill="#1f77b4">$e^*$ falls with coverage</text>
  <circle cx="540" cy="240" r="6" fill="#d62728"/>
  <text x="450" y="260" font-size="12" fill="#d62728">$e^*=0$ at full insurance</text>
  <text x="60" y="310" font-size="12" fill="#555">Optimal contract: partial coverage with deductible or co-insurance.</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Effort decreases with coverage. Optimal insurance balances risk-bearing against moral-hazard distortion.</p>""",
        "examples": r"""<ul>
<li><strong>Auto insurance.</strong> Deductibles and no-claims bonuses are the standard moral-hazard solution. Cohen (2005) documents large empirical effects in Israeli auto insurance.</li>
<li><strong>Health insurance.</strong> RAND HIE (Manning et al. 1987) randomised cost-sharing levels; spending fell with cost-sharing with limited health consequences for most people.</li>
<li><strong>Unemployment insurance.</strong> Generous UI lowers job search effort (Meyer 1990, Lalive 2007). Optimal UI design (Shavell-Weiss 1979) trades off insurance against search incentives.</li>
<li><strong>Essay move.</strong> Distinguish ex-ante from ex-post moral hazard. Doornik rewards explicit treatment of the latter as the dominant force in medical care utilisation studies.</li>
<li><strong>Essay move.</strong> Show the trade-off graphically: full insurance gives full risk-sharing but zero effort; no insurance gives full effort but full risk. Optimal contract is interior.</li>
<li><strong>Limitation.</strong> The model abstracts from selection: those who buy insurance may also be the lowest-effort types ex ante. Distinguishing moral hazard from adverse selection is hard (Chiappori-Salanie 2000, Einav-Finkelstein-Cullen 2010).</li>
<li>See also [[Concepts/Risk vs Insurance Trade-off]], [[Concepts/Moral Hazard]], [[Concepts/Peltzman Effect]].</li>
</ul>""",
    },
    "repeated-moral-hazard": {
        "math": r"""<p>The <strong>repeated moral hazard</strong> framework (Rogerson 1985, Spear-Srivastava 1987) studies how dynamic incentive contracts emerge when the principal-agent relationship lasts multiple periods. With observable past outcomes, the principal can condition future compensation on the history of signals, building a richer incentive structure than one-shot contracts.</p>

<p>The standard setup: in each period $t$, the agent exerts effort $e_t$, output $y_t$ is realised with distribution $f(y | e_t)$, and the agent receives a transfer $w_t(y_1, \dots, y_t)$. Both principal and agent have common discount factor $\delta$. The principal maximises expected discounted profit subject to dynamic IC and IR.</p>

<ol>
<li><strong>Recursive formulation:</strong> the state variable is the agent's promised continuation utility $U_t$. The Bellman equation reduces the dynamic problem to a sequence of static contracting problems indexed by promised utility.</li>
<li><strong>Optimal smoothing:</strong> when the agent is risk-averse and the principal risk-neutral, future utility is smoothed across history-dependent realisations.</li>
<li><strong>Memory and bonuses:</strong> Rogerson (1985) shows that even when current output is a sufficient statistic for current effort, optimal contracts use the entire history. The reason is dynamic insurance against the agent's effort-utility trade-off.</li>
</ol>

<p>Key results:</p>

<p>(i) Inverse Euler equation: $1/u'(c_t) = \delta E_t [1/u'(c_{t+1})]$ when agents are risk-averse and principals risk-neutral (Rogerson). This implies consumption is back-loaded relative to first-best.</p>

<p>(ii) Stationarity result (Spear-Srivastava): the optimal policy depends only on the promised continuation utility, not on calendar time, so the contract is a Markovian function.</p>

<p>(iii) "Wait and watch" feature: in long-horizon contracts, fluctuating compensation builds reputation. The agent's incentives improve over time as the gap between promised utility and the lower bound grows.</p>

<p>Reference: Micro2025.pdf Topic 8 Lecture on Repeated Moral Hazard; Rogerson 1985 Econometrica; Spear-Srivastava 1987 REStud; Sannikov 2008.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <line x1="60" y1="280" x2="540" y2="280" stroke="#333"/>
  <line x1="60" y1="280" x2="60" y2="60" stroke="#333"/>
  <text x="540" y="300" font-size="13">period $t$</text>
  <text x="60" y="70" font-size="13">utility $U_t$</text>
  <path d="M 80 240 L 130 200 L 180 220 L 230 170 L 280 190 L 330 140 L 380 160 L 430 110 L 480 130" fill="none" stroke="#1f77b4" stroke-width="2"/>
  <text x="100" y="220" font-size="12" fill="#1f77b4">Promised utility path (back-loaded)</text>
  <line x1="60" y1="180" x2="540" y2="180" stroke="#d62728" stroke-width="1" stroke-dasharray="4 2"/>
  <text x="60" y="175" font-size="11" fill="#d62728">First-best (smooth)</text>
  <text x="60" y="310" font-size="12" fill="#555">Promised continuation utility grows as the agent builds capital in the contract.</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Optimal repeated-moral-hazard contracts back-load utility to relax dynamic IC constraints.</p>""",
        "examples": r"""<ul>
<li><strong>Wage-tenure profiles.</strong> Lazear (1979) shows that upward-sloping wage profiles arise as incentive devices: workers underpaid early, overpaid late, with the threat of firing as discipline.</li>
<li><strong>Stock-based executive compensation.</strong> Bebchuk-Fried (2003) document that vesting schedules and stock-option features deliver back-loaded payment, consistent with the theory.</li>
<li><strong>Sovereign debt restructuring.</strong> Eaton-Gersovitz (1981) show that long-run lending relationships use the threat of exclusion from future credit to discipline current repayment.</li>
<li><strong>Essay move.</strong> Doornik rewards explicit recognition that repeated moral hazard delivers fundamentally different contract shapes than one-shot moral hazard. Continuation utility is the right state variable.</li>
<li><strong>Essay move.</strong> The inverse Euler equation gives back-loading. This is the dynamic version of risk-sharing distortion under moral hazard.</li>
<li><strong>Limitation.</strong> Renegotiation can destroy commitment to back-loaded payments. Fudenberg-Holmstrom-Milgrom (1990) study renegotiation-proof contracts. Sannikov (2008) provides a continuous-time framework that handles renegotiation explicitly.</li>
<li>See also [[Concepts/Holmstrom-Milgrom Linear Contracts Model]], [[Concepts/Infinitely Repeated Games]].</li>
</ul>""",
    },

    "hidden-information-vs-hidden-action": {
        "math": r"""<p><strong>Hidden information</strong> (adverse selection) and <strong>hidden action</strong> (moral hazard) are the two main forms of asymmetric information. The distinction governs which contracting framework applies.</p>

<p>Hidden information: the agent has a fixed type $\theta \in \Theta$ that the principal cannot observe. Examples: a worker's productivity, a borrower's default risk, an insurance applicant's accident propensity. The contracting problem is to design a menu that screens types or to interpret signals that reveal them.</p>

<p>Hidden action: the agent chooses an effort $e \in E$ after the contract is signed. The principal observes output $y$ correlated with $e$ but not $e$ itself. Examples: an employee's work intensity, an insured person's care-taking, a CEO's decision to undertake a risky project.</p>

<ol>
<li><strong>Timing differs.</strong> Hidden information is a pre-contract problem; hidden action is a post-contract problem. The mathematical structure differs accordingly.</li>
<li><strong>Solution concept differs.</strong> Hidden information uses revelation-principle and screening menus. Hidden action uses optimal incentive contracts (linear contracts with intensity $\beta$).</li>
<li><strong>Welfare loss differs.</strong> Hidden information generates information rents to high types and distortion to low types. Hidden action generates a risk premium and reduced effort.</li>
</ol>

<p><strong>Combined problems</strong> (hybrid models): some real settings have both. Insurance has selection on risk type (hidden information) and care-taking effort (hidden action). The Rothschild-Stiglitz model focuses on the former; Pauly (1968) on the latter; Chiappori-Salanie (2000) and Einav-Finkelstein-Cullen (2010) try to identify both empirically.</p>

<p>Diagnostic test: ask "what is unobservable to the principal, the agent's type or the agent's action?" Both lead to inefficient contracts, but the inefficiencies have different structures. Doornik often probes this distinction.</p>

<p>Reference: Micro2025.pdf Topic 7-8 Overview; Bolton-Dewatripont Ch. 2-4; Mas-Colell Ch. 13-14.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <text x="60" y="40" font-size="14" font-weight="bold">Two forms of asymmetric information</text>
  <rect x="60" y="80" width="240" height="180" fill="#dbeafe" stroke="#1d4ed8" stroke-width="2"/>
  <text x="180" y="110" font-size="13" font-weight="bold" text-anchor="middle">Hidden Information</text>
  <text x="180" y="135" font-size="12" text-anchor="middle">Type $\theta$ unobservable</text>
  <text x="180" y="160" font-size="12" text-anchor="middle">Pre-contract</text>
  <text x="180" y="185" font-size="12" text-anchor="middle">Adverse selection</text>
  <text x="180" y="215" font-size="12" text-anchor="middle">Screening, signalling</text>
  <text x="180" y="240" font-size="12" text-anchor="middle">Akerlof, Spence, R-S</text>
  <rect x="320" y="80" width="240" height="180" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
  <text x="440" y="110" font-size="13" font-weight="bold" text-anchor="middle">Hidden Action</text>
  <text x="440" y="135" font-size="12" text-anchor="middle">Effort $e$ unobservable</text>
  <text x="440" y="160" font-size="12" text-anchor="middle">Post-contract</text>
  <text x="440" y="185" font-size="12" text-anchor="middle">Moral hazard</text>
  <text x="440" y="215" font-size="12" text-anchor="middle">Incentive contracts</text>
  <text x="440" y="240" font-size="12" text-anchor="middle">Holmstrom, Mirrlees</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Hidden information acts before contracting; hidden action after.</p>""",
        "examples": r"""<ul>
<li><strong>Insurance markets.</strong> Insurance has both: customers have hidden risk types (adverse selection) and hidden care-taking effort (moral hazard). Disentangling them empirically is hard (Chiappori-Salanie 2000).</li>
<li><strong>Used car markets.</strong> Pure hidden information: seller knows vehicle quality, buyer does not. Lemons unravel as in Akerlof.</li>
<li><strong>Executive compensation.</strong> Predominantly hidden action: shareholders cannot observe the CEO's effort or care, only firm performance.</li>
<li><strong>Essay move.</strong> Doornik often asks students to classify a contracting problem before solving it. Get this right first; the wrong framework gives the wrong predictions.</li>
<li><strong>Essay move.</strong> Hybrid models combine both. The Rothschild-Stiglitz screening contract pools moral hazard concerns into the residual risk allocated to high types.</li>
<li><strong>Limitation.</strong> Identifying which asymmetry matters in real data requires sharp empirical strategies. Positive-correlation tests (Chiappori-Salanie) attempt to do this.</li>
<li>See also [[Concepts/Asymmetric Information]], [[Concepts/Moral Hazard]], [[Concepts/Adverse Selection]].</li>
</ul>""",
    },
    "riley-outcome": {
        "math": r"""<p>The <strong>Riley outcome</strong> (Riley 1979) is the least-cost separating equilibrium in a signalling game. Among all separating equilibria, the Riley outcome involves the minimum signal cost compatible with separation: it is the Pareto-best separating outcome from the high-type's perspective.</p>

<p>In the Spence model with two types $\theta_L, \theta_H$ and signal $s$ (education level), separation requires the IC constraint:</p>

$$w(\theta_H) - c_L(s_H) \leq w(\theta_L) - c_L(s_L),$$

<p>so that the low type does not mimic the high type. The Riley outcome chooses $s_H^*$ at the lowest value satisfying this constraint with equality. Setting $s_L = 0$ and $w(\theta) = \theta$ under competitive employers, we get:</p>

$$s_H^* = \frac{\theta_H - \theta_L}{c_L'(0)}.$$

<ol>
<li>Identify the set of separating equilibria parameterised by the high-type signal $s_H$.</li>
<li>Apply the lowest $s_H$ that prevents mimicking: this is the Riley equilibrium.</li>
<li>Verify single-crossing: the marginal cost of signalling is lower for the high type, so the constraint binds only at the boundary.</li>
</ol>

<p>The Riley outcome can be justified by several equilibrium refinements:</p>

<p>(i) Intuitive criterion (Cho-Kreps 1987): eliminates pooling equilibria and selects Riley as the unique separating equilibrium consistent with reasonable off-path beliefs.</p>

<p>(ii) Stable equilibria (Kohlberg-Mertens 1986): also selects Riley in standard signalling games.</p>

<p>(iii) Reactive equilibria (Riley 1979): the original refinement that motivated the name.</p>

<p>Welfare implication: even the best separating outcome is inefficient. Pooling at the average wage (when feasible) is sometimes Pareto-preferred, but requires a refinement that allows it. The Wilson equilibrium refinement supports pooling under some parameter values; the intuitive criterion does not.</p>

<p>Reference: Micro2025.pdf Topic 7 Lecture 2; Riley 1979 Econometrica; Cho-Kreps 1987 QJE; Mas-Colell Ch. 13.D.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <line x1="80" y1="260" x2="540" y2="260" stroke="#333"/>
  <line x1="80" y1="260" x2="80" y2="60" stroke="#333"/>
  <text x="540" y="280" font-size="13">signal $s$</text>
  <text x="60" y="70" font-size="13">utility</text>
  <line x1="80" y1="80" x2="540" y2="240" stroke="#1f77b4" stroke-width="2"/>
  <text x="120" y="100" font-size="12" fill="#1f77b4">High-type IC binds at Riley</text>
  <line x1="80" y1="120" x2="540" y2="200" stroke="#d62728" stroke-width="2"/>
  <text x="120" y="155" font-size="12" fill="#d62728">Low-type IC</text>
  <circle cx="280" cy="170" r="6" fill="#2ca02c"/>
  <text x="290" y="165" font-size="12" fill="#2ca02c">Riley $s_H^*$</text>
  <text x="60" y="305" font-size="12" fill="#555">Smallest signal that prevents low-type mimicking.</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Riley outcome: high type signals the minimum amount needed to separate.</p>""",
        "examples": r"""<ul>
<li><strong>Undergraduate degrees.</strong> The Riley outcome predicts that the minimum-cost separating signal is the lowest education level that the low-ability type cannot profitably mimic. Most empirical evidence (Card 1999) is consistent.</li>
<li><strong>Costly product advertising.</strong> Milgrom-Roberts (1986) show that high-quality firms burn money on uninformative ads as a Riley-style signal of quality.</li>
<li><strong>Sovereign bond auctions.</strong> Higher-quality issuers offer larger amounts at competitive yields, signalling their type at the lowest cost compatible with separation.</li>
<li><strong>Essay move.</strong> Use Riley as the canonical refinement-selected separating equilibrium. Doornik rewards explicit appeal to the intuitive criterion to justify this selection.</li>
<li><strong>Essay move.</strong> Compare Riley to the inefficient pooling that pre-Riley equilibria allowed. The selection question is the real content of signalling theory.</li>
<li><strong>Limitation.</strong> Riley requires single-crossing. If marginal signalling costs are not monotonic in type, separation may not be achievable.</li>
<li>See also [[Concepts/Intuitive Criterion]], [[Concepts/Spence Signalling]], [[Concepts/Separating vs Pooling]].</li>
</ul>""",
    },
    "wilson-refinement": {
        "math": r"""<p>The <strong>Wilson refinement</strong> (Wilson 1977) in screening games adds robustness to entry. A Wilson equilibrium is a pair of contracts (or a single contract pooling all types) such that no entrant can profitably enter offering a new contract, allowing for the incumbents to withdraw their unprofitable contracts.</p>

<p>The motivation: in the Rothschild-Stiglitz model, the separating equilibrium can be broken by an entrant offering a pooling contract. The pooling contract is profitable only because the entrant attracts both types. If the incumbent then withdraws the high-risk contract, the pooling contract becomes unprofitable for the entrant. Wilson required that entrants anticipate this.</p>

<ol>
<li><strong>Step 1.</strong> Identify the contract menu offered by incumbents.</li>
<li><strong>Step 2.</strong> Consider any deviation contract by an entrant. Compute which existing contracts are still profitable after the deviation (without the entrant in the market).</li>
<li><strong>Step 3.</strong> The deviation is Wilson-feasible iff it is still profitable after assuming the unprofitable incumbent contracts are withdrawn.</li>
</ol>

<p>Wilson equilibrium can be a pooling equilibrium when the proportion of high-risk types is low. The R-S separating equilibrium can be broken by a pooling contract; the pooling contract is Wilson-stable because the R-S separating contracts would not be profitable in its presence.</p>

<p>Comparison with other refinements:</p>

<p>R-S (no Wilson): only separating equilibrium exists; non-existence problem when the proportion of high types is low.</p>

<p>Wilson: pooling equilibria emerge; the non-existence problem is resolved.</p>

<p>Miyazaki-Wilson-Spence: extends to allow incumbents to break even on average across contracts. Generates cross-subsidisation from low-risk to high-risk types.</p>

<p>Wilson refinement is now seen as a model of foresighted competition. In modern industrial organisation, it gives a way to predict pooling outcomes that pure R-S precludes.</p>

<p>Reference: Micro2025.pdf Topic 7 Lecture 3; Wilson 1977 JET; Miyazaki 1977; Bolton-Dewatripont Ch. 3.4.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <text x="60" y="40" font-size="14" font-weight="bold">Wilson vs R-S</text>
  <rect x="60" y="80" width="240" height="180" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
  <text x="180" y="110" font-size="13" font-weight="bold" text-anchor="middle">R-S</text>
  <text x="180" y="140" font-size="12" text-anchor="middle">Separating only</text>
  <text x="180" y="165" font-size="12" text-anchor="middle">May not exist</text>
  <text x="180" y="190" font-size="12" text-anchor="middle">when high types rare</text>
  <text x="180" y="225" font-size="12" text-anchor="middle">Single-deviation logic</text>
  <rect x="320" y="80" width="240" height="180" fill="#dbeafe" stroke="#1d4ed8" stroke-width="2"/>
  <text x="440" y="110" font-size="13" font-weight="bold" text-anchor="middle">Wilson</text>
  <text x="440" y="140" font-size="12" text-anchor="middle">Pooling possible</text>
  <text x="440" y="165" font-size="12" text-anchor="middle">Always exists</text>
  <text x="440" y="190" font-size="12" text-anchor="middle">when low types abundant</text>
  <text x="440" y="225" font-size="12" text-anchor="middle">Foresighted entry</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Wilson refinement assumes entrants anticipate incumbent withdrawals, allowing pooling equilibria.</p>""",
        "examples": r"""<ul>
<li><strong>Group health insurance.</strong> Employer pools often deliver Wilson-style pooling. Bundling employees across risk types reduces selection problems.</li>
<li><strong>Universal social insurance.</strong> Government provision can sustain pooling that private markets cannot (Akerlof unravelling), consistent with Wilson logic when the high-type proportion is low.</li>
<li><strong>Crowdsourced ratings.</strong> Platforms like Airbnb pool diverse users; the absence of explicit screening reflects Wilson-style competitive pressures and reputation effects.</li>
<li><strong>Essay move.</strong> Doornik likes essays that contrast R-S and Wilson side-by-side. R-S is more standard in textbooks; Wilson is more realistic when entrants can anticipate competitive responses.</li>
<li><strong>Essay move.</strong> Wilson resolves the R-S non-existence problem. The Miyazaki-Wilson-Spence extension delivers cross-subsidising contracts as the second-best.</li>
<li><strong>Limitation.</strong> Wilson's reactive logic is somewhat ad hoc; it does not arise from a standard equilibrium concept. Mas-Colell, Whinston, Green call it "off-equilibrium reactions" rather than equilibrium per se.</li>
<li>See also [[Concepts/Rothschild-Stiglitz Screening]], [[Concepts/Pooling Equilibrium]], [[Concepts/Multiple Equilibria in Lemons Markets]].</li>
</ul>""",
    },
    "partial-unravelling": {
        "math": r"""<p><strong>Partial unravelling</strong> occurs in adverse-selection markets when high-quality types exit but not all middle-quality types do. The remaining market trades at a price reflecting the lower average quality, but the market does not collapse to zero. Akerlof's lemons model is the extreme case of full unravelling; partial unravelling is the more typical empirical outcome.</p>

<p>Setup: a continuum of types $\theta \in [\theta_L, \theta_H]$, $\theta \sim F$. Sellers value type $\theta$ at $\theta$; buyers value at $v(\theta) > \theta$. With observable type, all trade. With unobservable type, the market price is $p$ and the participating sellers are those with $\theta < p$. The buyer's break-even condition is $p = E[v(\theta) | \theta < p]$.</p>

<ol>
<li>The equilibrium price $p^*$ is a fixed point of $p = E[v(\theta) | \theta < p]$.</li>
<li>If $v(\theta_H) > \theta_H$ (mutually beneficial trade at the top) but $v(\theta_L) < \theta_L$ (top excluded at the equilibrium price), partial unravelling results: some trade occurs, but not at the maximum efficient level.</li>
<li>Full unravelling (Akerlof) occurs when the only fixed point is $p^* = \theta_L$ and all types above some threshold exit.</li>
</ol>

<p>Diagnostic: full unravelling requires that for every candidate $p$, the average type just below $p$ is too low to support that price. Partial unravelling requires interior fixed points.</p>

<p>Empirical correlates: residual demand for high-quality used cars suggests partial unravelling, not full. Quality indicators (warranties, dealer reputation, vehicle history reports) sustain trade in high-quality segments even with hidden information.</p>

<p>Akerlof 1970 emphasised full unravelling; subsequent work (Wilson 1980, Mailath-Samuelson 2001) clarified the conditions for partial vs full unravelling. The "thin market" outcome typical of partial unravelling explains why used-good markets exist but have lower volume than under full information.</p>

<p>Reference: Micro2025.pdf Topic 7 Lecture 1; Akerlof 1970 QJE; Mailath-Samuelson 2001; Bolton-Dewatripont Ch. 2.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <line x1="80" y1="260" x2="540" y2="260" stroke="#333"/>
  <line x1="80" y1="260" x2="80" y2="60" stroke="#333"/>
  <text x="540" y="280" font-size="13">price $p$</text>
  <text x="60" y="70" font-size="13">$E[v|\theta<p]$</text>
  <line x1="80" y1="260" x2="540" y2="60" stroke="#888" stroke-width="1" stroke-dasharray="3 3"/>
  <text x="450" y="80" font-size="11" fill="#888">$45°$</text>
  <path d="M 80 220 Q 250 180 540 80" fill="none" stroke="#1f77b4" stroke-width="2"/>
  <text x="200" y="170" font-size="12" fill="#1f77b4">avg quality curve</text>
  <circle cx="260" cy="180" r="6" fill="#2ca02c"/>
  <text x="270" y="175" font-size="12" fill="#2ca02c">Partial unravelling</text>
  <text x="60" y="305" font-size="12" fill="#555">Equilibrium where curve crosses 45° line: thin but nonzero market.</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Partial unravelling: an interior fixed point exists, supporting trade at a thinned-out price.</p>""",
        "examples": r"""<ul>
<li><strong>Used car markets.</strong> Volume is lower than under full information but not zero. Quality indicators (CarFax, certified pre-owned) help sustain trade.</li>
<li><strong>Used machinery markets.</strong> Genesove (1993) documents thinning but not vanishing of trade in used wholesale auto markets.</li>
<li><strong>Health insurance.</strong> Adverse selection thins the market for individual policies but does not eliminate them, partly because of regulation and partial pooling.</li>
<li><strong>Essay move.</strong> Distinguish partial from full unravelling. Doornik rewards essays that derive the fixed-point condition and check whether interior solutions exist.</li>
<li><strong>Essay move.</strong> Quality indicators and warranties act as signals that prevent full unravelling. Real markets sustain trade through institutional design.</li>
<li><strong>Limitation.</strong> The continuum-of-types model is a smooth approximation; with finite types, the analysis becomes piecewise constant and the equilibrium can jump.</li>
<li>See also [[Concepts/Full Unravelling]], [[Concepts/Akerlof Lemons Market]], [[Concepts/Asymmetric Information]].</li>
</ul>""",
    },
    "multiple-equilibria-lemons": {
        "math": r"""<p><strong>Multiple equilibria in lemons markets</strong> arise when the fixed-point equation $p = E[v(\theta) | \theta < p]$ has more than one solution. The market can sustain a high-price, high-quality equilibrium and a low-price, low-quality equilibrium simultaneously, with no further information to select between them.</p>

<p>The setup: sellers know their type $\theta \in [\theta_L, \theta_H]$, buyers do not. The buyer break-even price is $p = E[v(\theta) | \theta < p]$, where $v(\theta)$ is the buyer's valuation. Multiplicity arises when this equation has multiple fixed points, typically when $v(\theta)$ is non-linear or types are non-uniformly distributed.</p>

<ol>
<li><strong>Mailath-Samuelson example:</strong> with two types $\theta_L$ and $\theta_H$ and pooling proportion $\alpha$, the high-equilibrium has trade at $p_H = \alpha v(\theta_H) + (1-\alpha) v(\theta_L)$; the low-equilibrium has trade only at $p_L = v(\theta_L)$.</li>
<li><strong>Stability:</strong> the high equilibrium is "better" (more trade, higher welfare). It can be destabilised by a small perception shock that triggers high-quality sellers to exit, collapsing to the low equilibrium.</li>
<li><strong>Selection mechanisms:</strong> coordination devices (industry certifications, government quality standards) can resolve the selection problem. Without them, the market may oscillate between equilibria.</li>
</ol>

<p>Equilibrium selection in lemons markets has policy implications:</p>

<p>(i) The low equilibrium can be Pareto-dominated by the high equilibrium, so policies that "tip" the market toward the high-quality outcome can be welfare-improving (warranties, certifications).</p>

<p>(ii) Sunspot equilibria: shifts in beliefs about quality can move the market between equilibria without any change in fundamentals. This is the formal basis for "confidence crises" in financial markets.</p>

<p>(iii) The financial crisis (2008) is a frequently cited application: subprime mortgage securitisation can be modelled as a lemons market that shifted from a high-quality to a low-quality equilibrium.</p>

<p>Reference: Micro2025.pdf Topic 7 Lecture 1; Mailath-Samuelson 2001; Diamond 1971; Wilson 1980 JEL.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <line x1="80" y1="260" x2="540" y2="260" stroke="#333"/>
  <line x1="80" y1="260" x2="80" y2="60" stroke="#333"/>
  <text x="540" y="280" font-size="13">$p$</text>
  <text x="60" y="70" font-size="13">$E[v|\theta<p]$</text>
  <line x1="80" y1="260" x2="540" y2="60" stroke="#888" stroke-width="1" stroke-dasharray="3 3"/>
  <path d="M 80 220 Q 200 230 300 150 Q 400 90 540 80" fill="none" stroke="#1f77b4" stroke-width="2"/>
  <circle cx="190" cy="220" r="6" fill="#d62728"/>
  <text x="200" y="215" font-size="12" fill="#d62728">Low eq.</text>
  <circle cx="430" cy="110" r="6" fill="#2ca02c"/>
  <text x="350" y="105" font-size="12" fill="#2ca02c">High eq.</text>
  <text x="60" y="305" font-size="12" fill="#555">Two stable fixed points: confidence determines which prevails.</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Two equilibria coexist; coordination or sunspot shocks select between them.</p>""",
        "examples": r"""<ul>
<li><strong>Financial-asset markets in crisis.</strong> The 2008 crisis displays a shift between high-quality and low-quality equilibria in mortgage-backed securities, triggered by Lehman's collapse.</li>
<li><strong>Currency runs.</strong> Obstfeld (1996) shows that exchange-rate regimes can have multiple equilibria, with fundamentals consistent with either continued peg or collapse.</li>
<li><strong>Used car markets.</strong> Coordination on warranty schemes or independent inspection services can shift the equilibrium from low- to high-quality trade.</li>
<li><strong>Essay move.</strong> Doornik rewards students who note that multiplicity creates a selection problem unresolved by economic theory. Coordination devices (institutions, government interventions) can be welfare-improving.</li>
<li><strong>Essay move.</strong> Compare to coordination games (Battle of the Sexes, currency attacks). The lemons multiplicity has the same flavour: equilibrium prediction requires extra-economic input.</li>
<li><strong>Limitation.</strong> Multiplicity is sensitive to functional form. Under simple assumptions (uniform types, linear valuation), the lemons model has a unique equilibrium.</li>
<li>See also [[Concepts/Akerlof Lemons Market]], [[Concepts/Pooling Equilibrium]].</li>
</ul>""",
    },
    "winners-curse": {
        "math": r"""<p>The <strong>winner's curse</strong> arises in common-value auctions: the bidder who wins is precisely the one who most overestimated the asset's value. Conditional on winning, the bidder's value estimate is biased upward relative to the unconditional estimate.</p>

<p>Setup: $n$ bidders observe noisy signals $s_i = v + \epsilon_i$ of the common value $v$. In a first-price auction, the naive bid $b_i = s_i$ implies expected profit $E[v - b_i | i \text{ wins}] = E[v | s_i, s_j < s_i \forall j \neq i] - s_i < 0$. The winner's curse implies that conditioning on winning lowers the expected value below the signal.</p>

<ol>
<li><strong>Order-statistic intuition:</strong> winning is associated with $s_i$ being the highest signal. The order statistic shifts the conditional expectation: $E[v | s_i] \neq E[v | s_i, i \text{ wins}]$.</li>
<li><strong>Optimal bidding shading:</strong> rational bidders shade their bids below their signal to compensate. The shading depends on the number of bidders $n$ and the signal noise variance.</li>
<li><strong>Larger $n$ requires more shading.</strong> With more competitors, conditioning on winning shifts the expected value down further. Bidders rationally bid less aggressively in large auctions.</li>
</ol>

<p>The classic example: Capen, Clapp, Campbell (1971) document persistent under-performance in offshore oil-lease auctions, attributable to insufficient shading. Sophisticated bidders (Exxon) earn higher returns than less-sophisticated ones.</p>

<p>Bazerman and Samuelson (1983) experiment with classroom auctions for jars of pennies. The winner's curse appears robustly: average winning bid exceeds the actual value, even when subjects know the theory.</p>

<p>Eyster-Rabin (2005) develop "cursed equilibrium" as a behavioural concept: bidders partially neglect the informational content of winning. The full curse model is one extreme; rational behaviour is the other.</p>

<p>Empirical applications: takeover premia tend to exceed announced synergy gains, consistent with a winner's curse on bidding firms. Oil-lease and timber-sale auctions display similar patterns.</p>

<p>Reference: Micro2025.pdf Topic 7 Lecture on Auctions; Capen-Clapp-Campbell 1971 Journal of Petroleum Technology; Milgrom-Weber 1982; Klemperer "Auctions".</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <text x="60" y="40" font-size="14" font-weight="bold">Winner's Curse</text>
  <line x1="80" y1="260" x2="540" y2="260" stroke="#333"/>
  <line x1="80" y1="260" x2="80" y2="60" stroke="#333"/>
  <text x="540" y="280" font-size="13">signal $s_i$</text>
  <text x="60" y="70" font-size="13">value</text>
  <line x1="80" y1="260" x2="540" y2="80" stroke="#888" stroke-width="1" stroke-dasharray="3 3"/>
  <text x="430" y="90" font-size="11" fill="#888">$E[v | s_i] = s_i$</text>
  <line x1="80" y1="260" x2="540" y2="140" stroke="#d62728" stroke-width="2"/>
  <text x="250" y="200" font-size="12" fill="#d62728">$E[v | s_i, i \text{ wins}]$ (downward bias)</text>
  <text x="60" y="305" font-size="12" fill="#555">Conditional on winning, expected value is lower than the signal.</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Naive bidding equates bid to signal; rational bidding shades below to avoid the winner's curse.</p>""",
        "examples": r"""<ul>
<li><strong>Oil lease auctions.</strong> Capen-Clapp-Campbell (1971) and Hendricks-Porter (1988) document under-performance of winning bidders, consistent with insufficient shading.</li>
<li><strong>Takeovers.</strong> Acquirers' announced synergies typically exceed realised post-merger gains, consistent with winner's curse on bidding firms.</li>
<li><strong>Online auctions.</strong> Bajari-Hortacsu (2003) find that eBay bidders shade their bids to account for the winner's curse, though imperfectly.</li>
<li><strong>Essay move.</strong> Doornik likes students who distinguish common-value from private-value auctions. The winner's curse applies in the former, not the latter.</li>
<li><strong>Essay move.</strong> The optimal shading depends on the number of bidders. In large auctions, bid shading should be more aggressive.</li>
<li><strong>Limitation.</strong> Behavioural evidence (Bazerman-Samuelson, Kagel-Levin) shows that real bidders fail to shade fully. Cursed equilibrium (Eyster-Rabin) captures this.</li>
<li>See also [[Concepts/Vickrey (Second-Price) Auction]], [[Concepts/Asymmetric Information]].</li>
</ul>""",
    },
    "pooling-equilibrium": {
        "math": r"""<p>A <strong>pooling equilibrium</strong> in a signalling or screening game is one in which all types choose the same action (sender) or accept the same contract (screening menu). The action conveys no information about type, so beliefs equal the prior.</p>

<p>In the Spence signalling model, a pooling equilibrium has both types sending the same signal $s_P$, typically $s_P = 0$. The wage is the average productivity $w_P = E[\theta] = \mu_H \theta_H + \mu_L \theta_L$ where $\mu_H$ is the prior probability of high type.</p>

<ol>
<li><strong>IC for low type:</strong> $w_P - c_L(s_P) \geq w(\text{deviation}) - c_L(\text{deviation})$. Pooling is sustained by off-path beliefs that any deviation is from the low type, making the deviation wage $\theta_L$.</li>
<li><strong>IC for high type:</strong> the high type prefers $w_P$ to any deviation that would reveal type. With $w_P = \mu_H \theta_H + (1-\mu_H) \theta_L > \theta_L$, the high type is content with pooling iff the alternative separating signal costs more than the wage gain.</li>
<li><strong>Pooling sustained by pessimistic beliefs:</strong> employers believe any deviation is from the low type. The intuitive criterion (Cho-Kreps) rules this out by requiring beliefs to be reasonable.</li>
</ol>

<p>Pooling equilibria are typically Pareto-dominated by separating equilibria for the high type, but Pareto-superior for the low type. The pooled wage $w_P$ exceeds $\theta_L$, benefiting the low type at the high type's expense.</p>

<p>Refinements often eliminate pooling: the intuitive criterion eliminates it whenever the high type's deviation is unambiguously dominant. The Riley outcome is the surviving separating equilibrium.</p>

<p>Real-world pooling: many job postings (entry-level) treat all applicants alike, pooling on a fixed wage. Group insurance plans pool members regardless of individual risk. Common pricing in restaurants pools customers regardless of marginal willingness to pay.</p>

<p>Reference: Micro2025.pdf Topic 7 Lecture 2; Spence 1973 QJE; Mas-Colell Ch. 13.D.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <text x="60" y="40" font-size="14" font-weight="bold">Pooling Equilibrium</text>
  <line x1="80" y1="280" x2="540" y2="280" stroke="#333"/>
  <line x1="80" y1="280" x2="80" y2="60" stroke="#333"/>
  <text x="540" y="300" font-size="13">signal $s$</text>
  <text x="60" y="70" font-size="13">wage $w$</text>
  <line x1="80" y1="160" x2="540" y2="160" stroke="#1f77b4" stroke-width="2" stroke-dasharray="4 2"/>
  <text x="100" y="155" font-size="12" fill="#1f77b4">$w_P = E[\theta]$ (pooled wage)</text>
  <circle cx="100" cy="160" r="6" fill="#2ca02c"/>
  <text x="110" y="155" font-size="12" fill="#2ca02c">$s_P = 0$</text>
  <line x1="80" y1="100" x2="540" y2="100" stroke="#888" stroke-width="1" stroke-dasharray="3 3"/>
  <text x="450" y="95" font-size="11" fill="#888">$\theta_H$</text>
  <line x1="80" y1="240" x2="540" y2="240" stroke="#888" stroke-width="1" stroke-dasharray="3 3"/>
  <text x="450" y="255" font-size="11" fill="#888">$\theta_L$</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Pooling: both types send signal 0 and receive the prior-weighted wage. Eliminated by the intuitive criterion.</p>""",
        "examples": r"""<ul>
<li><strong>Group health insurance.</strong> Employer-provided plans pool employees, charging a uniform premium. Risk pooling sustains coverage that adverse selection would otherwise prevent.</li>
<li><strong>Subway fares.</strong> Uniform fares pool all passengers regardless of trip length. This survives because consumer differentiation is unobservable.</li>
<li><strong>Entry-level salaries.</strong> Bachelor's-degree applicants are pooled at a single starting salary. Differentiation occurs later through performance review.</li>
<li><strong>Essay move.</strong> Pooling equilibria are often eliminated by the intuitive criterion. Doornik rewards students who explicitly invoke the criterion to argue for separating outcomes.</li>
<li><strong>Essay move.</strong> Compare welfare in pooling vs separating equilibria. Pooling can Pareto-dominate when the cost of signalling is high and prior types are similar.</li>
<li><strong>Limitation.</strong> Pooling is fragile: a single screening menu can break it. Real-world pooling persists because of regulation, contracting frictions, or coordination.</li>
<li>See also [[Concepts/Separating vs Pooling]], [[Concepts/Intuitive Criterion]], [[Concepts/Wilson Refinement]].</li>
</ul>""",
    },
    "conspicuous-consumption": {
        "math": r"""<p><strong>Conspicuous consumption</strong> (Veblen 1899) describes goods purchased to signal wealth or status rather than for their direct utility. In modern signalling theory (Bagwell-Bernheim 1996), conspicuous consumption is a Spence-type signal: high-wealth types consume publicly visible luxury goods at levels that low-wealth types would not find profitable to mimic.</p>

<p>Veblen goods exhibit upward-sloping demand: as price rises, the signalling value rises and demand increases (within a range). The exact mechanism: consumers derive utility from being perceived as wealthy, and visible price levels are the signal.</p>

<ol>
<li><strong>Setup:</strong> consumer has wealth $w$ and chooses consumption $c$ of a luxury good of price $p$. Utility is $u(c) + \beta \cdot E[w | c, p]$ where the second term is the "esteem" derived from observed signalling.</li>
<li><strong>Equilibrium:</strong> in a separating equilibrium, high types consume more of the luxury good than low types, so observers can infer wealth from consumption. The single-crossing property holds when marginal utility of the luxury is higher for higher wealth.</li>
<li><strong>Welfare:</strong> conspicuous consumption is wasteful: it consumes resources only to signal wealth that would be socially observable through other means. Pigou (1920) suggested taxation as a corrective.</li>
</ol>

<p>Modern empirical evidence: Charles, Hurst, Roussanov (2009) document race-conditional differences in conspicuous-consumption shares, consistent with Veblen logic. Heffetz (2011) constructs a conspicuous-consumption index and shows it correlates with income elasticities of demand.</p>

<p>Policy implications: taxes on luxury goods (Yachts, premium cars) target signalling consumption with limited welfare loss. Optimal commodity taxation under Veblen externalities is studied by Frank (1985) and others.</p>

<p>Cross-references: conspicuous consumption is the cleanest empirical example of Spence signalling outside labour markets. The signalling cost is the consumption itself; the benefit is social status.</p>

<p>Reference: Micro2025.pdf Topic 7 Lecture on Signalling Applications; Veblen 1899; Bagwell-Bernheim 1996 AER; Frank 1985.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <line x1="80" y1="260" x2="540" y2="260" stroke="#333"/>
  <line x1="80" y1="260" x2="80" y2="60" stroke="#333"/>
  <text x="540" y="280" font-size="13">price $p$</text>
  <text x="60" y="70" font-size="13">quantity demanded</text>
  <path d="M 80 220 Q 150 180 220 150 Q 290 130 340 110" fill="none" stroke="#1f77b4" stroke-width="2"/>
  <text x="200" y="120" font-size="12" fill="#1f77b4">Veblen good (upward)</text>
  <path d="M 340 110 L 540 240" fill="none" stroke="#d62728" stroke-width="2"/>
  <text x="380" y="160" font-size="12" fill="#d62728">Normal range</text>
  <text x="60" y="305" font-size="12" fill="#555">Demand rises with price in the signalling range, falls beyond saturation.</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Veblen demand: signalling value drives upward-sloping demand at high prices.</p>""",
        "examples": r"""<ul>
<li><strong>Luxury watches.</strong> Rolex and Patek Philippe maintain high prices in part for signalling value. The brand-name premium captures conspicuous-consumption rent.</li>
<li><strong>Diamond engagement rings.</strong> Brinig (1990) and others document the social-signalling role of large gemstones in marriage markets.</li>
<li><strong>Designer fashion.</strong> Visible logos and label-conscious branding signal income to peer groups; sales depend on observability of brand.</li>
<li><strong>Essay move.</strong> Doornik likes students who connect Veblen consumption to Spence signalling. The mathematical structure is the same: high types consume more visible goods at a cost low types cannot match.</li>
<li><strong>Essay move.</strong> Use optimal taxation theory (Frank 1985) to argue for luxury taxes. Conspicuous consumption is a negative externality on others' status.</li>
<li><strong>Limitation.</strong> Empirical identification of pure conspicuous consumption is hard. Many luxury goods provide direct utility, and Veblen-mediated demand is one part of total demand.</li>
<li>See also [[Concepts/Spence Signalling]], [[Concepts/Single Crossing Property]].</li>
</ul>""",
    },

    "ricardian-trade-model": {
        "math": r"""<p>The <strong>Ricardian model</strong> (1817) of international trade derives gains from trade from cross-country differences in labour productivity. Two countries, Home and Foreign, produce two goods, $X$ and $Y$, using only labour. Home has labour productivity $a_X^H$ in $X$ and $a_Y^H$ in $Y$ (output per worker). Foreign has $a_X^F$ and $a_Y^F$.</p>

<p>Comparative advantage: Home has comparative advantage in $X$ if $a_X^H / a_Y^H > a_X^F / a_Y^F$, equivalently if its relative productivity ratio favours $X$. Note this is independent of absolute productivity levels.</p>

<ol>
<li>Autarky: each country produces both goods. Home's relative price is $p_X / p_Y = a_Y^H / a_X^H$ (from wage equalisation $w = p_X a_X^H = p_Y a_Y^H$).</li>
<li>Trade equilibrium: relative world price $p^*$ lies strictly between the two autarky relative prices. Each country specialises in its comparative-advantage good.</li>
<li>Gains from trade: each country consumes a bundle outside its PPF. Welfare gain is the difference between trade and autarky utility for each consumer.</li>
</ol>

<p>The classic numerical example: England produces 1 unit of cloth or 1.2 units of wine per worker; Portugal produces 1.5 units of cloth or 2 units of wine per worker. Portugal has absolute advantage in both, but England has comparative advantage in cloth ($1/1.2 > 1.5/2$, i.e., $0.83 > 0.75$ in opportunity-cost ratios for wine per cloth).</p>

<p>Welfare gains are unambiguous in aggregate but may not be Pareto: workers in the contracting sector may lose. The Stolper-Samuelson theorem captures this redistribution effect formally.</p>

<p>Reference: Micro2025.pdf Topic 1 Lecture on Trade; Ricardo, "On the Principles of Political Economy and Taxation" Ch. 7; Krugman-Obstfeld Ch. 3.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <text x="60" y="40" font-size="14" font-weight="bold">Ricardian PPFs</text>
  <line x1="80" y1="260" x2="540" y2="260" stroke="#333"/>
  <line x1="80" y1="260" x2="80" y2="60" stroke="#333"/>
  <text x="540" y="280" font-size="13">Cloth $X$</text>
  <text x="60" y="70" font-size="13">Wine $Y$</text>
  <line x1="80" y1="80" x2="280" y2="260" stroke="#1f77b4" stroke-width="2"/>
  <text x="100" y="100" font-size="12" fill="#1f77b4">Home PPF: slope $-a_Y/a_X$</text>
  <line x1="80" y1="140" x2="380" y2="260" stroke="#d62728" stroke-width="2"/>
  <text x="200" y="170" font-size="12" fill="#d62728">Foreign PPF (flatter, cloth-cheap)</text>
  <text x="60" y="305" font-size="12" fill="#555">Different slopes signal comparative advantage.</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">PPFs with different slopes: each country specialises in its comparative-advantage good.</p>""",
        "examples": r"""<ul>
<li><strong>UK-Portugal trade.</strong> Ricardo's original example uses cloth-for-wine. Empirically validated by 19th-century trade patterns (O'Rourke-Williamson 1999).</li>
<li><strong>US-China manufacturing.</strong> The "China shock" (Autor-Dorn-Hanson 2013) shows that US manufacturing lost jobs as China specialised in labour-intensive goods, the standard Ricardian prediction.</li>
<li><strong>Services trade.</strong> Modern offshoring of IT services exploits comparative advantage based on labour-skill productivity.</li>
<li><strong>Essay move.</strong> Doornik rewards essays that distinguish comparative from absolute advantage. The model predicts trade based on relative productivity, not which country is more productive overall.</li>
<li><strong>Essay move.</strong> Note that Ricardian gains are aggregate. Without lump-sum redistribution, individual workers in contracting sectors lose, motivating the Stolper-Samuelson analysis.</li>
<li><strong>Limitation.</strong> The single-factor model ignores capital, land, and skill differences. Heckscher-Ohlin generalises to multiple factors and changes the predictions about who gains and loses.</li>
<li>See also [[Concepts/Comparative Advantage]], [[Concepts/Heckscher-Ohlin Model]], [[Concepts/Stolper-Samuelson Theorem]].</li>
</ul>""",
    },
    "autarky": {
        "math": r"""<p><strong>Autarky</strong> is the no-trade equilibrium: a closed economy produces and consumes its own output without exchanging with other countries. In a two-good model, autarky equilibrium is the point on the PPF where the marginal rate of transformation equals the consumer's marginal rate of substitution: $MRT = MRS = p_X^A / p_Y^A$.</p>

<p>Autarky serves as the benchmark against which the gains from trade are measured. With identical preferences and technology across countries, autarky prices reveal which country has comparative advantage.</p>

<ol>
<li>Each consumer maximises $u(x, y)$ subject to $p_X x + p_Y y = w$ where $w$ is labour income.</li>
<li>Producers maximise profit subject to the PPF $T(x, y) = 0$.</li>
<li>Equilibrium: $MRS = MRT$, all markets clear, no trade.</li>
</ol>

<p>Welfare under autarky is strictly lower than under free trade for both countries, provided their autarky relative prices differ. The result is part of the elementary theorem that opening trade is Pareto-improving with appropriate transfers.</p>

<p>If autarky prices are identical across countries, trade is irrelevant: no exchange occurs. This is a knife-edge case generally violated by differences in productivity, factor endowments, or technology.</p>

<p>Empirical autarky episodes: North Korea (1950s onwards), Albania (1976-1991), Burma (1962-1988). All experienced lower productivity growth and consumption levels than open neighbours, consistent with the welfare-loss prediction.</p>

<p>Modern trade theory uses autarky as a counterfactual to compute gains from trade. Arkolakis-Costinot-Rodriguez-Clare (2012) show that across various models, the gains from trade depend only on the trade share and the trade elasticity.</p>

<p>Reference: Micro2025.pdf Topic 1 Lecture on Trade; Krugman-Obstfeld Ch. 4; Feenstra "Advanced International Trade" Ch. 1.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <text x="60" y="40" font-size="14" font-weight="bold">Autarky equilibrium</text>
  <line x1="80" y1="260" x2="540" y2="260" stroke="#333"/>
  <line x1="80" y1="260" x2="80" y2="60" stroke="#333"/>
  <text x="540" y="280" font-size="13">$X$</text>
  <text x="60" y="70" font-size="13">$Y$</text>
  <path d="M 80 100 Q 200 110 540 240" fill="none" stroke="#1f77b4" stroke-width="2"/>
  <text x="100" y="125" font-size="12" fill="#1f77b4">PPF</text>
  <path d="M 80 220 Q 200 150 540 100" fill="none" stroke="#d62728" stroke-width="2"/>
  <text x="100" y="200" font-size="12" fill="#d62728">indifference</text>
  <line x1="80" y1="60" x2="540" y2="280" stroke="#888" stroke-width="1" stroke-dasharray="3 3"/>
  <circle cx="280" cy="180" r="6" fill="#2ca02c"/>
  <text x="290" y="175" font-size="12" fill="#2ca02c">Autarky $E^A$</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Autarky: PPF tangent to indifference curve, $MRT = MRS$.</p>""",
        "examples": r"""<ul>
<li><strong>North Korea.</strong> Largely autarkic from the 1950s. Consumption per capita estimates are far below South Korean levels despite similar geography and initial conditions.</li>
<li><strong>Albania under Hoxha.</strong> Banned trade with both East and West from 1976 to 1991. Living standards collapsed compared to neighbouring Yugoslavia.</li>
<li><strong>Tokugawa Japan.</strong> Closed-country policy from 1633 to 1853. Productivity stagnated relative to industrialising Europe; the Meiji opening triggered rapid catch-up.</li>
<li><strong>Essay move.</strong> Use autarky as the counterfactual to compute gains from trade. Doornik rewards essays that explicitly compare autarky and trade equilibrium prices.</li>
<li><strong>Essay move.</strong> The autarky welfare bound is a tight one: any country with different autarky prices than the world gains from trade. The smaller the country, the larger the relative gain.</li>
<li><strong>Limitation.</strong> Real economies are rarely fully autarkic. The standard textbook autarky is a polar limit, with practical interest in degrees of trade openness.</li>
<li>See also [[Concepts/Competitive Equilibrium]], [[Concepts/Comparative Advantage]].</li>
</ul>""",
    },
    "comparative-advantage": {
        "math": r"""<p><strong>Comparative advantage</strong>: country $A$ has comparative advantage in good $X$ relative to country $B$ in good $Y$ if $A$'s opportunity cost of producing $X$ in terms of $Y$ is lower than $B$'s. With labour productivity $a_X^A, a_Y^A, a_X^B, a_Y^B$:</p>

$$\text{Comparative advantage in } X \iff \frac{a_Y^A}{a_X^A} < \frac{a_Y^B}{a_X^B} \iff \frac{a_X^A}{a_Y^A} > \frac{a_X^B}{a_Y^B}.$$

<p>The opportunity cost ratio is the key concept: not how much $X$ each country produces per worker, but how much $Y$ each country gives up to produce one more unit of $X$.</p>

<ol>
<li>Determine the opportunity cost of each good in each country: how many units of $Y$ are forgone for one unit of $X$.</li>
<li>The country with the lower opportunity cost has comparative advantage in $X$, and the other in $Y$.</li>
<li>Even if one country has absolute advantage in both goods (higher productivity in both), comparative advantage still exists for one of them.</li>
</ol>

<p>Numerical example: $A$ produces 4 cloth or 5 wine per worker; $B$ produces 1 cloth or 2 wine per worker. $A$ has absolute advantage in both. Opportunity costs: in $A$, 1 cloth costs $5/4 = 1.25$ wine; in $B$, 1 cloth costs $2$ wine. $A$ has comparative advantage in cloth.</p>

<p>Trade pattern: $A$ specialises in cloth, $B$ in wine. Both gain provided the world relative price lies between the two autarky opportunity costs, i.e., $1.25 < (p_W/p_C) < 2$.</p>

<p>Comparative advantage is the foundation of trade theory. Ricardo (1817) provided the cloth-wine example. Modern extensions (Eaton-Kortum 2002, Caliendo-Parro 2015) generalise to many goods and many countries with continuous productivity distributions.</p>

<p>Reference: Micro2025.pdf Topic 1 Lecture on Trade; Ricardo Ch. 7; Krugman-Obstfeld Ch. 3.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <text x="60" y="40" font-size="14" font-weight="bold">Opportunity costs</text>
  <line x1="80" y1="260" x2="540" y2="260" stroke="#333"/>
  <text x="540" y="280" font-size="13">good</text>
  <rect x="100" y="100" width="80" height="120" fill="#1f77b4"/>
  <text x="140" y="240" font-size="12" text-anchor="middle">$A$ cloth: 1.25</text>
  <rect x="220" y="60" width="80" height="160" fill="#1f77b4"/>
  <text x="260" y="240" font-size="12" text-anchor="middle">$B$ cloth: 2.0</text>
  <rect x="340" y="150" width="80" height="70" fill="#d62728"/>
  <text x="380" y="240" font-size="12" text-anchor="middle">$A$ wine: 0.8</text>
  <rect x="460" y="120" width="80" height="100" fill="#d62728"/>
  <text x="500" y="240" font-size="12" text-anchor="middle">$B$ wine: 0.5</text>
  <text x="60" y="80" font-size="12" fill="#555">$A$ has lower opp. cost of cloth; $B$ has lower opp. cost of wine.</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Comparative advantage flows from differences in opportunity-cost ratios, not absolute productivity.</p>""",
        "examples": r"""<ul>
<li><strong>Modern services offshoring.</strong> India has comparative advantage in IT services (low opportunity cost of programmer time), while developed countries specialise in R&D.</li>
<li><strong>Resource trade.</strong> Saudi Arabia's comparative advantage in oil flows from its low extraction cost, not from absolute productivity differences.</li>
<li><strong>Skill-based trade.</strong> Germany exports engineering goods; Bangladesh exports textiles. Comparative advantage tracks skill endowments, the Heckscher-Ohlin generalisation.</li>
<li><strong>Essay move.</strong> Comparative advantage is robust to many extensions: multiple goods (Dornbusch-Fischer-Samuelson 1977), monopolistic competition (Krugman 1980), heterogeneous firms (Melitz 2003). The basic insight survives.</li>
<li><strong>Essay move.</strong> Doornik rewards essays that emphasise the misunderstood nature of comparative advantage. Even high-productivity countries gain from trade with low-productivity countries because of differences in opportunity costs.</li>
<li><strong>Limitation.</strong> Comparative advantage is a static concept. Dynamic considerations (learning, infant industries) can complicate the case for free trade in developing economies.</li>
<li>See also [[Concepts/Ricardian Trade Model]], [[Concepts/Autarky]].</li>
</ul>""",
    },
    "heckscher-ohlin-model": {
        "math": r"""<p>The <strong>Heckscher-Ohlin model</strong> (Heckscher 1919, Ohlin 1933) explains trade patterns by relative factor endowments rather than productivity differences. Each country exports the good intensive in its abundant factor.</p>

<p>Two countries, two factors (labour $L$, capital $K$), two goods ($X$ labour-intensive, $Y$ capital-intensive). Home has higher labour-to-capital ratio: $L/K > L^*/K^*$. Both countries share identical technology and preferences.</p>

<ol>
<li><strong>Production functions:</strong> $X = F^X(L_X, K_X)$ and $Y = F^Y(L_Y, K_Y)$, both constant-returns. Factor intensities $L^X/K^X > L^Y/K^Y$ in autarky.</li>
<li><strong>Autarky equilibrium:</strong> the country abundant in labour has a low relative wage and produces $X$ relatively cheaply: $p_X / p_Y$ low at Home.</li>
<li><strong>Trade pattern (Heckscher-Ohlin theorem):</strong> Home exports $X$ (labour-intensive good), Foreign exports $Y$ (capital-intensive good).</li>
</ol>

<p>Companion theorems:</p>

<p>Stolper-Samuelson: trade raises the real wage of the abundant factor and lowers it for the scarce factor. Trade benefits factor owners who specialise in the export sector.</p>

<p>Rybczynski: an increase in the supply of one factor raises the output of the good intensive in that factor and reduces the output of the other (at constant prices).</p>

<p>Factor Price Equalisation: trade equalises factor prices across countries even without factor mobility, provided both countries produce both goods.</p>

<p>Empirical tests: the Leontief paradox (1953) showed that the US, a capital-abundant country, exported labour-intensive goods, contradicting H-O. Subsequent work (Trefler 1995, Davis-Weinstein 2001) reconciled the data using productivity differences and skill heterogeneity.</p>

<p>H-O remains the workhorse model for analysing the income-distributional effects of trade. The China shock literature (Autor-Dorn-Hanson 2013) confirms H-O predictions for wage inequality.</p>

<p>Reference: Micro2025.pdf Topic 1 Lecture on Trade; Heckscher 1919; Ohlin 1933; Krugman-Obstfeld Ch. 5; Feenstra Ch. 3.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <text x="60" y="40" font-size="14" font-weight="bold">Heckscher-Ohlin</text>
  <line x1="80" y1="260" x2="540" y2="260" stroke="#333"/>
  <line x1="80" y1="260" x2="80" y2="60" stroke="#333"/>
  <text x="540" y="280" font-size="13">$L/K$ in country</text>
  <text x="60" y="70" font-size="13">good exported</text>
  <line x1="80" y1="180" x2="280" y2="180" stroke="#1f77b4" stroke-width="3"/>
  <text x="100" y="175" font-size="12" fill="#1f77b4">Capital-intensive Y</text>
  <line x1="280" y1="180" x2="540" y2="180" stroke="#d62728" stroke-width="3"/>
  <text x="380" y="175" font-size="12" fill="#d62728">Labour-intensive X</text>
  <circle cx="180" cy="180" r="5" fill="#000"/>
  <text x="160" y="220" font-size="12">Foreign (K-rich)</text>
  <circle cx="420" cy="180" r="5" fill="#000"/>
  <text x="400" y="220" font-size="12">Home (L-rich)</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Country exports the good intensive in its abundant factor.</p>""",
        "examples": r"""<ul>
<li><strong>China-US trade.</strong> Labour-abundant China exports labour-intensive manufactures; capital-abundant US exports capital- and skill-intensive goods.</li>
<li><strong>Australia-Japan trade.</strong> Land-abundant Australia exports natural resources; capital-abundant Japan exports manufactured goods.</li>
<li><strong>EU enlargement.</strong> Eastern European entrants (relatively labour-abundant) increased exports of labour-intensive goods to Western European partners after 2004.</li>
<li><strong>Essay move.</strong> Doornik rewards essays that use H-O to analyse distributional effects. Stolper-Samuelson predicts losers concentrated among scarce-factor owners.</li>
<li><strong>Essay move.</strong> H-O makes specific predictions Leontief tested empirically. The paradox motivated extensions: H-O-Vanek with many factors, productivity-adjusted H-O (Trefler 1995).</li>
<li><strong>Limitation.</strong> H-O assumes identical technology and homothetic preferences. Modern trade theory (Melitz 2003, Eaton-Kortum 2002) generalises with firm heterogeneity and productivity variation.</li>
<li>See also [[Concepts/Stolper-Samuelson Theorem]], [[Concepts/Rybczynski Theorem]].</li>
</ul>""",
    },
    "stolper-samuelson": {
        "math": r"""<p>The <strong>Stolper-Samuelson theorem</strong> (1941) states: in a two-good, two-factor economy with constant returns and competitive markets, an increase in the relative price of a good raises the real return to the factor used intensively in producing that good and lowers the real return to the other factor.</p>

<p>Setup: goods $X$ (labour-intensive) and $Y$ (capital-intensive). Factor prices $w$ (wage) and $r$ (rental). Zero-profit conditions: $p_X = a_L^X w + a_K^X r$, $p_Y = a_L^Y w + a_K^Y r$, where $a_{ij}$ are unit factor requirements.</p>

<ol>
<li>Differentiate the zero-profit conditions: $\hat p_X = \theta_L^X \hat w + \theta_K^X \hat r$, $\hat p_Y = \theta_L^Y \hat w + \theta_K^Y \hat r$ where $\theta_{ij}$ is the cost share and $\hat z = dz/z$ is the proportional change.</li>
<li>Solve the two-equation system: $\hat w = [\theta_K^Y \hat p_X - \theta_K^X \hat p_Y]/D$ and $\hat r = [\theta_L^X \hat p_Y - \theta_L^Y \hat p_X]/D$ where $D = \theta_L^X \theta_K^Y - \theta_L^Y \theta_K^X$.</li>
<li>If $X$ is labour-intensive: $\theta_L^X > \theta_L^Y$, so $D > 0$.</li>
<li>An increase in $p_X$ raises $w$ and lowers $r$. Both effects are <strong>magnification</strong>: $\hat w > \hat p_X > \hat p_Y > \hat r$.</li>
</ol>

<p>Implication for trade: a country that liberalises trade and sees the relative price of its exported good rise will see the real return to the abundant factor rise and the scarce factor fall. The factor used intensively in the export sector gains.</p>

<p>Real-world example: US trade liberalisation with China lowered the relative price of labour-intensive goods. Stolper-Samuelson predicts (and Autor-Dorn-Hanson 2013 confirm) declining real wages for less-educated US workers, the country's scarce factor.</p>

<p>Policy implications: protectionist tariffs raise the return to the import-competing sector's intensive factor. Steel tariffs benefit steelworkers; trade liberalisation hurts them. The political economy of trade is well-explained by Stolper-Samuelson.</p>

<p>Reference: Micro2025.pdf Topic 1 Lecture on Trade; Stolper-Samuelson 1941 REStud; Krugman-Obstfeld Ch. 5.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <text x="60" y="40" font-size="14" font-weight="bold">Stolper-Samuelson magnification</text>
  <line x1="80" y1="260" x2="540" y2="260" stroke="#333"/>
  <line x1="80" y1="160" x2="540" y2="160" stroke="#333" stroke-dasharray="2 2"/>
  <text x="540" y="170" font-size="11" fill="#888">0</text>
  <rect x="120" y="100" width="40" height="60" fill="#1f77b4"/>
  <text x="140" y="180" font-size="12" text-anchor="middle">$\hat w$</text>
  <rect x="220" y="130" width="40" height="30" fill="#1f77b4"/>
  <text x="240" y="180" font-size="12" text-anchor="middle">$\hat p_X$</text>
  <rect x="320" y="160" width="40" height="30" fill="#d62728"/>
  <text x="340" y="220" font-size="12" text-anchor="middle">$\hat p_Y$</text>
  <rect x="420" y="160" width="40" height="60" fill="#d62728"/>
  <text x="440" y="250" font-size="12" text-anchor="middle">$\hat r$</text>
  <text x="60" y="295" font-size="12" fill="#555">$\hat w > \hat p_X > \hat p_Y > \hat r$: magnification on both ends.</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Magnification: factor-price changes exceed good-price changes in proportional terms.</p>""",
        "examples": r"""<ul>
<li><strong>China shock.</strong> Falling relative price of labour-intensive goods after 2001 reduced US blue-collar real wages (Autor-Dorn-Hanson 2013).</li>
<li><strong>NAFTA effect on Mexican wages.</strong> Trade with US lowered Mexican skilled-worker wage premia, consistent with Mexico being labour-abundant.</li>
<li><strong>Brexit and UK manufacturing.</strong> Anticipated trade barriers raised the relative price of imported manufactures, predicted to redistribute toward UK manufacturing workers.</li>
<li><strong>Essay move.</strong> Stolper-Samuelson explains the political economy of trade. Doornik rewards essays that connect the theorem to specific historical episodes like Trump tariffs or Brexit.</li>
<li><strong>Essay move.</strong> The magnification effect is striking: a 10% rise in $p_X$ raises $w$ by more than 10%. This makes trade-induced distributional effects sharper than aggregate price changes might suggest.</li>
<li><strong>Limitation.</strong> The two-factor framework abstracts from skill heterogeneity. Multi-factor extensions (Jones 1971, Mussa 1974) show similar but more nuanced results.</li>
<li>See also [[Concepts/Heckscher-Ohlin Model]], [[Concepts/Rybczynski Theorem]].</li>
</ul>""",
    },
    "rybczynski-theorem": {
        "math": r"""<p>The <strong>Rybczynski theorem</strong> (1955) states: at constant goods prices, an increase in the supply of one factor raises the output of the good intensive in that factor and reduces the output of the other. Like Stolper-Samuelson, it exhibits a magnification effect.</p>

<p>Setup: two goods $X$ (labour-intensive) and $Y$ (capital-intensive), two factors $L$ and $K$. Full employment: $a_L^X X + a_L^Y Y = L$, $a_K^X X + a_K^Y Y = K$.</p>

<ol>
<li>Differentiate the factor-market clearing conditions at constant prices (so $a_{ij}$ remain unchanged): $a_L^X dX + a_L^Y dY = dL$, $a_K^X dX + a_K^Y dY = dK$.</li>
<li>For an increase in $L$ alone, $dK = 0$: solving the system gives $dX = a_K^Y dL / D$ and $dY = -a_K^X dL / D$ where $D$ is the determinant.</li>
<li>If $X$ is labour-intensive: $a_K^Y / a_L^Y > a_K^X / a_L^X$, so $D > 0$ and $dX > 0$, $dY < 0$.</li>
<li><strong>Magnification:</strong> $\hat X > \hat L > 0 > \hat Y$. The increase in $X$ output exceeds the increase in $L$ supply in proportional terms.</li>
</ol>

<p>Implication: immigration into a country (labour increases) raises the output of the labour-intensive sector and shrinks the capital-intensive sector, at constant prices.</p>

<p>Real-world example: post-WWII US capital accumulation expanded output of capital-intensive manufactures (steel, autos) while reducing the share of labour-intensive textiles. Soviet capital accumulation in the 1930s-50s grew heavy industry while shrinking agriculture.</p>

<p>The Dutch disease (Corden-Neary 1982) is a Rybczynski application: a natural-resource boom raises factor supplies in the booming sector and crowds out tradables.</p>

<p>Combined with Stolper-Samuelson, Rybczynski gives a complete map of how factor supply and good prices interact in the 2x2 HO model. Together with Heckscher-Ohlin (trade pattern) and Factor Price Equalisation, they form the "four core theorems" of trade theory.</p>

<p>Reference: Micro2025.pdf Topic 1 Lecture on Trade; Rybczynski 1955 Economica; Jones 1965 JPE.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <text x="60" y="40" font-size="14" font-weight="bold">Rybczynski magnification</text>
  <line x1="80" y1="260" x2="540" y2="260" stroke="#333"/>
  <line x1="80" y1="160" x2="540" y2="160" stroke="#333" stroke-dasharray="2 2"/>
  <rect x="120" y="80" width="60" height="80" fill="#1f77b4"/>
  <text x="150" y="180" font-size="12" text-anchor="middle">$\hat X$ (L-intensive)</text>
  <rect x="240" y="130" width="60" height="30" fill="#1f77b4"/>
  <text x="270" y="180" font-size="12" text-anchor="middle">$\hat L$</text>
  <rect x="360" y="160" width="60" height="60" fill="#d62728"/>
  <text x="390" y="240" font-size="12" text-anchor="middle">$\hat Y$ (K-intensive)</text>
  <text x="60" y="295" font-size="12" fill="#555">$\hat X > \hat L > 0 > \hat Y$ at constant prices.</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">An increase in labour raises labour-intensive output by more than the factor supply increase.</p>""",
        "examples": r"""<ul>
<li><strong>Dutch disease.</strong> Discovery of natural gas in the Netherlands (1959 onwards) raised resource-sector output and shrank manufacturing, the classic Rybczynski application (Corden-Neary 1982).</li>
<li><strong>Immigration effects.</strong> Labour inflows raise output of labour-intensive sectors. Card (2001) and Borjas-Hilton (2006) document such effects in US destination cities.</li>
<li><strong>Capital deepening.</strong> Post-WWII US capital accumulation expanded capital-intensive manufacturing relative to labour-intensive agriculture and textiles.</li>
<li><strong>Essay move.</strong> Rybczynski explains why factor accumulation can reshape an economy's output mix. Doornik rewards essays that link this to industrialisation patterns.</li>
<li><strong>Essay move.</strong> The "growth at constant prices" qualifier matters: with endogenous prices, terms-of-trade effects modify the result. Combine with Stolper-Samuelson for general-equilibrium analysis.</li>
<li><strong>Limitation.</strong> The theorem assumes full employment and CRS technology. With unemployment or scale economies, the predicted output expansion may not occur.</li>
<li>See also [[Concepts/Stolper-Samuelson Theorem]], [[Concepts/Heckscher-Ohlin Model]].</li>
</ul>""",
    },
    "gross-substitutes": {
        "math": r"""<p>The <strong>gross substitutes</strong> property holds in a competitive market when an increase in the price of any good $i$ raises the excess demand for every other good $j$: $\partial z_j / \partial p_i > 0$ for $i \neq j$. This is a positive cross-price effect on excess demand (not Marshallian demand).</p>

<p>Formally, with $z_j(p) = \sum_h x_j^h(p, p \cdot \omega^h) - \omega_j^{\text{total}}$, the GS property is $\partial z_j / \partial p_i > 0$. Walras' law links cross-derivatives: $\sum_i p_i \partial z_j / \partial p_i = -z_j$, so own-price effects must be negative.</p>

<ol>
<li><strong>Uniqueness of equilibrium:</strong> if all goods are gross substitutes, the equilibrium price vector is unique (up to scaling). Proof: tatonnement converges, ruling out multiple equilibria.</li>
<li><strong>Sufficient conditions:</strong> in a pure exchange economy with two goods, GS always holds. With three or more, GS requires preferences satisfying certain regularity (e.g., demand functions whose Slutsky cross-effects are uniformly positive in net terms).</li>
<li><strong>Stability of tatonnement:</strong> under GS, the price adjustment dynamic $\dot p_i = z_i(p)$ converges to equilibrium globally. Arrow-Hurwicz (1958) prove this.</li>
</ol>

<p>The GS condition is restrictive: many economies fail it. Counterexamples include economies with significant income effects, complementary goods, or substantial heterogeneity. Scarf (1960) constructs three-good examples where GS fails and equilibrium is non-unique.</p>

<p>For exchange economies with Cobb-Douglas preferences, GS holds: cross-Marshallian-demand effects are zero by Cobb-Douglas separability, and the income effect (via Walras) gives positive net cross-effects.</p>

<p>The Sonnenschein-Mantel-Debreu theorem (1972-1974) says any continuous, homogeneous-of-degree-zero, Walras-law-satisfying excess demand function is realisable from some economy. This implies that GS is not a feature of GE in general: most economies will not exhibit GS.</p>

<p>Reference: Micro2025.pdf Topic 1 Lecture 4; Mas-Colell Ch. 17.F; Arrow-Hahn "General Competitive Analysis".</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <text x="60" y="40" font-size="14" font-weight="bold">Gross substitutes property</text>
  <line x1="80" y1="260" x2="540" y2="260" stroke="#333"/>
  <line x1="80" y1="260" x2="80" y2="60" stroke="#333"/>
  <text x="540" y="280" font-size="13">$p_i$</text>
  <text x="60" y="70" font-size="13">$z_j$ ($j \neq i$)</text>
  <line x1="80" y1="200" x2="540" y2="100" stroke="#1f77b4" stroke-width="2"/>
  <text x="120" y="160" font-size="12" fill="#1f77b4">GS: positive slope</text>
  <line x1="80" y1="180" x2="540" y2="220" stroke="#d62728" stroke-width="2" stroke-dasharray="4 2"/>
  <text x="200" y="240" font-size="12" fill="#d62728">non-GS counterexample</text>
  <text x="60" y="305" font-size="12" fill="#555">Under GS, equilibrium unique and tatonnement stable.</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Excess demand cross-effects: positive under GS gives uniqueness and stability.</p>""",
        "examples": r"""<ul>
<li><strong>Cobb-Douglas exchange economies.</strong> Always GS. Equilibrium is unique and tatonnement stable.</li>
<li><strong>Asset pricing with no complements.</strong> Stock prices typically rise together with bond yields if assets are gross substitutes in portfolios.</li>
<li><strong>Currency markets.</strong> Under GS, a depreciation of one currency raises demand for substitute currencies.</li>
<li><strong>Essay move.</strong> Doornik likes essays that distinguish GS (a stability condition on excess demand) from cross-Marshallian elasticities (a consumer-theory concept). The two are not the same.</li>
<li><strong>Essay move.</strong> Use GS as the cleanest sufficient condition for uniqueness in GE. Diagonal-dominance and revealed-preference monotonicity are alternatives.</li>
<li><strong>Limitation.</strong> Sonnenschein-Mantel-Debreu shows that GS is not a feature of arbitrary economies. Multiple equilibria can arise in any sufficiently rich economy.</li>
<li>See also [[Concepts/Uniqueness of Equilibrium]], [[Concepts/Excess Demand]].</li>
</ul>""",
    },
    "zero-profit-condition": {
        "math": r"""<p>The <strong>zero-profit condition</strong> in a competitive market with free entry: in long-run equilibrium, each firm earns zero economic profit. Equivalently, price equals average cost at the chosen output: $p = AC(q^*)$. The condition pins down the number of firms or the scale of operation.</p>

<p>Setup: identical firms with cost function $C(q) = F + cq$ where $F$ is a fixed cost and $c$ is constant marginal cost. Long-run total cost $LRTC = qc + F$. Free entry implies $p = c + F/q^*$.</p>

<ol>
<li><strong>Profit maximisation:</strong> $p = MC = c$. With constant MC, the firm operates at any scale.</li>
<li><strong>Zero profit:</strong> $p = AC$, so $p = c + F/q^*$. Combined with $p = MC = c$, this is contradictory unless $F = 0$. With $F > 0$ and constant MC, perfect competition is impossible.</li>
<li><strong>U-shaped cost case:</strong> $AC$ has a minimum at $q^*$ where $AC = MC$. Equilibrium price equals minimum AC; firms operate at the bottom of the U.</li>
</ol>

<p>For market clearing with $n$ firms: $n q^* = Q(p^*)$, where $Q$ is market demand. The number of firms is determined by market size and minimum efficient scale.</p>

<p>In international trade, the zero-profit condition links commodity prices to factor prices. In a competitive model:</p>

$$p_X = a_L^X w + a_K^X r, \quad p_Y = a_L^Y w + a_K^Y r.$$

<p>Two zero-profit conditions in two factor prices: solving gives Stolper-Samuelson's mapping from $(p_X, p_Y)$ to $(w, r)$.</p>

<p>In imperfect competition, zero profit holds in the long run with free entry but the equilibrium price exceeds marginal cost. Monopolistic competition (Chamberlin 1933, Krugman 1980) extends the zero-profit logic to differentiated products.</p>

<p>Reference: Micro2025.pdf Topic 1 Lecture 5; Varian Ch. 23; Krugman-Obstfeld Ch. 7.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <line x1="80" y1="260" x2="540" y2="260" stroke="#333"/>
  <line x1="80" y1="260" x2="80" y2="60" stroke="#333"/>
  <text x="540" y="280" font-size="13">$q$</text>
  <text x="60" y="70" font-size="13">$\$$</text>
  <path d="M 100 220 Q 200 100 540 100" fill="none" stroke="#1f77b4" stroke-width="2"/>
  <text x="100" y="240" font-size="12" fill="#1f77b4">AC (U-shaped)</text>
  <line x1="100" y1="200" x2="540" y2="200" stroke="#d62728" stroke-width="2"/>
  <text x="450" y="195" font-size="12" fill="#d62728">$MC = c$</text>
  <line x1="80" y1="180" x2="540" y2="180" stroke="#888" stroke-width="1" stroke-dasharray="3 3"/>
  <text x="450" y="170" font-size="11" fill="#888">$p^* = \min AC$</text>
  <circle cx="270" cy="180" r="6" fill="#2ca02c"/>
  <text x="280" y="175" font-size="12" fill="#2ca02c">Zero-profit point</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Zero-profit equilibrium: price equals minimum average cost, $p = AC$.</p>""",
        "examples": r"""<ul>
<li><strong>Agricultural commodity markets.</strong> Free entry of farmers drives long-run prices to average cost. Subsidies that shift LRTC down change the equilibrium price.</li>
<li><strong>Trucking after deregulation.</strong> Post-1980 entry drove US trucking margins to zero, consistent with the zero-profit prediction.</li>
<li><strong>Online platforms.</strong> Restaurant delivery services compete on fees; entry has driven margins to break-even levels.</li>
<li><strong>Essay move.</strong> Doornik rewards essays that distinguish accounting profit from economic profit. Economic profit being zero is consistent with accounting profit being positive (covering opportunity costs).</li>
<li><strong>Essay move.</strong> Long-run free entry is essential. In the short run, profits can be positive or negative; the zero-profit condition pins down only the long-run equilibrium.</li>
<li><strong>Limitation.</strong> The condition requires homogeneous goods and free entry. With differentiation or sunk entry costs, the long-run equilibrium has positive profits (monopolistic competition, oligopoly).</li>
<li>See also [[Concepts/Competitive Equilibrium]], [[Concepts/Heckscher-Ohlin Model]].</li>
</ul>""",
    },
    "uniqueness-of-equilibrium": {
        "math": r"""<p><strong>Uniqueness of equilibrium</strong> in general equilibrium is the property that the price vector clearing all markets is unique up to normalisation. Existence (Arrow-Debreu 1954) does not guarantee uniqueness; multiple equilibria are generic in some economies.</p>

<p>Sufficient conditions for uniqueness:</p>

<ol>
<li><strong>Gross substitutes (Arrow-Hurwicz 1958):</strong> if every good is a gross substitute for every other, the equilibrium is unique. Proof: differential argument using Walras' law.</li>
<li><strong>Diagonal dominance:</strong> if $|\partial z_i / \partial p_i| > \sum_{j \neq i} |\partial z_i / \partial p_j|$, the Jacobian is dominant and uniqueness holds.</li>
<li><strong>Weak axiom for aggregate excess demand:</strong> if $p \cdot z(p) \geq p \cdot z(p')$ whenever $z(p') \neq z(p)$, uniqueness holds (Mas-Colell).</li>
<li><strong>Monotonic substitutability:</strong> a generalisation due to Quah (2000).</li>
</ol>

<p>None of these conditions hold generically. The Sonnenschein-Mantel-Debreu theorem (1972-1974) shows that aggregate excess demand can have any shape consistent with continuity, homogeneity, and Walras' law. In particular, multiple equilibria are possible.</p>

<p>Scarf (1960) constructs a 3-good, 3-consumer economy with three distinct equilibria. Kehoe (1985, 1991) shows that with $n$ commodities, an economy can have up to $2n - 1$ equilibria.</p>

<p>Implications:</p>

<p>(i) Comparative statics: with non-unique equilibrium, the effect of a parameter change depends on which equilibrium is being compared.</p>

<p>(ii) Stability: tatonnement may converge to different equilibria from different initial price vectors. Globally stable economies have a unique equilibrium.</p>

<p>(iii) Policy analysis: predicting the effect of a tax or transfer requires knowing which equilibrium will be played.</p>

<p>Computable General Equilibrium (CGE) models routinely encounter multiple equilibria; software finds the one closest to initial conditions, which is not necessarily the "correct" one.</p>

<p>Reference: Micro2025.pdf Topic 1 Lecture 5; Mas-Colell Ch. 17; Kehoe 1991 Handbook of Mathematical Economics.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <line x1="80" y1="260" x2="540" y2="260" stroke="#333"/>
  <line x1="80" y1="160" x2="540" y2="160" stroke="#333" stroke-dasharray="2 2"/>
  <text x="540" y="170" font-size="11" fill="#888">0</text>
  <text x="540" y="280" font-size="13">$p$</text>
  <text x="60" y="70" font-size="13">$z(p)$</text>
  <path d="M 80 100 Q 200 200 300 130 Q 400 80 540 220" fill="none" stroke="#1f77b4" stroke-width="2"/>
  <circle cx="160" cy="160" r="6" fill="#2ca02c"/>
  <circle cx="280" cy="160" r="6" fill="#2ca02c"/>
  <circle cx="430" cy="160" r="6" fill="#2ca02c"/>
  <text x="170" y="155" font-size="11" fill="#2ca02c">$p_1^*$</text>
  <text x="290" y="155" font-size="11" fill="#2ca02c">$p_2^*$</text>
  <text x="440" y="155" font-size="11" fill="#2ca02c">$p_3^*$</text>
  <text x="60" y="305" font-size="12" fill="#555">Excess demand crosses zero three times: multiple equilibria.</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Without GS or diagonal dominance, excess demand can cross zero multiple times.</p>""",
        "examples": r"""<ul>
<li><strong>Currency-attack models.</strong> Obstfeld (1996) shows that exchange-rate regimes have multiple equilibria. Whether a peg survives depends on coordination, not fundamentals.</li>
<li><strong>Financial crises.</strong> Diamond-Dybvig (1983) bank-run models have a "no-run" and "run" equilibrium; the latter is self-fulfilling.</li>
<li><strong>Search markets.</strong> Diamond (1971) shows search-and-matching models can have multiple equilibria with different unemployment and wage levels.</li>
<li><strong>Essay move.</strong> Doornik rewards essays that note the empirical importance of multiplicity. Coordination failures are real, and policy can shift the equilibrium without changing fundamentals.</li>
<li><strong>Essay move.</strong> Distinguish local uniqueness (regular economy in the sense of Debreu) from global uniqueness. Local uniqueness is generic; global uniqueness requires additional structure.</li>
<li><strong>Limitation.</strong> Sufficient conditions for uniqueness are restrictive. Empirical work often assumes uniqueness as a working hypothesis.</li>
<li>See also [[Concepts/Gross Substitutes]], [[Concepts/Excess Demand]], [[Concepts/Competitive Equilibrium]].</li>
</ul>""",
    },
    "robinson-crusoe-economy": {
        "math": r"""<p>The <strong>Robinson Crusoe economy</strong> is the simplest general equilibrium setting: one consumer-producer, two goods (leisure $\ell$ and an output good $x$), one technology. Crusoe maximises utility $u(x, \ell)$ subject to the production function $x = f(L)$ where $L = T - \ell$ is labour.</p>

<p>The model serves as the cleanest illustration of the equivalence between (a) Crusoe as a single agent maximising utility subject to technology, and (b) Crusoe as separate consumer and producer who trade in a competitive market.</p>

<ol>
<li><strong>Single-agent solution:</strong> $\max_{L, x} u(f(L), T - L)$. FOC: $u_x f'(L) = u_\ell$, equivalently $MRS = MRT$.</li>
<li><strong>Decentralised solution:</strong> a "firm" maximises profit $\pi(p, w) = p f(L) - w L$, giving labour demand from $p f'(L) = w$. A "consumer" maximises utility subject to budget $p x + w \ell = w T + \pi$, giving labour supply.</li>
<li><strong>Equilibrium:</strong> equilibrium prices $(p^*, w^*)$ satisfy labour-market clearing (consumer's labour supply equals firm's labour demand) and output-market clearing.</li>
<li><strong>Equivalence:</strong> the decentralised equilibrium replicates the single-agent solution. This is the simplest case of the First Welfare Theorem.</li>
</ol>

<p>The Robinson Crusoe model illustrates several pedagogical points:</p>

<p>(i) Prices are accounting devices in a one-agent economy; the relative price $w/p$ equals the marginal rate of transformation, which is also the marginal rate of substitution.</p>

<p>(ii) The Second Welfare Theorem holds trivially: any Pareto-optimal allocation can be supported by appropriate prices.</p>

<p>(iii) Production possibility frontier and indifference curves are tangent at equilibrium.</p>

<p>Crusoe with two consumers (Crusoe and Friday) and a shared technology recovers the Edgeworth box plus production: the Walrasian model of GE in its simplest informative form.</p>

<p>Reference: Micro2025.pdf Topic 1 Lecture 2; Varian Ch. 17; Robinson Crusoe (1719) for the literary source.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <line x1="80" y1="260" x2="540" y2="260" stroke="#333"/>
  <line x1="80" y1="260" x2="80" y2="60" stroke="#333"/>
  <text x="540" y="280" font-size="13">$\ell$ (leisure)</text>
  <text x="60" y="70" font-size="13">$x$</text>
  <path d="M 540 260 Q 300 100 80 60" fill="none" stroke="#1f77b4" stroke-width="2"/>
  <text x="200" y="100" font-size="12" fill="#1f77b4">PPF: $x = f(T-\ell)$</text>
  <path d="M 80 200 Q 200 130 540 80" fill="none" stroke="#d62728" stroke-width="2"/>
  <text x="200" y="220" font-size="12" fill="#d62728">indifference</text>
  <circle cx="280" cy="150" r="6" fill="#2ca02c"/>
  <text x="290" y="145" font-size="12" fill="#2ca02c">$E^*$: $MRS = MRT$</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Robinson Crusoe: tangency of PPF and indifference curve at the optimum.</p>""",
        "examples": r"""<ul>
<li><strong>Subsistence farming.</strong> Family farms can be analysed as Robinson Crusoe economies: household members supply labour to home production and consume the output.</li>
<li><strong>Self-employed professionals.</strong> A solo consultant chooses hours-worked vs leisure; the budget constraint is effectively a PPF.</li>
<li><strong>Macroeconomic aggregation.</strong> The representative-agent model in macro is a Robinson Crusoe economy at large scale: one consumer-producer choosing aggregate consumption, leisure, and capital.</li>
<li><strong>Essay move.</strong> Doornik rewards essays that use Robinson Crusoe to illustrate the welfare theorems. The single-agent case is the cleanest, since distributional questions do not arise.</li>
<li><strong>Essay move.</strong> Show that prices in Crusoe are "shadow prices" reflecting the marginal rates of substitution and transformation. They have an informational role even with one agent.</li>
<li><strong>Limitation.</strong> The model lacks distributional questions, externalities, and strategic interaction. It is a pedagogical workhorse, not a realistic model.</li>
<li>See also [[Concepts/Competitive Equilibrium]], [[Concepts/PPF and MRT]], [[Concepts/First Welfare Theorem]].</li>
</ul>""",
    },

    "externality-internalisation": {
        "math": r"""<p><strong>Externality internalisation</strong> aligns private marginal cost (or benefit) with social marginal cost (or benefit) by altering the decision-maker's payoff. The canonical tool is a Pigouvian tax (or subsidy) set equal to the marginal external damage (or benefit) at the social optimum.</p>

<p>Consider a negative externality from producing $q$, with private marginal cost $MC(q)$ and external marginal damage $D'(q)$. Social marginal cost is $SMC(q) = MC(q) + D'(q)$. The competitive market produces where $p = MC$; the social optimum requires $p = SMC$, giving lower output $q^*$.</p>

<p>A Pigouvian tax $\tau = D'(q^*)$ levied per unit of output shifts the private cost to coincide with social cost. The decentralised choice $p = MC + \tau$ then matches the social optimum.</p>

<ol>
<li>Identify the marginal external cost or benefit function.</li>
<li>Solve for the social optimum $q^*$ where $p = SMC$ (or $SMB = MC$ for positive externalities).</li>
<li>Set the Pigouvian tax (or subsidy) equal to the marginal externality at the optimum.</li>
<li>Verify decentralised choice replicates the social optimum.</li>
</ol>

<p>Alternative internalisation mechanisms:</p>

<p>(i) <strong>Coasean bargaining:</strong> with clear property rights and zero transaction costs, parties internalise externalities through private negotiation.</p>

<p>(ii) <strong>Tradeable permits:</strong> set an aggregate quantity and allow trade; the market equates marginal abatement costs across firms.</p>

<p>(iii) <strong>Merger:</strong> internalising the externality within a single decision-maker, as in vertical integration of polluter and victim.</p>

<p>(iv) <strong>Liability rules:</strong> tort law making polluters compensate victims internalises the damage through ex post payments.</p>

<p>Pigou (1920) introduced the tax framework; Coase (1960) challenged its uniqueness by emphasising the role of property rights. The two approaches coincide under transaction-cost-free conditions but diverge in practice.</p>

<p>Reference: Micro2025.pdf Topic 3 Lecture 2; Pigou "The Economics of Welfare"; Hindriks-Myles Ch. 7.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <line x1="80" y1="260" x2="540" y2="260" stroke="#333"/>
  <line x1="80" y1="260" x2="80" y2="60" stroke="#333"/>
  <text x="540" y="280" font-size="13">$q$</text>
  <text x="60" y="70" font-size="13">$\$$</text>
  <line x1="80" y1="100" x2="540" y2="240" stroke="#1f77b4" stroke-width="2"/>
  <text x="430" y="230" font-size="12" fill="#1f77b4">MC (private)</text>
  <line x1="80" y1="60" x2="540" y2="200" stroke="#d62728" stroke-width="2"/>
  <text x="430" y="180" font-size="12" fill="#d62728">SMC = MC + $D'$</text>
  <line x1="80" y1="220" x2="540" y2="100" stroke="#2ca02c" stroke-width="2"/>
  <text x="430" y="105" font-size="12" fill="#2ca02c">demand</text>
  <line x1="300" y1="170" x2="300" y2="260" stroke="#666" stroke-dasharray="3 3"/>
  <text x="290" y="280" font-size="11">$q^*$</text>
  <line x1="380" y1="190" x2="380" y2="260" stroke="#666" stroke-dasharray="3 3"/>
  <text x="370" y="280" font-size="11">$q^M$</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Pigouvian tax raises private MC to social MC, moving market output from $q^M$ to social optimum $q^*$.</p>""",
        "examples": r"""<ul>
<li><strong>Carbon taxes.</strong> Sweden's carbon tax (1991) levied at SEK 1000+/tonne CO2. Empirical effects on emissions consistent with Pigouvian theory.</li>
<li><strong>Congestion charges.</strong> London's congestion zone (2003 onwards) charges drivers entering central London, internalising the externality on other road users.</li>
<li><strong>Sin taxes.</strong> Cigarette and alcohol taxes can be partly justified by Pigouvian logic if external costs (passive smoking, drunk driving) are present.</li>
<li><strong>Essay move.</strong> Doornik rewards essays that derive the Pigouvian tax rate from the social optimum first-order condition rather than treating it as a black box.</li>
<li><strong>Essay move.</strong> Compare Pigouvian taxes to Coasean bargaining and tradeable permits. Under information asymmetries, Weitzman's prices-vs-quantities framework explains when each is preferred.</li>
<li><strong>Limitation.</strong> Pigouvian taxes require knowing the marginal external cost function. Information rents and political economy considerations often complicate implementation.</li>
<li>See also [[Concepts/Pigouvian Tax]], [[Concepts/Coase Theorem]], [[Concepts/Tradeable Permits]].</li>
</ul>""",
    },
    "tradeable-permits": {
        "math": r"""<p><strong>Tradeable permits</strong> (cap-and-trade) implement quantity-based pollution control through a market for emission rights. The regulator sets an aggregate cap $\bar E$ and issues permits totalling $\bar E$. Firms must hold a permit for each unit of emission and may trade permits.</p>

<p>Let firm $i$ have abatement cost $C_i(a_i)$ where $a_i$ is abatement from a baseline emission level $e_i^0$. Total emissions are $\sum_i (e_i^0 - a_i)$. The cap requires $\sum_i a_i \geq \sum_i e_i^0 - \bar E$.</p>

<p>Under free trading, the equilibrium permit price $p^*$ satisfies $C_i'(a_i^*) = p^*$ for every firm $i$. This is the <strong>cost-effectiveness theorem</strong>: marginal abatement costs equalised across firms, minimising total abatement cost for the given aggregate target.</p>

<ol>
<li>Set the cap $\bar E$ based on the social damage function.</li>
<li>Allocate initial permits (auction, free grandfathering, or hybrid).</li>
<li>Allow trading: the market clears at $p^*$ where $\sum_i a_i(p^*) = \sum_i e_i^0 - \bar E$.</li>
<li>Each firm chooses $a_i^* = a_i(p^*)$ where its marginal cost equals $p^*$.</li>
</ol>

<p>Equivalence with Pigouvian tax: under certainty about abatement-cost and damage functions, a Pigouvian tax at rate $p^*$ produces the same outcome. The two instruments differ under uncertainty (Weitzman 1974).</p>

<p>Allocation matters distributionally but not for efficiency (Coase-like result): regardless of how permits are initially allocated, the equilibrium abatement profile is the same. Free grandfathering benefits incumbents; auctioning benefits the public.</p>

<p>Real-world implementations: EU Emissions Trading System (2005 onwards), US SO2 trading under the 1990 Clean Air Act, Regional Greenhouse Gas Initiative (RGGI). All show cost savings of 20 to 50% compared to command-and-control.</p>

<p>Reference: Micro2025.pdf Topic 3 Lecture 3; Tietenberg "Emissions Trading"; Hindriks-Myles Ch. 7.5.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <line x1="80" y1="260" x2="540" y2="260" stroke="#333"/>
  <line x1="80" y1="260" x2="80" y2="60" stroke="#333"/>
  <text x="540" y="280" font-size="13">abatement $a$</text>
  <text x="60" y="70" font-size="13">MC$_i$</text>
  <line x1="80" y1="240" x2="540" y2="80" stroke="#1f77b4" stroke-width="2"/>
  <text x="450" y="100" font-size="12" fill="#1f77b4">firm 1 (low cost)</text>
  <line x1="80" y1="220" x2="540" y2="60" stroke="#d62728" stroke-width="2"/>
  <text x="450" y="65" font-size="12" fill="#d62728">firm 2 (high cost)</text>
  <line x1="80" y1="160" x2="540" y2="160" stroke="#666" stroke-dasharray="3 3"/>
  <text x="540" y="155" font-size="12" fill="#666">permit price $p^*$</text>
  <text x="60" y="305" font-size="12" fill="#555">Both firms abate to where MC = $p^*$: cost-minimising.</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Tradeable permits equalise marginal abatement costs across firms at the price $p^*$.</p>""",
        "examples": r"""<ul>
<li><strong>EU ETS.</strong> Launched 2005 for major emitters in EU. Schmalensee-Stavins (2017) survey cost savings and policy lessons.</li>
<li><strong>US SO2 trading.</strong> 1990 Clean Air Act, phase-down of acid-rain precursors. Schmalensee et al. (1998) document large cost savings vs command-and-control.</li>
<li><strong>California cap-and-trade.</strong> Operational since 2013, covers about 80% of state GHG emissions. Permit price has stabilised around $20/tonne CO2.</li>
<li><strong>Essay move.</strong> Doornik likes essays that derive cost-effectiveness from marginal-cost equalisation. Use the differential argument explicitly.</li>
<li><strong>Essay move.</strong> Compare to a uniform abatement standard: same total reduction but higher cost because marginal costs are not equalised. The cost-effectiveness gain is the welfare advantage of trading.</li>
<li><strong>Limitation.</strong> Tradeable permits work best for stock pollutants with well-mixed atmospheric effects. For localised damages (e.g., hot spots), spatial heterogeneity complicates the scheme.</li>
<li>See also [[Concepts/Cap-and-Trade]], [[Concepts/Pigouvian Tax]], [[Concepts/Weitzman Prices vs Quantities]].</li>
</ul>""",
    },
    "weitzman-prices-vs-quantities": {
        "math": r"""<p><strong>Weitzman (1974)</strong> compares Pigouvian price instruments (taxes) to quantity instruments (permits) under uncertainty about abatement costs and damages. The result: when marginal damages are steep relative to marginal abatement costs, quantity instruments dominate; when damages are flat relative to costs, prices dominate.</p>

<p>Let marginal abatement cost be $C'(a) + \epsilon$ where $\epsilon$ is mean-zero noise, and marginal damage be $D'(a)$ (deterministic). Welfare loss from incorrect policy compared to the first best:</p>

$$\Delta = \frac{\sigma^2}{2} \left( \frac{1}{D''} - \frac{1}{C''} \right),$$

<p>where $\sigma^2$ is the variance of $\epsilon$, $D''$ is the slope of marginal damage, and $C''$ is the slope of marginal cost.</p>

<ol>
<li>Under a quantity instrument, the policy fixes $a$; cost variation passes through to permit prices.</li>
<li>Under a price instrument, the policy fixes $\tau$; cost variation changes $a$ directly.</li>
<li>Comparing the welfare losses gives Weitzman's formula. The sign of $\Delta$ determines which instrument is preferred.</li>
</ol>

<p><strong>Steep marginal damages</strong> ($D''$ large): damages rise sharply with emissions. The cost of allowing more emissions than intended is high. Quantity instruments fix emissions, dominating taxes.</p>

<p><strong>Flat marginal damages</strong> ($D''$ small): damages are roughly linear. The cost of mistakenly setting emissions is small. Price instruments are robust to cost shocks, dominating quantities.</p>

<p>Climate change is typically modelled with flat marginal damages (Nordhaus, Stern), favouring carbon taxes. Local air pollution can have threshold effects (steep damages), favouring permits.</p>

<p>Hybrid instruments (Pizer 2002, Roberts-Spence 1976) combine prices and quantities to exploit the strengths of each. EU ETS price stability reserve is one such hybrid.</p>

<p>Reference: Micro2025.pdf Topic 3 Lecture 3; Weitzman 1974 REStud; Roberts-Spence 1976 JPubE.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <line x1="80" y1="260" x2="540" y2="260" stroke="#333"/>
  <line x1="80" y1="260" x2="80" y2="60" stroke="#333"/>
  <text x="540" y="280" font-size="13">emissions</text>
  <text x="60" y="70" font-size="13">$\$$</text>
  <line x1="80" y1="220" x2="540" y2="100" stroke="#1f77b4" stroke-width="2"/>
  <text x="430" y="90" font-size="12" fill="#1f77b4">MC (expected)</text>
  <line x1="80" y1="200" x2="540" y2="80" stroke="#1f77b4" stroke-width="1" stroke-dasharray="3 3"/>
  <line x1="80" y1="240" x2="540" y2="120" stroke="#1f77b4" stroke-width="1" stroke-dasharray="3 3"/>
  <line x1="80" y1="100" x2="540" y2="220" stroke="#d62728" stroke-width="3"/>
  <text x="430" y="220" font-size="12" fill="#d62728">steep MD</text>
  <line x1="80" y1="150" x2="540" y2="180" stroke="#d62728" stroke-width="1" stroke-dasharray="4 2"/>
  <text x="430" y="170" font-size="12" fill="#d62728">flat MD</text>
  <text x="60" y="305" font-size="12" fill="#555">Steep MD favours quantity instruments; flat MD favours prices.</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Weitzman: relative slopes of MC and MD determine instrument choice under cost uncertainty.</p>""",
        "examples": r"""<ul>
<li><strong>Climate change policy.</strong> Marginal damage from global CO2 is roughly flat (Nordhaus DICE model), favouring carbon taxes over fixed emission caps.</li>
<li><strong>Local air pollution.</strong> Threshold effects (urban smog days) give steep marginal damage, favouring quantity caps.</li>
<li><strong>Acid rain SO2.</strong> Steep marginal damage near ecosystems with low buffering capacity favoured the quantity-based US SO2 trading scheme.</li>
<li><strong>Essay move.</strong> Doornik rewards essays that derive the Weitzman formula and apply it to a real policy choice. The formula's two terms have clear economic meaning.</li>
<li><strong>Essay move.</strong> Use Weitzman to argue for hybrid instruments. Pizer-Roberts-Spence price collars combine the best of both.</li>
<li><strong>Limitation.</strong> Weitzman assumes mean-zero cost shocks and known damage function. With uncertainty about damages too, the analysis is more complicated.</li>
<li>See also [[Concepts/Tradeable Permits]], [[Concepts/Pigouvian Tax]], [[Concepts/Cap-and-Trade]].</li>
</ul>""",
    },
    "club-goods": {
        "math": r"""<p><strong>Club goods</strong> (Buchanan 1965) are excludable but non-rival up to a congestion point. A club good can be provided by a voluntary association that charges members for access. Examples: private parks, gym memberships, toll roads, cable TV.</p>

<p>Setup: $n$ members share a club good with quality $q$ and total cost $C(q)$. Per-member utility $u(q, n)$ depends on quality and congestion. The club maximises per-member surplus:</p>

$$\max_{q, n} u(q, n) - C(q)/n.$$

<ol>
<li>FOC in $q$: $u_q = C'(q)/n$. This is the per-member Samuelson rule for the club: marginal benefit per person equals marginal cost share.</li>
<li>FOC in $n$: $u_n = -C(q)/n^2$. Adding a member changes congestion (typically negative $u_n$) and reduces cost share. Balance these effects.</li>
<li>Optimal membership size $n^*$ trades off congestion against cost-sharing.</li>
</ol>

<p>Comparison with pure public goods: in pure public goods, $n_n = 0$ (no congestion) and the optimal size is the entire population. In private goods, $n = 1$ (no sharing). Club goods are intermediate.</p>

<p>Tiebout (1956) argued that competing clubs (jurisdictions) allow consumers to sort by preferences, achieving efficient provision via "voting with feet". Each jurisdiction offers a different bundle of local public goods financed by taxes; consumers self-select.</p>

<p>Real-world examples:</p>

<p>Private swimming pools, golf clubs, fraternal orders. Membership pricing internalises both cost-sharing and congestion.</p>

<p>Internet platforms with subscription models (Netflix, Spotify). Marginal cost of an additional user is low; congestion (network speeds) is a small concern.</p>

<p>Cable TV, telephone services. Standard club-good economics with infrastructure costs and capacity constraints.</p>

<p>Reference: Micro2025.pdf Topic 3 Lecture on Public Goods; Buchanan 1965; Hindriks-Myles Ch. 6.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <line x1="80" y1="260" x2="540" y2="260" stroke="#333"/>
  <line x1="80" y1="260" x2="80" y2="60" stroke="#333"/>
  <text x="540" y="280" font-size="13">members $n$</text>
  <text x="60" y="70" font-size="13">per-member welfare</text>
  <path d="M 100 220 Q 200 100 300 80 Q 400 100 540 200" fill="none" stroke="#1f77b4" stroke-width="2"/>
  <text x="100" y="125" font-size="12" fill="#1f77b4">welfare</text>
  <circle cx="300" cy="80" r="6" fill="#2ca02c"/>
  <text x="270" y="55" font-size="12" fill="#2ca02c">optimal $n^*$</text>
  <text x="60" y="305" font-size="12" fill="#555">Trade-off: cost-sharing pulls $n$ up, congestion pulls it down.</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Per-member welfare has interior maximum at $n^*$.</p>""",
        "examples": r"""<ul>
<li><strong>Streaming services.</strong> Netflix, Spotify pricing reflects club economics: shared content cost, congestion from bandwidth or licensing.</li>
<li><strong>Highway toll roads.</strong> California's express lanes and London's congestion zone are club-good applications.</li>
<li><strong>Private golf clubs.</strong> Member fees reflect both cost-sharing and limit access to control course congestion.</li>
<li><strong>Essay move.</strong> Doornik rewards essays that link Buchanan's club theory to Tiebout's competing-jurisdictions framework. Both rely on exclusion and sorting.</li>
<li><strong>Essay move.</strong> Compare clubs to pure public goods. The exclusion technology is the key distinction; if exclusion is costly, government provision is required.</li>
<li><strong>Limitation.</strong> Club theory assumes free entry and exit and identical preferences within a club. With heterogeneity, more sophisticated mechanism design is needed.</li>
<li>See also [[Concepts/Public Goods]], [[Concepts/Rivalry and Excludability]], [[Concepts/Common Pool Resources]].</li>
</ul>""",
    },
    "common-pool-resources": {
        "math": r"""<p><strong>Common pool resources</strong> (CPRs) are rival but non-excludable: usage by one person reduces what is available to others, but it is costly or impossible to prevent access. Examples: fisheries, groundwater, common pastures, atmospheric carbon-absorption capacity.</p>

<p>Classic model: $n$ harvesters share a fishery with stock $S$ and growth function $g(S)$. Total harvest $H = \sum_i h_i$. Each harvester chooses $h_i$ to maximise own catch, ignoring the negative externality on stock dynamics.</p>

<ol>
<li>Individual problem: $\max_{h_i} p \cdot h_i - c(h_i, S)$ where $c$ is the cost of effort and depends on remaining stock.</li>
<li>Nash equilibrium: each harvester takes others' efforts as given. The aggregate harvest typically exceeds the maximum sustainable yield.</li>
<li>Comparing the Nash outcome to the social planner's: the planner chooses $H^* = g(S^*)$ at the steady state, balancing current harvest against stock dynamics.</li>
</ol>

<p>Gordon (1954): the open-access equilibrium has rents dissipated to zero. Profit-driven entry continues until the marginal harvester's catch just covers cost, regardless of the resource's productive potential.</p>

<p><strong>Solutions:</strong></p>

<p>(i) Individual transferable quotas (ITQs): Iceland, New Zealand fisheries assign tradable harvest rights. Marginal abatement costs equalised, sustainable yield achieved.</p>

<p>(ii) Cooperative governance: Ostrom (1990) documents that local communities can self-govern CPRs through trust, norms, and graduated sanctions. Examples: Spanish irrigation huertas, Maine lobster gangs.</p>

<p>(iii) Privatisation: convert the CPR to private property. Effective for some resources (timber lots) but politically infeasible for many (oceans, air).</p>

<p>(iv) Taxation: levy a per-unit charge that internalises the marginal external cost. Pigouvian tax applied to the harvest.</p>

<p>Reference: Micro2025.pdf Topic 3 Lecture on Externalities; Gordon 1954 JPE; Ostrom 1990 "Governing the Commons".</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <line x1="80" y1="260" x2="540" y2="260" stroke="#333"/>
  <line x1="80" y1="260" x2="80" y2="60" stroke="#333"/>
  <text x="540" y="280" font-size="13">effort</text>
  <text x="60" y="70" font-size="13">harvest</text>
  <path d="M 80 240 Q 250 100 540 240" fill="none" stroke="#1f77b4" stroke-width="2"/>
  <text x="220" y="120" font-size="12" fill="#1f77b4">sustainable yield</text>
  <line x1="80" y1="260" x2="540" y2="60" stroke="#d62728" stroke-width="2" stroke-dasharray="4 2"/>
  <text x="430" y="80" font-size="12" fill="#d62728">total cost</text>
  <circle cx="250" cy="100" r="5" fill="#2ca02c"/>
  <text x="200" y="80" font-size="12" fill="#2ca02c">MSY</text>
  <circle cx="430" cy="240" r="5" fill="#888"/>
  <text x="380" y="260" font-size="12" fill="#888">open access</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Open-access equilibrium dissipates rents at the intersection with the cost line, beyond MSY.</p>""",
        "examples": r"""<ul>
<li><strong>Atlantic cod fishery collapse.</strong> Newfoundland cod stocks collapsed in 1992 after decades of overfishing under open access, the canonical CPR tragedy.</li>
<li><strong>California groundwater.</strong> Aquifer depletion under unmanaged pumping; recent regulation (SGMA 2014) imposes basin-level management.</li>
<li><strong>Atmospheric carbon.</strong> The global climate-change problem is a CPR challenge at planetary scale. International coordination through Paris Agreement is the governance attempt.</li>
<li><strong>Essay move.</strong> Doornik rewards essays that distinguish CPRs from public goods. Both have non-excludability; CPRs are rival, public goods are not.</li>
<li><strong>Essay move.</strong> Cite Ostrom's design principles for successful self-governance: clearly defined boundaries, congruence, collective choice, monitoring, sanctions, conflict resolution.</li>
<li><strong>Limitation.</strong> The tragedy framework assumes selfish utility maximisation. Empirical evidence of cooperation in CPR experiments (Cardenas-Stranlund-Willis 2000) suggests preferences are richer.</li>
<li>See also [[Concepts/Tragedy of the Commons]], [[Concepts/Public Goods]], [[Concepts/Coase Theorem]].</li>
</ul>""",
    },
    "clarke-tax": {
        "math": r"""<p>The <strong>Clarke tax</strong> (also called Clarke-Groves or pivotal mechanism) elicits truthful preferences for public goods. Each agent pays a tax equal to the harm their report causes to others. The mechanism is dominant-strategy incentive compatible: truthful reporting is optimal regardless of others' reports.</p>

<p>Setup: $n$ agents with private valuations $v_i$ for a public good. Provision cost $c$ is split equally. The public good is provided iff $\sum_i v_i \geq c$. Agent $i$ reports $\tilde v_i$; provision decision is based on $\sum \tilde v_j$.</p>

<p>Clarke tax for agent $i$:</p>

$$t_i = \max\left\{0, c - \sum_{j \neq i} \tilde v_j\right\} - \max\left\{0, \sum_{j \neq i} \tilde v_j - c\right\} \cdot \mathbb{1}[\text{decision changed}].$$

<p>In words: $i$ pays a tax only if their report was <strong>pivotal</strong> (changed the decision). The tax equals the externality imposed on others by changing the outcome.</p>

<ol>
<li>If $i$'s report does not change the decision, $i$ pays no tax.</li>
<li>If $i$'s report tips the decision toward provision, $i$ pays the net loss to others: $c - \sum_{j \neq i} \tilde v_j$.</li>
<li>If $i$'s report tips against provision, $i$ pays the net loss to others (in opposite direction).</li>
<li>Truth-telling is dominant: misreporting cannot improve $i$'s payoff because the tax matches the externality.</li>
</ol>

<p>Properties:</p>

<p>(i) Dominant-strategy incentive compatibility: truth-telling is the best strategy regardless of what others do.</p>

<p>(ii) Efficient: the social-optimal provision decision is made.</p>

<p>(iii) Budget imbalance: total taxes collected typically do not match the cost. The pivotal mechanism is not budget-balanced.</p>

<p>(iv) Manipulation by coalitions: groups can collude to misreport, even though no individual can profitably deviate.</p>

<p>The Clarke-Groves family (Groves 1973, Clarke 1971) gives general mechanisms beyond binary public-good decisions. Vickrey-Clarke-Groves (VCG) is the extension to multi-unit auctions and general allocations.</p>

<p>Reference: Micro2025.pdf Topic 3 Lecture on Mechanism Design; Clarke 1971; Groves 1973; Mas-Colell Ch. 23.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <text x="60" y="40" font-size="14" font-weight="bold">Clarke pivotal mechanism</text>
  <line x1="80" y1="260" x2="540" y2="260" stroke="#333"/>
  <line x1="80" y1="260" x2="80" y2="60" stroke="#333"/>
  <text x="540" y="280" font-size="13">$\sum_{j \neq i} \tilde v_j$</text>
  <text x="60" y="70" font-size="13">$i$'s tax</text>
  <line x1="80" y1="260" x2="280" y2="100" stroke="#1f77b4" stroke-width="2"/>
  <line x1="280" y1="100" x2="380" y2="100" stroke="#1f77b4" stroke-width="2"/>
  <text x="100" y="155" font-size="12" fill="#1f77b4">$i$ pivotal: tax = $c - \sum_{j \neq i} \tilde v_j$</text>
  <line x1="380" y1="260" x2="540" y2="260" stroke="#2ca02c" stroke-width="2"/>
  <text x="420" y="240" font-size="12" fill="#2ca02c">$i$ not pivotal: tax = 0</text>
  <line x1="280" y1="60" x2="280" y2="260" stroke="#666" stroke-dasharray="3 3"/>
  <text x="270" y="280" font-size="12">$c$</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Tax = externality imposed on others by tipping the decision.</p>""",
        "examples": r"""<ul>
<li><strong>Lab experiments.</strong> Attiyeh-Franciosi-Isaac (2000) test Clarke tax in classroom settings. Truth-telling rates rise with the mechanism, though imperfectly.</li>
<li><strong>Spectrum auctions.</strong> FCC clock auctions use VCG-style pricing to elicit truthful bidding for spectrum bundles.</li>
<li><strong>Cost allocation.</strong> Sharing infrastructure costs among coalition members can use VCG to ensure no member overpays relative to the externality they impose.</li>
<li><strong>Essay move.</strong> Doornik rewards essays that show the mechanism's dominant-strategy property by direct calculation. Misreporting cannot help $i$.</li>
<li><strong>Essay move.</strong> The budget-balance failure is the standard critique. In practice, the surplus or deficit is absorbed by the government or auctioneer.</li>
<li><strong>Limitation.</strong> Coalitional manipulation, complex pricing, and budget imbalance limit real-world adoption. Hybrid mechanisms approximate VCG with practical adjustments.</li>
<li>See also [[Concepts/Clarke-Groves Mechanism]], [[Concepts/Vickrey (Second-Price) Auction]].</li>
</ul>""",
    },
    "vickrey-auction": {
        "math": r"""<p>The <strong>Vickrey (second-price sealed-bid) auction</strong> assigns the item to the highest bidder at a price equal to the second-highest bid. Truthful bidding $b_i = v_i$ is a weakly dominant strategy: for any opponent bids, no other bid can yield a higher payoff.</p>

<p>Proof: consider bidder $i$ with valuation $v_i$ and opponent's highest bid $h_{-i}$.</p>

<ol>
<li>Case $h_{-i} < v_i$: bidder $i$ wants to win. Bidding $b_i = v_i$ wins and pays $h_{-i}$, payoff $v_i - h_{-i} > 0$. Bidding higher still wins and pays $h_{-i}$ (same payoff). Bidding lower may lose, payoff 0 or $v_i - h_{-i}$.</li>
<li>Case $h_{-i} > v_i$: bidder $i$ does not want to win. Bidding $b_i = v_i$ loses, payoff 0. Bidding higher could win and pay $h_{-i} > v_i$, payoff negative. Bidding lower also loses (payoff 0).</li>
<li>In both cases, $b_i = v_i$ is at least as good as any other bid. Truth-telling weakly dominates.</li>
</ol>

<p>Properties:</p>

<p>(i) <strong>Dominant-strategy incentive compatibility.</strong> No knowledge of opponent valuations or distributions needed.</p>

<p>(ii) <strong>Efficient allocation.</strong> The highest-valuing bidder wins.</p>

<p>(iii) <strong>Revenue equivalence.</strong> Under symmetric private values, expected revenue equals first-price sealed-bid, Dutch, and English auction revenues (Vickrey 1961, Myerson 1981).</p>

<p>The Vickrey-Clarke-Groves (VCG) mechanism generalises this idea to multi-unit and combinatorial settings: each winner pays the marginal externality imposed on others by their win.</p>

<p>Critique: Ausubel-Milgrom (2006) argue that Vickrey auctions can be susceptible to "low-revenue equilibria" in multi-unit settings, where bidders coordinate to bid less aggressively. The dominant-strategy property holds for single-unit Vickrey but not always for multi-unit VCG.</p>

<p>Real-world adoption: Vickrey-style designs are used in online advertising (Google AdWords approximates), spectrum auctions, and academic resource allocation. Outright single-unit Vickrey is rarer due to the "revelation paradox" and transparency concerns.</p>

<p>Reference: Micro2025.pdf Topic 3 Lecture on Auctions; Vickrey 1961 JF; Klemperer "Auctions: Theory and Practice".</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <text x="60" y="40" font-size="14" font-weight="bold">Vickrey: winner pays 2nd-highest bid</text>
  <rect x="100" y="100" width="80" height="150" fill="#1f77b4"/>
  <text x="140" y="270" font-size="12" text-anchor="middle">Bid 1: 100</text>
  <text x="140" y="90" font-size="12" text-anchor="middle">winner</text>
  <rect x="220" y="140" width="80" height="110" fill="#d62728"/>
  <text x="260" y="270" font-size="12" text-anchor="middle">Bid 2: 80</text>
  <text x="260" y="130" font-size="12" text-anchor="middle">price paid</text>
  <rect x="340" y="180" width="80" height="70" fill="#888"/>
  <text x="380" y="270" font-size="12" text-anchor="middle">Bid 3: 50</text>
  <rect x="460" y="210" width="80" height="40" fill="#888"/>
  <text x="500" y="270" font-size="12" text-anchor="middle">Bid 4: 30</text>
  <text x="60" y="300" font-size="12" fill="#555">Truth-telling weakly dominant: $b_i = v_i$ regardless of others.</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Vickrey auction: highest bid wins, pays second-highest bid. Truthful bidding is dominant.</p>""",
        "examples": r"""<ul>
<li><strong>Online advertising.</strong> Google AdWords second-price auctions for keywords approximate Vickrey, accounting for billions in annual revenue.</li>
<li><strong>Stamp auctions.</strong> Historical Vickrey-style usage by philatelic dealers since the early 20th century, predating Vickrey's formal analysis.</li>
<li><strong>Spectrum auctions.</strong> FCC and Ofcom (UK) auctions use VCG-style multi-unit designs for wireless spectrum.</li>
<li><strong>Essay move.</strong> Doornik rewards essays that prove dominant-strategy incentive compatibility step-by-step. The simplicity of the argument is striking.</li>
<li><strong>Essay move.</strong> Use revenue equivalence to compare Vickrey to first-price, English, and Dutch auctions. Under symmetric IPV, all four yield the same expected revenue.</li>
<li><strong>Limitation.</strong> Vickrey is vulnerable to bidder collusion and budget constraints. Multi-unit Vickrey can have low-revenue equilibria (Ausubel-Milgrom).</li>
<li>See also [[Concepts/Clarke-Groves Mechanism]], [[Concepts/Winner's Curse]].</li>
</ul>""",
    },
    "cap-and-trade": {
        "math": r"""<p><strong>Cap-and-trade</strong> is the practical implementation of tradeable permits. The regulator sets an aggregate emission cap $\bar E$, issues permits totalling $\bar E$, and allows firms to trade. Each firm must hold a permit for each unit emitted.</p>

<p>Equilibrium: with marginal abatement costs $C_i'(a_i)$, the permit price $p^*$ satisfies $C_i'(a_i^*) = p^*$ for all firms. Total abatement $\sum_i a_i^* = \sum_i e_i^0 - \bar E$ meets the cap.</p>

<ol>
<li>Set the cap based on the targeted emission level (typically informed by damage function).</li>
<li>Allocate initial permits via auction, grandfathering, or output-based.</li>
<li>Permit market clears at the equilibrium price $p^*$.</li>
<li>Marginal abatement costs equalised across firms, achieving cost-effectiveness.</li>
</ol>

<p>Allocation efficiency: as long as trading is allowed, the abatement profile is efficient regardless of initial allocation. Coase-like result for permits.</p>

<p>Equivalence with carbon tax: under cost certainty, a tax at rate $p^*$ produces the same outcome. Under uncertainty, Weitzman (1974) gives the comparison.</p>

<p>Real-world cap-and-trade systems:</p>

<p>(i) EU ETS (2005 onwards): largest system covering about 11,000 installations across electricity, manufacturing, aviation. Phase IV (2021-2030) tightens caps to align with 55% emission reduction by 2030.</p>

<p>(ii) US Acid Rain Program (1990 Clean Air Act): SO2 emissions from US power plants. Achieved targeted reductions at 50% lower cost than command-and-control alternatives (Schmalensee et al. 1998).</p>

<p>(iii) California cap-and-trade (2013 onwards): linked with Quebec. Permit prices around $20/tonne CO2, generating revenue for green spending.</p>

<p>(iv) RGGI (2009 onwards): northeastern US states for power-plant emissions. Stable permit prices, used as a model for state-level climate policy.</p>

<p>Design issues: free vs auctioned permits, banking and borrowing, offset credits, price floors and ceilings. EU ETS uses Market Stability Reserve to address price collapses.</p>

<p>Reference: Micro2025.pdf Topic 3 Lecture on Externalities; Tietenberg "Emissions Trading"; Schmalensee-Stavins 2017 REEP.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <text x="60" y="40" font-size="14" font-weight="bold">Cap-and-trade market</text>
  <line x1="80" y1="260" x2="540" y2="260" stroke="#333"/>
  <line x1="80" y1="260" x2="80" y2="60" stroke="#333"/>
  <text x="540" y="280" font-size="13">total abatement</text>
  <text x="60" y="70" font-size="13">permit price</text>
  <line x1="80" y1="240" x2="540" y2="80" stroke="#1f77b4" stroke-width="2"/>
  <text x="430" y="100" font-size="12" fill="#1f77b4">marginal abatement cost</text>
  <line x1="280" y1="60" x2="280" y2="260" stroke="#d62728" stroke-width="2" stroke-dasharray="5 3"/>
  <text x="270" y="290" font-size="12" fill="#d62728">cap $\bar E$</text>
  <circle cx="280" cy="160" r="6" fill="#2ca02c"/>
  <text x="290" y="155" font-size="12" fill="#2ca02c">permit price $p^*$</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Cap-and-trade clears at the price where industry MAC equals the cap.</p>""",
        "examples": r"""<ul>
<li><strong>EU ETS.</strong> 2005 onwards, expanded to cover aviation (2012), maritime (2024). Caps tightened across phases. Carbon price reached EUR 100/tonne in 2023.</li>
<li><strong>RGGI.</strong> US northeastern states (2009 onwards). Documented health benefits (Burtraw-Palmer 2014) from co-pollutant reductions.</li>
<li><strong>China national ETS.</strong> Launched 2021, covers power sector. Largest carbon market by emissions volume, though prices remain low.</li>
<li><strong>Essay move.</strong> Doornik rewards essays that derive cost-effectiveness from marginal-cost equalisation. Compare to uniform standards (higher cost, same emissions).</li>
<li><strong>Essay move.</strong> Discuss permit price volatility and design responses (Market Stability Reserve in EU ETS, price floors in California). These are practical extensions of Weitzman.</li>
<li><strong>Limitation.</strong> Cap-and-trade is vulnerable to leakage: emissions migrate to non-covered regions. Border adjustments (CBAM) attempt to address this.</li>
<li>See also [[Concepts/Tradeable Permits]], [[Concepts/Weitzman Prices vs Quantities]].</li>
</ul>""",
    },
    "coasean-bargaining": {
        "math": r"""<p><strong>Coasean bargaining</strong> (Coase 1960) refers to private negotiation between parties affected by an externality. With clearly defined property rights and zero transaction costs, the parties reach the efficient outcome regardless of which party holds the entitlement.</p>

<p>Setup: a polluter generates negative externality on a victim. Without bargaining, the polluter chooses emission level $e^M$ maximising own profit, ignoring damages $D(e)$. The social optimum $e^*$ balances polluter profit against damages: $\pi'(e^*) = D'(e^*)$.</p>

<ol>
<li><strong>Polluter has right to pollute:</strong> the victim pays the polluter to reduce emissions. The victim pays up to $D'(e)$ per unit; the polluter accepts as long as the payment exceeds the foregone profit $\pi'(e)$. At equilibrium, $\pi'(e^*) = D'(e^*)$: efficient.</li>
<li><strong>Victim has right to be free of pollution:</strong> the polluter pays the victim to permit emissions. The polluter pays up to $\pi'(e)$ per unit; the victim accepts as long as the payment exceeds the damage $D'(e)$. Same equilibrium.</li>
</ol>

<p>The Coase theorem: under zero transaction costs and clear property rights, the equilibrium emission level is socially optimal regardless of who holds the entitlement. The distribution of surplus depends on the assignment.</p>

<p>When does Coasean bargaining fail?</p>

<p>(i) <strong>Many parties (high transaction costs).</strong> Coordination among thousands of pollution victims is prohibitive. Carbon emissions cannot be Coase-negotiated.</p>

<p>(ii) <strong>Asymmetric information.</strong> If parties do not know each other's valuations or damages, strategic misrepresentation prevents reaching the efficient outcome (Myerson-Satterthwaite 1983).</p>

<p>(iii) <strong>Wealth effects.</strong> If utility is not quasi-linear in money, the efficient quantity depends on who holds the entitlement.</p>

<p>(iv) <strong>Holdout problems.</strong> With multiple affected parties, individuals can refuse to settle in hopes of better terms.</p>

<p>Coase's contribution was to clarify that externalities are reciprocal: both the polluter and victim cause the conflict by being present. The Pigouvian framework treats them asymmetrically (polluter bears burden); Coase argues the optimal assignment depends on relative costs of avoidance.</p>

<p>Reference: Micro2025.pdf Topic 3 Lecture on Externalities; Coase 1960 JLE; Hindriks-Myles Ch. 7.2.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <line x1="80" y1="260" x2="540" y2="260" stroke="#333"/>
  <line x1="80" y1="260" x2="80" y2="60" stroke="#333"/>
  <text x="540" y="280" font-size="13">$e$</text>
  <text x="60" y="70" font-size="13">$\$$</text>
  <line x1="80" y1="100" x2="540" y2="220" stroke="#1f77b4" stroke-width="2"/>
  <text x="430" y="240" font-size="12" fill="#1f77b4">marginal damage $D'(e)$</text>
  <line x1="80" y1="220" x2="540" y2="100" stroke="#d62728" stroke-width="2"/>
  <text x="430" y="120" font-size="12" fill="#d62728">marginal profit $\pi'(e)$</text>
  <circle cx="290" cy="160" r="6" fill="#2ca02c"/>
  <text x="300" y="155" font-size="12" fill="#2ca02c">$e^*$</text>
  <text x="60" y="305" font-size="12" fill="#555">Coase: equilibrium is $e^*$ regardless of property-right assignment.</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Coasean bargaining yields the social optimum where $\pi' = D'$, regardless of who holds the right.</p>""",
        "examples": r"""<ul>
<li><strong>Easement negotiations.</strong> Neighbors negotiate compensation for noise, light blockage, or visual nuisances. Standard small-numbers Coase application.</li>
<li><strong>Conservation easements.</strong> Land trusts pay landowners to preserve habitats. Private agreement internalises positive externalities.</li>
<li><strong>Cap-and-trade markets.</strong> Permits create explicit property rights and allow Coasean-style trading among polluters; transaction costs are minimised by exchange-based platforms.</li>
<li><strong>Essay move.</strong> Doornik rewards essays that emphasise Coase's reciprocity insight. Externalities are not one-sided; both parties contribute to the conflict.</li>
<li><strong>Essay move.</strong> Coase's theorem is often misread. The point is not that Pigouvian taxes are unnecessary, but that the choice of policy instrument depends on transaction costs.</li>
<li><strong>Limitation.</strong> With many parties, asymmetric information, or wealth effects, Coasean bargaining fails. Government intervention (taxes, regulation, mediation) is then needed.</li>
<li>See also [[Concepts/Coase Theorem]], [[Concepts/Pigouvian Tax]], [[Concepts/Externality Internalisation]].</li>
</ul>""",
    },

    "pareto-efficiency": {
        "math": r"""<p><strong>Pareto efficiency</strong>: an allocation $(x_i)_{i=1}^I$ is Pareto efficient if no feasible reallocation makes at least one agent strictly better off without making any agent worse off. In an exchange economy, the Pareto-efficient allocations form the <strong>contract curve</strong>: the locus where $MRS_1 = MRS_2 = \cdots = MRS_I$.</p>

<ol>
<li>Planner's problem: $\max u_1(x_1)$ subject to $u_i(x_i) \geq \bar u_i$ for $i = 2, \dots, I$ and $\sum_i x_i = \sum_i \omega_i$.</li>
<li>FOC give tangency: $MRS_i = \lambda$ for all $i$.</li>
<li>Hence $MRS_1 = MRS_2 = \dots = MRS_I$ at any Pareto-efficient point.</li>
</ol>

<p>In production economies, Pareto efficiency requires (i) MRTS equalised across firms, (ii) MRS equalised across consumers, and (iii) $MRS = MRT$ between any pair of goods.</p>

<p>The set of Pareto-efficient allocations is typically a curve. Selecting among them requires distributional judgments captured by a social welfare function.</p>

<p>Pareto efficiency is the most widely accepted normative criterion in economics, but it is incomplete. The Kaldor-Hicks criterion extends Pareto via compensation tests.</p>

<p>Reference: Micro2025.pdf Topic 2 Lecture 1; Varian Ch. 17; Mas-Colell Ch. 16.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <rect x="80" y="40" width="440" height="240" fill="none" stroke="#333" stroke-width="2"/>
  <path d="M 100 60 Q 250 140 510 270" fill="none" stroke="#2ca02c" stroke-width="2"/>
  <text x="300" y="100" font-size="12" fill="#2ca02c">contract curve</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Pareto-efficient allocations form the contract curve.</p>""",
        "examples": r"""<ul>
<li><strong>Trade and gains.</strong> Free trade is Pareto-improving in aggregate, not necessarily across all workers.</li>
<li><strong>Health-care prioritisation.</strong> Organ-transplant allocations can be Pareto efficient yet differ widely in distribution.</li>
<li><strong>Climate policy.</strong> Carbon taxes can be Pareto-improving with appropriate rebates.</li>
<li><strong>Essay move.</strong> Doornik rewards essays distinguishing Pareto efficiency from social desirability. Efficient can still be inequitable.</li>
<li><strong>Essay move.</strong> Use FOC tangency to derive the contract curve.</li>
<li><strong>Limitation.</strong> Pareto efficiency is an incomplete ordering; many allocations are Pareto-incomparable.</li>
<li>See also [[Concepts/Contract Curve]], [[Concepts/First Welfare Theorem]].</li>
</ul>""",
    },
    "pareto-criterion": {
        "math": r"""<p>The <strong>Pareto criterion</strong> ranks two allocations: $(\hat x_i)$ Pareto-dominates $(x_i)$ if $u_i(\hat x_i) \geq u_i(x_i)$ for all $i$ with strict inequality for at least one. It provides a partial order.</p>

<ol>
<li><strong>Reflexivity:</strong> every allocation Pareto-dominates itself weakly.</li>
<li><strong>Transitivity:</strong> if $A$ Pareto-dominates $B$ and $B$ Pareto-dominates $C$, then $A$ Pareto-dominates $C$.</li>
<li><strong>Incompleteness:</strong> two allocations can be Pareto-incomparable.</li>
</ol>

<p>The Pareto criterion is the weakest normative criterion. Any reasonable SWF respects Pareto.</p>

<p>Pareto-efficient allocations are not Pareto-dominated by any feasible allocation. Pareto efficiency is the absence of Pareto improvements.</p>

<p>Most allocations are Pareto-incomparable. Without compensation, very few policies are Pareto improvements. The criterion ignores fairness and equity.</p>

<p>Kaldor (1939) and Hicks (1939) proposed compensation: $A$ K-H-dominates $B$ if winners could hypothetically compensate losers. More decisive but inconsistent (Scitovsky 1941).</p>

<p>Reference: Micro2025.pdf Topic 2 Lecture 1; Mas-Colell Ch. 16; Sen "Collective Choice and Social Welfare".</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <line x1="80" y1="260" x2="540" y2="260" stroke="#333"/>
  <line x1="80" y1="260" x2="80" y2="60" stroke="#333"/>
  <text x="540" y="280" font-size="13">$u_1$</text>
  <text x="60" y="70" font-size="13">$u_2$</text>
  <circle cx="200" cy="180" r="6" fill="#1f77b4"/>
  <text x="180" y="170" font-size="12" fill="#1f77b4">$A$</text>
  <circle cx="300" cy="120" r="6" fill="#2ca02c"/>
  <text x="310" y="115" font-size="12" fill="#2ca02c">$B$ dominates</text>
  <circle cx="150" cy="80" r="6" fill="#d62728"/>
  <text x="100" y="75" font-size="12" fill="#d62728">$C$ incomparable</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">$B$ Pareto-dominates $A$; $C$ is incomparable.</p>""",
        "examples": r"""<ul>
<li><strong>Voluntary trade.</strong> Trades both parties agree to are Pareto improvements.</li>
<li><strong>Public health interventions.</strong> Smallpox eradication is a near-perfect Pareto improvement.</li>
<li><strong>Tariff reductions with compensation.</strong> Lowering tariffs is Pareto-improving only with compensation.</li>
<li><strong>Essay move.</strong> Doornik likes essays emphasising the partial-ordering nature. Most policy choices are Pareto-incomparable.</li>
<li><strong>Essay move.</strong> Compare Pareto to K-H. K-H delivers complete rankings at the cost of actual-compensation.</li>
<li><strong>Limitation.</strong> Pareto ignores process; two allocations with same utility distribution are equivalent regardless of provenance.</li>
<li>See also [[Concepts/Pareto Efficiency]], [[Concepts/Kaldor-Hicks Compensation]].</li>
</ul>""",
    },
    "first-welfare-theorem": {
        "math": r"""<p><strong>First Welfare Theorem</strong> (Arrow 1951, Debreu 1959): every competitive equilibrium is Pareto efficient, provided preferences are locally non-satiated and markets are complete.</p>

<p>Proof: let $(p^*, (x_i^*))$ be a CE. Suppose $(\hat x_i)$ Pareto-dominates.</p>

<ol>
<li>By local non-satiation, $\hat x_i$ either equals $x_i^*$ or costs strictly more: $p^* \cdot \hat x_i > p^* \cdot \omega_i$.</li>
<li>For some $i$ with strict utility gain: $p^* \cdot \hat x_i > p^* \cdot \omega_i$.</li>
<li>Others: $p^* \cdot \hat x_i \geq p^* \cdot \omega_i$.</li>
<li>Sum: $p^* \cdot \sum_i \hat x_i > p^* \cdot \sum_i \omega_i$. Feasibility requires equality: contradiction.</li>
</ol>

<p>The proof requires only local non-satiation. Failures: externalities, public goods, asymmetric information, increasing returns.</p>

<p>FWT is the formal invisible hand. Says nothing about distribution.</p>

<p>Reference: Micro2025.pdf Topic 2 Lecture 2; Mas-Colell Ch. 16; Arrow 1951.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <rect x="80" y="40" width="440" height="240" fill="none" stroke="#333" stroke-width="2"/>
  <path d="M 80 200 Q 200 180 300 140 Q 400 110 520 80" fill="none" stroke="#1f77b4" stroke-width="2"/>
  <path d="M 80 130 Q 200 160 300 200 Q 400 230 520 250" fill="none" stroke="#d62728" stroke-width="2"/>
  <line x1="120" y1="40" x2="540" y2="280" stroke="#2ca02c" stroke-width="1.5" stroke-dasharray="6 4"/>
  <circle cx="300" cy="170" r="6" fill="#9467bd"/>
  <text x="310" y="165" font-size="13" fill="#9467bd">$E^*$</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">FWT: CE lies on the contract curve.</p>""",
        "examples": r"""<ul>
<li><strong>Commodity exchanges.</strong> Wheat, copper markets approximate FWT conditions.</li>
<li><strong>Electricity wholesale markets.</strong> Day-ahead markets clear at uniform prices.</li>
<li><strong>Online ad auctions.</strong> Real-time price-taking competition with allocative efficiency.</li>
<li><strong>Essay move.</strong> Doornik rewards essays distinguishing positive from normative content. Efficient, not equitable.</li>
<li><strong>Essay move.</strong> Walk through the proof: contradiction, local non-satiation, summing over agents.</li>
<li><strong>Limitation.</strong> FWT fails under externalities, public goods, asymmetric information, market incompleteness.</li>
<li>See also [[Concepts/Second Welfare Theorem]], [[Concepts/Competitive Equilibrium]].</li>
</ul>""",
    },
    "second-welfare-theorem": {
        "math": r"""<p><strong>Second Welfare Theorem</strong> (Arrow 1951, Debreu 1954): any Pareto-efficient allocation can be supported as a CE with appropriate lump-sum transfers, provided preferences are convex and continuous.</p>

<ol>
<li>Construct "better" sets $B_i = \{x_i : u_i(x_i) > u_i(x_i^*)\}$. Convex by convexity of preferences.</li>
<li>Aggregate $B = \sum_i B_i$ is convex.</li>
<li>By separating-hyperplane theorem, there exists $p^*$ such that $p^* \cdot x > p^* \cdot \omega$ for all $x \in B$.</li>
<li>Lump-sum transfers $T_i = p^* \cdot x_i^* - p^* \cdot \omega_i$ support $x_i^*$.</li>
</ol>

<p>Caveats:</p>

<p>(i) Lump-sum transfers usually infeasible.</p>

<p>(ii) Convexity is needed.</p>

<p>(iii) Theorem is non-constructive.</p>

<p>SWT is the formal basis for the equity-efficiency separation: markets handle efficiency, government handles distribution via lump-sum transfers.</p>

<p>Reference: Micro2025.pdf Topic 2 Lecture 2; Arrow 1951, Debreu 1954; Mas-Colell Ch. 16.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <rect x="80" y="40" width="440" height="240" fill="none" stroke="#333" stroke-width="2"/>
  <path d="M 120 60 Q 270 140 500 270" fill="none" stroke="#2ca02c" stroke-width="2"/>
  <text x="220" y="100" font-size="12" fill="#2ca02c">contract curve</text>
  <circle cx="200" cy="100" r="6" fill="#1f77b4"/>
  <text x="210" y="95" font-size="12" fill="#1f77b4">$E_1^*$</text>
  <circle cx="400" cy="200" r="6" fill="#d62728"/>
  <text x="410" y="195" font-size="12" fill="#d62728">$E_2^*$</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Each PE point is a CE for some redistribution.</p>""",
        "examples": r"""<ul>
<li><strong>Cap-and-rebate climate policy.</strong> Emission caps plus per-capita dividends approximate the SWT separation.</li>
<li><strong>Negative income taxes.</strong> Friedman's proposal of cash transfers leaves markets undistorted.</li>
<li><strong>Universal basic income.</strong> UBI separates redistribution from market prices.</li>
<li><strong>Essay move.</strong> Doornik rewards essays articulating the equity-efficiency separation.</li>
<li><strong>Essay move.</strong> Note the convexity assumption.</li>
<li><strong>Limitation.</strong> True lump-sum transfers are rare.</li>
<li>See also [[Concepts/First Welfare Theorem]], [[Concepts/Competitive Equilibrium]].</li>
</ul>""",
    },
    "social-welfare-functions": {
        "math": r"""<p>A <strong>social welfare function</strong> (SWF) aggregates individual utility profiles into a social ranking $W(u_1, \dots, u_I)$.</p>

<ol>
<li><strong>Utilitarian:</strong> $W = \sum_i u_i$.</li>
<li><strong>Weighted utilitarian:</strong> $W = \sum_i \alpha_i u_i$.</li>
<li><strong>Rawlsian:</strong> $W = \min_i u_i$.</li>
<li><strong>Atkinson:</strong> $W = \sum_i u_i^{1-\eta}/(1-\eta)$.</li>
</ol>

<p>FOC: planner equates marginal contribution to social welfare. For utilitarianism, $u_i'(x_i) = \lambda$, equalising marginal utility.</p>

<p>Arrow (1951) showed no SWF aggregates ordinal preferences consistently under reasonable axioms. With cardinal interpersonally comparable utilities, the impossibility is escaped.</p>

<p>UK Treasury uses inequality aversion 1 to 2 for CBA.</p>

<p>Reference: Micro2025.pdf Topic 2 Lecture 2-3; Atkinson 1970 JET; Sen "Collective Choice".</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <line x1="80" y1="260" x2="540" y2="260" stroke="#333"/>
  <line x1="80" y1="260" x2="80" y2="60" stroke="#333"/>
  <text x="540" y="280" font-size="13">$u_1$</text>
  <text x="60" y="70" font-size="13">$u_2$</text>
  <line x1="80" y1="80" x2="540" y2="240" stroke="#1f77b4" stroke-width="2"/>
  <text x="90" y="100" font-size="11" fill="#1f77b4">utilitarian</text>
  <path d="M 80 200 L 280 200 L 280 60" fill="none" stroke="#d62728" stroke-width="2"/>
  <text x="90" y="195" font-size="11" fill="#d62728">Rawlsian</text>
  <path d="M 80 60 Q 180 180 280 200 Q 400 220 540 240" fill="none" stroke="#2ca02c" stroke-width="2"/>
  <text x="350" y="180" font-size="11" fill="#2ca02c">Atkinson</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Iso-welfare curves under different SWFs.</p>""",
        "examples": r"""<ul>
<li><strong>UK Treasury Green Book.</strong> Uses Atkinson SWF with inequality aversion 1.0 to 1.5.</li>
<li><strong>Climate discounting.</strong> Nordhaus DICE uses utilitarian aggregation.</li>
<li><strong>Optimal income tax.</strong> Mirrlees (1971) characterises optimal schedule for any SWF.</li>
<li><strong>Essay move.</strong> Doornik rewards essays showing SWF choice affects optimal policy.</li>
<li><strong>Essay move.</strong> Address Arrow's impossibility: SWFs require cardinal utility.</li>
<li><strong>Limitation.</strong> SWFs rely on interpersonal utility comparisons.</li>
<li>See also [[Concepts/Arrow's Impossibility Theorem]], [[Concepts/Utilitarian Planner]].</li>
</ul>""",
    },
    "utilitarian-planner": {
        "math": r"""<p>The <strong>utilitarian planner</strong> maximises $W = \sum_i u_i(x_i)$ subject to feasibility. FOC: $u_i'(x_i^*) = \lambda$ for all $i$.</p>

<ol>
<li>$\max \sum_i u_i(x_i)$ subject to $\sum_i x_i \leq E$.</li>
<li>FOC: equal marginal utility across individuals.</li>
<li>Identical preferences plus diminishing MU: $x_i^* = E/I$ (perfect equality).</li>
<li>Different preferences: higher-MU individuals receive more.</li>
</ol>

<p>Limitations:</p>

<p>(i) Interpersonal utility comparison required.</p>

<p>(ii) Utility monsters: extreme MU/resource ratios receive disproportionate resources.</p>

<p>(iii) Distributional insensitivity within fixed total utility.</p>

<p>CBA implicitly uses utilitarianism. Sen's capability approach is an alternative.</p>

<p>Reference: Micro2025.pdf Topic 2 Lecture 3; Bentham 1789; Mas-Colell Ch. 22.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <line x1="80" y1="260" x2="540" y2="260" stroke="#333"/>
  <line x1="80" y1="260" x2="80" y2="60" stroke="#333"/>
  <text x="540" y="280" font-size="13">$x$</text>
  <text x="60" y="70" font-size="13">$u'(x)$</text>
  <path d="M 80 80 Q 200 180 540 240" fill="none" stroke="#1f77b4" stroke-width="2"/>
  <line x1="80" y1="180" x2="540" y2="180" stroke="#d62728" stroke-width="2" stroke-dasharray="3 3"/>
  <text x="450" y="170" font-size="12" fill="#d62728">$\lambda$ common</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Utilitarian: equalise marginal utility.</p>""",
        "examples": r"""<ul>
<li><strong>UK climate damage assessment.</strong> Treasury Green Book aggregates household consumption.</li>
<li><strong>Mirrlees optimal taxation.</strong> Utilitarian SWF gives high top marginal tax rates.</li>
<li><strong>CBA.</strong> Implicitly utilitarian without inequality weights.</li>
<li><strong>Essay move.</strong> Doornik rewards essays deriving the equal-marginal-utility condition.</li>
<li><strong>Essay move.</strong> Critique on distributional insensitivity.</li>
<li><strong>Limitation.</strong> Requires interpersonal comparison and cardinal utility.</li>
<li>See also [[Concepts/Rawlsian Planner]], [[Concepts/Social Welfare Functions]].</li>
</ul>""",
    },
    "rawlsian-planner": {
        "math": r"""<p>The <strong>Rawlsian planner</strong> maximises $W = \min_i u_i(x_i)$. FOC equalises utility across individuals.</p>

<ol>
<li>$\max \min_i u_i(x_i)$ subject to $\sum_i x_i \leq E$.</li>
<li>Interior optimum: $u_i(x_i^*) = U^*$ for all $i$.</li>
<li>Identical preferences: $x_i^* = E/I$.</li>
<li>Different preferences: less productive individuals receive more.</li>
</ol>

<p>Rawls (1971) derived this from the "veil of ignorance": rational choice without knowing one's social position would adopt maximin.</p>

<p>Comparison with utilitarianism:</p>

<p>(i) Equality in identical-preference cases.</p>

<p>(ii) Productivity differences: Rawlsian gives more to less productive.</p>

<p>(iii) Behavioural responses: high-earners may reduce effort. Mirrlees (1971) shows optimal Rawlsian tax has 100% rate on top.</p>

<p>Sen (1974): maximin insensitive to gains above the worst-off. Atkinson generalises.</p>

<p>Reference: Micro2025.pdf Topic 2 Lecture 3; Rawls 1971; Sen "Collective Choice".</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <line x1="80" y1="260" x2="540" y2="260" stroke="#333"/>
  <line x1="80" y1="260" x2="80" y2="60" stroke="#333"/>
  <text x="540" y="280" font-size="13">$u_1$</text>
  <text x="60" y="70" font-size="13">$u_2$</text>
  <path d="M 80 100 L 200 100 L 200 260" fill="none" stroke="#d62728" stroke-width="2"/>
  <path d="M 80 200 L 300 200 L 300 100" fill="none" stroke="#d62728" stroke-width="2"/>
  <line x1="80" y1="260" x2="540" y2="60" stroke="#888" stroke-width="1" stroke-dasharray="3 3"/>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Rawlsian iso-welfare curves are right-angled.</p>""",
        "examples": r"""<ul>
<li><strong>UBI proposals.</strong> Draw on Rawlsian intuitions.</li>
<li><strong>Minimum wage and welfare-state design.</strong> Rawlsian thinking supports floors.</li>
<li><strong>Disability policy.</strong> Differential support for greater needs.</li>
<li><strong>Essay move.</strong> Doornik rewards essays comparing Rawlsian to utilitarian on worked examples.</li>
<li><strong>Essay move.</strong> Use veil-of-ignorance argument.</li>
<li><strong>Limitation.</strong> Maximin insensitive to gains above worst-off.</li>
<li>See also [[Concepts/Utilitarian Planner]], [[Concepts/Social Welfare Functions]].</li>
</ul>""",
    },
    "kaldor-hicks-compensation": {
        "math": r"""<p>The <strong>Kaldor-Hicks criterion</strong> extends Pareto. $A$ K-H-dominates $B$ if winners could hypothetically compensate losers.</p>

<p>Formally: there exists transfers $(t_i)$ with $\sum_i t_i = 0$ such that $(x_i^A + t_i)$ is a Pareto improvement over $(x_i^B)$.</p>

<ol>
<li>Compute welfare gain (CV or EV) for each winner and loss for each loser.</li>
<li>If gains exceed losses, $A$ K-H-dominates $B$.</li>
<li>Compensation hypothetical, need not be paid.</li>
</ol>

<p>Under quasi-linear utility: $\Delta CS + \Delta PS > 0$. Standard CBA criterion.</p>

<p>Scitovsky (1941) critique: K-H can give inconsistent rankings. Double criterion resolves but is demanding.</p>

<p>K-H remains the default in applied welfare economics.</p>

<p>Reference: Micro2025.pdf Topic 2 Lecture on Welfare; Kaldor 1939, Hicks 1939, Scitovsky 1941.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <line x1="80" y1="260" x2="540" y2="260" stroke="#333"/>
  <line x1="80" y1="260" x2="80" y2="60" stroke="#333"/>
  <circle cx="200" cy="180" r="6" fill="#d62728"/>
  <text x="180" y="200" font-size="12" fill="#d62728">$B$</text>
  <circle cx="300" cy="120" r="6" fill="#1f77b4"/>
  <text x="310" y="115" font-size="12" fill="#1f77b4">$A$</text>
  <circle cx="240" cy="140" r="6" fill="#2ca02c"/>
  <text x="250" y="135" font-size="12" fill="#2ca02c">$A$ + transfers</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">K-H: hypothetical compensation makes losers indifferent.</p>""",
        "examples": r"""<ul>
<li><strong>NAFTA CBA.</strong> Trade liberalisation produced aggregate gains exceeding losses.</li>
<li><strong>Road infrastructure.</strong> K-H-dominates if user-time savings exceed displacement costs.</li>
<li><strong>Pollution regulations.</strong> EPA applies K-H.</li>
<li><strong>Essay move.</strong> Doornik rewards essays contrasting K-H to Pareto.</li>
<li><strong>Essay move.</strong> Cite Scitovsky's reversal paradox.</li>
<li><strong>Limitation.</strong> Hypothetical compensation may not be ethically equivalent.</li>
<li>See also [[Concepts/Pareto Criterion]], [[Concepts/Compensating Variation]].</li>
</ul>""",
    },
    "contract-curve": {
        "math": r"""<p>The <strong>contract curve</strong> is the locus of Pareto-efficient allocations in an Edgeworth box. Algebraically: $MRS_A = MRS_B$.</p>

<ol>
<li>Compute MRS for each consumer.</li>
<li>Substitute feasibility to eliminate $B$'s bundle.</li>
<li>Set $MRS_A = MRS_B$ and solve for the locus.</li>
</ol>

<p>For Cobb-Douglas with different exponents, the contract curve is interior and curved.</p>

<p>Endpoints are the origins: at $O_A$, $A$ has nothing and $B$ has everything.</p>

<p>FWT: CE lies on the contract curve. SWT: every contract-curve point is a CE for some endowment.</p>

<p>Reference: Micro2025.pdf Topic 2 Lecture 1; Varian Ch. 17.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <rect x="80" y="40" width="440" height="240" fill="none" stroke="#333" stroke-width="2"/>
  <path d="M 80 200 Q 200 180 300 140 Q 400 110 520 80" fill="none" stroke="#1f77b4" stroke-width="2"/>
  <path d="M 80 130 Q 200 160 300 200 Q 400 230 520 250" fill="none" stroke="#d62728" stroke-width="2"/>
  <path d="M 100 60 Q 250 140 510 270" fill="none" stroke="#2ca02c" stroke-width="3"/>
  <text x="280" y="100" font-size="13" fill="#2ca02c" font-weight="bold">contract curve</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Locus of indifference-curve tangencies.</p>""",
        "examples": r"""<ul>
<li><strong>Two-person trade.</strong> Voluntary trade moves toward the contract curve.</li>
<li><strong>Marriage and household allocation.</strong> Becker (1981).</li>
<li><strong>International trade.</strong> Free trade pushes allocations to world contract curve.</li>
<li><strong>Essay move.</strong> Doornik likes essays deriving the contract curve from FOC tangency.</li>
<li><strong>Essay move.</strong> Connect to welfare theorems.</li>
<li><strong>Limitation.</strong> Symmetric treatment ignores distributional fairness.</li>
<li>See also [[Concepts/Pareto Efficiency]], [[Concepts/Edgeworth Box]].</li>
</ul>""",
    },
    "utility-possibility-frontier": {
        "math": r"""<p>The <strong>utility possibility frontier</strong> (UPF) is the locus of utility profiles achievable by Pareto-efficient allocations. The image of the contract curve in utility space.</p>

<ol>
<li>Parameterise the contract curve.</li>
<li>Compute $u_1, u_2$ at each point.</li>
<li>Plot $(u_1, u_2)$ pairs.</li>
</ol>

<p>Quasi-linear utility gives a straight-line UPF.</p>

<p>Planner maximises SWF subject to UPF. Tangency at optimum.</p>

<p>Special cases: utilitarian (slope $-1$), Rawlsian ($u_1 = u_2$), Atkinson (interior).</p>

<p>Visualises equity-efficiency trade-off.</p>

<p>Reference: Micro2025.pdf Topic 2 Lecture 2; Mas-Colell Ch. 22.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <line x1="80" y1="260" x2="540" y2="260" stroke="#333"/>
  <line x1="80" y1="260" x2="80" y2="60" stroke="#333"/>
  <path d="M 80 80 Q 200 100 300 140 Q 400 200 540 260" fill="none" stroke="#1f77b4" stroke-width="2"/>
  <text x="100" y="100" font-size="12" fill="#1f77b4">UPF</text>
  <line x1="80" y1="200" x2="540" y2="80" stroke="#d62728" stroke-width="1" stroke-dasharray="3 3"/>
  <circle cx="250" cy="125" r="6" fill="#2ca02c"/>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">UPF: tangency with SWF gives the social optimum.</p>""",
        "examples": r"""<ul>
<li><strong>Optimal taxation.</strong> Mirrlees maps UPF, then maximises SWF.</li>
<li><strong>International redistribution.</strong> Cross-country UPF informs aid policy.</li>
<li><strong>Climate distributional analysis.</strong> Carbon tax-and-rebate via UPF.</li>
<li><strong>Essay move.</strong> Doornik rewards essays distinguishing UPF from SWF.</li>
<li><strong>Essay move.</strong> Movement along UPF is pure redistribution.</li>
<li><strong>Limitation.</strong> Constructing UPF requires complete information.</li>
<li>See also [[Concepts/Contract Curve]], [[Concepts/Social Welfare Functions]].</li>
</ul>""",
    },
    "compensating-variation": {
        "math": r"""<p><strong>Compensating variation</strong> (CV): wealth change needed to restore original utility after a price change.</p>

$$CV = e(p^1, u^0) - w = e(p^1, u^0) - e(p^0, u^0).$$

<ol>
<li>Identify $u^0 = v(p^0, w)$.</li>
<li>Compute $e(p^1, u^0)$.</li>
<li>$CV = e(p^1, u^0) - w$.</li>
</ol>

<p>Equivalent: $CV = \int_{p^0}^{p^1} h(p, u^0) dp$, area to left of Hicksian demand at initial utility.</p>

<p>Comparison: EV uses post-change utility; $\Delta CS$ uses Marshallian. Quasi-linear: $CV = EV = \Delta CS$.</p>

<p>Reference: Micro2025.pdf Topic 2 Lecture 3; Varian Ch. 10.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <line x1="80" y1="260" x2="540" y2="260" stroke="#333"/>
  <line x1="80" y1="260" x2="80" y2="60" stroke="#333"/>
  <line x1="80" y1="80" x2="540" y2="240" stroke="#1f77b4" stroke-width="2"/>
  <text x="430" y="100" font-size="12" fill="#1f77b4">Hicksian</text>
  <line x1="80" y1="140" x2="540" y2="140" stroke="#666" stroke-width="1" stroke-dasharray="2 2"/>
  <text x="540" y="135" font-size="11" fill="#666">$p^1$</text>
  <line x1="80" y1="200" x2="540" y2="200" stroke="#666" stroke-width="1" stroke-dasharray="2 2"/>
  <text x="540" y="215" font-size="11" fill="#666">$p^0$</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">CV: area to left of Hicksian at initial utility.</p>""",
        "examples": r"""<ul>
<li><strong>Tax welfare cost.</strong> CV measures wealth needed to compensate.</li>
<li><strong>Climate policy CBA.</strong> CV of carbon tax measures household burden.</li>
<li><strong>Energy price subsidies.</strong> CV computes welfare gain.</li>
<li><strong>Essay move.</strong> Doornik rewards distinguishing CV, EV, CS.</li>
<li><strong>Essay move.</strong> Quasi-linear gives equivalence.</li>
<li><strong>Limitation.</strong> Reference utility choice is path-dependent.</li>
<li>See also [[Concepts/Equivalent Variation]], [[Concepts/Hicksian Demand]].</li>
</ul>""",
    },
    "equivalent-variation": {
        "math": r"""<p><strong>Equivalent variation</strong> (EV): wealth change at original prices giving the same utility as the price change.</p>

$$EV = e(p^0, u^1) - w = e(p^0, u^1) - e(p^0, u^0).$$

<ol>
<li>Compute $u^1 = v(p^1, w)$.</li>
<li>Compute $e(p^0, u^1)$.</li>
<li>$EV = e(p^0, u^1) - w$.</li>
</ol>

<p>$EV = \int_{p^0}^{p^1} h(p, u^1) dp$, Hicksian at new utility.</p>

<p>For normal good and price increase: $EV < CS < CV$.</p>

<p>EV common in policy-reform CBA; CV common in taxation capacity.</p>

<p>Reference: Micro2025.pdf Topic 2 Lecture 3; Varian Ch. 10.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <line x1="80" y1="260" x2="540" y2="260" stroke="#333"/>
  <line x1="80" y1="260" x2="80" y2="60" stroke="#333"/>
  <line x1="80" y1="100" x2="540" y2="260" stroke="#1f77b4" stroke-width="2"/>
  <text x="430" y="280" font-size="12" fill="#1f77b4">Hicksian at $u^1$</text>
  <line x1="80" y1="80" x2="540" y2="240" stroke="#888" stroke-width="2" stroke-dasharray="3 3"/>
  <text x="430" y="100" font-size="12" fill="#888">Hicksian at $u^0$</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">EV uses Hicksian at final utility.</p>""",
        "examples": r"""<ul>
<li><strong>Tariff reform.</strong> EV evaluates trade-policy welfare.</li>
<li><strong>VAT changes.</strong> Treasury uses EV for distributional impact.</li>
<li><strong>Subsidy evaluation.</strong> EV measures cash-equivalent gain.</li>
<li><strong>Essay move.</strong> Doornik likes essays deriving EV from expenditure function.</li>
<li><strong>Essay move.</strong> Distinguish EV from CV.</li>
<li><strong>Limitation.</strong> EV requires post-policy utility.</li>
<li>See also [[Concepts/Compensating Variation]], [[Concepts/Consumer Surplus]].</li>
</ul>""",
    },
    "consumer-surplus": {
        "math": r"""<p><strong>Consumer surplus</strong> (Marshall 1890): area between Marshallian demand and price.</p>

$$\Delta CS = -\int_{p^0}^{p^1} x(p) dp.$$

<ol>
<li>Identify Marshallian demand.</li>
<li>Integrate between prices.</li>
<li>Result is change in CS.</li>
</ol>

<p>Widely used because computable from observable data. Quasi-linear: exact equal to CV and EV.</p>

<p>Willig (1976): bounds CS approximation by half income elasticity times relative price change.</p>

<p>Sum of CS+PS is standard CBA metric.</p>

<p>Reference: Micro2025.pdf Topic 2 Lecture 3; Marshall; Willig 1976.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <line x1="80" y1="260" x2="540" y2="260" stroke="#333"/>
  <line x1="80" y1="260" x2="80" y2="60" stroke="#333"/>
  <line x1="80" y1="80" x2="540" y2="280" stroke="#1f77b4" stroke-width="2"/>
  <text x="430" y="100" font-size="12" fill="#1f77b4">demand</text>
  <line x1="80" y1="180" x2="540" y2="180" stroke="#666" stroke-width="1" stroke-dasharray="3 3"/>
  <polygon points="80,80 80,180 360,180" fill="#a7f3d0" fill-opacity="0.5" stroke="#10b981"/>
  <text x="180" y="150" font-size="14" fill="#10b981">CS</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Triangular area between demand and price.</p>""",
        "examples": r"""<ul>
<li><strong>Internet valuation.</strong> Brynjolfsson et al. (2019) estimate CS in thousands per household.</li>
<li><strong>Transport CBA.</strong> UK DfT primary metric.</li>
<li><strong>Public-good valuation.</strong> Contingent valuation.</li>
<li><strong>Essay move.</strong> Doornik rewards essays noting CS is exact only under quasi-linearity.</li>
<li><strong>Essay move.</strong> Use Willig bounds.</li>
<li><strong>Limitation.</strong> Aggregation implicitly assumes equal social weights.</li>
<li>See also [[Concepts/Marshallian Demand]], [[Concepts/Compensating Variation]].</li>
</ul>""",
    },
    "deadweight-loss": {
        "math": r"""<p><strong>Deadweight loss</strong> (DWL): welfare loss not captured as revenue or transfer.</p>

$$DWL = \frac{1}{2} t \cdot \Delta Q,$$

<p>area of Harberger triangle between demand and supply.</p>

<ol>
<li>Pre-tax equilibrium $p^* Q^*$.</li>
<li>Tax $t$ drives wedge; new quantity $Q^t < Q^*$.</li>
<li>Revenue $R = t Q^t$.</li>
<li>DWL = original surplus minus new surplus minus revenue.</li>
</ol>

<p>Properties: quadratic in tax rate; increasing in elasticities. Foundation for Ramsey rules.</p>

<p>Feldstein (1995) estimates US income tax DWL at 30-50% of revenue.</p>

<p>Reference: Micro2025.pdf Topic 2 Lecture 4; Ramsey 1927; Harberger 1964.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <line x1="80" y1="260" x2="540" y2="260" stroke="#333"/>
  <line x1="80" y1="260" x2="80" y2="60" stroke="#333"/>
  <line x1="80" y1="80" x2="540" y2="260" stroke="#1f77b4" stroke-width="2"/>
  <line x1="80" y1="260" x2="540" y2="100" stroke="#d62728" stroke-width="2"/>
  <polygon points="220,160 320,170 220,180" fill="#ffd2c2" stroke="#dc2626"/>
  <text x="240" y="190" font-size="12" fill="#dc2626">DWL</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Harberger triangle.</p>""",
        "examples": r"""<ul>
<li><strong>Income tax.</strong> Feldstein (1995) 30-50% of revenue.</li>
<li><strong>Tariff.</strong> Krugman triangles in trade.</li>
<li><strong>Rent control.</strong> Glaeser-Luttmer (2003) on NYC.</li>
<li><strong>Essay move.</strong> Doornik rewards essays deriving DWL as quadratic in tax rate.</li>
<li><strong>Essay move.</strong> Apply inverse elasticity rule.</li>
<li><strong>Limitation.</strong> Dynamic effects can amplify.</li>
<li>See also [[Concepts/Consumer Surplus]], [[Concepts/Ramsey Taxation]].</li>
</ul>""",
    },
    "ramsey-taxation": {
        "math": r"""<p><strong>Ramsey taxation</strong> (1927) minimises DWL subject to revenue. <strong>Inverse elasticity rule</strong>:</p>

$$\frac{t_i/p_i}{\epsilon_i^c} = \text{constant}.$$

<ol>
<li>Planner minimises DWL subject to revenue.</li>
<li>FOC via Slutsky.</li>
<li>$t_i^*/p_i$ inversely proportional to compensated elasticity.</li>
</ol>

<p>Implications: necessities taxed more (regressive); leisure-complements taxed more.</p>

<p>Atkinson-Stiglitz (1976): under separable utility plus non-linear income tax, commodity taxation should be uniform.</p>

<p>UK VAT reflects Ramsey: zero on food, 5% on fuel, 20% otherwise.</p>

<p>Reference: Micro2025.pdf Topic 2 Lecture 4; Ramsey 1927; Atkinson-Stiglitz 1976.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <line x1="80" y1="260" x2="540" y2="260" stroke="#333"/>
  <line x1="80" y1="260" x2="80" y2="60" stroke="#333"/>
  <text x="540" y="280" font-size="13">$\epsilon^c$</text>
  <text x="60" y="70" font-size="13">$t^*/p$</text>
  <path d="M 100 80 Q 250 180 540 240" fill="none" stroke="#1f77b4" stroke-width="2"/>
  <text x="100" y="120" font-size="12" fill="#1f77b4">$t^*/p \propto 1/\epsilon^c$</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Tax falls with compensated elasticity.</p>""",
        "examples": r"""<ul>
<li><strong>UK VAT.</strong> Zero on food, reduced on fuel, full elsewhere.</li>
<li><strong>Excise taxes.</strong> Alcohol, tobacco, petrol with inelastic demand.</li>
<li><strong>Pigouvian-Ramsey hybrid.</strong> Sandmo (1975).</li>
<li><strong>Essay move.</strong> Doornik rewards deriving inverse elasticity rule.</li>
<li><strong>Essay move.</strong> Invoke Atkinson-Stiglitz.</li>
<li><strong>Limitation.</strong> Distributional impacts ignored in pure Ramsey.</li>
<li>See also [[Concepts/Deadweight Loss]], [[Concepts/Hicksian Demand]].</li>
</ul>""",
    },
    "expenditure-function": {
        "math": r"""<p>The <strong>expenditure function</strong> $e(p, u) = \min_x p \cdot x$ s.t. $u(x) \geq u$. Minimum wealth to reach utility $u$.</p>

<ol>
<li>Homogeneous degree 1 in $p$.</li>
<li>Increasing in $u$.</li>
<li>Concave in $p$.</li>
<li>Continuous and differentiable.</li>
</ol>

<p><strong>Shephard's lemma:</strong> $\partial e/\partial p_i = h_i$, Hicksian demand.</p>

<p>Duality: $e(p, v(p, w)) = w$, $v(p, e(p, u)) = u$.</p>

<p>Slutsky: $\partial x_i/\partial p_j = \partial h_i/\partial p_j - x_j \partial x_i/\partial w$.</p>

<p>Used for welfare measurement, tax incidence, cost-of-living indices.</p>

<p>Cobb-Douglas: $e(p_x, p_y, u) = u (p_x/\alpha)^\alpha (p_y/(1-\alpha))^{1-\alpha}$.</p>

<p>Reference: Micro2025.pdf Topic 2 Lecture 3; Varian Ch. 7.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <line x1="80" y1="260" x2="540" y2="260" stroke="#333"/>
  <line x1="80" y1="260" x2="80" y2="60" stroke="#333"/>
  <path d="M 100 240 Q 200 160 540 80" fill="none" stroke="#1f77b4" stroke-width="2"/>
  <text x="100" y="120" font-size="12" fill="#1f77b4">$e(p, u)$ concave</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Concave in prices, increasing in utility.</p>""",
        "examples": r"""<ul>
<li><strong>Cost-of-living indices.</strong> Konus indices ratio of expenditure functions.</li>
<li><strong>Welfare-of-policy.</strong> CV, EV rely on $e(p, u)$.</li>
<li><strong>Tax incidence.</strong> Compensated demand via Shephard's lemma.</li>
<li><strong>Essay move.</strong> Doornik rewards proving Shephard's lemma.</li>
<li><strong>Essay move.</strong> Use duality identities.</li>
<li><strong>Limitation.</strong> Binding constraints can create kinks.</li>
<li>See also [[Concepts/Hicksian Demand]], [[Concepts/Compensating Variation]].</li>
</ul>""",
    },
    "marshallian-demand": {
        "math": r"""<p><strong>Marshallian demand</strong> $x(p, w) = \arg\max_x u(x)$ subject to $p \cdot x \leq w$.</p>

<ol>
<li>Homogeneous degree 0 in $(p, w)$.</li>
<li>Walras' law: $p \cdot x(p, w) = w$.</li>
<li>Slutsky symmetry.</li>
<li>Negative semidefinite Slutsky matrix.</li>
</ol>

<p>Slutsky decomposition:</p>

$$\frac{\partial x_i}{\partial p_j} = \frac{\partial h_i}{\partial p_j} - x_j \frac{\partial x_i}{\partial w}.$$

<p>Income effects: normal ($\partial x/\partial w > 0$), inferior, Giffen.</p>

<p>Estimation: AIDS (Deaton-Muellbauer 1980), translog, LES.</p>

<p>Observable; Hicksian is recovered via duality.</p>

<p>Reference: Micro2025.pdf Topic 2 Lecture 3; Varian Ch. 5-7.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <line x1="80" y1="260" x2="540" y2="260" stroke="#333"/>
  <line x1="80" y1="260" x2="80" y2="60" stroke="#333"/>
  <path d="M 80 80 Q 200 130 540 240" fill="none" stroke="#1f77b4" stroke-width="2"/>
  <text x="430" y="220" font-size="12" fill="#1f77b4">Marshallian</text>
  <line x1="80" y1="80" x2="540" y2="220" stroke="#888" stroke-width="2" stroke-dasharray="3 3"/>
  <text x="430" y="115" font-size="12" fill="#888">Hicksian</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Marshallian = Hicksian + income effect.</p>""",
        "examples": r"""<ul>
<li><strong>Food demand systems.</strong> AIDS models.</li>
<li><strong>Tax simulation.</strong> Welfare effects of commodity tax.</li>
<li><strong>Trade-policy.</strong> Tariff incidence.</li>
<li><strong>Essay move.</strong> Doornik rewards deriving from FOC.</li>
<li><strong>Essay move.</strong> Slutsky decomposition.</li>
<li><strong>Limitation.</strong> Estimation needs exogeneity.</li>
<li>See also [[Concepts/Hicksian Demand]], [[Concepts/Consumer Surplus]].</li>
</ul>""",
    },

    "social-discount-rate": {
        "math": r"""<p>The <strong>social discount rate</strong> (SDR) discounts future welfare in cost-benefit analysis. The Ramsey rule decomposes SDR as $r = \rho + \eta g$, where $\rho$ is pure time preference, $\eta$ is inequality aversion, and $g$ is expected per-capita consumption growth.</p>

<ol>
<li>$\rho$: utility weight of future generations versus current.</li>
<li>$\eta$: elasticity of marginal utility of consumption (inequality aversion).</li>
<li>$g$: forecast growth rate; high $g$ raises $r$ via wealth-effect logic.</li>
</ol>

<p>UK Treasury Green Book uses $r = 3.5\%$ for short horizons, declining for very long horizons. Stern Review (2007) used $\rho = 0.1\%$, $\eta = 1$, giving $r \approx 1.4\%$. Nordhaus uses higher $\rho$ giving $r \approx 4\%$.</p>

<p>SDR matters enormously for climate policy: a 1% change in $r$ can double or halve the present-value cost of climate damages 100 years out.</p>

<p>Reference: Micro2025.pdf Topic 2 Lecture on CBA; Ramsey 1928; Stern Review 2007; Nordhaus 2008.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <line x1="80" y1="260" x2="540" y2="260" stroke="#333"/>
  <line x1="80" y1="260" x2="80" y2="60" stroke="#333"/>
  <text x="540" y="280" font-size="13">years</text>
  <text x="60" y="70" font-size="13">PV factor</text>
  <path d="M 80 80 Q 200 150 540 240" fill="none" stroke="#1f77b4" stroke-width="2"/>
  <text x="100" y="100" font-size="12" fill="#1f77b4">$r = 1.4\%$ (Stern)</text>
  <path d="M 80 80 Q 200 220 540 250" fill="none" stroke="#d62728" stroke-width="2"/>
  <text x="100" y="200" font-size="12" fill="#d62728">$r = 4\%$ (Nordhaus)</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">SDR choice dramatically affects present value of long-horizon benefits.</p>""",
        "examples": r"""<ul>
<li><strong>Climate policy.</strong> Stern vs Nordhaus disagreement over carbon price driven largely by SDR.</li>
<li><strong>Infrastructure CBA.</strong> UK Treasury Green Book uses 3.5% declining schedule.</li>
<li><strong>Nuclear waste storage.</strong> Long-horizon discounting requires very low $r$ to keep PV non-trivial.</li>
<li><strong>Essay move.</strong> Doornik rewards essays distinguishing $\rho$ (ethical) from $\eta g$ (positive). The pure time preference debate is normative.</li>
<li><strong>Essay move.</strong> Cite hyperbolic discounting evidence (Laibson 1997) as challenging exponential SDR.</li>
<li><strong>Limitation.</strong> Constant $r$ over centuries is contestable. Declining discount rates (Weitzman 2001) reflect uncertainty about future $r$.</li>
<li>See also [[Concepts/Ramsey Equation]], [[Concepts/Cost-Benefit Analysis]].</li>
</ul>""",
    },
    "ramsey-equation": {
        "math": r"""<p>The <strong>Ramsey equation</strong> for the social discount rate:</p>

$$r = \rho + \eta g,$$

<p>where $\rho$ is the pure rate of time preference, $\eta$ is the elasticity of marginal utility of consumption, and $g$ is the growth rate of per-capita consumption.</p>

<p>Derivation: a planner maximises $\int_0^\infty e^{-\rho t} u(c_t) dt$ subject to a resource constraint. The Euler equation gives:</p>

$$\frac{\dot c}{c} = \frac{r - \rho}{\eta},$$

<p>rearranged to $r = \rho + \eta g$ along a balanced growth path.</p>

<ol>
<li>$\rho$ reflects pure impatience or the value placed on future welfare.</li>
<li>$\eta$ captures inequality aversion across consumption levels.</li>
<li>$g$ is the expected growth rate of per-capita consumption.</li>
</ol>

<p>For Stern (2007): $\rho = 0.1\%$, $\eta = 1$, $g \approx 1.3\%$, giving $r \approx 1.4\%$. Nordhaus uses higher $\rho$ (around 1.5%), giving $r \approx 4\%$.</p>

<p>The equation links the SDR to fundamental parameters that can in principle be calibrated. The choice of $\rho$ is the most contested: should we weight future generations less?</p>

<p>Reference: Micro2025.pdf Topic 2 Lecture on CBA; Ramsey 1928 EJ; Nordhaus 2007.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <text x="60" y="60" font-size="14" font-weight="bold">$r = \rho + \eta g$</text>
  <rect x="100" y="100" width="80" height="40" fill="#1f77b4"/>
  <text x="140" y="125" font-size="13" text-anchor="middle" fill="#fff">$\rho$ (pure time pref)</text>
  <text x="200" y="125" font-size="14">+</text>
  <rect x="220" y="100" width="80" height="40" fill="#d62728"/>
  <text x="260" y="125" font-size="13" text-anchor="middle" fill="#fff">$\eta$ (aversion)</text>
  <text x="320" y="125" font-size="14">$\times$</text>
  <rect x="340" y="100" width="80" height="40" fill="#2ca02c"/>
  <text x="380" y="125" font-size="13" text-anchor="middle" fill="#fff">$g$ (growth)</text>
  <text x="440" y="125" font-size="14">=</text>
  <rect x="460" y="100" width="80" height="40" fill="#9467bd"/>
  <text x="500" y="125" font-size="13" text-anchor="middle" fill="#fff">$r$ (SDR)</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Decomposition of the SDR into time preference and growth-adjusted wealth effect.</p>""",
        "examples": r"""<ul>
<li><strong>Stern Review (2007).</strong> Low $\rho$ delivers high carbon price recommendation.</li>
<li><strong>Nordhaus DICE.</strong> Higher $\rho$ delivers lower optimal carbon price.</li>
<li><strong>Pension policy.</strong> Calibrating intergenerational transfers depends on $\eta$.</li>
<li><strong>Essay move.</strong> Doornik likes essays deriving Ramsey from the consumption Euler equation.</li>
<li><strong>Essay move.</strong> Compare Stern and Nordhaus parameter choices.</li>
<li><strong>Limitation.</strong> Assumes balanced growth and CRRA utility.</li>
<li>See also [[Concepts/Social Discount Rate]], [[Concepts/Cost-Benefit Analysis]].</li>
</ul>""",
    },
    "majority-rule": {
        "math": r"""<p><strong>Majority rule</strong> selects the alternative preferred by more than half of voters in pairwise comparison. With $n$ voters and $k$ alternatives, a Condorcet winner is an alternative that beats every other alternative in pairwise majority votes.</p>

<ol>
<li>Each voter ranks alternatives.</li>
<li>For each pair, count voters preferring each alternative.</li>
<li>An alternative is a Condorcet winner if it beats every other in pairwise vote.</li>
</ol>

<p>Properties:</p>

<p>(i) Decisive in two-alternative cases.</p>

<p>(ii) Anonymous (treats all voters symmetrically).</p>

<p>(iii) Neutral (treats alternatives symmetrically).</p>

<p>(iv) Vulnerable to Condorcet cycles: $A$ beats $B$, $B$ beats $C$, $C$ beats $A$. With three or more alternatives and unrestricted preferences, cycles are possible.</p>

<p>May's theorem (1952): majority rule is the unique social choice rule satisfying anonymity, neutrality, and positive responsiveness in two-alternative settings.</p>

<p>Single-peaked preferences (Black 1948) rule out cycles: the Condorcet winner is the median voter's preferred alternative.</p>

<p>Reference: Micro2025.pdf Topic 2 Lecture on Social Choice; May 1952; Black 1948.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <text x="60" y="40" font-size="14" font-weight="bold">Condorcet cycle example</text>
  <text x="80" y="80" font-size="13">Voter 1: A &gt; B &gt; C</text>
  <text x="80" y="105" font-size="13">Voter 2: B &gt; C &gt; A</text>
  <text x="80" y="130" font-size="13">Voter 3: C &gt; A &gt; B</text>
  <text x="80" y="170" font-size="13" fill="#d62728">A vs B: A wins (1, 3)</text>
  <text x="80" y="195" font-size="13" fill="#d62728">B vs C: B wins (1, 2)</text>
  <text x="80" y="220" font-size="13" fill="#d62728">C vs A: C wins (2, 3)</text>
  <text x="80" y="260" font-size="13" fill="#1f77b4">Cycle: A &gt; B &gt; C &gt; A</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Condorcet cycle: no alternative beats all others in pairwise vote.</p>""",
        "examples": r"""<ul>
<li><strong>UK referendum on EU membership.</strong> Single-question majority votes are decisive but vulnerable to agenda manipulation.</li>
<li><strong>Committee voting.</strong> Pairwise votes on amendments can produce different outcomes depending on the order.</li>
<li><strong>Plurality vs majority.</strong> US Electoral College uses plurality; some voting systems use majority runoff.</li>
<li><strong>Essay move.</strong> Doornik rewards essays distinguishing majority from plurality. May's theorem axiomatises majority rule.</li>
<li><strong>Essay move.</strong> Condorcet cycles are central. Single-peaked preferences rule them out (Black 1948).</li>
<li><strong>Limitation.</strong> Majority rule can produce cycles, manipulation through agenda-setting (McKelvey 1976), and tyranny-of-majority outcomes.</li>
<li>See also [[Concepts/Condorcet Paradox]], [[Concepts/Median Voter Theorem]].</li>
</ul>""",
    },
    "borda-count": {
        "math": r"""<p>The <strong>Borda count</strong> (Borda 1781) assigns points to alternatives based on rank position. With $k$ alternatives, the top-ranked gets $k-1$ points, second-ranked $k-2$, ..., last-ranked 0. Sum across voters; alternative with highest total wins.</p>

<ol>
<li>Each voter submits a ranked list.</li>
<li>For each alternative, sum points across voters.</li>
<li>Alternative with highest sum wins.</li>
</ol>

<p>Properties:</p>

<p>(i) Avoids Condorcet cycles by aggregating ranks rather than pairwise comparisons.</p>

<p>(ii) Sensitive to irrelevant alternatives: adding a new alternative can change the ranking among existing ones (violates Arrow's IIA).</p>

<p>(iii) Vulnerable to strategic voting: voters can manipulate rankings to favour their preferred alternative.</p>

<p>Sen (1970) shows Borda satisfies most desirable properties except IIA. Used in academic voting, sports rankings (Heisman Trophy, college football polls), and consensus-building.</p>

<p>Variant: <strong>positional voting</strong> with different weights $w_1 \geq w_2 \geq \dots \geq w_k = 0$. Borda is the linear special case. Plurality assigns $w_1 = 1, w_2 = \dots = w_k = 0$.</p>

<p>Reference: Micro2025.pdf Topic 2 Lecture on Social Choice; Borda 1781; Sen 1970.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <text x="60" y="40" font-size="14" font-weight="bold">Borda example (3 alternatives)</text>
  <text x="80" y="80" font-size="13">Voter 1: A=2, B=1, C=0</text>
  <text x="80" y="105" font-size="13">Voter 2: B=2, A=1, C=0</text>
  <text x="80" y="130" font-size="13">Voter 3: C=2, B=1, A=0</text>
  <text x="80" y="170" font-size="13" fill="#1f77b4">A: 2+1+0 = 3</text>
  <text x="80" y="195" font-size="13" fill="#1f77b4">B: 1+2+1 = 4 (winner)</text>
  <text x="80" y="220" font-size="13" fill="#1f77b4">C: 0+0+2 = 2</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Borda aggregates ranks; compromise candidates often win.</p>""",
        "examples": r"""<ul>
<li><strong>Heisman Trophy.</strong> Borda-like rule with top-3 ballots.</li>
<li><strong>Slovenia and Nauru elections.</strong> Both use modified Borda.</li>
<li><strong>Eurovision Song Contest.</strong> Modified Borda-like rule.</li>
<li><strong>Essay move.</strong> Doornik rewards essays comparing Borda to plurality and majority. Borda favours compromise candidates.</li>
<li><strong>Essay move.</strong> Borda violates Arrow's IIA: a new candidate can change the ranking.</li>
<li><strong>Limitation.</strong> Vulnerable to strategic voting; sensitive to candidate slate.</li>
<li>See also [[Concepts/Majority Rule]], [[Concepts/Arrow's Impossibility Theorem]].</li>
</ul>""",
    },
    "condorcet-paradox": {
        "math": r"""<p>The <strong>Condorcet paradox</strong>: pairwise majority votes can be cyclic, with $A$ beating $B$, $B$ beating $C$, and $C$ beating $A$. No alternative beats all others.</p>

<p>Classic example: three voters with preferences:</p>

<ol>
<li>Voter 1: $A > B > C$.</li>
<li>Voter 2: $B > C > A$.</li>
<li>Voter 3: $C > A > B$.</li>
</ol>

<p>Pairwise votes: $A$ beats $B$ (voters 1, 3), $B$ beats $C$ (voters 1, 2), $C$ beats $A$ (voters 2, 3). The collective preference is cyclic.</p>

<p>Implications:</p>

<p>(i) No Condorcet winner exists.</p>

<p>(ii) Pairwise voting outcomes depend on agenda. The first vote eliminates one alternative; whichever is eliminated affects which of the remaining two wins.</p>

<p>(iii) Agenda-setter has substantial power. McKelvey (1976) shows that with cyclic preferences, any alternative can be reached by a sufficiently clever agenda.</p>

<p>The Condorcet paradox is the simplest illustration of Arrow's impossibility theorem: aggregate preferences can be intransitive even when individual preferences are transitive.</p>

<p>Single-peaked preferences (Black 1948) rule out the paradox: along a single dimension, the median voter is the Condorcet winner.</p>

<p>Reference: Micro2025.pdf Topic 2 Lecture on Social Choice; Condorcet 1785; Black 1948.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <circle cx="200" cy="120" r="40" fill="#dbeafe" stroke="#1d4ed8"/>
  <text x="200" y="125" font-size="20" text-anchor="middle">A</text>
  <circle cx="400" cy="120" r="40" fill="#fee2e2" stroke="#dc2626"/>
  <text x="400" y="125" font-size="20" text-anchor="middle">B</text>
  <circle cx="300" cy="240" r="40" fill="#dcfce7" stroke="#16a34a"/>
  <text x="300" y="245" font-size="20" text-anchor="middle">C</text>
  <path d="M 240 120 L 360 120" stroke="#333" stroke-width="2" marker-end="url(#a3)"/>
  <text x="290" y="110" font-size="12" text-anchor="middle">beats</text>
  <path d="M 380 155 L 320 220" stroke="#333" stroke-width="2" marker-end="url(#a3)"/>
  <text x="380" y="200" font-size="12">beats</text>
  <path d="M 280 220 L 220 155" stroke="#333" stroke-width="2" marker-end="url(#a3)"/>
  <text x="200" y="200" font-size="12">beats</text>
  <defs><marker id="a3" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#333"/></marker></defs>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Cyclic majority: A beats B, B beats C, C beats A.</p>""",
        "examples": r"""<ul>
<li><strong>Committee voting on three options.</strong> Cycles common when preferences are heterogeneous.</li>
<li><strong>Legislative agenda manipulation.</strong> Strategic agenda-setting can produce desired outcomes under cycles.</li>
<li><strong>Tournaments.</strong> Round-robin sports can produce cyclic results (rock-paper-scissors structure).</li>
<li><strong>Essay move.</strong> Doornik rewards essays showing the simplest cyclic example. Use it to motivate Arrow.</li>
<li><strong>Essay move.</strong> Single-peaked preferences rule out cycles. Median voter theorem applies.</li>
<li><strong>Limitation.</strong> Cycles arise only under heterogeneous preferences. Random committees rarely cycle.</li>
<li>See also [[Concepts/Majority Rule]], [[Concepts/Arrow's Impossibility Theorem]], [[Concepts/Single-Peaked Preferences]].</li>
</ul>""",
    },
    "arrow-impossibility": {
        "math": r"""<p><strong>Arrow's Impossibility Theorem</strong> (1951): no social welfare function can aggregate individual ordinal preferences into a social ordering while satisfying all four axioms:</p>

<ol>
<li><strong>Unrestricted domain (U):</strong> all logically possible preference profiles are admissible.</li>
<li><strong>Pareto (P):</strong> if everyone prefers $a$ to $b$, the social ordering ranks $a$ above $b$.</li>
<li><strong>Independence of Irrelevant Alternatives (IIA):</strong> the social ranking between $a$ and $b$ depends only on individual rankings between $a$ and $b$.</li>
<li><strong>Non-dictatorship (ND):</strong> no single voter's preference determines the social ordering.</li>
</ol>

<p>Theorem: with at least three alternatives and two voters, the only social welfare function satisfying U + P + IIA is dictatorship. Equivalently, no SWF satisfies U + P + IIA + ND.</p>

<p>Proof sketch: by U + P + IIA, the social ordering is determined by a "decisive coalition" structure. Tracing decisiveness across alternatives shows the decisive coalition must shrink to a single individual.</p>

<p>Implications:</p>

<p>(i) Aggregating ordinal preferences alone is hopeless.</p>

<p>(ii) Real voting systems must relax some axiom. Plurality rule violates Pareto (in pathological cases). Borda violates IIA. Restricted-domain procedures (single-peaked) circumvent the theorem.</p>

<p>(iii) Cardinal utility with interpersonal comparability (Sen 1970) escapes the impossibility.</p>

<p>(iv) Limited Pareto and IIA (Sen) deliver partial possibility results.</p>

<p>Reference: Micro2025.pdf Topic 2 Lecture on Social Choice; Arrow 1951; Sen "Collective Choice".</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <text x="60" y="40" font-size="14" font-weight="bold">Arrow's four axioms</text>
  <rect x="60" y="60" width="220" height="60" fill="#dbeafe" stroke="#1d4ed8"/>
  <text x="170" y="85" font-size="13" text-anchor="middle">U: Universal domain</text>
  <text x="170" y="105" font-size="11" text-anchor="middle">all preference profiles OK</text>
  <rect x="320" y="60" width="220" height="60" fill="#dcfce7" stroke="#16a34a"/>
  <text x="430" y="85" font-size="13" text-anchor="middle">P: Pareto unanimity</text>
  <text x="430" y="105" font-size="11" text-anchor="middle">everyone agrees, so does social</text>
  <rect x="60" y="140" width="220" height="60" fill="#fef3c7" stroke="#ca8a04"/>
  <text x="170" y="165" font-size="13" text-anchor="middle">IIA: Independence</text>
  <text x="170" y="185" font-size="11" text-anchor="middle">only pairwise prefs matter</text>
  <rect x="320" y="140" width="220" height="60" fill="#fee2e2" stroke="#dc2626"/>
  <text x="430" y="165" font-size="13" text-anchor="middle">ND: No dictator</text>
  <text x="430" y="185" font-size="11" text-anchor="middle">no single voter decides</text>
  <text x="300" y="260" font-size="14" text-anchor="middle" font-weight="bold" fill="#dc2626">Cannot satisfy all four simultaneously.</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Arrow's impossibility: no SWF satisfies all four axioms.</p>""",
        "examples": r"""<ul>
<li><strong>Constitutional design.</strong> Arrow shows why constitutions involve trade-offs among voting rules.</li>
<li><strong>Mechanism design.</strong> The Gibbard-Satterthwaite theorem extends Arrow to strategy-proof rules.</li>
<li><strong>Multi-criteria decision analysis.</strong> Aggregating multiple criteria faces Arrow-type impossibilities.</li>
<li><strong>Essay move.</strong> Doornik rewards essays showing how each real-world rule violates one axiom. Plurality violates Pareto; Borda violates IIA.</li>
<li><strong>Essay move.</strong> Sen's possibility theorem with cardinal comparability is the escape route.</li>
<li><strong>Limitation.</strong> Arrow is about ordinal preferences. With cardinal utility, SWFs are feasible (Sen 1970).</li>
<li>See also [[Concepts/Gibbard-Satterthwaite Theorem]], [[Concepts/Social Welfare Functions]], [[Concepts/Condorcet Paradox]].</li>
</ul>""",
    },
    "single-peaked-preferences": {
        "math": r"""<p><strong>Single-peaked preferences</strong>: each voter has a most-preferred alternative on a single dimension, with utility declining monotonically as we move away from that peak. Formally, there exists an ordering of alternatives such that each voter's utility is single-peaked on this ordering.</p>

<p>Black (1948) showed that single-peakedness rules out Condorcet cycles: with single-peaked preferences, the Condorcet winner is the median voter's preferred alternative.</p>

<ol>
<li>Order alternatives along a dimension (left-right, low-high tax rate).</li>
<li>Each voter has a peak: the alternative they most prefer.</li>
<li>Utility declines on either side of the peak.</li>
<li>Pairwise majority votes always select the median voter's peak.</li>
</ol>

<p>The median voter theorem follows: under single-peaked preferences, the median voter is the Condorcet winner. The result extends to candidates positioning on the policy line: both will converge to the median voter (Hotelling 1929, Downs 1957).</p>

<p>Empirical relevance: single-peakedness is plausible on many policy dimensions (tax rate, government spending, immigration), making the median voter theorem applicable.</p>

<p>Multi-dimensional preferences can fail single-peakedness even if each dimension is single-peaked: cross-dimensional intransitivities arise. McKelvey (1976) shows multidimensional majority cycles are pervasive.</p>

<p>Reference: Micro2025.pdf Topic 2 Lecture on Social Choice; Black 1948; Downs 1957.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <line x1="80" y1="260" x2="540" y2="260" stroke="#333"/>
  <line x1="80" y1="260" x2="80" y2="60" stroke="#333"/>
  <text x="540" y="280" font-size="13">policy</text>
  <text x="60" y="70" font-size="13">utility</text>
  <path d="M 80 240 Q 150 100 220 240" fill="none" stroke="#1f77b4" stroke-width="2"/>
  <text x="150" y="95" font-size="12" fill="#1f77b4">voter 1</text>
  <path d="M 200 240 Q 300 100 400 240" fill="none" stroke="#d62728" stroke-width="2"/>
  <text x="300" y="95" font-size="12" fill="#d62728">voter 2 (median)</text>
  <path d="M 380 240 Q 460 100 540 240" fill="none" stroke="#2ca02c" stroke-width="2"/>
  <text x="450" y="95" font-size="12" fill="#2ca02c">voter 3</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Single-peaked preferences: each voter has a unique peak, utility declines on both sides.</p>""",
        "examples": r"""<ul>
<li><strong>Tax-rate elections.</strong> Voters typically have single-peaked preferences on income-tax rate.</li>
<li><strong>Government spending.</strong> Each voter has a preferred spending level.</li>
<li><strong>Immigration policy.</strong> Approximately single-peaked on a single dimension.</li>
<li><strong>Essay move.</strong> Doornik rewards essays linking single-peakedness to the median voter theorem.</li>
<li><strong>Essay move.</strong> Note that multidimensional cases violate single-peakedness even if each dimension is.</li>
<li><strong>Limitation.</strong> Multi-dimensional preferences and bundle-issue voting can produce cycles.</li>
<li>See also [[Concepts/Median Voter Theorem]], [[Concepts/Condorcet Paradox]].</li>
</ul>""",
    },
    "median-voter-theorem": {
        "math": r"""<p>The <strong>median voter theorem</strong> (Black 1948): under single-peaked preferences and pairwise majority voting on a one-dimensional policy space, the Condorcet winner is the median voter's most-preferred policy.</p>

<p>Proof: order voters by their peaks. The median voter prefers their peak to any alternative on either side. Any alternative strictly above the median is rejected by all voters with peaks at or below the median (a majority). Symmetric argument for alternatives strictly below.</p>

<ol>
<li>Order voters by their ideal points $\theta_1 < \theta_2 < \dots < \theta_n$.</li>
<li>Median voter has ideal point $\theta_m$ where $m = (n+1)/2$.</li>
<li>For any alternative $a > \theta_m$: voters $1, \dots, m$ prefer $\theta_m$ (or lower) to $a$. Majority rejection.</li>
<li>By symmetry, alternatives below $\theta_m$ also rejected.</li>
</ol>

<p>Downs (1957): in two-candidate elections with single-peaked preferences, candidates converge to the median voter. Both lose if they deviate.</p>

<p>Implications:</p>

<p>(i) Electoral platforms cluster at the centre.</p>

<p>(ii) Strong-form prediction is implausible: real campaigns differentiate. Polarisation models (Wittman 1973) introduce candidate preferences.</p>

<p>(iii) Two-party systems are predicted to be centripetal; multi-party systems centrifugal.</p>

<p>Empirical evidence: party platforms have indeed converged in many democracies (Caplan 2007), but recent trends show polarisation, requiring extensions of the simple median voter framework.</p>

<p>Reference: Micro2025.pdf Topic 2 Lecture on Social Choice; Black 1948; Downs 1957; Hotelling 1929.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <line x1="80" y1="200" x2="540" y2="200" stroke="#333" stroke-width="2"/>
  <text x="540" y="220" font-size="13">policy axis</text>
  <circle cx="120" cy="200" r="8" fill="#1f77b4"/>
  <text x="120" y="240" font-size="12" text-anchor="middle">V1</text>
  <circle cx="220" cy="200" r="8" fill="#1f77b4"/>
  <text x="220" y="240" font-size="12" text-anchor="middle">V2</text>
  <circle cx="320" cy="200" r="10" fill="#dc2626"/>
  <text x="320" y="240" font-size="12" text-anchor="middle" fill="#dc2626" font-weight="bold">Median</text>
  <circle cx="420" cy="200" r="8" fill="#1f77b4"/>
  <text x="420" y="240" font-size="12" text-anchor="middle">V4</text>
  <circle cx="520" cy="200" r="8" fill="#1f77b4"/>
  <text x="520" y="240" font-size="12" text-anchor="middle">V5</text>
  <text x="60" y="90" font-size="13">Median voter's peak is the Condorcet winner.</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Five voters, median is decisive under single-peaked preferences.</p>""",
        "examples": r"""<ul>
<li><strong>US politics.</strong> Two-party convergence to centre is the median voter prediction.</li>
<li><strong>UK Labour-Conservative.</strong> Both parties converged on centrist policies during the New Labour and Cameron eras.</li>
<li><strong>Tax-rate setting.</strong> Median income elasticity often pins down policy outcomes.</li>
<li><strong>Essay move.</strong> Doornik rewards essays deriving median voter from single-peakedness. Walk through the proof.</li>
<li><strong>Essay move.</strong> Note that real campaigns deviate from convergence due to candidate preferences and information asymmetries.</li>
<li><strong>Limitation.</strong> Multi-dimensional policies, strategic abstention, and candidate motivation break the strict convergence prediction.</li>
<li>See also [[Concepts/Single-Peaked Preferences]], [[Concepts/Condorcet Paradox]].</li>
</ul>""",
    },
    "gibbard-satterthwaite": {
        "math": r"""<p>The <strong>Gibbard-Satterthwaite theorem</strong> (Gibbard 1973, Satterthwaite 1975): every social choice rule defined on the universal domain with at least three alternatives, that is non-dictatorial and onto (any alternative can win), is manipulable. Equivalently, no such rule is strategy-proof.</p>

<p>The theorem is the strategic-voting analogue of Arrow's impossibility. While Arrow says ordinal preference aggregation is impossible, Gibbard-Satterthwaite says strategy-proof aggregation is impossible too.</p>

<ol>
<li>Strategy-proofness: truthful reporting is a weakly dominant strategy.</li>
<li>Non-dictatorship: no single voter determines the outcome.</li>
<li>Universal domain: all preference profiles allowed.</li>
<li>Surjectivity: any of the three or more alternatives can be the chosen one.</li>
</ol>

<p>Proof: G-S follows from Arrow's theorem applied to a "strategy-proof equivalent" construction. The proof shows that strategy-proofness implies IIA-like properties.</p>

<p>Implications:</p>

<p>(i) Real voting systems are vulnerable to strategic voting.</p>

<p>(ii) Mechanism design must either restrict the domain (single-peaked preferences) or accept some manipulability.</p>

<p>(iii) Specific strategy-proof rules exist on restricted domains:</p>

<p>Single-peaked preferences: the median voter rule is strategy-proof (Black 1948).</p>

<p>Quasi-linear utility: Vickrey-Clarke-Groves (VCG) mechanisms are strategy-proof.</p>

<p>Two alternatives: majority rule is strategy-proof (May 1952).</p>

<p>Reference: Micro2025.pdf Topic 2 Lecture on Social Choice; Gibbard 1973; Satterthwaite 1975.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <text x="60" y="40" font-size="14" font-weight="bold">G-S impossibility</text>
  <rect x="60" y="60" width="220" height="60" fill="#dbeafe" stroke="#1d4ed8"/>
  <text x="170" y="85" font-size="13" text-anchor="middle">Strategy-proof</text>
  <text x="170" y="105" font-size="11" text-anchor="middle">truthful is dominant</text>
  <rect x="320" y="60" width="220" height="60" fill="#dcfce7" stroke="#16a34a"/>
  <text x="430" y="85" font-size="13" text-anchor="middle">Non-dictatorial</text>
  <rect x="60" y="140" width="220" height="60" fill="#fef3c7" stroke="#ca8a04"/>
  <text x="170" y="170" font-size="13" text-anchor="middle">Universal domain</text>
  <rect x="320" y="140" width="220" height="60" fill="#fee2e2" stroke="#dc2626"/>
  <text x="430" y="170" font-size="13" text-anchor="middle">3+ alternatives</text>
  <text x="300" y="260" font-size="14" text-anchor="middle" font-weight="bold" fill="#dc2626">Cannot satisfy all four.</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">G-S: no strategy-proof, non-dictatorial rule exists on universal domain with 3+ alternatives.</p>""",
        "examples": r"""<ul>
<li><strong>School choice mechanisms.</strong> Boston (manipulable) replaced by Deferred Acceptance (strategy-proof under restricted preferences, Roth-Sotomayor 1990).</li>
<li><strong>Spectrum auctions.</strong> VCG-style designs achieve strategy-proofness on quasi-linear domain.</li>
<li><strong>Political elections.</strong> All real-world elections are manipulable (strategic voting is rational).</li>
<li><strong>Essay move.</strong> Doornik rewards essays linking G-S to Arrow. Both are impossibility results on universal domains.</li>
<li><strong>Essay move.</strong> Escape routes: restrict domain (single-peakedness), or use cardinal utility (VCG).</li>
<li><strong>Limitation.</strong> G-S assumes deterministic mechanisms. Random mechanisms can achieve strategy-proofness under weaker conditions (Gibbard 1977).</li>
<li>See also [[Concepts/Arrow's Impossibility Theorem]], [[Concepts/Strategy-Proofness]].</li>
</ul>""",
    },
    "strategy-proofness": {
        "math": r"""<p>A mechanism is <strong>strategy-proof</strong> if truthful reporting is a weakly dominant strategy for every agent: for every agent $i$, every type $\theta_i$, and every report $\hat\theta_i$, the outcome from reporting truthfully is at least as good as the outcome from any misreport, regardless of others' reports.</p>

<p>Formally: $u_i(\theta_i, f(\theta_i, \theta_{-i})) \geq u_i(\theta_i, f(\hat\theta_i, \theta_{-i}))$ for all $\theta_i, \hat\theta_i, \theta_{-i}$.</p>

<ol>
<li>Identify all reportable strategies.</li>
<li>Verify that truth-telling is at least as good as any other for every type and any opponent reports.</li>
<li>Strategy-proofness is dominant-strategy incentive compatibility, the strongest possible.</li>
</ol>

<p>Strategy-proof mechanisms:</p>

<p>(i) Vickrey (second-price) auctions: truthful bidding dominant (Vickrey 1961).</p>

<p>(ii) Clarke-Groves-VCG: strategy-proof on quasi-linear domain (Clarke 1971, Groves 1973).</p>

<p>(iii) Deferred Acceptance: strategy-proof for the proposing side (Roth 1982).</p>

<p>(iv) Median voter rule on single-peaked preferences (Black 1948).</p>

<p>Gibbard-Satterthwaite (1973-1975): on universal domain with 3+ alternatives, only dictatorial mechanisms are strategy-proof.</p>

<p>Real-world value: strategy-proof mechanisms eliminate the cognitive cost of strategising and the unfairness of outcomes determined by sophisticated participants. Boston-to-Deferred-Acceptance reform in school choice is the leading practical example.</p>

<p>Reference: Micro2025.pdf Topic 2 Lecture on Social Choice; Gibbard 1973; Mas-Colell Ch. 23.</p>""",
        "widget": r"""<svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#fafafa">
  <text x="60" y="40" font-size="14" font-weight="bold">Strategy-proof mechanisms</text>
  <rect x="60" y="80" width="240" height="40" fill="#a7f3d0" stroke="#10b981"/>
  <text x="180" y="105" font-size="13" text-anchor="middle">Vickrey auction</text>
  <rect x="60" y="130" width="240" height="40" fill="#a7f3d0" stroke="#10b981"/>
  <text x="180" y="155" font-size="13" text-anchor="middle">VCG / Clarke</text>
  <rect x="60" y="180" width="240" height="40" fill="#a7f3d0" stroke="#10b981"/>
  <text x="180" y="205" font-size="13" text-anchor="middle">Deferred Acceptance</text>
  <rect x="60" y="230" width="240" height="40" fill="#a7f3d0" stroke="#10b981"/>
  <text x="180" y="255" font-size="13" text-anchor="middle">Median voter rule</text>
  <text x="350" y="120" font-size="13" fill="#555">All on restricted domain</text>
  <text x="350" y="140" font-size="13" fill="#555">or with limited alternatives.</text>
</svg>
<p class="caption" style="font-size:0.9em;color:#555;margin-top:0.4em">Strategy-proof mechanisms exist on restricted domains; G-S shows no general possibility.</p>""",
        "examples": r"""<ul>
<li><strong>NYC school choice.</strong> Switched from manipulable to Deferred Acceptance in 2004.</li>
<li><strong>FCC spectrum auctions.</strong> VCG-style designs aim for strategy-proofness.</li>
<li><strong>Online ad auctions.</strong> Generalised second-price approximates strategy-proofness in the second-bid case.</li>
<li><strong>Essay move.</strong> Doornik rewards essays distinguishing strategy-proofness from Bayes-Nash IC. The former is stronger.</li>
<li><strong>Essay move.</strong> Invoke G-S to explain why strategy-proofness requires domain restrictions or quasi-linear utility.</li>
<li><strong>Limitation.</strong> Strategy-proofness can come at the cost of efficiency or revenue (Holmstrom 1979 on auctions).</li>
<li>See also [[Concepts/Gibbard-Satterthwaite Theorem]], [[Concepts/Vickrey (Second-Price) Auction]], [[Concepts/Clarke-Groves Mechanism]].</li>
</ul>""",
    },
}
