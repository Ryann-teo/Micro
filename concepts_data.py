"""Master concept manifest for the Core Micro study website.

Each entry: (slug, name, topic_id, tier, intuition_paragraph(s)).
Intuition is the only section filled in for Phase 1. Math, graphs, and
real-life examples are TODO placeholders that future sessions will fill.

Topic IDs:
  1 = General Equilibrium
  2 = Welfare and Social Choice
  3 = Externalities and Public Goods
  4 = Game Theory
  5 = Industrial Organisation and Competition Policy
  6 = Decisions under Risk
  7 = Adverse Selection (Information Economics 1)
  8 = Moral Hazard (Information Economics 2)

Tier 1 = 8+ mentions in Question Typing files. Tier 2 = 5 to 7. Tier 3 = 3 to 4.
Tier 4 = 1 to 2. Tier S = from slides, not yet referenced in past papers.
"""

TOPICS = [
    (1, "General Equilibrium",
     "Walrasian competitive equilibrium in exchange and production economies. The core machinery: budget constraints, market clearing, Walras' Law, excess demand, existence and uniqueness of equilibrium.",
     "FHSMicroWk1 Lectures 1 to 3 (Lecture_1_GE_Intro, Lecture_2_Trade, Lecture_3_Finding_GE). Textbook: Varian Intermediate Ch 31 to 33."),
    (2, "Welfare and Social Choice",
     "Evaluating allocations: Pareto efficiency, the two welfare theorems, Bergson-Samuelson social welfare functions, social choice (Arrow's impossibility, the median voter), and money-metric measures like CV and EV.",
     "Lectures 4 to 6 (Welfare, SocialChoice, AppliedWelfare). Textbook: Varian Intermediate Ch 32 to 33."),
    (3, "Externalities and Public Goods",
     "When private markets fail to internalise external effects: externalities, public goods, the tragedy of the commons, Pigouvian taxes, Coase bargaining, Lindahl pricing, and the Clarke-Groves mechanism.",
     "Lectures 7 to 8. Textbook: Hindriks and Myles; Varian Ch 35 to 36."),
    (4, "Game Theory",
     "Strategic interaction: simultaneous and sequential games, Nash equilibrium (pure and mixed), backward induction, subgame perfection, and infinitely repeated games with grim-trigger strategies.",
     "FHSMicroWk4 L1 to L3. Textbook: Osborne, A Course in Game Theory; Varian Ch 28 to 29."),
    (5, "Industrial Organisation and Competition Policy",
     "Oligopoly models (Cournot, Bertrand, Stackelberg, differentiated products), collusion sustainability, entry and entry deterrence, merger analysis, and the legal framework for antitrust.",
     "Lecture12IO, Lecture13Collusion, FHSMicroWk6. Textbook: Belleflamme and Peitz; Tirole."),
    (6, "Decisions under Risk",
     "Expected utility theory: vNM axioms, risk aversion and its measures (ARA, RRA, CARA, CRRA, DARA), certainty equivalent, risk premium, stochastic dominance, and risk-sharing.",
     "FHSMicroWk6 L1 to L3. Textbook: Mas-Colell, Whinston, Green Ch 6; Gravelle and Rees."),
    (7, "Adverse Selection",
     "Hidden information before contracting: Akerlof lemons, full unravelling, Spence signalling, Rothschild-Stiglitz screening, single-crossing condition, and equilibrium refinements.",
     "FHSMicroWk7 L1 to L2. Textbook: Gravelle and Rees; Bolton and Dewatripont."),
    (8, "Moral Hazard",
     "Hidden action after contracting: the principal-agent problem, individual rationality and incentive compatibility, first-best vs second-best contracts, agency cost, and linear contracts under CARA-normal.",
     "FHSMicroWk7 L3. Textbook: Bolton and Dewatripont; Laffont and Martimort."),
]

# Concept list: (slug, display_name, topic_id, tier, intuition_paragraphs)
# intuition_paragraphs is a list of paragraph strings (1 to 3 paragraphs)
CONCEPTS = [
    # ===== TOPIC 1: GENERAL EQUILIBRIUM =====
    ("competitive-equilibrium", "Competitive Equilibrium", 1, 1, [
        "A competitive equilibrium is a price vector together with an allocation such that, taking prices as given, every consumer maximises utility within their budget and every firm maximises profits, and all markets clear (supply equals demand for every good).",
        "The key idea is that prices coordinate decisions made independently by many agents. No one is in charge of matching demand to supply: the price simply adjusts until the two coincide. This is the workhorse benchmark of microeconomics, and almost every Part A question on GE asks you to compute one.",
    ]),
    ("walras-law", "Walras Law", 1, 3, [
        "Walras' Law says that the value of total excess demand across all markets is identically zero, regardless of prices. The intuition is just budget balance summed across agents: each consumer spends exactly what their endowment is worth, so summing across consumers, total spending equals total endowment value.",
        "The practical use: in an n-good economy you only need to check that n-1 markets clear, and the last one clears automatically. This is the standard shortcut for computing GE.",
    ]),
    ("excess-demand", "Excess Demand", 1, 3, [
        "Excess demand for a good is aggregate demand minus aggregate supply at a given price. In equilibrium it equals zero for every good. Out of equilibrium, positive excess demand pushes price up; negative excess demand pushes price down.",
        "Excess demand functions are homogeneous of degree zero in prices: doubling all prices leaves real demand and supply unchanged, hence excess demand unchanged. This is why we can normalise one price (the numeraire).",
    ]),
    ("homogeneity-degree-zero", "Homogeneity of Degree Zero", 1, "S", [
        "Excess demand depends only on relative prices, not on the price level. Scaling every price (and every nominal income) by the same factor leaves all real choices unchanged. This is sometimes called 'no money illusion'.",
    ]),
    ("numeraire-good", "Numeraire Good", 1, 2, [
        "Because excess demand is homogeneous of degree zero, only relative prices matter. We can fix the price of one good (the numeraire) at 1 and solve for the remaining n-1 prices. Conventionally we use whichever good simplifies the algebra.",
    ]),
    ("cobb-douglas-demand", "Cobb-Douglas Demand", 1, 2, [
        "With utility $u = x^\\alpha y^{1-\\alpha}$ and budget $p_x x + p_y y = m$, the consumer spends fraction alpha of income on x and 1-alpha on y. So demand is $x^* = \\alpha m / p_x$ and $y^* = (1-\\alpha) m / p_y$.",
        "This functional form shows up in almost every Part A question because it gives clean closed-form demands and constant expenditure shares. Worth memorising.",
    ]),
    ("quasi-linear-utility", "Quasi-linear Utility", 1, 1, [
        "Utility takes the form $u(x, y) = v(x) + y$, where x is the good we care about and y is a numeraire (often interpreted as money). The key property is no income effect on x: demand for x depends only on price, not income.",
        "Quasi-linear utility makes welfare analysis trivial because compensating variation, equivalent variation, and change in consumer surplus all coincide. It is also the assumption behind summing utilities for Pareto efficiency in externality problems.",
    ]),
    ("edgeworth-box", "Edgeworth Box", 1, 3, [
        "A graphical device for analysing a two-person two-good exchange economy. The width is the total endowment of good x; the height is the total endowment of good y. Agent A is measured from the bottom-left; agent B from the top-right.",
        "Inside the box, points represent allocations. Pareto-efficient allocations lie on the contract curve where A's and B's indifference curves are tangent (MRS_A equals MRS_B). The competitive equilibrium is found where the budget line (through the endowment) is tangent to both agents' indifference curves at the same point.",
    ]),
    ("ppf-and-mrt", "PPF and MRT", 1, 3, [
        "The production possibility frontier (PPF) shows the maximum output combinations of two goods that an economy can produce with its fixed factor endowment. Its slope at any point is the marginal rate of transformation (MRT): how much of one good you give up to produce one more unit of the other.",
        "In equilibrium with competitive firms, MRT equals the relative price ratio p_x / p_y. Pareto efficiency requires MRS (the consumer's tradeoff) to equal MRT (the producer's tradeoff).",
    ]),
    ("ricardian-trade-model", "Ricardian Trade Model", 1, 3, [
        "Two countries, two goods, one factor (labour) with different productivities across countries. Each country specialises in the good in which it has comparative advantage (lower relative labour cost) and trades for the other. The PPF is linear because labour productivity is constant.",
        "Trade lets both countries consume outside their own PPF, generating gains from trade. The terms of trade (world price) sit between the two autarky price ratios.",
    ]),
    ("autarky", "Autarky", 1, 1, [
        "Closed-economy equilibrium with no international trade. Used as the baseline against which to measure gains from trade. The autarky price ratio reflects the country's relative scarcity (or productivity) of each good.",
    ]),
    ("comparative-advantage", "Comparative Advantage", 1, 1, [
        "A country has comparative advantage in the good for which its opportunity cost (the amount of the other good it gives up) is lowest. Trade based on comparative advantage benefits both countries even if one has absolute advantage in every good.",
    ]),
    ("heckscher-ohlin-model", "Heckscher-Ohlin Model", 1, 2, [
        "A two-good, two-factor model where comparative advantage stems from differences in factor endowments. A country exports the good that intensively uses its abundant factor. Adds Stolper-Samuelson (factor returns) and Rybczynski (factor supply) theorems.",
    ]),
    ("stolper-samuelson", "Stolper-Samuelson Theorem", 1, 2, [
        "An increase in the relative price of a good raises the real return to the factor used intensively in producing it, and lowers the real return to the other factor. This is the foundation of distributional arguments about trade: opening to trade hurts a country's scarce factor."]),
    ("rybczynski-theorem", "Rybczynski Theorem", 1, "S", [
        "Holding goods prices constant, an increase in the supply of one factor raises output of the good using it intensively and lowers output of the other good. Together with Stolper-Samuelson, this gives the H-O theorem its bite."]),
    ("gross-substitutes", "Gross Substitutes", 1, 3, [
        "Two goods are gross substitutes if an increase in the price of one raises (rather than lowers) the demand for the other. When all goods are gross substitutes, the Walrasian equilibrium is unique."]),
    ("zero-profit-condition", "Zero-Profit Condition", 1, 3, [
        "Under constant returns to scale and free entry, competitive firms earn zero profits in equilibrium: price equals average cost equals marginal cost. This is a constraint, not an assumption, in long-run GE models."]),
    ("uniqueness-of-equilibrium", "Uniqueness of Equilibrium", 1, "S", [
        "Under fairly weak conditions (e.g., gross substitutes, or the WARP at the aggregate level), the Walrasian equilibrium price vector is unique. Without such conditions, multiple equilibria are possible and comparative statics become harder."]),
    ("robinson-crusoe-economy", "Robinson Crusoe Economy", 1, "S", [
        "A model with one consumer who is also the only producer (Robinson Crusoe on his island). He chooses labour, consumption, and leisure. The model shows that the planner solution and the competitive solution coincide, illustrating the first welfare theorem in miniature."]),

    # ===== TOPIC 2: WELFARE AND SOCIAL CHOICE =====
    ("pareto-efficiency", "Pareto Efficiency", 2, 2, [
        "An allocation is Pareto efficient if no reallocation can make someone better off without making someone else worse off. This is a minimal benchmark: it does not say anything about fairness or distribution, only about avoiding waste.",
        "Pareto efficiency in an exchange economy requires equalised MRS across consumers. With production, you also need MRS equal to MRT. The set of all Pareto efficient allocations forms the contract curve (in exchange) or the utility possibility frontier."]),
    ("pareto-criterion", "Pareto Criterion", 2, 2, [
        "Allocation x is Pareto-preferred to y if everyone weakly prefers x and at least one person strictly prefers x. The Pareto criterion ranks only those pairs related this way, leaving most pairs unranked. That incompleteness is the criterion's main weakness."]),
    ("first-welfare-theorem", "First Welfare Theorem", 2, 3, [
        "Every competitive equilibrium allocation is Pareto efficient, provided preferences are locally non-satiated. This is the formal statement of Adam Smith's invisible hand: self-interested decentralised behaviour produces a no-waste outcome.",
        "The theorem requires no externalities, no public goods, no asymmetric information, no market power. Any of those breaks the result, which is why most of the rest of micro is about what goes wrong when an assumption fails.",
    ]),
    ("second-welfare-theorem", "Second Welfare Theorem", 2, 2, [
        "Any Pareto efficient allocation can be supported as a competitive equilibrium after a suitable lump-sum redistribution of endowments. So efficiency and distribution can be separated: pick the distribution you want and let the market find the prices that decentralise it.",
        "The theorem requires convex preferences and technologies. The bigger practical caveat is that lump-sum transfers are hard to implement in reality (because they depend on unobservable types), so policymakers fall back on distortionary taxation."]),
    ("social-welfare-functions", "Social Welfare Functions", 2, 3, [
        "A social welfare function (SWF) aggregates individual utilities into a single social objective W(u_1, ..., u_n). Different SWFs encode different ethical positions: the utilitarian sums utilities, the Rawlsian takes the minimum, the Bergson-Samuelson is any increasing function."]),
    ("utilitarian-planner", "Utilitarian Planner", 2, 4, [
        "Maximises the unweighted sum of individual utilities. Cardinal information matters: it must be meaningful to add utility levels across people. With concave utility, the utilitarian allocates more resources to those whose marginal utility of income is higher (often the poor)."]),
    ("rawlsian-planner", "Rawlsian Planner", 2, 4, [
        "Maximises the utility of the worst-off person (the maximin criterion). Cares only about the position of the lowest individual. Requires only ordinal information across people, but at the cost of being insensitive to gains for everyone except the worst-off."]),
    ("kaldor-hicks-compensation", "Kaldor-Hicks Compensation", 2, 3, [
        "A change is judged welfare-improving if the winners could in principle compensate the losers and still be better off, even if no actual compensation is paid. This is the standard tool of cost-benefit analysis. Its weakness is that the 'in principle' compensation is rarely enforced, so real losers stay worse off."]),
    ("contract-curve", "Contract Curve", 2, 1, [
        "Inside an Edgeworth box, the contract curve is the locus of allocations where the two agents' indifference curves are tangent (their MRSs are equal). These are the Pareto efficient allocations: any move off the contract curve makes at least one agent worse off."]),
    ("utility-possibility-frontier", "Utility Possibility Frontier", 2, 3, [
        "The UPF traces out all combinations of utilities (u_A, u_B) that are achievable by Pareto efficient allocations. Inefficient allocations sit inside the frontier; nothing sits beyond it. Social welfare maximisation picks the point on the UPF where the social indifference curve is tangent."]),
    ("compensating-variation", "Compensating Variation", 2, "S", [
        "After a price change, compensating variation is the amount of money you would need to take from (give to) the consumer to restore them to their original utility level. CV uses the new prices as the reference point."]),
    ("equivalent-variation", "Equivalent Variation", 2, "S", [
        "After a price change, equivalent variation is the amount of money you would give to (or take from) the consumer at the old prices to make them as well off as they would be after the change. EV uses the old prices as the reference point."]),
    ("consumer-surplus", "Consumer Surplus", 2, 1, [
        "The area under the (Marshallian) demand curve and above the price line. For quasi-linear preferences, consumer surplus equals both CV and EV exactly. For other preferences, ΔCS sits between CV and EV but is the easiest to compute and is the standard CBA approximation."]),
    ("deadweight-loss", "Deadweight Loss", 2, 2, [
        "The welfare loss caused by a tax or other distortion that drives a wedge between the price paid by consumers and received by producers. Geometrically the Harberger triangle between the demand and supply curves over the lost-trade region."]),
    ("ramsey-taxation", "Ramsey Taxation", 2, "S", [
        "When lump-sum taxes are unavailable, raising a given amount of revenue with minimum deadweight loss requires taxing goods with low demand elasticity more heavily (the inverse elasticity rule). This is the second-best benchmark for indirect taxation."]),
    ("expenditure-function", "Expenditure Function", 2, "S", [
        "$e(p, u)$ is the minimum spending required to reach utility level u at prices p. Its derivatives give the Hicksian (compensated) demands by Shephard's lemma. The expenditure function is the workhorse for computing CV and EV."]),
    ("marshallian-demand", "Marshallian Demand", 2, 2, [
        "Demand derived from utility maximisation subject to a budget constraint at given prices and income. Shows the total response to a price change, including the income effect."]),
    ("hicksian-demand", "Hicksian Demand", 2, "S", [
        "Compensated demand: how a consumer would respond to a price change if their utility were held constant by an income adjustment. Hicksian demand isolates the substitution effect. Derived from expenditure minimisation."]),
    ("cost-benefit-analysis", "Cost-Benefit Analysis", 2, 3, [
        "A systematic comparison of the present value of a project's benefits against its costs, including non-market valuations and a social discount rate. CBA operationalises the Kaldor-Hicks criterion for policy decisions."]),
    ("contingent-valuation", "Contingent Valuation", 2, "S", [
        "A survey-based method for valuing non-market goods (e.g., a clean river) by asking respondents directly how much they would pay or accept. Subject to hypothetical bias because the answers are not enforced by real choices."]),
    ("hedonic-pricing", "Hedonic Pricing", 2, "S", [
        "Inferring the implicit price of an amenity (e.g., proximity to a park) from regressions of house prices on house attributes. A way to extract willingness-to-pay from observed market data."]),
    ("travel-cost-method", "Travel Cost Method", 2, "S", [
        "Valuing a recreational facility by treating travel cost as a 'price' and observing visit frequencies. Generates a demand curve from which consumer surplus can be inferred."]),
    ("qaly", "Quality-Adjusted Life Year (QALY)", 2, "S", [
        "A health-outcome measure combining length of life and quality of life. One QALY equals one year in perfect health. Used in CBA to compare medical interventions without putting monetary value on life directly."]),
    ("social-discount-rate", "Social Discount Rate", 2, "S", [
        "The rate at which future consumption is discounted in social welfare calculations. The Ramsey equation decomposes it into the pure rate of time preference plus the product of the elasticity of marginal utility and the growth rate."]),
    ("ramsey-equation", "Ramsey Equation", 2, "S", [
        "$r = \\rho + \\eta g$. The social discount rate equals impatience ($\\rho$) plus inequality aversion ($\\eta$) times the consumption growth rate ($g$). The Stern-Nordhaus debate on climate policy hinges on what value of $\\rho$ to use."]),
    ("majority-rule", "Majority Rule", 2, "S", [
        "Pairwise voting: x beats y if more people prefer x to y. May produce cyclic social rankings (Condorcet paradox). Works cleanly only when preferences are single-peaked, in which case the median voter wins."]),
    ("borda-count", "Borda Count", 2, "S", [
        "Each voter ranks the alternatives; alternatives receive points by rank position (n-1 for top, 0 for bottom). Society's ranking is by total points. Satisfies many desiderata but violates Independence of Irrelevant Alternatives."]),
    ("condorcet-paradox", "Condorcet Paradox", 2, "S", [
        "With three voters and three alternatives, majority rule can produce a cyclic social ranking (x beats y beats z beats x). Shows that aggregating consistent individual preferences into a consistent social preference can fail."]),
    ("arrow-impossibility", "Arrow's Impossibility Theorem", 2, 2, [
        "With three or more alternatives, no preference aggregation rule can simultaneously satisfy unrestricted domain, the Pareto principle, non-dictatorship, and independence of irrelevant alternatives while producing a transitive social ordering. Some axiom has to give.",
        "Arrow's theorem is not a counsel of despair; it tells you that any actual rule (majority, Borda, etc.) is making implicit trade-offs between the axioms. Knowing which trade-off your rule is making is the substantive content."]),
    ("single-peaked-preferences", "Single-Peaked Preferences", 2, 3, [
        "Preferences over a one-dimensional alternative space (e.g., tax rate from 0 to 100 percent) are single-peaked if each voter has a unique bliss point and prefers alternatives closer to it. Under single-peakedness, majority rule is transitive."]),
    ("median-voter-theorem", "Median Voter Theorem", 2, "S", [
        "With single-peaked preferences and majority rule on a one-dimensional space, the alternative preferred by the median voter is the Condorcet winner. Office-motivated candidates therefore converge on the median voter's bliss point."]),
    ("gibbard-satterthwaite", "Gibbard-Satterthwaite Theorem", 2, "S", [
        "Any non-dictatorial social choice function with at least three alternatives in its range is manipulable: some voter can do better by misreporting preferences. Strategy-proofness essentially requires dictatorship in the general case."]),
    ("strategy-proofness", "Strategy-Proofness", 2, 2, [
        "A social choice rule is strategy-proof (dominant-strategy incentive compatible) if no voter ever benefits from misreporting preferences. The Vickrey auction and the Clarke-Groves mechanism are leading examples."]),

    # ===== TOPIC 3: EXTERNALITIES AND PUBLIC GOODS =====
    ("public-goods", "Public Goods", 3, 2, [
        "A pure public good is non-rival (one person's consumption does not reduce another's) and non-excludable (you cannot prevent non-payers from consuming). Classic examples: national defence, lighthouses, clean air, basic research.",
        "Public goods are under-provided in private markets because of the free-rider problem. The efficient quantity is given by the Samuelson condition: sum of marginal benefits across all consumers equals marginal cost."]),
    ("samuelson-condition", "Samuelson Condition", 3, 1, [
        "The Pareto-efficient quantity of a public good satisfies $\\sum_i MRS_i = MRT$. In words: the sum of marginal willingness-to-pay across all consumers equals the marginal cost of provision. This is the public-good analogue of the private-good condition MRS = MRT.",
        "Why sum and not equate? With a public good, every consumer enjoys every unit, so the social marginal benefit at any quantity is the vertical sum of individual marginal benefits, not the horizontal sum that you would use for a private good."]),
    ("free-rider-problem", "Free Rider Problem", 3, 2, [
        "When a public good is non-excludable, individuals have an incentive to let others pay while still consuming. If everyone reasons this way, the public good is under-provided or not provided at all.",
        "The free-rider problem is the central justification for government provision of public goods (defence, infrastructure) or for mechanism design solutions like the Clarke-Groves scheme."]),
    ("voluntary-contribution-nash", "Voluntary Contribution Nash Equilibrium", 3, 2, [
        "Each agent contributes to a public good, taking others' contributions as given. The Nash equilibrium has every agent equating their private marginal benefit (not the social one) to marginal cost. Total provision is below the Samuelson level, often dramatically so.",
        "A surprising property: total provision is invariant to the number of agents, because adding more agents simply reduces each individual's contribution proportionally. This 'neutrality' result depends on interior contributions for everyone."]),
    ("lindahl-prices", "Lindahl Prices", 3, 2, [
        "Each consumer faces a personalised price for the public good equal to their marginal willingness-to-pay at the optimum. With Lindahl prices, everyone agrees on the same quantity (the Samuelson optimum), and each pays their share of marginal cost.",
        "Lindahl pricing decentralises the public-good problem the way ordinary prices decentralise private-good provision. The practical problem is that the planner does not know preferences, and consumers have no incentive to reveal them truthfully."]),
    ("clarke-groves-mechanism", "Clarke-Groves Mechanism", 3, 2, [
        "A direct-revelation mechanism for public goods in which truthful reporting of preferences is a dominant strategy. Each agent pays a tax equal to the externality their report imposes on others (the change in others' utility if their report changes the outcome).",
        "Clarke-Groves achieves efficient provision and incentive compatibility, but is not budget-balanced (revenue is collected but cannot be redistributed without breaking incentives) and not always individually rational. These are the practical limits."]),
    ("pigouvian-tax", "Pigouvian Tax", 3, 1, [
        "A per-unit tax on an externality-producing activity set equal to the marginal external cost at the efficient quantity. Private agents then face the social marginal cost and choose the socially optimal activity level.",
        "Pigouvian taxes implement first-best efficiency under certainty. Their main practical challenge is that the regulator needs to know the marginal external cost function, and they may need to vary with output. Cap-and-trade is the dual quantity instrument."]),
    ("coase-theorem", "Coase Theorem", 3, 2, [
        "If property rights over an externality are clearly assigned and transaction costs are zero, the parties will bargain to the efficient quantity regardless of who holds the right. The distribution of payoffs depends on who has the right; the quantity does not.",
        "The Coase theorem is the case for using private bargaining rather than Pigouvian taxes. Its assumptions almost never literally hold (transaction costs are real and large for many externalities), but it provides a useful benchmark."]),
    ("tragedy-of-the-commons", "Tragedy of the Commons", 3, 2, [
        "An open-access resource (a fishery, a grazing land, a road) is over-used because each user ignores the negative externality their use imposes on others. The equilibrium has too many users; the resource is dissipated of any rent it could generate.",
        "Solutions include privatisation (assigning property rights), regulation (quotas), or Pigouvian charges (congestion tolls). The political-economy challenge is that the losers from any solution are concentrated and the gains diffuse."]),
    ("rivalry-and-excludability", "Rivalry and Excludability", 3, 3, [
        "The two key axes that classify goods. Rivalry: does my consumption reduce yours? Excludability: can non-payers be kept out? The four cells are private goods (yes, yes), club goods (no, yes), common-pool resources (yes, no), and public goods (no, no)."]),
    ("marginal-private-vs-social-benefit", "Marginal Private vs Social Benefit", 3, 2, [
        "Marginal private benefit is what the consumer privately captures; marginal social benefit also includes any positive externality on third parties (or subtracts any negative externality). With externalities, MSB differs from MPB, and decentralised choice yields the wrong quantity.",
        "Pigouvian taxes and subsidies are designed to close the wedge between MPB and MSB so that the private choice coincides with the social optimum."]),
    ("externality-internalisation", "Externality Internalisation", 3, 2, [
        "Mechanisms by which the externality is brought back into the private cost-benefit calculation: Pigouvian taxes, tradeable permits, Coasean bargaining, regulation, social norms. The point is to make the private decision-maker face the social cost."]),
    ("tradeable-permits", "Tradeable Permits", 3, 3, [
        "Cap-and-trade: the regulator sets a total quantity of allowable emissions and allocates permits that firms can buy and sell. Under certainty, the permit market replicates the Pigouvian tax outcome with the same efficiency.",
        "Permits fix quantities and let prices adjust; taxes fix prices and let quantities adjust. The choice between them under uncertainty is the Weitzman prices-vs-quantities question."]),
    ("weitzman-prices-vs-quantities", "Weitzman Prices vs Quantities", 3, 2, [
        "Under uncertainty about marginal costs (or benefits) of pollution control, taxes (price instruments) and permits (quantity instruments) differ. Weitzman (1974): taxes are preferred when the marginal damage curve is flatter than the marginal cost curve; permits are preferred when the marginal damage curve is steeper.",
        "Intuitively, if a small quantity error is catastrophic (steep damages), fix the quantity. If a small price shock is catastrophic but quantity is forgiving (steep costs, flat damages), fix the price."]),
    ("club-goods", "Club Goods", 3, 4, [
        "Non-rival but excludable goods (a private highway, a cable TV signal, a swimming club). The Buchanan club theory derives the optimal club size by trading off congestion costs against the cost of capacity."]),
    ("common-pool-resources", "Common Pool Resources", 3, 4, [
        "Rival but non-excludable: fisheries, groundwater, the atmosphere as a sink. Subject to the tragedy of the commons. Elinor Ostrom's work documents how communities sometimes solve this with informal norms rather than markets or regulation."]),
    ("clarke-tax", "Clarke Tax (Pivotal Mechanism)", 3, "S", [
        "The most prominent Clarke-Groves variant: a pivotal agent (one whose report changes the public-good decision) pays a tax equal to the harm their report imposes on others. Non-pivotal agents pay nothing. Truth-telling is a dominant strategy."]),
    ("vickrey-auction", "Vickrey (Second-Price) Auction", 3, "S", [
        "Single-good special case of the Clarke-Groves mechanism: the highest bidder wins and pays the second-highest bid. Bidding one's true value is a (weakly) dominant strategy. A canonical example of strategy-proof design."]),
    ("cap-and-trade", "Cap-and-Trade", 3, 3, [
        "Common name for tradeable emissions permits. The regulator sets a cap on total emissions; permits are auctioned or grandfathered; firms trade them. The EU ETS is the largest operating example. Equivalent to a Pigouvian tax under certainty."]),
    ("coasean-bargaining", "Coasean Bargaining", 3, 2, [
        "The negotiation process by which parties to an externality settle on the efficient quantity once property rights are clearly assigned. The Coase theorem says this works under zero transaction costs; in practice, transaction costs determine whether it does."]),

    # ===== TOPIC 4: GAME THEORY =====
    ("nash-equilibrium", "Nash Equilibrium", 4, 2, [
        "A strategy profile in which each player's strategy is a best response to the others. No player can improve their payoff by unilaterally deviating. This is the central solution concept of non-cooperative game theory.",
        "Nash equilibria exist in mixed strategies for every finite game (Nash's theorem). They may be unique (e.g., Prisoner's Dilemma) or multiple (e.g., Battle of the Sexes), and may not coincide with any reasonable notion of efficiency."]),
    ("mixed-strategy-equilibrium", "Mixed Strategy Equilibrium", 4, 4, [
        "A Nash equilibrium in which at least one player randomises over their pure strategies. In equilibrium, each player's mix makes the others indifferent across the strategies they themselves randomise over. That indifference condition is how you solve for the mixing probabilities.",
        "Mixed strategies are essential whenever no pure-strategy NE exists (e.g., Matching Pennies). They also arise in coordination games with multiple equilibria as a third symmetric equilibrium."]),
    ("dominance", "Dominance", 4, 3, [
        "A strategy is strictly dominant if it yields strictly higher payoff than any alternative regardless of opponents' play. A strategy is strictly dominated if some alternative strictly beats it everywhere. Rational players never play strictly dominated strategies.",
        "Iterated elimination of strictly dominated strategies (IESDS) reduces the game by repeatedly removing dominated strategies. The remaining set always contains every Nash equilibrium."]),
    ("subgame-perfect-equilibrium", "Subgame Perfect Equilibrium", 4, 2, [
        "A Nash equilibrium that induces a Nash equilibrium on every subgame, including those off the equilibrium path. Equivalently, found by backward induction in finite extensive-form games of perfect information.",
        "SPE rules out non-credible threats: a threat the player would not actually carry out if asked to. This is the key refinement of Nash in sequential games."]),
    ("backward-induction", "Backward Induction", 4, 4, [
        "Solving a finite-horizon sequential game by starting at the final decision nodes and working backwards. At each node, the player chooses the action that maximises their continuation payoff given the equilibrium play that follows.",
        "Backward induction yields the SPE in games of perfect information with no ties. The Centipede game and the Pirates puzzle are canonical illustrations."]),
    ("infinitely-repeated-games", "Infinitely Repeated Games", 4, 3, [
        "The same stage game is played in periods t = 0, 1, 2, ... with discount factor delta. Cooperation that is not a stage-game NE can be sustained as an SPE of the repeated game if delta is high enough and players use punishment strategies (e.g., grim trigger).",
        "The Folk Theorem says that for delta close to 1, essentially any individually rational payoff is achievable as an SPE. This makes the model rich but the equilibrium-selection problem severe."]),
    ("grim-trigger-strategy", "Grim Trigger Strategy", 4, 2, [
        "Cooperate as long as everyone has cooperated; defect forever after the first defection. This sustains cooperation when the present value of cooperation exceeds the gain from one-shot deviation plus the discounted punishment payoffs.",
        "Grim trigger gives the simplest critical discount factor for collusion: delta >= (g/(g+p)) where g is the one-shot deviation gain and p is the per-period punishment loss."]),
    ("critical-discount-factor", "Critical Discount Factor", 4, 3, [
        "The smallest delta for which a given cooperative outcome can be sustained as an SPE using a specified punishment strategy. Below this threshold, deviation pays. Comparative statics in delta tell you when collusion becomes harder to sustain (more firms, less frequent interaction)."]),
    ("folk-theorem", "Folk Theorem", 4, 4, [
        "For sufficiently patient players in an infinitely repeated game, any feasible payoff vector that gives every player at least their minmax value can be sustained as an SPE. The result is permissive: many things can happen, so the model needs additional structure to predict."]),
    ("best-response-functions", "Best Response Functions", 4, 2, [
        "Each player's best response function maps the opponent's strategy to the player's optimal reply. Nash equilibria are fixed points of the joint best-response map: each player is best responding to the other.",
        "Drawing best-response functions in a two-player game lets you read off pure-strategy NE as intersections. In Cournot, best responses slope downward (strategic substitutes); in differentiated Bertrand they slope upward (strategic complements)."]),
    ("affine-utility-normalisation", "Affine Utility Normalisation", 4, 4, [
        "Replacing the vNM utility u with v = a + b u (where b > 0) leaves preferences over lotteries unchanged. Best responses and Nash equilibria of a game are invariant under this transformation applied independently to each player."]),
    ("strategic-form-game", "Strategic Form Game", 4, 3, [
        "Specification of a game by (players, strategy sets, payoff functions). The most compact representation, suitable for simultaneous-move games. Sequential games are usually drawn in extensive form."]),
    ("extensive-form-game", "Extensive Form Game", 4, "S", [
        "Specification of a game as a tree of decision nodes, with the moving player and the action labels at each node. Captures the order of moves and what each player knows when moving."]),
    ("information-set", "Information Set", 4, "S", [
        "A set of decision nodes a player cannot distinguish among when choosing. Singleton information sets correspond to perfect information; non-singleton sets capture imperfect information (e.g., simultaneous moves embedded in a tree)."]),
    ("matching-pennies", "Matching Pennies", 4, 4, [
        "Canonical zero-sum 2x2 game with no pure-strategy NE. The unique equilibrium has each player mixing 50-50. The standard illustration of why mixed strategies are needed."]),
    ("battle-of-the-sexes", "Battle of the Sexes", 4, "S", [
        "2x2 coordination game with two asymmetric pure NE (both go to opera, both go to football) and a mixed NE. Illustrates equilibrium selection: which pure outcome occurs depends on focal points or communication, not the model alone."]),
    ("hawk-dove-game", "Hawk-Dove (Chicken) Game", 4, "S", [
        "Anti-coordination 2x2 game in which each player wants to do the opposite of the other (be Hawk if the other is Dove). Two asymmetric pure NE plus one mixed. Standard model for cuban-missile-style brinksmanship."]),
    ("iterated-elimination-strictly-dominated", "Iterated Elimination of Strictly Dominated Strategies", 4, "S", [
        "Recursively delete strictly dominated strategies until no further deletions are possible. The set that survives always contains every Nash equilibrium. Justified by common knowledge of rationality."]),
    ("strict-vs-weak-dominance", "Strict vs Weak Dominance", 4, 3, [
        "Strict dominance: strictly higher payoff against every opponent strategy. Weak dominance: at least as high everywhere, strictly higher somewhere. Iterated elimination of weakly dominated strategies is path-dependent and can remove NE; iterated elimination of strictly dominated strategies cannot."]),
    ("tit-for-tat", "Tit-for-Tat Strategy", 4, "S", [
        "Cooperate in the first period; thereafter copy the opponent's previous action. Won Axelrod's repeated Prisoner's Dilemma tournament twice. Less punishing than grim trigger but more forgiving."]),
    ("nash-reversion", "Nash Reversion Strategy", 4, "S", [
        "Punish a deviator by reverting permanently to one-shot Nash play. A milder punishment than minmax-then-revert, but easier to verify as an SPE because the punishment phase is itself a NE."]),
    ("strategic-substitutes-complements", "Strategic Substitutes vs Complements", 4, 3, [
        "Strategic substitutes: a more aggressive action by one player makes a less aggressive response optimal for the other (Cournot quantities). Strategic complements: aggression begets aggression (Bertrand prices). Determines whether reaction functions slope down or up and how shocks propagate."]),
    ("first-mover-advantage", "First-Mover Advantage", 4, 4, [
        "When commitment is valuable, the player who moves first can do better than in the simultaneous game. Stackelberg quantity competition is the leading example. Not universal: in some games (Bertrand-like, or matching pennies) moving first is a disadvantage."]),
    ("credible-threat", "Credible Threat", 4, 2, [
        "A threat to take an action whose execution is itself sequentially rational. Non-credible threats can support Nash equilibria but not SPE. The distinction matters in entry deterrence and bargaining models."]),
    ("nash-existence-theorem", "Nash Existence Theorem", 4, "S", [
        "Every finite game has at least one Nash equilibrium (in pure or mixed strategies). The proof uses Brouwer's or Kakutani's fixed-point theorem applied to the best-response correspondence."]),

    # ===== TOPIC 5: INDUSTRIAL ORGANISATION =====
    ("cournot-duopoly", "Cournot Duopoly", 5, 3, [
        "Two firms simultaneously choose quantities; market price clears total demand. Each firm's best response is downward sloping (strategic substitutes). The symmetric equilibrium has each firm producing $(a-c)/(3b)$ for linear demand $p = a - bQ$ and marginal cost c.",
        "Cournot lies between perfect competition and monopoly: price is above MC but below the monopoly level. As the number of firms grows, the equilibrium converges to the competitive outcome."]),
    ("bertrand-duopoly", "Bertrand Duopoly", 5, 3, [
        "Two firms simultaneously set prices for a homogeneous good; the lower-price firm captures all demand. The unique NE has both firms pricing at marginal cost, yielding zero profits. The 'Bertrand paradox' is that two firms suffice for the competitive outcome.",
        "The paradox is resolved by relaxing assumptions: differentiated products, capacity constraints, repeated interaction (collusion), or asymmetric costs all give positive markups."]),
    ("differentiated-bertrand", "Differentiated Bertrand", 5, 4, [
        "Firms set prices for imperfect substitutes. Linear demands such as $q_i = a - b p_i + d p_j$ generate upward-sloping best responses (strategic complements). The symmetric NE has positive markups that decrease as the substitution parameter d grows.",
        "Differentiation breaks the Bertrand paradox: with horizontally differentiated goods, firms compete on price but retain market power over their loyal segment."]),
    ("stackelberg-leadership", "Stackelberg Leadership", 5, "S", [
        "Sequential Cournot: leader chooses quantity first, follower observes and best responds. The leader's optimal quantity is higher than Cournot, exploiting the follower's downward-sloping best response. Gives a first-mover advantage that does not exist in simultaneous play."]),
    ("entry-deterrence", "Entry Deterrence", 5, 3, [
        "An incumbent firm taking actions before an entrant moves so that entry becomes unattractive. Classic strategies: capacity expansion (Dixit), advertising sunk costs, predatory pricing threats. Credibility requires that the deterrent action be sequentially rational.",
        "The Chain Store Paradox shows that simple backward induction unravels entry deterrence in finite games; resolutions involve incomplete information about the incumbent's type."]),
    ("merger-analysis", "Merger Analysis", 5, 3, [
        "Comparing pre- and post-merger market outcomes to decide whether a merger should be allowed. Standard inputs: changes in concentration (HHI), upward pricing pressure, possible efficiencies, and the Williamson trade-off between deadweight loss and cost savings."]),
    ("williamson-trade-off", "Williamson Trade-off", 5, 2, [
        "A merger that reduces marginal cost (efficiency gain) but also raises market power (price rise) can be welfare-improving if the cost saving on inframarginal output outweighs the deadweight loss on lost trades. The standard CBA tool for merger review.",
        "Diagrammatically: shaded rectangle of cost savings against shaded triangle of deadweight loss. Whether the rectangle exceeds the triangle is a quantitative question depending on demand elasticity and the size of cost cuts."]),
    ("collusion-sustainability", "Collusion Sustainability", 5, 1, [
        "Cartels sustain collusion when delta exceeds the critical discount factor for the relevant punishment strategy. Conditions that help collusion: few firms, frequent interactions, symmetric costs, transparent prices, stable demand, multimarket contact."]),
    ("hhi-index", "Herfindahl-Hirschman Index (HHI)", 5, "S", [
        "Sum of squared market shares (in percent), ranging from near 0 (atomistic) to 10000 (monopoly). Antitrust authorities use HHI thresholds (e.g., post-merger > 2500 with delta > 200 triggers scrutiny) as a screening rule for mergers."]),
    ("ssnip-test", "SSNIP Test", 5, "S", [
        "Small but Significant Non-transitory Increase in Price test. Used to define the relevant market for antitrust analysis: would a 5 to 10 percent price increase by a hypothetical monopolist over the candidate market be profitable? If yes, the market is defined narrowly enough."]),
    ("hotelling-linear-city", "Hotelling Linear City", 5, "S", [
        "Standard model of horizontal differentiation: consumers are uniformly distributed on a line, firms locate on the line, and each consumer buys from the nearest firm net of price. Generates rich predictions on location choice and price competition."]),
    ("price-discrimination", "Price Discrimination", 5, "S", [
        "Charging different prices to different consumers for the same good. First-degree: perfect (extract all surplus). Second-degree: by self-selection (different versions/bundles). Third-degree: by observable characteristics (student discounts). Welfare effects are ambiguous."]),
    ("two-part-tariff", "Two-Part Tariff", 5, "S", [
        "A pricing scheme with a fixed fee plus a per-unit price (e.g., gym membership plus per-class charge). Allows a monopolist to extract more surplus than a single per-unit price. Efficient when the per-unit price equals marginal cost and the fee captures surplus."]),
    ("leniency-programme", "Leniency Programme", 5, 3, [
        "Antitrust policy granting immunity (or reduced penalties) to the first cartel member to confess. Designed to destabilise collusion by making each member fear betrayal. Empirically successful in detecting cartels."]),
    ("uk-competition-act", "UK Competition Act 1998 and EU Articles 101-102", 5, "S", [
        "Statutory framework: Chapter I / Article 101 prohibits anti-competitive agreements (cartels). Chapter II / Article 102 prohibits abuse of dominance. The Enterprise Act 2002 adds criminal liability for individuals participating in cartels."]),

    # ===== TOPIC 6: DECISIONS UNDER RISK =====
    ("expected-utility", "Expected Utility", 6, 1, [
        "A decision-maker evaluates a lottery L by $E[u(L)] = \\sum_i p_i u(x_i)$, where u is the von Neumann-Morgenstern (vNM) utility function and the sum is over outcomes. The decision-maker prefers L to L' if and only if expected utility of L exceeds that of L'.",
        "Expected utility is not utility of the expected outcome: $E[u(L)] \\neq u(E[L])$ except under risk neutrality. For a risk-averse agent (u concave), $E[u(L)] < u(E[L])$, which generates the risk premium."]),
    ("von-neumann-morgenstern-axioms", "von Neumann Morgenstern Axioms", 6, 2, [
        "Four axioms on preferences over lotteries: completeness, transitivity, continuity, and independence. The vNM theorem says that preferences satisfying these axioms can be represented by expected utility with some utility function u, unique up to positive affine transformations.",
        "The axioms are normative: they say what a 'rational' chooser over risk should obey. Empirically, violations are common (Allais paradox tests independence)."]),
    ("independence-axiom", "Independence Axiom", 6, 2, [
        "If L is preferred to L', then any mixture (alpha L + (1-alpha) M) is preferred to (alpha L' + (1-alpha) M). Adding the same 'side lottery' M with the same probability does not change the ranking between L and L'.",
        "Independence is the substantive axiom of EU. The Allais paradox shows real subjects violate it: they care about the 'sure thing' aspect of one option in a way EU theory rules out."]),
    ("continuity-axiom", "Continuity Axiom", 6, 3, [
        "If L is preferred to M and M is preferred to N, then there is a probability p such that the lottery (p L + (1-p) N) is indifferent to M. Equivalent to saying preferences over lotteries are continuous in probabilities.",
        "Continuity rules out lexicographic preferences over lotteries (e.g., 'I will accept any chance of death to save a million pounds, but no chance of death for any smaller amount'). Required for the existence of a utility representation."]),
    ("reduction-of-compound-lotteries", "Reduction of Compound Lotteries", 6, 4, [
        "A compound lottery (a lottery over lotteries) is treated as equivalent to the simple lottery obtained by multiplying out the probabilities. The decision-maker cares only about the final distribution over outcomes, not the procedural structure.",
        "Reduction is sometimes treated as an axiom and sometimes as a definition. Violations include preferences for 'feeling lucky' or for procedural fairness."]),
    ("risk-aversion", "Risk Aversion", 6, 2, [
        "An agent is risk averse if u is strictly concave: for any non-degenerate lottery, the agent strictly prefers the expected value of the lottery to the lottery itself. Equivalently, the certainty equivalent is below the expected value, and the risk premium is positive.",
        "Risk aversion reflects diminishing marginal utility of wealth: an extra pound matters more when poor than when rich. This is the workhorse assumption for almost every applied risk problem."]),
    ("certainty-equivalent", "Certainty Equivalent", 6, 2, [
        "The certainty equivalent (CE) of a lottery is the amount of certain wealth that leaves the agent indifferent to the lottery: $u(CE) = E[u(L)]$. For a risk-averse agent, $CE < E[L]$; the gap is the risk premium.",
        "The CE is the most useful single-number summary of how an agent values a risky prospect. It is used to derive insurance demand, optimal portfolio choice, and willingness to pay for risk reduction."]),
    ("risk-premium", "Risk Premium", 6, 3, [
        "The risk premium $\\pi$ of a lottery is the difference between its expected value and its certainty equivalent: $\\pi = E[L] - CE$. It measures how much the agent would pay to convert the lottery into a sure thing.",
        "For small risks, the Arrow-Pratt approximation gives $\\pi \\approx \\frac{1}{2} A(w) \\sigma^2$, where A(w) is absolute risk aversion and sigma^2 is the variance. Risk premium scales with variance and curvature of utility."]),
    ("arrow-pratt-ara", "Arrow-Pratt ARA", 6, 1, [
        "$A(w) = -u''(w)/u'(w)$. Measures the curvature of utility in dollars: how much risk premium the agent demands for a small gamble of given variance. Higher A means more risk-averse.",
        "ARA's comparative statics distinguish CARA (constant), DARA (decreasing in wealth, the empirically reasonable case), and IARA (increasing, exotic) utilities. DARA implies wealthy people accept more dollar risk."]),
    ("arrow-pratt-rra", "Arrow-Pratt RRA", 6, 4, [
        "$R(w) = w A(w) = -w u''(w)/u'(w)$. Measures risk aversion to proportional gambles (e.g., a 10 percent gain or loss). Constant RRA (CRRA) means the agent's appetite for proportional risk does not depend on their wealth level, which fits broad stylised facts.",
        "Log utility has RRA = 1 everywhere. Power utility $u(w) = w^{1-\\gamma}/(1-\\gamma)$ has RRA = gamma. CRRA is the standard functional form in finance and macroeconomics."]),
    ("cara-utility", "CARA Utility", 6, 1, [
        "Constant Absolute Risk Aversion: $u(w) = -e^{-a w}/a$ for $a > 0$. ARA is constant at $a$. Wealth does not affect the risk premium for a given dollar gamble, which is unrealistic but tractable.",
        "CARA shines under normally distributed wealth: $CE = E[w] - \\frac{1}{2} a \\sigma^2$. This is the basis of mean-variance analysis and Holmstrom-Milgrom linear contracts."]),
    ("crra-utility", "CRRA Utility", 6, 1, [
        "Constant Relative Risk Aversion: $u(w) = w^{1-\\gamma}/(1-\\gamma)$ for $\\gamma \\neq 1$, with log utility as the limiting case at $\\gamma = 1$. RRA is constant at gamma; ARA decreases with wealth.",
        "The workhorse utility function in finance (asset pricing, portfolio choice) and growth theory (Ramsey-Cass-Koopmans). Captures the stylised fact that the rich and the poor seem to demand similar fractions of their wealth for proportional gambles."]),
    ("dara-utility", "DARA Utility", 6, 1, [
        "Decreasing Absolute Risk Aversion: A'(w) < 0. The agent demands a smaller dollar risk premium as wealth grows. Standard assumption because it matches the empirical fact that wealthier people invest a larger absolute amount in risky assets.",
        "Log utility, CRRA with gamma < infinity, and many other reasonable forms exhibit DARA. The classic 2017 Q3 Part A question exploits this property in u(w) = 2 sqrt(w)."]),
    ("first-order-stochastic-dominance", "First-Order Stochastic Dominance", 6, 2, [
        "L FOSDs L' if $F_L(x) \\leq F_{L'}(x)$ for all x, with strict inequality somewhere. Equivalently, L gives at least as much probability to every upper tail. Every expected-utility maximiser with weakly increasing u prefers L to L'.",
        "FOSD is a strong dominance: it does not require knowledge of the agent's curvature, only that they prefer more wealth. Useful for ruling out one lottery without specifying risk attitude."]),
    ("second-order-stochastic-dominance", "Second-Order Stochastic Dominance", 6, 2, [
        "L SOSDs L' if every risk-averse expected-utility maximiser prefers L to L'. Equivalently, $\\int_{-\\infty}^x F_L(t) dt \\leq \\int_{-\\infty}^x F_{L'}(t) dt$ for all x, with equal means.",
        "SOSD captures 'mean-preserving spread' reductions: L and L' have the same mean, but L is less spread out. Less restrictive than FOSD, more restrictive than expected utility plus any utility function."]),
    ("risk-pooling", "Risk Pooling", 6, 4, [
        "Sharing independent risks across many agents reduces per-capita variance, so a profitable but risky project becomes acceptable when shared. The classic insurance principle: many small independent risks averaged are nearly riskless.",
        "Risk pooling differs from risk sharing: pooling exploits independence to reduce variance per capita, sharing simply divides a fixed total risk among more agents."]),
    ("state-space-insurance-diagram", "State-Space Insurance Diagram", 6, 2, [
        "Axes are wealth in state 1 (no loss) and state 2 (loss). The endowment is below the 45-degree line. Fair-odds budget lines through the endowment slope as $-p_1/p_2 = -(1-\\pi)/\\pi$. Indifference curves are convex, with slope at the 45-degree line equal to the same fair-odds ratio.",
        "Full insurance corresponds to the 45-degree line (equalised wealth across states). Risk-averse agents with fair-priced insurance fully insure; with actuarially unfair insurance, they partially insure."]),
    ("fair-premium", "Fair Premium", 6, 4, [
        "An insurance premium equal to the expected loss. With fair pricing, the insurer breaks even in expectation and the consumer transfers risk costlessly. A risk-averse agent always fully insures at fair prices; underinsurance arises only when premiums are unfair."]),
    ("allais-paradox", "Allais Paradox", 6, 3, [
        "Empirical finding that most subjects violate the independence axiom in a specific way: they over-weight certainty. Demonstrates that real preferences over lotteries are not (always) expected utility. The most-cited evidence against EU as a positive theory."]),
    ("st-petersburg-paradox", "St Petersburg Paradox", 6, "S", [
        "A coin-flip lottery paying $2^n$ if heads first appears on flip n has infinite expected value, but most people would pay only a small amount to play. Bernoulli's resolution: use a concave utility (log) over outcomes. The historical origin of expected utility theory."]),
    ("dutch-book-argument", "Dutch Book Argument", 6, "S", [
        "If your preferences over lotteries violate EU axioms, a bookmaker can offer you a sequence of bets you would each accept individually but which together leave you sure to lose money. The standard normative defence of EU theory."]),
    ("mean-variance-utility", "Mean-Variance Utility", 6, 2, [
        "Under CARA utility and normally distributed wealth, $CE = E[w] - \\frac{a}{2} \\sigma^2$. The agent maximises mean minus a scaled variance. This collapses the dimensionality of the choice problem to two statistics and underlies modern portfolio theory."]),
    ("mean-preserving-spread", "Mean-Preserving Spread", 6, 3, [
        "A transformation that adds noise to a random variable without changing its mean. Increases variance and (more generally) spreads probability mass to the tails. Rothschild-Stiglitz: L is SOSD by L' iff L' is obtained from L by adding mean-preserving spreads."]),

    # ===== TOPIC 7: ADVERSE SELECTION =====
    ("adverse-selection", "Adverse Selection", 7, 1, [
        "When one side of a market has private information about its type before contracting, the uninformed side faces an adverse selection of types willing to trade at a given price. The classic example is Akerlof's used-car market.",
        "Adverse selection can shut down trade entirely (full unravelling) or reduce its scope. Solutions include signalling (informed party reveals type) and screening (uninformed party offers a menu inducing self-selection)."]),
    ("akerlof-lemons-market", "Akerlof Lemons Market", 7, 2, [
        "Sellers know the quality of their used cars; buyers do not. At any single price, only the lowest-quality cars willing to sell at that price are offered. Buyers anticipate this and offer a low price, which drives out medium-quality cars, and so on.",
        "In the extreme, the market unravels completely: only the worst cars are traded, or no cars trade at all. The Nobel-cited 1970 paper that launched information economics."]),
    ("full-unravelling", "Full Unravelling", 7, 2, [
        "When all types choose to participate, the unique adverse-selection equilibrium has only the lowest type trading (or sometimes no trade at all). The mechanism: at any pooled price, the highest-value types drop out, lowering the average quality, lowering the price, and pushing more types out."]),
    ("spence-signalling", "Spence Signalling", 7, 2, [
        "High-productivity workers undertake costly education to signal their type to employers. In a separating equilibrium, the cost of education is high enough that low-productivity workers will not mimic, so the signal is credible.",
        "Spence showed that even when education has no productive value, it can be a useful signal because it sorts workers by type. Welfare implication: signalling burns resources but reveals information that was otherwise hidden."]),
    ("single-crossing-property", "Single Crossing Property", 7, 2, [
        "Indifference curves of different types cross at most once: the high type has a relatively lower marginal cost of the signal than the low type. Equivalently, the marginal rate of substitution between signal and reward differs monotonically across types.",
        "Single crossing is necessary for separating equilibria to exist: it ensures one type cares enough less about the signal cost relative to the wage payoff that they alone find it worthwhile."]),
    ("separating-vs-pooling", "Separating vs Pooling Equilibrium", 7, 3, [
        "In a separating equilibrium, different types choose different signals (or contracts), revealing their type to the uninformed party. In a pooling equilibrium, all types choose the same signal, leaving the uninformed party with the prior distribution.",
        "Spence-style signalling games typically have multiple equilibria, both separating and pooling. Refinements like the intuitive criterion are used to select among them."]),
    ("intuitive-criterion", "Intuitive Criterion", 7, 2, [
        "An equilibrium refinement that restricts out-of-equilibrium beliefs in signalling games. If an off-path signal is dominated for type L but not for type H, the receiver should believe it came from H. Rules out pooling equilibria where H could profitably deviate to a separating signal.",
        "The intuitive criterion typically selects the Riley outcome: the unique separating equilibrium with the lowest signal level (least-cost separation)."]),
    ("rothschild-stiglitz-screening", "Rothschild-Stiglitz Screening", 7, 2, [
        "Competitive insurers offer a menu of contracts; consumers self-select. In a separating equilibrium, high-risk types get full insurance at a fair premium; low-risk types accept partial coverage at a fair premium (the IC binding constraint).",
        "The model can fail to have an equilibrium when low-risk types are sufficiently common (a pooling contract would attract them and break the candidate separating contracts). This existence issue is a major theoretical wrinkle."]),
    ("state-space-rothschild-stiglitz", "State-Space Diagram (Rothschild-Stiglitz)", 7, 2, [
        "Axes are wealth in no-loss state and loss state. Endowment E sits below the 45-degree line. H's fair-odds line is steeper than L's. H gets full insurance on H's fair-odds line. L gets the contract on L's fair-odds line that just makes H indifferent to taking the H-contract."]),
    ("fair-odds-line", "Fair Odds Line", 7, 2, [
        "In a state-space insurance diagram, the locus of insurance contracts that breaks even for the insurer on a given risk pool. Its slope equals the loss probability ratio. Each risk type has its own fair-odds line through the endowment."]),
    ("reimbursement-contracts", "Reimbursement Contracts", 7, 4, [
        "A contract that pays a partial refund if the good turns out to be defective. With appropriate reimbursement, asymmetric-information markets can sometimes restore efficiency (e.g., 2018 Q4 used bicycle with reimbursement of 50)."]),
    ("asymmetric-information", "Asymmetric Information", 7, 3, [
        "One party to a transaction has more information than the other. The textbook taxonomy: adverse selection (hidden type, pre-contracting) and moral hazard (hidden action, post-contracting). Information asymmetry breaks the first welfare theorem."]),
    ("hidden-information-vs-hidden-action", "Hidden Information vs Hidden Action", 7, 2, [
        "The two pure types of information asymmetry. Hidden information (adverse selection): type is private before contracting. Hidden action (moral hazard): effort is private after contracting. Many real situations involve both."]),
    ("riley-outcome", "Riley Outcome", 7, "S", [
        "The unique separating equilibrium that survives standard refinements in signalling games: the least-cost separating equilibrium. Each type sends the smallest signal compatible with separation."]),
    ("wilson-refinement", "Wilson Equilibrium Refinement", 7, "S", [
        "In Rothschild-Stiglitz models, allowing insurers to withdraw contracts that become unprofitable in response to other firms' entry. Restores equilibrium existence in cases where the basic model has none."]),
    ("partial-unravelling", "Partial Unravelling", 7, "S", [
        "An adverse-selection equilibrium in which some, but not all, types participate. The Akerlof model with a finite type distribution typically has equilibria with cutoff types: everyone below a threshold trades, everyone above stays out."]),
    ("multiple-equilibria-lemons", "Multiple Equilibria in Lemons Markets", 7, 4, [
        "Akerlof's used car model can have several equilibria: an active high-quality market, an intermediate market with some withdrawal, and a collapsed market. Coordination on which equilibrium prevails depends on beliefs."]),
    ("winners-curse", "Winner's Curse", 7, "S", [
        "In a common-value auction, the winning bidder is the one whose value estimate was most optimistic. Rational bidders shade their bids down to account for this. The phenomenon is a form of adverse selection over information."]),
    ("pooling-equilibrium", "Pooling Equilibrium", 7, 4, [
        "An equilibrium in which all types of the informed party choose the same action (e.g., all worker types choose the same education level). The receiver cannot infer type from the signal and uses the prior distribution.",
        "Contrasted with separating equilibria, where types choose different actions. Pooling can be Pareto-inferior to separating when signalling resources are wasted; or Pareto-superior when separation is even more wasteful."]),
    ("conspicuous-consumption", "Conspicuous Consumption (Veblen Goods)", 7, "S", [
        "Demand rising with price because the high price is a signal of status. A specific application of signalling: the consumer signals wealth or sophistication via the wasteful expenditure. Equivalent to Zahavi's handicap principle in evolutionary biology."]),

    # ===== TOPIC 8: MORAL HAZARD =====
    ("moral-hazard", "Moral Hazard", 8, 2, [
        "After a contract is signed, the agent takes an action (effort) that the principal cannot observe but that affects the joint payoff. The agent's incentive to exert effort depends on the wage schedule, generating a trade-off between insurance and incentives.",
        "The canonical example is insurance: insured drivers may drive less carefully because the insurer bears the cost of accidents. Solutions include partial coverage, deductibles, and performance-contingent contracts."]),
    ("principal-agent-problem", "Principal-Agent Problem", 8, 1, [
        "A principal (employer, owner, government) hires an agent (worker, manager, contractor) whose effort is unobservable but affects output. The principal designs a wage schedule maximising expected profit subject to the agent's participation (IR) and incentive (IC) constraints.",
        "The first-best solution (with observable effort) pays a flat wage and forces the efficient effort. With unobservable effort, the second-best balances incentives against risk imposition on the agent, generating agency cost."]),
    ("individual-rationality", "Individual Rationality", 8, 1, [
        "The agent must receive at least their reservation utility ($\\bar u$) in expectation, otherwise they will not accept the contract. IR pins down the level of expected utility the agent gets; in the second-best optimum it binds (the principal extracts all surplus above the outside option)."]),
    ("incentive-compatibility", "Incentive Compatibility", 8, 1, [
        "The agent must prefer the principal's desired action (e.g., high effort) over any deviation. IC is the constraint that turns the principal's effort-implementation problem into a constrained optimisation: a wage schedule must reward the desired action enough to overcome the cost difference."]),
    ("first-best-contract", "First-Best Contract", 8, 2, [
        "When effort is observable (or output perfectly reveals effort), the principal can pay a constant wage conditional on the desired effort. The risk-averse agent fully insured; the risk-neutral principal bears all output risk. First-best implements the efficient effort level."]),
    ("second-best-contract", "Second-Best Contract", 8, 2, [
        "When effort is unobservable, the principal must use output as a noisy signal of effort. The optimal contract pays a higher wage in high-output states to satisfy IC, but this imposes risk on the agent, who must be compensated for it (raising the IR-binding wage).",
        "The second-best is strictly inferior to the first-best: there is a deadweight loss called the agency cost. The size of the agency cost depends on the agent's risk aversion and the noisiness of the output signal."]),
    ("agency-cost", "Agency Cost", 8, 1, [
        "The difference between the principal's expected profit under the first-best (observable effort) and the second-best (unobservable effort) contracts. Measures the welfare loss from the information asymmetry, expressed in pounds.",
        "Agency cost rises with the agent's risk aversion, with the variance of output given effort, and with the gap between marginal product of effort across states. It falls to zero when effort is verifiable or when the agent is risk-neutral."]),
    ("linear-contracts", "Linear Contracts", 8, 3, [
        "Wage $w = t + s x$ where x is observable output, t is a base wage, and s is the slope of incentive intensity. Optimal in Holmstrom-Milgrom's CARA-normal model: $s^* = 1/(1 + r \\sigma^2 c)$.",
        "Higher agent risk aversion r, higher output noise sigma^2, or higher effort cost convexity c all reduce optimal s. The trade-off between insurance (flat wage) and incentives (steep wage) is sharpest in this model."]),
    ("revenue-sharing", "Revenue Sharing", 8, 4, [
        "A contract paying the agent a fixed share of revenue (e.g., 30 percent commission). A special case of linear contracts with t = 0. Used widely in sharecropping, sales commissions, and real estate brokerage."]),
    ("risk-vs-insurance-tradeoff", "Risk vs Insurance Trade-off", 8, 2, [
        "Steeper wage schedules give the agent stronger incentives to exert effort but expose them to more output risk, raising the wage premium required to satisfy IR. Flatter wages insure the agent against output risk but weaken incentives. The optimal contract balances these.",
        "The trade-off vanishes if the agent is risk neutral (sell the firm to the agent and get the first-best) or if output perfectly reveals effort (set wage on output)."]),
    ("wage-bounds-limited-liability", "Wage Bounds Limited Liability", 8, 4, [
        "When wages cannot go below a floor (e.g., $w \\geq 0$ or $w \\geq -100$), the principal cannot impose arbitrarily large punishments for low output. This binds in second-best problems with very risky output and amplifies agency cost.",
        "Under limited liability, the agent earns rents (utility above the reservation level) because the principal cannot extract them via large penalties for bad outcomes."]),
    ("monotone-likelihood-ratio", "Monotone Likelihood Ratio", 8, 4, [
        "If the likelihood ratio $f(x|e_H) / f(x|e_L)$ is increasing in output x, then the optimal second-best wage schedule is increasing in x. MLRP guarantees the natural intuition that higher output should be rewarded with higher wages."]),
    ("peltzman-effect", "Peltzman Effect", 8, 4, [
        "When safety regulations make a dangerous activity safer (e.g., seatbelts, helmets, better roads), agents respond by behaving more riskily. A specific form of moral hazard in which the agent compensates for reduced risk by taking more of it. Empirically supported in some contexts, contested in others."]),
    ("holmstrom-milgrom-model", "Holmstrom-Milgrom Linear Contracts Model", 8, 1, [
        "An extension of the static principal-agent model to continuous time with Brownian noise. Shows that under CARA utility and normally distributed output, the optimal contract is linear in observed output. Used to justify linear pay-for-performance schemes."]),
    ("multitasking", "Multitasking", 8, "S", [
        "When the agent allocates effort across multiple tasks (some measurable, some not), incentivising the measurable task can distort effort away from the unmeasurable one. The Holmstrom-Milgrom multi-task model: pay for performance can backfire when output measures are incomplete."]),
    ("selling-the-firm", "Selling the Firm to the Agent", 8, 3, [
        "A theoretical solution to moral hazard: the principal sells the firm to the agent for an upfront fee equal to expected profit. The agent then bears all output risk and chooses first-best effort. Fails when the agent is risk-averse: they would not accept the deal because they cannot bear the risk."]),
    ("insurance-moral-hazard", "Moral Hazard in Insurance", 8, "S", [
        "Insured agents bear less of the cost of an accident and so take less care to avoid it. Insurers respond with partial coverage, deductibles, no-claims discounts, and exclusions. The standard practical example of moral hazard."]),
    ("repeated-moral-hazard", "Repeated Moral Hazard", 8, "S", [
        "Long-term contracting between principal and agent in which past performance affects future wages. Repeated interaction can mitigate the agency cost by spreading incentives over time and using career concerns. Heart of efficiency-wage and career-concerns literatures."]),
]

# Where the existing concepts from the original Concept Index that are still
# missing from CONCEPTS above? Let's complete the list:

# Sanity check after building all CONCEPTS:
def coverage_check():
    expected_from_index = [
        "Expected Utility", "Incentive Compatibility", "Quasi-linear Utility", "CARA Utility",
        "Competitive Equilibrium", "Pigouvian Tax", "Agency Cost", "Arrow-Pratt ARA",
        "CRRA Utility", "DARA Utility", "Individual Rationality", "Principal-Agent Problem",
        "Samuelson Condition", "Adverse Selection", "Independence Axiom", "Lindahl Prices",
        "Moral Hazard", "Akerlof Lemons Market", "Certainty Equivalent", "Free Rider Problem",
        "Full Unravelling", "Intuitive Criterion", "Nash Equilibrium", "Pareto Efficiency",
        "Risk Aversion", "Second-Best Contract", "Voluntary Contribution Nash Equilibrium",
        "Williamson Trade-off", "von Neumann Morgenstern Axioms", "Best Response Functions",
        "Clarke-Groves Mechanism", "Coase Theorem", "Externality Internalisation",
        "Fair Odds Line", "First-Best Contract", "Marginal Private vs Social Benefit",
        "Risk vs Insurance Trade-off", "Rothschild-Stiglitz Screening",
        "Second-Order Stochastic Dominance", "Single Crossing Property", "Spence Signalling",
        "Tragedy of the Commons", "Cobb-Douglas Demand", "First-Order Stochastic Dominance",
        "Grim Trigger Strategy", "Merger Analysis", "Pareto Criterion", "Public Goods",
        "Risk Premium", "Second Welfare Theorem", "Subgame Perfect Equilibrium",
        "Weitzman Prices vs Quantities", "Bertrand Duopoly", "Continuity Axiom",
        "Cournot Duopoly", "Critical Discount Factor", "Entry Deterrence", "Excess Demand",
        "First Welfare Theorem", "Infinitely Repeated Games", "Kaldor-Hicks Compensation",
        "PPF and MRT", "Rivalry and Excludability", "Separating vs Pooling Equilibrium",
        "Social Welfare Functions", "Asymmetric Information", "Dominance", "Edgeworth Box",
        "Linear Contracts", "Ricardian Trade Model", "Tradeable Permits", "Walras Law",
        "Affine Utility Normalisation", "Arrow-Pratt RRA", "Backward Induction",
        "Differentiated Bertrand", "Fair Premium", "Folk Theorem", "Mixed Strategy Equilibrium",
        "Pooling Equilibrium", "Reduction of Compound Lotteries", "Reimbursement Contracts",
        "Revenue Sharing", "Risk Pooling", "Monotone Likelihood Ratio", "Peltzman Effect",
        "Rawlsian Planner", "Utilitarian Planner", "Wage Bounds Limited Liability",
        "State-Space Insurance Diagram",
    ]
    names = {c[1] for c in CONCEPTS}
    missing = [e for e in expected_from_index if e not in names]
    return missing

if __name__ == "__main__":
    missing = coverage_check()
    print(f"Total concepts: {len(CONCEPTS)}")
    print(f"Total topics: {len(TOPICS)}")
    print(f"Concept Index entries not yet in CONCEPTS: {len(missing)}")
    for m in missing:
        print(f"  - {m}")
