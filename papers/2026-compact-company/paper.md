---
title: "The Compact Company: An Actor-Graph Theory of the Firm in the LLM Era"
author:
  - name: Alexander Vityaz
    orcid: 0009-0006-0489-7881
    affiliation: Corezoid Inc., Dnipro, Ukraine
date: 2026-08-03
doi: 10.5281/zenodo.21774758
version: v1
license: CC-BY-4.0
keywords: [Compact Company, theory of the firm, Coase, boundary of the firm, actor graph, LLM, large language models, AI agents, Digital Twin of an Organization, Good Regulator, requisite variety, organizational succession, resilience, transaction costs, opacity rent, human reserve]
---

> **Note.** This markdown version is provided for convenient reading on GitHub. Mathematical notation and figures are authoritative in [paper.pdf](paper.pdf) and in the version of record: [doi:10.5281/zenodo.21774758](https://doi.org/10.5281/zenodo.21774758).

# The Compact Company: An Actor-Graph Theory of the Firm in the LLM Era

Alexander Vityaz · *Corezoid Inc., Dnipro, Ukraine* · ORCID: [0009-0006-0489-7881](https://orcid.org/0009-0006-0489-7881)

## Abstract

This paper introduces the **Compact Company** as a distinct category in organizational theory. A Compact Company is an organizationally closed firm whose human core is minimized by cost or headcount while remaining sufficient to satisfy legal, governance, capacity, and probabilistic viability requirements. The category is distinct from one-person, small, virtual, lean, and AI-native businesses. Most of its operational and regulatory variety is realized by an executable graph of human, software, LLM, agentic, and external actors.

The economic mechanism behind this organizational form arises from the ability of large language models to reduce the costs of semantic coordination: interpreting incomplete instructions, decomposing tasks, transferring context, preparing decisions, and processing standard exceptions. This shift changes the Coasean choice between the market and internal organization. Its effects may contract the firm along one dimension while expanding it along another: the human core can shrink as the number and variety of controlled transactions increase.

The theoretical object of the paper is a typed temporal actor graph. Its contribution lies not in a new graphical notation but in four constructions. First, the paper introduces an organizationalclosure operator that uses weak probabilistic bisimulation to represent an internal graph as a composite institutional actor while preserving the type distinction between a graph and a node. Second, it defines the boundary of the firm as an operator that attributes a particular transaction across authority, accountability, data regime, economic outcome, and control. Third, it formalizes continuity and succession through the resilience of the authority-and-state graph to families of individual and correlated failures. Fourth, it formulates compactness as the minimization of the human core under viability constraints and shows that even a simplified version of the problem is NP-hard by reduction from Minimum Set Cover.

The Conant–Ashby Good Regulator Theorem is applied within its proper scope. It rules out effective regulation without model correspondence while remaining agnostic about the medium that carries the model. This paper advances an independent thesis: for a compact digital firm, an executable digital twin provides the most complete non-personal carrier of critical organizational state and policy. The actor graph supplies the theory of the company; the digital twin provides its synchronized, versioned, and executable embodiment.

The transition to a Compact Company constitutes an institutional migration. The explication of roles, authority, and organizational state redistributes power and reduces opacity rents. A minimal human core must therefore preserve formal resilience together with a verifiable capacity for human response through hot and warm reserves.

**Keywords:** Compact Company; theory of the firm; Coase; boundary of the firm; actor graph; LLM; AI agents; Digital Twin of an Organization; Good Regulator; requisite variety; organizational succession; resilience; transaction costs; opacity rent; human reserve.

## **1 Introduction: A Company Must Outlive Any Individual Participant** 

LLMs have produced an appealing image of a one-person company surrounded by numerous software agents. The image demonstrates the growth of individual productivity; a theory of the firm requires a stronger institutional account. 

A person sleeps, becomes ill, loses connectivity, exits the business, and ultimately leaves the organization forever. When that person’s unavailability extinguishes authority, memory, the capacity to discharge obligations, and the means to restore control, the arrangement remains a personal activity wrapped in legal form. It lacks the continuity of a resilient organization. 

Incorporation and the first hire mark legal and staffing events. Organizational autonomy begins when the company can: 

- continue critical operations without the permanent presence of any single person; 

- recover unfinished obligations and the grounds for earlier decisions; 

- transfer a role together with its state, rights, and context; 

- retain control over assets and external interfaces; 

- restore governance legitimately after the temporary or permanent loss of a participant. 

LLMs preserve this requirement and make it achievable with a substantially smaller human core. The relevant frontier is therefore the **boundary of the minimally sufficient organization** . 

This paper proposes the term **Compact Company** . The novelty lies in a specific definition of the organizational form through: 

1. the organizational closure of a heterogeneous actor graph; 

2. minimization of the human core under viability constraints; 

3. a transactional boundary of the firm; 

4. a non-personal carrier of critical state; 

5. an executable Digital Twin of the Organization. 

The central hypothesis has a conditional and concrete form: 

In activities where a substantial share of coordination occurs through language and digital interfaces, outcomes are observable, and critical actions admit verification, LLM-enabled reductions in the cost of semantic coordination create directional economic pressure toward the Compact Company: a minimally sufficient human core around a large executable graph of actors. 

The hypothesis applies to a growing share of digitally mediated economic activity. Physical production, medicine, care, education, construction, security, public authority, and many licensed professions retain substantial human constraints. Across digitally representable activities, however, a large permanent human apparatus increasingly ceases to be a prerequisite for organizational complexity. 

The paper pursues five objectives. 

First, it establishes a precise boundary around the concept of the Compact Company and distinguishes it from adjacent terms. 

Second, it identifies the economic mechanism through which LLMs change the Coasean boundary of the firm. 

Third, it defines the actor graph as an independent object in the theory of the firm and as more than a practical language for model construction. 

Fourth, it derives testable results concerning the firm’s boundary, organizational succession, and the complexity of designing a compact human core. 


Fifth, it specifies the place of the digital twin as the proposed executable embodiment of the actorgraph model of the company. This proposition extends beyond the logical content of the Good Regulator Theorem. 

## **2 Defining the Compact Company** 

### **2.1 Working Definition** 

Let a firm be represented by an organizational model 𝒪𝑡, a human core 𝐻𝑡, a set of critical functions 𝐾, a family of admissible failure scenarios 𝔉𝑘, an admissible recovery time Δ, and a residual-risk level 𝜀. 

**Definition 1** (Compact Company) **.** A Compact Company is an organizationally closed firm whose human core is minimized by cost or headcount while simultaneously satisfying: 

1. legal requirements concerning legal personality, governing bodies, and personal accountability; 

2. requirements for segregation of authority and independent verification; 

3. human-reserve capacity requirements for handling non-automatable exceptions; 

4. (𝑘, Δ, 𝜀)-viability requirements relative to a specified family of failures; 

5. the requirement that critical organizational state be stored in a non-personal form; 

6. the requirement that actions be attributable to a single institutional actor. 

A substantial share of the firm’s operational and regulatory variety is realized in a synchronized and executable digital twin represented as a graph of human, software, LLM, agentic, and external actors. 

The definition contains no separate postulate requiring more than one person. Multiplicity follows from resilience, segregation-of-duties, or legal requirements. For 𝑘≥1, an organization wholly dependent on a single human bearer of control fails to satisfy the definition. 

### **2.2 Compactness as an Architectural Property** 

A small enterprise is usually defined through external quantitative attributes such as headcount, turnover, or asset volume. Compactness is an internal architectural property. 

A ten-person company may qualify as small while remaining structurally non-compact when: 

- every critical relationship converges on the founder; 

- the state of obligations exists in personal correspondence; 

- rights cannot be transferred without the manual intervention of one person; 

- independent verification is absent; 

- the loss of one specialist halts a critical process. 

Conversely, several dozen people may form the compact core of a company that serves millions of customers, coordinates thousands of software and external actors, and operates across multiple jurisdictions. 

Compactness therefore characterizes the ratio of controlled variety to the human core under preserved resilience. Absolute size alone provides no such measure. 


### **2.3 Adjacent Concepts** 

Table 1: Adjacent concepts and their relation to the Compact Company. 

|**Concept**|**Defining Feature**|**Relation to the Compact Company**|
|---|---|---|
|One-person busi-<br>ness|Activity of a single owner|Organizational continuity may remain dependent on the<br>owner|
|Small enterprise|Statistical threshold for<br>headcount or turnover|Architecture, succession, and boundary remain unspeci-<br>fed|
|Lean organization|Elimination of waste|Actor-graph modeling and a digital twin are optional|
|Virtual corporation|Geographically and contrac-<br>tually distributed execution|Coordination may remain manual and personalized|
|Hollow corporation|Small core with production<br>externalized|Action attribution and succession remain unspecifed|
|Exponential Organi-<br>zation|Scaling through external<br>resources, algorithms, and<br>interfaces|Growth is the defining concern; institutional viability lies<br>outside the category’s core criterion|
|AI-native company|Deep use of AI|AI adoption alone leaves the shared model, accountability,<br>and closure unresolved|
|Autonomous organi-<br>zation|Machine autonomy|Machine autonomy may obscure human legitimacy and<br>residual accountability|
|Compact Company|Minimally sufficient core,<br>closed graph, transactional<br>boundary, and verifiable<br>succession|A distinct organizational category|


A concise formula for the term is: 

**A Compact Company is a minimally sufficient human core within a large, executable, and succession-capable graph of actors.** 

## **3 Related Work: Positioning the Concept among Theories of the Firm and Organizational Models** 

The theory of the Compact Company emerges at the intersection of the economics of the firm, cybernetics, organizational theory, multi-agent systems, enterprise modeling, and digital twins. Each of these traditions already contains substantial theoretical machinery. The contribution therefore rests on a precise synthesis and on consequences that can be derived from that synthesis. 

### **3.1 Coase, Williamson, and the Boundary of the Firm** 

Coase explained the existence of the firm through the costs of using the price mechanism. A firm substitutes administrative coordination for a subset of market transactions and expands until the internal organization of an additional transaction ceases to be cheaper than using the market or another firm [1]. This foundation remains central to the present paper. 

Williamson extended the Coasean program through transaction-cost economics, asset specificity, uncertainty, opportunism, and the comparative analysis of governance structures [2, 3]. In Williamsonian terms, LLMs can reduce both _ex ante_ specification costs and _ex post_ adaptation and monitoring costs. They also create new specific dependencies on models, providers, data, tool environments, and verification methods. The resulting effect on the make-or-buy decision is therefore directionally ambiguous. 

This paper extends that line of inquiry through a new representation of the firm’s boundary. In the classical formulation, a transaction is organized within the firm or through the market. A hybrid agentic infrastructure permits a single executor to be external in ownership and computing infrastructure, 


internal in mandate, partially internal in data, and fully internal in economic attribution. Binary node membership cannot represent this configuration; the boundary requires an operator over a particular transaction. 

### **3.2 Property Rights, Team Production, and the Nexus of Contracts** 

Grossman, Hart, and Moore relate firm boundaries to ownership of non-human assets and residual rights of control under incomplete contracts [4, 5]. Their theory is a direct benchmark for any new account of the boundary. The transactional attribution proposed here operates at a different analytical level. It describes the mode of action when ownership, computing infrastructure, mandate, accountability, and data are distributed across several parties. Property rights enter the transaction profile through control and economic attribution while remaining one component of a broader profile. 

Alchian and Demsetz describe the firm through team production and the problem of monitoring joint output [6]. Jensen and Meckling analyze the firm as a legal fiction and a nexus of contractual relations, emphasizing agency costs [7]. Actor-graph theory represents these relations as edge types and adds temporal state, executable authority, software bearers of roles, and a mechanism that folds the internal graph into a single external actor. 

Simon identified the distinctive structure of the employment contract: the employee accepts an area of the employer’s future decisions whose content cannot be fully specified in advance [8]. This insight directly anticipates the treatment of a position as a bundle of unspecified functions. LLMs alter the cost of using that zone of authority because a machine semantic layer can now interpret and decompose a subset of future assignments. A residual domain of authority and responsibility remains. 

The broader organizational tradition of March and Simon links firm structure to bounded rationality and decision procedures [9]. Simon’s later work treats markets and organizations as distinct mechanisms of coordination [10]. Arrow identifies organizational limits created by information and authority [11], while North situates formal rules, informal constraints, and enforcement mechanisms within a general institutional framework [12]. Together, these works caution against reducing compactness to a single cost function. 

### **3.3 Information Technology and Firm Size** 

The prediction that information technology would alter the structure of markets and hierarchies long predates LLMs. Malone, Yates, and Benjamin linked lower coordination costs to a shift of some activity toward electronic markets [13]. Brynjolfsson, Malone, Gurbaxani, and Kambil found a lagged association between IT investment and smaller average firm size [14]. Clemons, Reddi, and Row proposed the alternative _move to the middle_ hypothesis, under which greater external sourcing coexists with durable relationships involving a limited number of partners [15]. 

The proposition that IT can reduce firm size is therefore well established. LLMs differ in the object of cost reduction. Earlier automation primarily lowered the cost of transmitting structured data, performing calculations, and executing prespecified procedures. LLMs act on linguistic interpretation, incomplete specification, and local adaptation—functions that historically sustained a large human coordination layer. 

The theory of the Compact Company predicts a double movement: headcount may decline while the number and variety of transactions organized under a single mandate increase. 

Shahidi, Rusak, Manning, Fradkin, and Horton directly examine the market side of this shift in their account of the “Coasean singularity” [16]. They treat AI agents as market participants capable of reducing the costs of search, communication, contracting, enforcement, and identity verification. The same agents can create new frictions through market congestion, price opacity, and platform dependence. Their framework explains the expanding set of feasible market configurations. The theory of the Compact Company asks which configurations preserve the firm as a single accountable and succession-capable institutional actor. 


### **3.4 Organizational Routines, Memory, and Tacit Knowledge** 

Nelson and Winter treat organizational routines as heritable carriers of firm behavior [17]. Cohen and Bacdayan show that routines can function as distributed procedural memory [18]. This tradition helps explain the persistence of firm identity as individual participants change. 

Polanyi emphasizes tacit knowledge that cannot be reduced to a fully articulated instruction [19]. The Compact Company permits tacit human competence to remain human. It imposes a narrower requirement: any critical state required to restore governance must remain available outside every admissible failure set. Negotiating skill, clinical judgment, engineering intuition, and social trust may remain embodied in people. The sole copy of rights, obligations, keys, and critical process state cannot remain embodied in one person. 

Crozier and Friedberg show that control over zones of organizational uncertainty generates power: a participant who monopolizes exceptional context, an informal route, or the capacity to resolve an exception gains a strategic advantage within the organization [20]. The explication of tacit state therefore changes the distribution of power and creates political transition costs. Section 17.12 examines these costs in detail. 

### **3.5 Cybernetics, Viability, and Closure** 

Ashby’s Law of Requisite Variety and the Conant–Ashby Good Regulator Theorem impose constraints on the regulation of complex systems [21, 22, 23]. These results remain agnostic about digital twins. A regulator can model a system functionally without containing an explicit digital representation. The transition from model correspondence to an executable, non-personal carrier of the model is an independent thesis of this paper, grounded in the requirements of succession. 

Stafford Beer’s Viable System Model identifies the functional subsystems required by a viable organization: operations, coordination, control, intelligence, and policy [24, 25]. The layered architecture developed below draws on this lineage. Its additional contribution is a unified ontology of human and machine actors, a transactional boundary operator, and an executable link among the model, authority, and state transition. 

Maturana and Varela introduced autopoiesis and operational closure [26]; Luhmann transferred the idea of self-reproducing operations into social systems theory [27]. Organizational closure has a narrower computable meaning in this paper: it specifies the conditions under which the actions of a heterogeneous internal graph can be correctly attributed to a single institutional actor. This formulation leaves the autopoietic theoretical program intact. 

### **3.6 The Actor Model and Organizational Models of Multi-Agent Systems** 

In the computational Actor Model of Hewitt, Bishop, and Steiger, actors are addressable computational entities that respond to messages; Agha subsequently developed the formalism further [28, 29]. The present paper retains addressability, state, and behavior as the core properties of an actor. It extends the set of organizationally significant actor types and adds mandate, accountability, rights, economic attribution, and lifecycle. 

Multi-agent organizational models have long separated a role from its bearer. AGR describes agents, groups, and roles [30]. MOISE+ integrates the structural, functional, and deontic dimensions of an organization [31]. OperA specifies a formal organizational structure compatible with participant autonomy [32, 33]. Electronic institutions define admissible protocols and norms for interactions among heterogeneous human and software agents [34, 35]. 

The role–bearer distinction is therefore an established construction. The present contribution connects that construction to the theory of the firm: a role is linked to a Coasean transaction, legal and economic accountability, organizational succession, and the operator that folds a graph into a composite institutional actor. 


### **3.7 Enterprise Ontology, REA, DEMO, e3value, and ArchiMate** 

REA distinguishes economic resources, events, and agents and develops a model of commitments and exchanges [36, 37]. DEMO provides an enterprise ontology grounded in organizational transactions and commitments [38]. e3value separates the modeling of value exchange among actors from process modeling [39, 40]. ArchiMate supplies an integrated language for describing the business, application, and technology layers of an enterprise [41]. 

These traditions already establish machine-readable organizations, roles, commitments, and value. The incremental contribution proposed here has five elements: 

- active actors, roles, resources, artifacts, and norms are separated by type; 

- organizational closure defines the company as a specific institutional whole; 

- the boundary is applied to a transaction across several dimensions; 

- succession is tested against failures of role bearers; 

- the same model supports description, normative constraint, and execution. 

### **3.8 Digital Twin of an Organization** 

Kritzinger et al. distinguish a digital model, a digital shadow, and a digital twin by the degree of automated data exchange between the physical and digital objects [42]. Riss, Maus, Javaid, and Jilek describe the DTO as a graph-based, machine-readable representation of an enterprise model connected to operational reality [43]. Research on digital twins of business processes further develops the relationship among models, events, simulation, and execution [44]. 

Digital Twins of Organizations and graph-based enterprises therefore have an established literature. The question advanced here is more specific: **what theoretical object should a digital twin embody when a company consists of people, LLMs, agents, software, external counterparties, and physical devices, while its boundary diverges from its infrastructure perimeter?** This paper proposes an organizationally closed, typed actor graph as that object. 

### **3.9 Virtual Corporations and Exponential Organizations** 

Davidow and Malone describe the virtual corporation as a flexible network of capabilities and partners [45]. The concept of Exponential Organizations links a small core to staff on demand, communities, algorithms, leveraged assets, interfaces, and dashboards [46]. These concepts are the closest organizational relatives of the Compact Company. 

Four criteria define the distinction: 

1. compactness is determined by minimization under viability constraints; 

2. transactional attribution integrates internal and external executors; 

3. critical state survives admissible failures of its carriers; 

4. the digital twin constitutes the executable state of the organizational graph. 

### **3.10 Direct Theories of the Firm in the Age of Agentic AI** 

By 2026, several studies had begun to reconsider the Coasean firm under the influence of agentic AI. They form a set of complementary research programs: AI-mediated market design [16], a new scaling law for coordination costs [47], preservation of the accountability boundary of vertical AI firms [48], and changes in the curvature of internal coordination costs [49]. 

Klein and Wieczorek’s concept of the **Headless Firm** distinguishes topology-dominated and throughput-dominated regimes of coordination [47]. In earlier modular systems, integration cost 


depends on the topology of bilateral links. In a protocol-mediated agentic system, every executor connects to a shared “waist,” shifting the dominant cost term toward verification of task throughput. The resulting architectural equilibrium has an hourglass structure: a personalized generative interface for intent, a thin layer of protocols and policies, and a market of micro-specialized execution agents. 

For these authors, _headless_ design compresses governance into standard contracts, policy gates, provenance, and output evaluation. Their model identifies the conditions under which external modular execution remains economically scalable. The theory of the Compact Company identifies the economically attractive configurations that preserve organizational closure, action attribution, critical state, human accountability, and the firm’s capacity to continue through time. 

Headlessness and compactness are therefore orthogonal characteristics. Headlessness describes the location and coordination of execution. Compactness describes the minimum resilient human and institutional perimeter. In the terminology of this paper, a headless architecture often shifts a transaction from _internal_ to _delegated_ . The executor may remain external in infrastructure while mandate, authoritative state, control, economic attribution, and residual accountability remain within the firm. 

The two theories can therefore be connected precisely. **The Headless Firm supplies the economic objective function for reconfiguring execution; the Compact Company supplies the institutionally admissible solution set.** Their respective applicability conditions make this complementarity particularly clear. As workflow coupling, the density of inter-agent invariants, irreversibility, and accountability increase—in tightly coupled state machines, safety-critical systems, and high-invariant ledgers—the thin waist loses its coordination advantage [47]. This domain requires the deterministic execution layer, boundary actors, transactional attribution, authoritative ledger, and non-personal carrier of critical state introduced by the theory of the Compact Company. 

Klein and Wieczorek add another important axis: the rate of knowledge decay. Rapidly obsolescing expertise tends toward external specialized actors that can amortize knowledge updates across many clients; stable and highly specific capabilities more often remain integrated [47]. The appropriate unit of analysis is a role or transaction class. In law, medicine, finance, and software development, research and option generation may be external, while the irreversible decision, professional signature, or change to the system of record remains inside the institutional perimeter. 

This distinction extends the author’s earlier Law of Functional Migration, under which functions of basic organizational units progressively move into external infrastructure along the independent dimensions of activity, ownership, and skill [50]. The theory of the Compact Company adds an institutional constraint: functional migration must preserve the chain of mandate, authoritative state, accountability, and restoration of governance. 

Hydari and Muzaffar develop a related framework in **Going Headless? On the Boundaries of Vertical AI Firms** [48]. They distinguish the interface boundary, value-capture boundary, and accountability boundary and propose three regimes—component, integrated platform, and dual-track—according to the task-accountability regime. Their dual-track model closely corresponds to the _delegated_ mode developed here: execution of a particular task moves outside, while evidence, authority, authoritative state, professional accountability, and final commitment remain within the governed perimeter. 

The same work introduces **rule debt** : the future costs of governance, maintenance, and accountability that arise when business rules and professional standards migrate from governed systems into prompts, saved tasks, ad hoc scripts, and agent instructions [48]. In actor-graph theory, rule debt appears as divergence between declared policy and the set of rules actually executed. Section 17.3 examines this risk in detail. 

The **Zero-Marginal-Cost Firm** proposes that AI changes the curvature of the internal coordinationcost function: the marginal cost of coordinating additional complexity may asymptotically approach zero, shifting the center of the theory of the firm toward objective-function design [49]. The Compact Company retains positive costs for verification, security, accountability, and succession as a general condition. It therefore establishes a lower bound on the human core and identifies institutional constraints that persist under radical reductions in operating cost. 


In summary, _The Coasean Singularity_ studies AI-mediated markets; the _Headless Firm_ studies the economics of protocol-based disaggregation of execution; _Going Headless?_ studies the preservation of accountability assets in a vertical firm; the _Zero-Marginal-Cost Firm_ studies the marginal cost of algorithmic hierarchy; and the _Compact Company_ studies the minimum resilient institutional perimeter around an executable actor graph. The relationship can be stated concisely: **headless at the execution periphery, compact in the institutional core** . 

### **3.11 Relation to the Author’s Prior Work: A Genealogy of the Theory** 

This article synthesizes several lines previously developed in the author’s work into a unified actor-graph theory of the Compact Company. A precise claim to novelty therefore requires an explicit account of the inherited constructions and the incremental results introduced here. 

**Formal substrate: active transaction graphs.** In _Active Transaction Graphs_ , actors are defined through state, interface, and capacity for transition; an actor may be recursively represented by an internal graph; edges become first-class mediating actors; and observational semantics is given by the triple “result–trace–ledger” [51]. The present paper inherits the actor, transaction, active edge, recursion, and ledger sensitivity as established components. It uses them to define the firm itself through institutional attribution, organizational closure, the human core, and conditions for preserving identity as carriers are replaced. 

**Boundary and viability.** _The Computable Boundary of the Firm_ already treats the boundary as an independent object of the governance model. It represents the firm as a controlled Markov process and proves that observability of the membership of causally significant actors and controllability of boundary permeability are necessary conditions for viability in a nonstationary overloaded environment [52]. The present paper shifts the analysis from topological membership and permeability to the attribution of each transaction across authority, accountability, data regime, economic outcome, and control, with executable modes I, D, M, P, and U. Reference [52] explains why the boundary must be represented and governed; this paper specifies how to determine whether a particular action constitutes an action of the firm. 

**Regulatory line.** The work on minimal Good Regulators proves the necessity of factorization through a projection that suppresses distinctions that leave the action space unchanged [53]. _Regulatory Quality of Asymptotic Models_ introduces regulatory quality and a critical scale below which a model fails to distinguish the system with the required resolution [54]. _On the Nature of the Regulator_ formulates the actor graph as a self-computing framework for a hybrid regulator in which the LLM functions as an internal computational participant within a wider regulatory system [55]. _Company Brain_ connects the digital core, digital twin, meta-regulation, and human goal formation within a single control loop [56], while the phase model of enterprise evolution describes the transition from fragmentation to a digital core, a digital twin, and an autonomous enterprise [57]. _Metaunderstanding_ develops the related idea of pragmatic policy compression: the regulator compresses distinctions relevant to action selection [58]. The present paper uses this line as the basis for the distributed regulator 𝑅𝐻 ∪𝑅𝐴 ∪𝑅𝐷 and adds a previously absent object—a firm with a measurable boundary, a legal lower bound, and verifiable succession. 

**Functional migration and the cost of AI coordination.** _The Law of Functional Migration_ formalizes the long-term transfer of functions from households, firms, organisms, and states into external infrastructure, distinguishing the externalization of activity, ownership, and skill [50]. This line directly precedes the headless periphery of the Compact Company. _What Is Work?_ uses an informationtheoretic argument to show that a rapid first LLM output redistributes the work of relevant information processing, verification, and correction among participants [59]. _Convergence Theory and Practice for Iterative Generation with Drifting Goals_ formalizes the generator, reviewer, and goal setter as a coupled stochastic system and describes oscillation, goal drift, false attractors, and reviewer degradation [60]. The essay _How to Become a Smart Company_ introduces the “fragmentation tax” and distinguishes local functional amplification by AI tools from the architectural integrity of the company [61]. The present paper combines these observations: external agentic specialization is admissible where outcomes are 


reversible and verifiable, while the authoritative transition, policy, and residual accountability close within the institutional spine. 

**Accountability and management debt.** _Management Debt_ defines an unmade, deferred, unformalized, or unexecuted management decision as a source of observable ambiguity, manual intervention, excessive coordination, errors, and losses; materialized debt is attributed to the accounts of responsible actors [62]. The present paper gives this line an architectural continuation. Incomplete policy produces mode U, hidden instructions create rule debt, and compactness becomes false when decisions are displaced into individual minds, prompts, or opaque external agents. 

The present paper directly inherits six foundations from the author’s corpus: the transaction graph [51], the computable boundary [52], factorization of the minimal regulator [53], the company as a hybrid regulatory loop [56], functional migration [50], and attribution of management debt [62]. The remaining works [54, 55, 57, 58, 59, 60, 61] provide adjacent metrics, mechanisms, and architectural constraints; they do not serve as proofs of the central propositions advanced here. 

References to the author’s prior corpus establish the genealogy of definitions and formal constructions. Independent empirical validation requires external data, independent cases, and research conducted under the program specified in Section 16. 

**The specific increment of this article** consists of the following: 

1. established actor-graph constructions are extended into the theory of the firm alongside their computational and regulatory applications; 

2. the recursive actor receives institutional semantics through the organizational-closure operator 𝑄 and weak probabilistic bisimulation; 

3. the computable boundary is refined into the transactional operator 𝐵𝑡<sup>𝑈</sup> , which distinguishes internal, delegated, market, prohibited, and indeterminate action; 

4. continuity and succession are defined as (𝑘, Δ, 𝜀)-viability with a requirement for a non-personal carrier of critical state; 

5. the Compact Company is defined as optimization of the human core under legal, capacity, and probabilistic constraints, and the simplified core-design problem is shown to be NP-hard; 

6. functional migration and headless execution are incorporated into a single model with an institutional core: a function may leave the firm’s infrastructure perimeter while remaining within its perimeter of authority and accountability. 

The paper therefore constitutes a **synthesizing step in the author’s research program** : from actors and transactions to the boundary, from the boundary to a viable regulator, from the regulator to the digital twin, and from the digital twin to the formal organizational category of the Compact Company. 

### **3.12 Precise Statement of the Theoretical Contribution** 

After accounting for prior work, the paper advances five connected results: 

1. **Actor-graph definition of the firm:** a firm is an organizationally closed heterogeneous graph that can be represented in external relations as a composite institutional actor. 

2. **Transactional theory of the boundary:** the boundary attributes action at the transaction level across multiple organizational dimensions. 

3. **Theory of succession:** firm identity persists through roles, critical states, policies, and admissible transitions as carriers are replaced. 

4. **Formal concept of compactness:** the human core is minimized under legal, capacity, and (𝑘, Δ, 𝜀)viability constraints. 


5. **Non-personal carrier of critical state:** resilience requires critical state to remain outside every admissible failure set; the digital twin is proposed as its integrated executable embodiment. 

## **4 Primitives of Actor-Graph Theory** 

The theory loses discriminating power when every object is classified as an actor. Active entities, normative templates, and passive objects therefore require distinct types. 

### **4.1 Actor** 

**Definition 2** (Actor) **.** An actor is an addressable entity with an identity, state, interface, and a rule for responding to admissible messages or events. 

An actor 𝑎𝑖 is represented by the tuple 

𝑎𝑖 = ⟨𝑖𝑑𝑖, 𝜃𝑖, 𝑥𝑖, 𝐼𝑖, 𝛿𝑖, 𝑐𝑎𝑝𝑖, 𝑙𝑖𝑓𝑒𝑖⟩, (1) 

where: 

- 𝑖𝑑𝑖 is a persistent identity; 

- 𝜃𝑖 is the actor type; 

- 𝑥𝑖 is the current state; 

- 𝐼𝑖 is the input and output interface; 

- 𝛿𝑖 is the transition or behavior rule; 

- 𝑐𝑎𝑝𝑖 denotes available capabilities and tools; 

- 𝑙𝑖𝑓𝑒𝑖 specifies the rules for creation, suspension, replacement, and termination. 

A human participant, an LLM service, an agent, a software process, a legal entity, and a physical device can each qualify as an actor under this definition. 

### **4.2 Role and Role Bearer** 

**Definition 3** (Role) **.** A role is a normative template for participation in an organization that specifies mandate, rights, duties, interface, eligibility criteria, and transfer conditions. 


A role and its current bearer are distinct organizational objects. Their association is represented by the relation 


which may be temporary, partial, and conditional. One actor may bear several roles when segregationof-duties requirements permit it; one role may have several bearers with different levels of authority. 


### **4.3 Resource, Artifact, and Norm** 

A **resource** is a passive object, usage right, stock, or capacity that actors control or transform. 

An **artifact** is a document, record, model, item of evidence, version, key, or other carrier of organizational information. 

A **norm** is a rule, policy, prohibition, limit, priority, or condition applied when evaluating a transition. 

A document stored as a file is an artifact. A contract becomes **actorized** when it receives an address, state, interface, and behavior: it accepts events, tracks performance, initiates checks, and changes status under specified rules. 

An account represented as a number is a resource or a state variable. An addressable account that accepts debit and credit commands, checks constraints, and maintains a journal is an actor. The broad ontological formula is therefore: 

**Any organizationally significant entity can be actorized; it becomes an actor after acquiring identity, state, interface, and behavior.** 

### **4.4 Transaction** 

**Definition 4** (Transaction) **.** A transaction is a typed, organizationally significant transition that connects the pre-action state, initiator, basis of authority, state change, economic or legal outcome, and completion record. 

𝑒= ⟨𝑎src, 𝑎dst, 𝜃𝑒, payload, mandate, pre, post, value, time, status⟩. (4) 

Here 𝑎src and 𝑎dst are the initiating and target actors; the remaining components record the type, content, basis of authority, precondition, outcome, value, time, and status of the transition. Transactions may include: 

- a message that changes an obligation; 

- delegation of authority; 

- conclusion of a contract; 

- a payment; 

- grant of access; 

- acceptance of an outcome; 

- transfer of a role; 

- amendment of organizational policy; 

- a call to an external service that has consequences for the firm. 

Many technical messages remain below the level of an economically significant transaction. The purpose of the analysis determines the appropriate level of aggregation. 

### **4.5 LLM, Agent, and Actor** 

An LLM is a probabilistic model or service. It can function as a computational actor when it is addressable and maintains interaction state. Organizational mandate arises from its placement within a governed organizational structure. 

An agent emerges when the model is placed inside a persistent wrapper: 


𝑎𝑔= ⟨id, 𝑥, goal, memory, tools, rights, budget, policy, lifecycle⟩. (5) 

A single LLM may serve many agents. A single agentic role may switch among models. Organizational succession therefore requires: 


This distinction has practical and theoretical significance. Replacing the provider must preserve the role, its history, obligations, and interfaces. 

## **5 A Formal Model of the Organization** 

At time 𝑡, an organization is represented by the typed, attributed temporal multigraph 


where: 

- 𝐴𝑡 is the set of active actors; 

- 𝑅𝑡 is the set of roles; 

- 𝑈𝑡 is the set of resources; 

- 𝐹𝑡 is the set of artifacts; 

- 𝑁𝑡 is the set of norms; 

- 𝐸𝑡 is the set of typed transactions and interactions; 

- 𝛽𝑡 ⊆𝑅𝑡 × 𝐴𝑡 is the role-assignment relation; 

- 𝑥𝑡 is the aggregate state; 

- Π𝑡 = ⟨ℛ𝑡, ≻𝑡⟩ is a finite set of active rules together with a strict partial order of priority; 

- ℒ𝑡 is the ledger of events, decisions, and completed transitions. 

The actor set may include: 


Here 𝐻𝑡 denotes humans; 𝑀𝑡<sup>𝑙𝑙𝑚</sup> , LLM actors; 𝐺𝑡<sup>𝑎𝑔𝑒𝑛𝑡</sup> , agents; 𝑃𝑡<sup>𝑝𝑟𝑜𝑔</sup> , deterministic software processes; 𝐷𝑡<sup>𝑑𝑒𝑣𝑖𝑐𝑒</sup> , devices; 𝐽𝑡<sup>𝑙𝑒𝑔𝑎𝑙</sup> , legal actors; and 𝑋𝑡<sup>𝑒𝑥𝑡𝑒𝑟𝑛𝑎𝑙</sup> , external counterparties and institutions. The organizational chart is a projection of this model onto the human bearers of roles: 


In a traditional firm, this projection could approximate the center of coordination. In a Compact Company, it is structurally incomplete because a substantial share of active roles, memory, and transitions lies outside the human subgraph. 


### **5.1 Probabilistic Semantics and the External Interface** 

The inclusion of LLM actors requires an explicitly probabilistic semantics. The operational behavior of an organizational subgraph is therefore represented by an image-finite probabilistic labeled transition system in the tradition of probabilistic automata [63, 64]: 


Here: 

- 𝑆𝐶 is the set of reachable composite states of the subgraph; 

- Λ𝐶 = 𝐼𝐶 ∪𝑂𝐶 ∪{𝜏} comprises external inputs, external outputs, and the internal unobservable action 𝜏; 

- ℓ 

- • a transition 𝑠 →𝜇 leads to a probability distribution 𝜇 over 𝑆𝐶; 

- 𝑠<sup>0</sup> 𝐶<sup>is the initial state;</sup> 

- 𝜂𝐶 preserves the organizational attribution profile of each observable action: mandate, accountability, data regime, economic account, and control. 

A fixed admissible scheduler 𝜒𝐶, incorporated into executable policy, must resolve any nondeterminism arising from planning and competing internal actions. In the remainder of the paper, P𝐶 denotes the fully probabilistic external semantics induced by that scheduler. Fixing the scheduler makes Pr(𝜔) a uniquely defined number. Weak transitions are understood in the Segala–Lynch sense for probabilistic automata [64]. The result also assumes image finiteness and the absence of uncontrolled 𝜏-divergence. 

A relation ≈𝑤𝑝 is a **weak probabilistic bisimulation** when related states can match every external or internal transition with a weak combined transition that assigns equal probability mass to each equivalence class and preserves the metadata 𝜂𝐶 of the observable action. This equivalence preserves more structure than equality of trace sets: it preserves the probabilities of observable outcomes and branching structure and distinguishes a deadlocked state from a state in which an action remains possible [63, 64]. External attribution requires precisely these properties. A counterparty or regulator must be able to observe the probability of an outcome, the possibility of failure, and the institutional basis of the company’s action alongside the possible message sequence. 

## **6 Organizational Closure: How a Graph Becomes a Company** 

A collection of actors can jointly produce an outcome without forming a unified institutional subject. Organizational closure distinguishes a firm from an agent swarm, a group of contractors, or an assemblage of software. 

**Definition 5** (Organizationally Closed Subgraph) **.** A subgraph 𝐺𝐶 ⊆𝒪𝑡 is organizationally closed with respect to policy Π𝑡 and ledger ℒ𝑡 when five conditions hold. 

1. **Closure of authority.** Every externally significant action can be traced to a valid mandate or to a prescribed procedure for obtaining one. 

2. **Closure of accountability.** Every action and its consequences have an identified bearer of organizational, contractual, or legal accountability. 

3. **Economic closure.** Value, obligations, and residual outcomes are attributed to a specified account or property perimeter of the firm. 

4. **Closure of state.** Critical states and unfinished obligations remain available to authorized successors and survive the loss of any current bearer. 

5. **Interface closure.** External participants interact through a defined company interface, and access to internal actors remains governed. 


Let P𝐶 be the probabilistic operational semantics of subgraph 𝐺𝐶 defined in Section 5.1. Define the organizational-closure operator as factorization by weak probabilistic bisimulation: 


The quotient system defines the composite institutional actor 𝑎𝐶. Its states are the equivalence classes of weak probabilistic bisimulation, and its external interface inherits the observable labels and attribution 𝜂𝐶. 

**Proposition 1** (Composite Actor of an Organizationally Closed Graph) **.** _Let_ 𝐺𝐶 _be organizationally closed; let the admissible scheduler_ 𝜒𝐶 _be fixed; let_ P𝐶 _be image-finite and free of uncontrolled_ 𝜏 _-divergence; let the boundary policy be total and decision-consistent for every reachable external profile; and let every externally significant input and output pass through a stable interface. Then the quotient system_ 𝒬Π,ℒ(P𝐶) _is well defined and weakly probabilistically bisimilar to the original operational system at the external interface. Denote the corresponding composite actor by_ 𝑎𝐶 _. For every measurable external outcome_ 𝜔 _that is invariant under bisimulation, both probability and organizational attribution are preserved:_ 


_The operator_ 𝒬 _is idempotent up to weak probabilistic bisimulation:_ 


_Proof sketch._ Factorization of a probabilistic transition system by bisimulation is well defined because transitions from any two states in the same equivalence class are matched by distributions that coincide on equivalence classes. The choice of representative therefore leaves the transition of the quotient system unchanged. Weak bisimulation hides internal 𝜏-transitions while preserving probabilistic branching, reachability of external actions, deadlocks, observable outcomes, and attribution metadata. Equalities (11) follow from the definition of bisimulation for outcomes measurable on the quotient space and therefore invariant under ≈𝑤𝑝. The first factorization already identifies bisimilar states, so applying 𝒬 again leaves the external semantics unchanged, yielding (12). 

**Methodological note.** Proposition 1 operates without requiring a real company to recover an objective stationary distribution over every action of every human and LLM actor or to compute the complete bisimulation relation for the enterprise. The probabilistic transition system is defined relative to a selected external interface, observation horizon, admissible scheduler, and set of organizationally significant outcomes. The result establishes the conditions under which the internal graph admits a valid abstraction as one institutional actor. An empirical audit may approximate these conditions through observed traces, interval estimates, failure frequencies, and stress scenarios. 

**Note on recursive composition.** The result makes no unconditional compositionality claim. Closed subgraphs can be nested recursively when message types and interface alphabets are compatible, outputs of one subgraph are admissible inputs to another, policies agree on shared labels, and the selected relation ≈𝑤𝑝 is a congruence for the composition operator in use. A failure of these conditions can cause locally valid factorizations to change the behavior of the whole graph. 

The proposition resolves a type error by assigning the company two distinct representational levels. 

#### **Internally, the company is an organizationally closed graph of actors. In external relations, the operator** 𝒬 **represents that graph as a composite probabilistic institutional actor.** 

### **6.1 Theoretical Significance of Closure** 

Organizational closure supplies a criterion absent from a simple relationship diagram. It explains: 

- how a collection of AI tools differs from a firm; 


- when the action of an external agent can count as an action of the company; 

- how a subsidiary or business unit can simultaneously function as an internal graph and an external actor; 

- how identity persists when most internal carriers are replaced; 

- why a unified interface without closure of accountability creates an institutional facade. 

Firm identity resides in the preservation of critical closure invariants: mandates, obligations, economic accounts, policies, state, probabilistic external semantics, and interface. 

## **7 The Transactional Boundary of the Firm** 

This section develops the author’s earlier concept of a computable boundary of the firm [52]. In that model, representability of the membership of causally significant actors and controllability of boundary permeability are conditions of viability. The present formulation refines the boundary into an operator over an individual transaction: an action belongs to the firm through a coherent attribution of authority, accountability, data, economic outcome, and control, irrespective of the executor’s location. 

### **7.1 Attribution Profile** 

For every organizationally significant transaction 𝑒, define the profile 

𝛼𝑡(𝑒) = ⟨𝑎𝑒, ℓ𝑒, 𝑑𝑒, 𝑚𝑒, 𝑐𝑒⟩, (13) 

where: 

- 𝑎𝑒 is the source of authority and the delegation chain; 

- ℓ𝑒 is the bearer of accountability and risk; 

- 𝑑𝑒 is the data regime: ownership, access, location, and permitted use; 

- 𝑚𝑒 is the economic attribution of value, costs, and obligations; 

- 𝑐𝑒 is control: the capacity to authorize, stop, review, reverse, or compensate the action. 

The profile supplies the facts from which policy determines the transaction mode. The boundary operator performs that determination. 

### **7.2 Boundary Operator** 

Let the set of base decisions be 

ℳ= {𝐼, 𝐷, 𝑀, 𝑃}, (14) 

where: 

- 𝐼 denotes _internal_ : a transaction organized internally; 

- 𝐷 denotes _delegated_ : execution is external, while mandate, control, or accountability remains substantially closed within the firm; 

- 𝑀 denotes _market_ : a transaction between autonomous institutional actors; 

- 𝑃 denotes _prohibited_ : policy or law prohibits the configuration. 


Policy has the structure 


Here ℛ𝑡 is a finite set of partial rules 𝑟∶𝒜𝑡 ⇀ℳ, ≻𝑡 is a strict partial priority order, and 𝑟(𝛼) = dec𝑟(𝛼) is the decision returned by an applicable rule. 

The partial boundary operator has signature 𝐵𝑡 ∶𝒜𝑡 ⇀ℳ and is defined exactly when all maximally applicable rules return the same decision: 


An executable system uses the symbolically distinct totalized version 


Here 𝑈 denotes _indeterminate_ : no rule applies, maximally applicable rules conflict, or the available data are insufficient. Mode 𝑈 must trigger a halt or escalation. 

**Proposition 2** (Totality and Uniqueness of the Boundary) **.** _The partial operator_ 𝐵𝑡 _is total and singlevalued on the set of admissible profiles_ 𝒜𝑡 _if and only if policy_ Π𝑡 = ⟨ℛ𝑡, ≻𝑡⟩ _is:_ 

_1._ **_complete:_** _for every_ 𝛼∈𝒜𝑡 _, the set_ MaxΠ𝑡(𝛼) _is nonempty;_ 

_2._ **_decision-consistent:_** _for every_ 𝛼∈𝒜𝑡 _, all maximally applicable rules return the same decision._ 

_Proof._ Completeness ensures that every profile has at least one maximally applicable rule. Decision consistency makes the set of decisions returned by those rules a singleton, so (16) defines a unique value 𝐵𝑡(𝛼). Hence 𝐵𝑡 is total and single-valued. Conversely, totality excludes an empty set of maximally applicable rules, and uniqueness excludes two different decisions among them. 

The proposition has a direct engineering interpretation. When two boundary actors return _allow_ and _deny_ for the same profile and no higher-priority rule resolves the conflict, the firm has a formally underdetermined boundary disguised as dual protection. 

### **7.3 Admissible and Hazardous Configurations** 

Table 2: Admissible and hazardous boundary configurations. 

|**Authority**|**Accountability**|**Control**|**Typical Classifica-**<br>**tion**|**Comment**|
|---|---|---|---|---|
|Internal|Internal|Internal|𝐼|Classical internal operation|
|Internal|Internal|Joint / external<br>executor|𝐷|Delegated execution|
|External|External|Limited contrac-<br>tual control|𝑀|Market transaction|
|Internal|External|Internal|𝑈or𝑃|Possible displacement of accountability while<br>effective control remains internal|
|External|Internal|Absent|𝑈or𝑃|The company bears risk without effective<br>control|
|Undetermined|Any|Any|𝑈|The action cannot be attributed|


Classification depends on sector, contractual regime, law, and jurisdiction. The operator 𝐵𝑡 is therefore parameterized by policy, contract, and jurisdiction. The theory requires ambiguity to remain visible as 𝑈; technical success cannot erase institutional indeterminacy. 


### **7.4 Firm Size and the Measure of Internalization** 

A multidimensional boundary must preserve the Coasean concept of size. For a transaction set 𝑇, define the subset of operations admissible for measuring internalization: 


where 𝑤𝑒 reflects the economic significance or regulatory variety of the transaction, and 


Transactions in modes 𝑃 and 𝑈 are recorded separately as prohibited and indeterminate and remain outside the measure of normal firm operations. 

With equal weights and only the modes 𝐼/𝑀, the numerator reduces to the number of internal transactions, consistent with the Coasean intuition of firm size. The parameter 𝜌 is context-dependent: the degree of internalization of a delegated operation depends on mandate, control, and residual risk. 

Monotonicity of 𝜇𝑡 in 𝜌 supports the comparative static “more delegated internal control implies greater internalization” only when policy Π𝑡, weights 𝑤𝑒, and the composition of 𝑇 remain fixed. A policy change makes transaction modes and 𝜌 endogenous, requiring recalibration before comparison. 

The central conclusion is: 

#### **Firm membership attaches to the mode of a particular transaction.** 

The same external LLM provider may act as a market counterparty when selling computation, as part of a delegated internal perimeter when performing an agentic role, and as a prohibited participant when processing a specified class of data. 

## **8 LLMs and the Economic Mechanism of Compactness** 

### **8.1 The Human as a Carrier of Incomplete Specification** 

A traditional position bundled productive operations with several adaptive functions. The human bearer also: 

- interpreted incomplete instructions; 

- reconstructed context; 

- recognized exceptions; 

- coordinated action with adjacent functions; 

- remembered the grounds for decisions; 

- compensated for imperfect systems; 

- maintained local continuity. 

Simon’s zone of employer authority existed because a contract cannot enumerate every future action in advance [8]. The position functioned as an economically indivisible bundle of adaptability. 

LLMs reduce the cost of decomposing this bundle. They can interpret a linguistic instruction, propose a task decomposition, transform context, generate alternatives, and support standard exceptions. The probability of error remains, and authoritative status still requires a separate institutional procedure. LLMs nevertheless reduce the cost of connecting formal automation to human purpose. 


#### **LLMs automate individual task execution and lower the cost of assembling and reassembling an organization around a task.** 

The total labor still includes verification, correction, and completion to the required quality level. The author’s prior work treats this information-processing volume as a positive component of work even when the time to the first plausible output falls sharply [59]. For the theory of the firm, the implication is direct: LLMs can reduce the cost of option generation and context transfer, while verification and the acceptance of accountability must retain explicit places in the organizational graph. 

### **8.2 Decomposition of the Position** 

The functional bundle 


can be transformed into a subgraph of roles and carriers: 

𝑃𝑜𝑠𝑖𝑡𝑖𝑜𝑛→𝑅𝑜𝑙𝑒𝑠→{𝐻𝑢𝑚𝑎𝑛, 𝐿𝐿𝑀, 𝐴𝑔𝑒𝑛𝑡, 𝑃𝑟𝑜𝑐𝑒𝑠𝑠, 𝐸𝑥𝑡𝑒𝑟𝑛𝑎𝑙} →𝑇𝑟𝑎𝑛𝑠𝑎𝑐𝑡𝑖𝑜𝑛𝑠. (21) 

Positions persist where bundling functions creates trust, accountability, mastery, or economies in context switching. The firm can now use roles and transactions as additional primary design units. 

### **8.3 The Double Movement of the Firm** 

Let 𝑉𝑡 > 0 denote the weighted variety of transactions controlled by the company, and let ℎ𝑡 ∶= |𝐻𝑡| > 0 denote the size of its permanent human core. Define the human intensity of the organization as 


Then 


and, under a continuous approximation, 


For the human core to contract while controlled variety grows—that is, foṙ ℎ𝑡 < 0 wheṅ 𝑉𝑡 > 0—the following condition is necessary: 


This condition transforms the rhetorical formula “fewer people, a larger firm” into a testable proposition. Human participation intensity must decline faster than the variety of activity grows. Empirical proxies for 𝑉𝑡 may include: 

- the number of weighted transaction classes; 

- the number of exceptions processed; 

- the volume of active obligations; 

- the variety of roles and external interfaces; 

- normalized turnover or customer count, provided these measures do not conceal structural heterogeneity. 


A raw transaction count lacks sufficient information: one million identical payments and one hundred unique contractual exceptions require different levels of regulatory variety. 

### **8.4 The Bidirectional Coasean Effect** 

LLMs can reduce both internal and market costs. 

Within the firm, they lower the costs of: 

- interpretation; 

- decomposition; 

- context transfer; 

- documentation; 

- coordination; 

- initial processing of exceptions. 

In the market, they lower the costs of: 

- finding a supplier; 

- preparing a specification; 

- comparing offers; 

- integrating through an API; 

- verifying an outcome; 

- switching counterparties. 

A Compact Company may therefore use the market more extensively while controlling a broader set of functions. It can preserve mandate, state, and accountability without owning every carrier of execution. 

In the terms of the Law of Functional Migration [50], LLMs and agentic markets accelerate the transfer of activity and skill into external infrastructure. Technological externalization can preserve a _delegated_ classification when authority, data, control, and accountability remain institutionally internal. 

Two further properties distinguish individual roles and transactions: the decay rate of required knowledge and institutional coupling—the density of invariants, irreversibility, cost of error, and difficulty of transferring accountability [47, 48]. High knowledge decay combined with low coupling favors an external market of specialized agents. High coupling keeps authoritative state and final commitment within a deterministic perimeter. The characteristic mixed configuration draws knowledge and decision options from outside while closing authorization, irreversible transition, and accountability within the Compact Company. 

## **9 The Good Regulator, Requisite Variety, and the Limit of Human Reduction** 

### **9.1 The Scope of the Conant–Ashby Theorem** 

Conant and Ashby showed that, under specified assumptions, the simplest successful regulator must implement a mapping of the relevant states of the regulated system [22]. The familiar formulation—“every good regulator of a system must be a model of that system”—is useful when applied with precision. The theorem leaves open whether the regulator: 

- stores an explicit schema of the system; 


- contains a digital model; 

- uses a knowledge graph; 

- possesses a digital twin; 

- separates its model from its own behavioral mechanism. 

A thermostat can model the regulated system in a functional sense while containing no separate descriptive object. 

The appropriate formulation for this paper is therefore: 

#### **The Good Regulator Theorem requires model correspondence for effective regulation and remains agnostic about the carrier of the model. The transition to an explicit executable digital twin is an independent thesis of the theory of the Compact Company.** 

The author’s prior corpus developed this transition in stages: from factorization of a minimal regulator through pragmatic noise suppression [53] and estimation of the critical scale of model quality [54], to the actor graph as the framework of a hybrid regulator [55], the Company Brain architecture [56], and the enterprise’s phase transition toward a digital twin [57]. This article treats those results as the preceding regulatory line and preserves the historical scope of each contribution. 

### **9.2 The Law of Requisite Variety** 

Ashby’s Law of Requisite Variety provides the more relevant basis for establishing the lower limit of the human core [21]. A system can compensate only for disturbances whose relevant differences the regulator can distinguish and process. 

Let 𝑍 denote the classes of relevant organizational situations that must be distinguished in order to select an admissible action. Let regulatory capacity be distributed across: 

- 𝑅𝐻, the human layer; 

- 𝑅𝐴, the LLM and agentic layer; 

- 𝑅𝐷, the digital twin, policies, and deterministic execution. 

Assume that the random variables 𝑍, 𝑅𝐻, 𝑅𝐴, 𝑅𝐷 are defined on a common probability space and that their joint distribution is stationary over the selected horizon of analysis. Under structural change, the equations below apply locally after re-estimating both the distribution and the composition of relevant situations. The parameter 𝛿≥0 specifies the admissible residual uncertainty in distinguishing relevant situations. 

A stochastic information-theoretic operationalization requires 


or equivalently 


By the chain rule, 


When the required level of discrimination remains fixed and the contribution of the human layer 𝐼(𝑍; 𝑅𝐻) declines, the conditional contribution of the agentic and digital layers must increase: 


Equation (29) is an information-theoretic operationalization proposed here under explicit assumptions. Its status is independent of Ashby’s theorem. Removing people without transferring relevant variety into other layers produces regulatory blindness and fails the compactness criterion. 

### **9.3 Principle of Compensatory Regulatory Variety** 

_Principle_ 1 _._ Human regulatory variety may be reduced only to the extent that relevant variety is transferred into agentic, model-based, procedural, and reserve human layers without deterioration in target control performance. 

This principle refines the earlier formula “fewer people require greater explicitness.” Compensation can take several forms: 

- deterministic policy; 

- a software controller; 

- an agent; 

- a second human; 

- an external professional layer; 

- a physical safety mechanism; 

- a digital twin. 

Succession additionally requires critical state to remain accessible to a new role bearer. A Compact Company therefore requires a regulator that is both sufficient and **transferable** . 

### **9.4 The Polanyi Constraint** 

Tacit knowledge is not fully interchangeable with an explicit model [19]. Negotiating ability, clinical judgment, engineering intuition, and social trust may remain embodied in people and develop through practice. 

Equation (29) therefore supports a narrower claim: 

**Full formalization of company knowledge is unnecessary. Every state required to restore governance legitimately and continue a critical obligation must have a carrier outside each admissible failure set.** 

The next section formalizes this claim. 

## **10 Continuity, Succession, and Viability under Parameters k, Δ, and ε** 

### **10.1 Families of Failures** 

A single-person removal test underestimates the risk faced by a small core. Correlated failures are especially consequential when: 

- several participants are located in the same city; 

- all participants use the same identity provider; 

- governance depends on a single jurisdiction; 

- the human and agentic layers use the same LLM provider; 

- keys reside in one infrastructure environment; 


- one attack compromises policy and the ledger simultaneously. 

Let 𝔉𝑘 be the family of anticipated failure scenarios. It may include every set of up to 𝑘 carriers together with specifically defined correlated scenarios of greater cardinality. 

Let 𝑇rec(𝐹) be the recovery time for critical functions after scenario 𝐹, let Loss(𝐹) be the loss incurred before recovery, and let 𝐿max be the maximum admissible loss. Each scenario has an admissible violation probability 𝜀𝐹, with 0 ≤𝜀𝐹 ≤𝜀. 

**Definition 6** ((𝑘, Δ, 𝜀)-viability) **.** An organization is viable relative to 𝔉𝑘 when, for every 𝐹∈𝔉𝑘, 


The parameters are sector-specific. A payment function may require recovery within seconds; governance succession may permit hours or days; restoration of a rare expert capability may take weeks. The requirements must be specified before failure and verified through testing. 

### **10.2 The Authority-and-State Graph** 

For a critical role 𝑟, construct a directed graph Γ𝑟 containing: 

- human and machine carriers capable of assuming the role; 

- sources of valid authority; 

- authoritative stores of state; 

- channels for transferring keys and rights; 

- admissible escalation paths; 

- dependencies on providers and infrastructure. 

Add a super-source 𝑠 connected to independent sources of authority and critical state. The role is recoverable when an admissible path from 𝑠 to an active role bearer remains after a failure. 

**Proposition 3** (Resilience through Vertex Cuts) **.** _In a simplified directed model without time or capacity constraints, vertices_ 𝑠 _and_ 𝑟 _are non-removable. A critical role_ 𝑟 _remains reachable after the removal of any set of at most_ 𝑘 _other removable vertices if and only if the minimum internal vertex cut between super-source_ 𝑠 _and_ 𝑟 _has cardinality at least_ 𝑘+ 1 _._ 

_Equivalently, by the directed vertex form of Menger’s theorem [65], at least_ 𝑘+1 _internally vertex-disjoint admissible directed paths exist from_ 𝑠 _to_ 𝑟 _._ 

_Proof._ If a cut of cardinality at most 𝑘 exists, removing its vertices separates the role from all sources of authority and state, so resilience fails. If the minimum cut has cardinality at least 𝑘+ 1, removing any 𝑘 vertices leaves at least one path intact. The equivalence with the number of vertex-disjoint paths follows from the vertex form of Menger’s theorem. 

For 𝑘= 1, the direct test searches for articulation points or, in a directed model, dominators and single-vertex cuts. When a particular founder, key, agent, or repository separates a critical role from every source of governance, the organization is fragile and fails the compactness criterion. 

Under a recovery-time constraint Δ, the existence of 𝑘+ 1 disjoint paths, each completing within Δ, is a sufficient condition. A full characterization involving delays, capacities, and probabilities requires a network-reliability model beyond Menger’s theorem alone. 


### **10.3 Lemma on the Non-Personal Carrier of Critical State** 

Let 𝑞 be a state required to restore at least one critical function—for example, a valid key, a register of obligations, a map of authority, the current ledger, the grounds for an unfinished decision, or a policy version. 

**Lemma 1.** _If every accessible carrier of critical state_ 𝑞 _belongs to some admissible failure set_ 𝐹∈𝔉𝑘 _, the organization cannot remain viable relative to_ 𝐹 _._ 

_Proof._ Following failure 𝐹, state 𝑞 becomes unavailable. By the definition of criticality, at least one critical function cannot be restored without 𝑞. Condition (30) therefore fails. 

**Corollary.** _Every critical state must have a valid and accessible carrier outside every anticipated failure set._ 

The carrier may be another person, an independent trusted layer, a legally valid record, a distributed repository, or an actor within the digital twin. The lemma establishes an architectural requirement and remains technology-neutral; a digital twin can satisfy that requirement systematically. 

### **10.4 Succession as an Operation over the Graph** 

Role transfer must combine the appointment of a new bearer with the transfer of: 

- current state; 

- unfinished obligations; 

- rights; 

- budget; 

- decision logs; 

- the grounds for exceptions; 

- escalation channels; 

- external relationships. 

Formally, state transfer and binding of the new bearer must occur atomically or within a controlled period of dual authority: 

[transfer𝑎𝑖→𝑎𝑗 (𝑥𝑟, 𝑟𝑖𝑔ℎ𝑡𝑠𝑟, 𝑜𝑏𝑙𝑖𝑔𝑎𝑡𝑖𝑜𝑛𝑠𝑟, 𝑐𝑜𝑛𝑡𝑒𝑥𝑡𝑟) ∧ bind(𝑟, 𝑎𝑗)] → verify(𝑟, 𝑎𝑗) → unbind(𝑟, 𝑎𝑖). (31) 

Creating the new role binding without transferring state produces organizational amnesia. 

## **11 Compactness as an Optimization Problem** 

### **11.1 Admissible Set** 

Let 𝒫 be the set of candidates for the human core; let 𝑅𝑐 be the set of critical human roles; let 𝐶𝑝 ⊆𝑅𝑐 be the roles that person 𝑝 can assume legitimately and competently; and let 𝑐𝑝 be the cost of including that person in the permanent core. 

The desired core 𝐻⊆𝒫 is selected from an explicitly defined candidate set. This finite domain gives the optimization problem a determinate scope. 

- The minimization problem is 


subject to: 


Here 𝐶risk(𝐻) captures the residual risk of the selected configuration, and 𝐶coord(𝐻) captures the internal coordination costs of the core. The risk term prevents mechanical selection of a zero-buffer solution. Parameter 𝜒 specifies capacity reserve for a demand shock, investigation, litigation, regulatory review, or mass processing of exceptions. 

### **11.2 Legal Lower Bound** 

Legal personality and sector-specific requirements remain binding under technological change. Define 


where 𝐻legal is determined by applicable law and may include: 

- a minimum composition of governing bodies; 

- personally accountable licensed professionals; 

- a four-eyes principle; 

- independent audit; 

- AML/KYC functions; 

- data protection; 

- prohibitions on combining specified powers. 

The aggregate lower bound on core size is 


Interactions among constraints may require a larger core, so (35) provides a lower bound; the exact optimum may be higher. A one-person company becomes infeasible wherever a unitary core violates at least one constraint in (33)–(35). 

**Proposition 4** (NP-Hardness of Designing the Minimum Human Core) **.** _Consider the simplified version of problem_ (32) _–_ (33) _in which:_ 

- 𝑘= 0 _;_ 

- _probabilistic, legal, capacity, and segregation constraints are absent;_ 

- _every candidate has unit cost;_ 

- _every critical role must be covered by at least one person._ 

_This simplified problem is NP-hard._ 


_Proof by reduction._ Take an arbitrary instance of Minimum Set Cover with universe 𝑈 and family of subsets 𝑆1, … , 𝑆𝑛. Associate each element 𝑢∈𝑈 with a critical role and each subset 𝑆𝑖 with a candidate capable of covering the corresponding roles. Selecting the minimum human core that covers all roles solves the original Set Cover instance exactly. Since Set Cover is NP-hard [66], the simplified compactcore problem is NP-hard. 

For 𝑘> 0, the problem adds multi-cover, role-incompatibility constraints, correlated failures, and probabilistic reliability, thereby preserving or increasing its difficulty. 

The reduction preserves the objective value. Moshkovitz established the corresponding inapproximability threshold for Set Cover [67], building on the results of Dinur and Steurer [68]: if 𝑛= |𝑅𝑐| is the number of critical roles, then for any fixed 𝛼> 0, obtaining a polynomial-time approximation ratio better than (1 −𝛼) ln 𝑛 is NP-hard. Thus, in the general case, the compact core is difficult both to find exactly and to approximate substantially beyond the logarithmic threshold unless **P** = **NP** . 

Proposition 4 gives a lower bound on the computational complexity of core design; it claims no new result in complexity theory. Its practical implication is that sequentially deleting “redundant” positions or exhaustively enumerating configurations cannot reliably produce the minimally sufficient core. Design requires heuristics, scenario search, interactive optimization, and regular re-evaluation as roles, policies, and failure families change. 

### **11.3 Theoretical Consequence** 

A target such as “reduce headcount by 𝑥%” cannot design a Compact Company. Design requires joint optimization of: 

- the role set; 

- admissible carriers; 

- paths of authority; 

- placement of state; 

- segregation of duties; 

- capacity reserve; 

- the cost of human and machine layers. 

The actor graph serves as the computational object over which this optimization problem is solved. 

### **11.4 Conditional Proposition on Organizational Selection** 

Suppose that, for a given output or set of functions, an agentic-digital architecture reduces the required human intensity 𝜆 while satisfying (33), and that its total cost is lower than that of an alternative with a larger permanent workforce. In a competitive market without offsetting rents, a firm that retains a higher admissible 𝜆 bears persistently higher costs. 

Under these assumptions, competition creates directional pressure toward the lower admissible boundary of the human core. 

This result has the status of a conditional economic consequence awaiting empirical generalization. Its force depends on: 

- verifiability of outcomes; 

- cost of error; 

- availability of digital interfaces; 

- cost of models and verification; 


- legal constraints; 

- asset specificity; 

- the value of trust-based human relationships. 

## **12 The Digital Twin as the Executable Embodiment of the Actor Graph** 

### **12.1 Three Levels** 

Three levels must be distinguished: 

|Actor-graph theory<br>→<br>formal model of the firm,|(36)|
|---|---|
|Digital twin<br>→<br>current executable embodiment of the model,|(37)|
|Real company<br>→<br>legal, economic, social, and physical system.|(38)|


The actor graph answers theoretical questions: 

- what constitutes an organizational unit; 

- when a set of participants forms a firm; 

- how an action is attributed to the company; 

- what preserves identity when carriers are replaced; 

- where the boundary lies; 

- what compactness means. 

The digital twin answers an engineering question: how the model exists, synchronizes, executes, remains observable, and changes in real time. 

### **12.2 Model, Shadow, and Twin** 

Following the distinction among a digital model, digital shadow, and digital twin [42]: 

- a **digital model** may be updated manually and may have no control connection to the real object; 

- a **digital shadow** receives data from reality automatically while supporting limited feedback; 

- a **digital twin** maintains a bidirectional loop: it observes, computes, simulates, and initiates admissible changes. 

A static model cannot sustain succession in a Compact Company. A role diagram that lacks the current role bearer, open obligations, and the policy version applied to a decision cannot transfer authoritative organizational state. 

This understanding of the DTO extends _Company Brain_ [56] and the phase model of enterprise evolution [57], where the digital twin emerges after the digital core as a higher regulatory layer. The present paper refines their architectural thesis: the twin should embody an organizationally closed actor graph with a transactional boundary and verifiable transfer of critical roles. 

The work on the Headless Firm independently shows that machine observability of the process is a logical prerequisite even for calculating coordination costs [47]. The number of executors, task throughput, workflow width, and integration links remain unmeasurable when the actual process topology exists only in sequences of interface actions, human memory, and undocumented branches. 


Operationalization requires a representation of the actually reachable state space, exceptions, permissionconditioned branches, transition semantics, and path frequencies. 

Process observability supplies the factual layer of the digital twin. An actor-graph DTO also specifies the admissible layer: which transitions are permitted, the authority under which they occur, the bearer of accountability, the authoritative state, and the transfer path for a role after carrier failure. The digital twin thereby closes both the observability gap and the institutional gap between observing a workflow and preserving the firm through time. 

### **12.3 State of the Digital Twin** 

Represent the company’s DTO as 

𝐷𝑇𝑂𝑡 = ⟨𝒪<sup>𝑡𝑦𝑝𝑒</sup> , 𝒪𝑡, 𝑥𝑡, Π𝑡, ℒ𝑡, 𝒯𝑡, Ω𝑡⟩, (39) 

where: 

- 𝒪<sup>𝑡𝑦𝑝𝑒</sup> contains the types of actors, roles, transactions, and admissible relations; 

- 𝒪𝑡 contains the current instances; 

- 𝑥𝑡 is the current state; 

- Π𝑡 contains policies, rights, limits, and escalation rules; 

- ℒ𝑡 is the authoritative ledger of events, decisions, and transactions; 

- 𝒯𝑡 contains telemetry and observations from the external environment; 

- Ω𝑡 contains model versions, migrations, and rules for changing the organization itself. The digital twin must support at least six functions. 

1. **Descriptive:** represent the current topology and state. 

2. **Normative:** define admissible transitions, authority, and prohibitions. 

3. **Performative:** participate in executing authorized changes. 

4. **Diagnostic:** detect divergence between model and reality. 

5. **Simulative:** test changes before application. 

6. **Succession-supporting:** transfer a role together with context and authoritative state. 

### **12.4 Endogenous Model** 

In a Compact Company, the digital twin forms part of the causal loop: 

𝐶𝑜𝑚𝑝𝑎𝑛𝑦𝑡 →𝒯𝑡 →𝐷𝑇𝑂𝑡 →𝐷𝑒𝑐𝑖𝑠𝑖𝑜𝑛𝑡 →𝐴𝑐𝑡𝑖𝑜𝑛𝑡 →𝐶𝑜𝑚𝑝𝑎𝑛𝑦𝑡+1. (40) 

The model changes the system it models, and the changed system requires an updated model. Versioning, data provenance, logging, and the authority to modify the model therefore become elements of the organizational constitution. 

### **12.5 Authoritative State and LLM Output** 

An LLM is useful for: 

- interpretation; 

- contextual retrieval; 


- classification; 

- synthesis; 

- preparation of options; 

- explanation of state to a human. 

Institutional authorization creates authoritative state. The statistical character of a computation does not determine that status: a deterministic program can be wrong, and a probabilistic model can produce a correct result. A record becomes authoritative through a policy-governed procedure of authority, verification, and registration. 

The formal distinction is: 

proposal ≠ authoritative commit. 

An LLM or agent may propose an action, interpret evidence, or prepare a candidate state. The candidate becomes company state after an authorized layer applies the active policy, verifies the required invariants, and records the transition in the authoritative ledger. 

A reliable chain has the form: 

LLM/agent proposes → policy verifies → boundary actor authorizes 


The LLM contributes semantic flexibility. The actor graph and digital twin establish organizational determinacy: who had authority to propose and confirm the transition, which invariants were verified, and which record became authoritative. 

## **13 The Anatomy of a Compact Company** 

A Compact Company has the architecture of a cybernetic loop composed of interdependent layers. A reduced organizational pyramid cannot adequately represent this structure. Figure 1 summarizes the layered architecture. 


<!-- Start of picture text -->
Market · customers · suppliers · state · physical environment<br>│<br>events and telemetry<br>▼<br>The company's digital twin<br>as a living actor graph<br>│<br>┌───────────────────┼───────────────────┐<br>▼ ▼ ▼<br>human core LLMs and agents deterministic<br>processes<br>│ │ │<br>└───────────────────┼───────────────────┘<br>▼<br>policies · verification · boundary actors<br>│<br>▼<br>ledger and changes in reality<br><!-- End of picture text -->

Figure 1: Layered cybernetic architecture of a Compact Company. 

### **13.1 Human Core** 

The human core preserves: 


- definition of ultimate goals; 

- values and admissible trade-offs; 

- legal and social legitimacy; 

- acceptance of residual risk; 

- amendment of the organizational constitution; 

- critical relationships of trust; 

- resolution of exception classes lacking reliable machine verification; 

- recovery from unanticipated failure. 

Most daily operations may reside outside the core. Constraints (33)–(35) determine its size, and permanent human assignment to every process is unnecessary. 

### **13.2 Constitutional Layer** 

The constitutional layer determines: 

- who may create and terminate actors; 

- who appoints role bearers; 

- how authority is delegated and revoked; 

- which actions require a quorum; 

- which roles are mutually incompatible; 

- who changes policies; 

- how emergency transfer of governance occurs; 

- how policy conflicts are resolved; 

- who can stop the digital twin. 

Agent improvisation cannot govern this layer. An LLM may propose an amendment, while the act of amending the constitution must follow a stricter regime than an ordinary operational transaction. 

### **13.3 Agentic Layer** 

Agents may perform roles in: 

- research; 

- qualification of incoming requests; 

- sales; 

- support; 

- procurement; 

- contract preparation; 

- planning; 

- financial analysis; 

- deviation monitoring; 


- preparation of management decisions; 

- identification of external executors. 

A persistent agent has a durable identity, state, and mandate. An ephemeral agent is created for one task, receives the minimum necessary rights, and terminates after its result is recorded. 

### **13.4 Deterministic Execution Layer** 

Legally, financially, or physically significant changes must occur within a controlled execution layer: 

- making a payment; 

- changing a limit; 

- granting access; 

- posting an accounting entry; 

- changing an order; 

- signing a document; 

- initiating delivery; 

- blocking an operation; 

- changing the set of role bearers. 

A deterministic layer may implement a complex process. Its authoritative transition must have verifiable preconditions, an identifiable outcome, and a ledger record. 

### **13.5 Memory and Ledger** 

Organizational memory includes: 

- current state; 

- open obligations; 

- decision history; 

- grounds for exceptions; 

- policy versions; 

- delegation chains; 

- data provenance; 

- unfinished transactions; 

- evidence of execution. 

The LLM provides an interface to memory. The authoritative record remains a separately governed organizational object, and a plausible explanation cannot replace it. 

### **13.6 Boundary Actors** 

A boundary actor computes profile 𝛼𝑡(𝑒), applies the totalized operator 𝐵𝑡<sup>𝑈</sup> (𝛼𝑡(𝑒)), and returns: 

- authorization; 

- prohibition; 


- delegated mode; 

- classification as a market transaction; 

- escalation due to indeterminacy. 

Its object of evaluation is the institutional basis of the action. 

### **13.7 Telemetry and the Reconciliation Loop** 

The digital twin must measure divergence between the model and reality. Without that measurement, it degrades into a normative fiction. 

For observed state 𝑦𝑡 and modeled statê 𝑦𝑡, define the divergence measure 


where metric 𝑑 depends on the state type. Exceeding the threshold must trigger reconciliation, a halt, or transition to a safe mode. 

## **14 Illustrative Scenario: A Lead-to-Cash Transaction** 

This section illustrates the formalism and supplies no empirical validation. 

A customer submits an unstructured request. An LLM actor identifies its language, subject, and urgency. A qualification agent connects the request to the existing customer context and proposes a product type. 

A proposal agent drafts the terms and retrieves the applicable price from a deterministic pricingpolicy actor. A risk actor checks the customer, limit, and contractual constraints. 

When the parameters fall within the authorized range, the transaction proceeds. When an exception is detected, the digital twin transfers the role to an authorized human together with: 

- the original request; 

- the current state; 

- identified risks; 

- the policy version applied; 

- decision options; 

- the limits of the mandate. 

Following the decision, a contract actor creates the contract artifact. An authority actor verifies the right of a specific bearer to accept the terms. A payment actor records receipt of payment. An execution actor initiates delivery. The ledger records each transition. 

For each transaction, profile 𝛼𝑡(𝑒) identifies: 

- the source of mandate; 

- the bearer of accountability; 

- the data regime; 

- economic attribution; 

- control and reversibility. 


When an external LLM service processes text on behalf of an internal agent, the purchase of computation may be a market transaction 𝑀, while preparation of the proposal is a delegated transaction 𝐷. Contract signature remains an internal transaction 𝐼 under an enhanced authority regime. 

The system retains full context; the human enters the loop because policy assigns this decision class to human residual accountability. 

## **15 A Design-Based Feasibility Example: Corezoid and Simulator.Company** 

This section demonstrates the technical feasibility of selected elements of the proposed architecture within an existing class of systems. It provides no independent empirical validation of the theory. 

The author is the founder of Corezoid Inc., which creates a direct conflict of interest disclosed below. All product claims in this section describe the platform’s architectural intent and should not be read as an independent assessment of effectiveness. 

Corezoid implements event-driven process execution and exposes processes as APIs. Its developer positions Simulator.Company as a computable digital twin of an organization’s processes, roles, events, and automations. An MCP connector allows AI agents to launch Corezoid processes, thereby separating an agent’s semantic proposal from executable business logic [69, 70, 71]. 

This architecture illustrates several propositions of the paper: 

1. an agentic role can use an external LLM while remaining distinct from that model; 

2. agent actions pass through an addressable process; 

3. authoritative state is stored outside model parameters; 

4. a process can execute the deterministic part of a transition; 

5. a graph of processes and actors can serve as the core of a digital twin. 

The example leaves five empirical claims unresolved: 

- whether implementation automatically reduces the human core; 

- whether the company becomes (𝑘, Δ, 𝜀)-viable; 

- whether the economic performance claimed for the product is achieved; 

- whether actor-graph theory outperforms alternative enterprise ontologies; 

- whether the Compact Company becomes a dominant organizational form. 

Converting the design example into an empirical case requires pre- and post-measurement of human intensity, role-transfer time, the number of single points of failure, the share of indeterminate transactions, and actual recovery time. 

## **16 Empirical Program and Conditions of Falsification** 

### **16.1 Established Evidence and Open Claims** 

Existing research on generative AI primarily measures individual worker productivity or performance on bounded task sets. 

Noy and Zhang found shorter completion times and higher quality in professional writing tasks [72]. Brynjolfsson, Li, and Raymond found an average productivity increase among customer-support agents, with strong heterogeneity by experience [73]. Dell’Acqua et al. identified a “jagged frontier”: within the AI capability frontier, participants completed more tasks faster and at higher quality; on a task outside that frontier, they produced incorrect results more frequently [74]. In an experiment 


spanning 66 firms, Dillon et al. found time savings in email work, while individual access to an AI tool produced no detectable change in the number or composition of tasks [75]. 

These findings support the premise that some linguistic operations have become cheaper. The following organizational propositions remain empirically unestablished: 

- a change in the boundary of the firm; 

- contraction of the human core; 

- improved succession; 

- emergence of organizationally closed agent graphs; 

- dominance of the Compact Company. 

The transition from an individual assistant to a new form of firm is a separate empirical hypothesis. 

### **16.2 Observable Variables** 

Testing the theory requires measures available before and after organizational change. 

Table 3: Observable variables for empirical testing. 

|**Construct**|**Possible Operationalization**|
|---|---|
|Human intensity𝜆|FTE per weighted unit of transaction variety|
|Human-core size|Permanent bearers of critical roles|
|Succession|Time and completeness of role transfer to a new bearer|
|Resilience|Share of failure scenarios recovered withinΔ|
|Non-personal state|Share of critical states with a carrier outside every𝐹∈𝔉𝑘|
|Boundary indeterminacy|Share of transactions with𝐵<sup>𝑈</sup><br>𝑡<sup>(𝛼</sup>𝑡<sup>(𝑒)) = 𝑈</sup>|
|Model divergence|Frequency and duration of threshold exceedance for𝜉𝑡|
|Human reserve|Available capacity for stress exceptions|
|Provider dependence|Number of critical roles without a verifed alternative carrier|
|Organizational closure|Share of external actions with complete traceability of mandate, accountabil-<br>ity, and economic account|


### **16.3 Testable Hypotheses** 

**H1. Human-intensity hypothesis.** In digitally representable activities, implementation of an executable actor-graph DTO should reduce 𝜆 without a statistically and economically significant deterioration in quality, recovery time, or losses. 

**H2. Role-transfer hypothesis.** Explicit separation of a role from its bearer and storage of critical state in the DTO should reduce both median role-transfer time and the share of lost obligations. 

**H3. Compensatory-variety hypothesis.** A reduction in the human core without growth in agentic, procedural, or reserve regulatory variety should increase the frequency of unrecovered exceptions and extend recovery time. 

**H4. Transactional-indeterminacy hypothesis.** A high share of mode-𝑈 transactions should predict more attribution incidents, security incidents, regulatory violations, and manual investigations. 

**H5. Organizational-closure hypothesis.** Groups of agents with complete closure of authority, accountability, state, and economic account should exhibit fewer unattributable actions than functionally comparable agent swarms lacking closure. 


**H6. Double-movement hypothesis.** Mature Compact Companies should satisfy condition (25): human intensity declines faster than controlled variety grows, allowing |𝐻| to contract while 𝑉 expands. 

### **16.4 Explicit Falsification Criteria** 

Falsifiability requires negative results to count. The label “not a true Compact Company” cannot immunize the theory against every adverse observation. 

For a specified sector, the proposition that the Compact Company constitutes the primary architecture is falsified or materially weakened when digital prerequisites are satisfied and a representative sample exhibits any of the following over a prespecified period: 

1. median human intensity 𝜆 fails to decline after mature implementation of LLMs and executable organizational models; 

2. lower 𝜆 is systematically accompanied by disproportionate increases in losses, recovery time, or regulatory violations; 

3. firms repeatedly return critical functions to large human layers after initial implementation defects have been resolved; 

4. the digital twin fails to reduce role-transfer time relative to conventional document and workflow systems; 

5. the transactional boundary operator explains incidents no better than a simpler criterion based on ownership or employment status; 

6. organizational closure fails to distinguish a resilient firm from an agent swarm in observable outcomes. 

A strong test requires advance selection of the sector, observation window, and effect threshold. For example, if median FTE per normalized unit of transaction variety in digital customer support does not decline during the five years following broad agentic-system adoption, while quality and recoverability also fail to improve, the sectoral thesis remains unsupported. 

### **16.5 Recommended Research Design** 

A multilevel design provides the most persuasive test. 

Transaction classes, weights 𝑤𝑒, normalization rules for 𝑉𝑡, the observation window, quality thresholds, and exclusion criteria should be preregistered before access to outcomes. Preregistration prevents the human-intensity measure from being fitted to a desired trend. 

1. **Before implementation:** map roles, transactions, failure points, and 𝜆0. 

2. **After basic AI assistance:** measure individual productivity while preserving the organizational graph. 

3. **After agentic decomposition:** measure changes in roles and the number of transitions. 

4. **After DTO implementation:** measure the boundary, state, role transfer, and recovery. 

5. **Stress test:** conduct controlled failures of people, providers, keys, and channels. 

6. **Comparison:** use a matched firm or business unit without an actor-graph DTO. 

This design separates the effect of the LLM as a tool from the effect of organizational architecture. 

## **17 Risks and Limits of the Compact Company** 

### **17.1 Incorrect Model** 

An incorrect model executed well scales error more efficiently than slow informal coordination. 


#### **An incorrect model can govern a company wrongly with exceptional compactness, speed, and discipline.** 

The author’s earlier work on the regulatory quality of models introduces a critical scale below which a model fails to distinguish the system with sufficient accuracy for effective regulation [54]. For a Compact Company, empirical model quality determines the admissible scale and classes of situations in which the human core can safely contract. The existence of a DTO alone supplies no guarantee. 

### **17.2 Divergence between Twin and Reality** 

A DTO that fails to receive external events becomes a digital decoration. The model requires a measurable divergence 𝜉𝑡, reconciliation procedures, and a safe mode. 

### **17.3 Rule Debt** 

Hydari and Muzaffar define rule debt as the future cost of governance, maintenance, and accountability created when business rules and professional standards migrate from governed systems into prompts, saved tasks, ad hoc scripts, and agent instructions [48]. The initial flexibility of a local instruction becomes an unaccounted organizational constitution as the system grows. 

In the terminology of this paper, rule debt is the divergence between declared company policy and the body of rules that actually determines the behavior of human and machine actors. A portion of active policy then lies outside the norm registry, priority order, version control, and amendment procedure. This divergence threatens the totality and uniqueness of the boundary operator, organizational closure, auditability, reproducibility of decisions, and succession. 

This construction extends the author’s concept of management debt [62]. Management debt arises from a missing or unexecuted decision; rule debt arises from an existing rule that remains unformalized or unmanaged. Both forms of debt increase ambiguity, reliance on manual intervention, and the probability of loss. Each requires a distinct recognition and repayment procedure. 

Minimum control of rule debt requires: 

- a unified registry of prompts, saved tasks, scripts, and external instructions containing normative logic; 

- an assigned owner and basis of authority for each rule; 

- versioning, testing, expiration, and revocation procedures; 

- conflict checks against formal policy and higher-priority rules; 

- provenance of the instruction actually applied in the transaction ledger; 

- regular reconciliation of declared and effective policy. 

### **17.4 Prompt Injection and Compromise of the Boundary Actor** 

An LLM agent interacts with untrusted content. An instruction hidden in an email, document, or web page may attempt to alter the goal, extract data, or invoke a tool. 

When a boundary actor trusts the agent’s semantic output without independent verification, Π𝑡 becomes a single point of failure. Required controls include: 

- least privilege; 

- context isolation; 

- typed tools; 

- confirmation of critical actions; 


- an independent policy engine; 

- command-provenance logging; 

- an emergency shutdown mechanism. 

### **17.5 Goodhart’s Law** 

When the digital twin measures and executes simultaneously, its indicators become targets. Actors begin optimizing the measured proxy instead of the underlying objective [76]. Protective measures include: 

- multiple independent indicators; 

- audits of consequences outside the metric system; 

- randomized sampling and review; 

- external data sources; 

- periodic rotation of diagnostic metrics; 

- separation of measurement and reward layers. 

### **17.6 Deficit of Human Response Capacity** 

Automation of routine work can conceal insufficient human capacity until the first atypical event. Litigation, a mass incident, regulatory inspection, model compromise, or a demand shock requires intensive human investigation, interpretation, and acceptance of accountability. 

Reserve capacity can be distributed among cross-trained members of the core, contractually committed experts, partner organizations, and temporary crisis roles. A capability qualifies as a real reserve only after its availability, authority, access to critical state, tool compatibility, and context-recovery time have been verified in advance. 

Critical roles must satisfy: 


Three reserve modes must be distinguished: 

- **hot reserve** already operates within the execution perimeter and has current authority and context; 

- **warm reserve** remains outside daily operations, receives regular state updates, participates in exercises, and can be mobilized within Δ; 

- **cold reserve** is available in the market but lacks current context and preverified access; it can support prolonged recovery and falls outside the reserve calculation for a critical role with a short admissible recovery time. 

A contract with an external specialist acquires reserve status only through regular context updates, role-transfer exercises, and verified restoration of access. The constraint CapacityReserve(𝐻) ≥𝜒 therefore denotes maintained and testable human response capacity; it does not require excess permanent staffing. 

### **17.7 Correlated Failures** 

Two people located within one risk domain form a correlated reserve. Two models operated by one cloud provider share a common failure domain. Two keys protected by one account provide a single effective point of control. 

The family 𝔉𝑘 must include dependencies involving: 


- geography; 

- jurisdiction; 

- identity provider; 

- cloud provider; 

- model; 

- communication channel; 

- update chain; 

- shared data source. 

### **17.8 Model and Provider Dependence** 

Embedding the role, memory, and tool contract inside one model replaces dependence on an employee with dependence on a provider. The architecture therefore requires: 

- a portable role interface; 

- exportable state; 

- an alternative model; 

- equivalence tests; 

- a degraded operating mode; 

- contractual guarantees of access to data and logs. 

An agentic layer may also fail to converge while every carrier remains available: the generator, reviewer, and goal setter may enter oscillation, goal drift, a false attractor, or reviewer degradation [60]. Viability therefore requires monitoring both actor availability and the dynamics of their joint regulation. 

### **17.9 Erosion of Human Recovery Capability** 

A fully automated graph can become unintelligible to its own human core. Under this condition, the DTO becomes the sole point of knowledge and loses its successional function. 

A Compact Company must regularly verify that humans can: 

- explain critical control loops; 

- stop execution; 

- restore a role; 

- verify a record; 

- redesign a policy; 

- operate in a degraded mode. 

### **17.10 Automation without Accountability** 

An agent’s participation in a decision leaves residual accountability intact. Profile 𝛼𝑡(𝑒) must preserve the human and institutional perimeter responsible for the consequences of the action. 


### **17.11 Systemic Concentration** 

Many Compact Companies may depend on a small number of giant providers of models, cloud infrastructure, payments, and logistics. Local compactness can therefore coexist with a global concentration of risk. 

A two-tier economy is plausible: 

large infrastructure systems + many compact application firms. (43) 

The theory of the Compact Company must make this transfer of organizational scale beyond the boundaries of individual firms explicit. 

### **17.12 The Political Economy of Explication** 

Building a digital twin redistributes power within the company. Information moves from human memory into a shared digital model, and actors who control undocumented knowledge, exclusive access, informal links, or ambiguous procedures may lose an advantage derived from organizational opacity. Their indispensability is simultaneously a risk to the firm and a private organizational asset. 

Define **opacity rent** as the organizational advantage that arises from exclusive control over unformalized state, a relationship, a rule, or a procedure. It may take the form of a de facto veto, a monopoly over interpreting an exception, the selective delay of information, or the ability to connect formally separate parts of the company only through personal participation. Control over zones of uncertainty is a classical source of organizational power [20]. 

Explication of roles, authority, states, and decision grounds reduces opacity rents. It enables substitution, audit, and attribution of consequences while creating groups that lose status, influence, or control over resources. A technically rational Compact Company architecture may therefore encounter equally rational resistance from participants in the existing organization. 

Transition cost must include more than technical migration: 

𝐶𝑡𝑟𝑎𝑛𝑠𝑖𝑡𝑖𝑜𝑛 = 𝐶𝑡𝑒𝑐ℎ𝑛𝑖𝑐𝑎𝑙 + 𝐶𝑣𝑒𝑟𝑖𝑓𝑖𝑐𝑎𝑡𝑖𝑜𝑛 + 𝐶𝑝𝑜𝑙𝑖𝑡𝑖𝑐𝑎𝑙 + 𝐶𝑟𝑒𝑑𝑖𝑠𝑡𝑟𝑖𝑏𝑢𝑡𝑖𝑜𝑛. 

The political component includes resistance to revealing actual processes, retention of context, creation of shadow routes, manipulation of telemetry, and obstruction of authority transfer. The redistributive component includes changes in status, decision rights, zones of discretion, and organizational rents. 

An efficient target graph may remain institutionally unreachable. The design of a Compact Company must therefore include both the optimal end state and an institutionally feasible transition path: participant incentives, redistribution of rights, protection of observation channels, sequencing of functional migration, and mechanisms for resolving conflicts between the declared and actual structures of the company. 

## **18 Discussion** 

### **18.1 The Contribution of the Actor Graph to the Theory of the Firm** 

Economics and organizational theory already contain accounts of roles, contracts, assets, norms, and organizational memory. The actor graph contributes a common theoretical object and a set of derivable operations over that object. 

**First:** the firm is defined as an organizationally closed heterogeneous graph whose institutional identity exceeds any separate inventory of people, assets, or contracts. 

**Second:** operator 𝒬 explains how an internal graph can act as one institutional actor while preserving type distinctions. 

**Third:** the boundary is applied to the transaction. This makes external infrastructure with an internal mandate, hybrid accountability, and partial internalization formally representable. 


**Fourth:** succession becomes a reachability property of authority and state under failures. **Fifth:** compactness becomes an optimization problem over the graph, and even its simplified version is NP-hard. 

**Sixth:** the digital twin acquires theoretically specified content. It embodies the state of an organizationally closed graph of actors, roles, norms, and transactions. 

### **18.2 A New Connection across Levels** 

The individual components have established lineages: 

- Coase—the economic boundary; 

- GHM—residual rights of control; 

- VSM—functional viability; 

- AGR/MOISE+/OperA—agent roles and norms; 

- REA/DEMO/e3value—economic events and commitments; 

- DTO—the digital representation of an organization. 

Actor-graph theory connects them through a single transition: 

actor in state + mandate + transaction + attribution + ledger. (44) 

This connection moves the analysis from the theoretical question “why does the firm exist?” to the engineering-theoretical question “which concrete network of human and machine actions still constitutes one firm?” 

### **18.3 The Compact Company as a Distinct Form** 

The Compact Company transforms the architecture of the traditional hierarchy. In a traditional firm, much of the organizational model remains distributed across people, positions, meetings, and informal relationships. In a compact firm, structure, state, and rules move into a transferable organizational perimeter. 

Headlessness and compactness are complementary. A company may radically disaggregate its execution periphery and connect to a market of external agents while preserving a compact, institutionally closed core. Its thin protocol waist must rest on an institutional spine: identity, roles, policies, authoritative state, ledger, boundary actors, audit, and succession procedures. Headless execution therefore requires a fully constituted institutional core. 

Compactness is both an architectural state and an institutional transition. A more efficient target graph may remain politically unreachable when explication deprives influential participants of control over zones of uncertainty and the company has not designed an acceptable redistribution of rights, status, and accountability. 

The form therefore combines: 

- a small human core; 

- high transaction variety; 

- extensive model explicitness; 

- a strong executable boundary; 

- verifiable succession; 

- a reserve of human accountability. 

Compactness requires greater institutionalization. 


### **18.4 The Sense in Which This Form Becomes Primary** 

The term _primary_ expresses a hypothesis about the default architecture of new digital activity. It makes no claim that every company already has this form or will ultimately adopt it. 

The traditional default sequence for launching a function was: 

1. define a position; 

2. hire a person; 

3. place that person in the hierarchy; 

4. accumulate informal relationships; 

5. automate selected parts later. 

The Compact Company changes the default sequence: 

1. define the role and transactions; 

2. define the authoritative state and boundary; 

3. appoint the optimal carrier—a human, agent, process, or external actor; 

4. specify escalation and succession; 

5. incorporate the role into the digital twin. 

In digitally representable sectors, this sequence has an economic advantage when viability constraints are satisfied. The Compact Company therefore functions as an **organizational attractor** whose realization remains contingent on sectoral and institutional conditions. 

### **18.5 The Multi-Person Viability Requirement** 

A single human bearer may control many agents while remaining unable to provide: 

- independent verification; 

- a human quorum; 

- recovery from that bearer’s own unavailability; 

- succession of purpose and legitimacy; 

- reserve capacity for correlated and unanticipated failures. 

The central formula of compactness is: 

**The objective is the smallest human core that eliminates dependence on any single member and preserves sufficient reserve for the unforeseen.** 

## **19 Conclusion** 

LLMs change the firm by entering the universal linguistic layer through which an organization formulates goals, transfers context, decomposes work, coordinates decisions, and processes exceptions. 

This change lowers the cost of semantic coordination and makes it economically feasible to decompose some positions into specialized human, agentic, and software roles. Permanent headcount consequently becomes an unreliable measure of the firm’s operational scale. 

Removing people also removes local models, memory, informal relationships, and reserves of adaptation. The human core can therefore contract only to the boundary established by law, segregation of authority, capacity, and (𝑘, Δ, 𝜀)-viability. 


The Good Regulator Theorem establishes the requirement of model correspondence. The Law of Requisite Variety shows that lost human regulatory variety requires compensation. This paper advances the independent thesis that the digital twin becomes the most complete non-personal carrier of critical state, policy, and execution for a compact digital firm. 

The actor graph contributes to theory by specifying: 

- the unit of active organizational reality; 

- the distinction between a role and its bearer; 

- the operator that closes an internal graph into a composite institutional actor; 

- the transactional boundary operator; 

- a formal model of succession and fault tolerance; 

- the optimization problem for a compact human core; 

- the content of an executable digital twin. 

Coase explains why comparative coordination costs change the boundary of the firm. Actor-graph theory identifies **what continues to constitute a firm** when LLMs, agents, software, and external services perform a substantial share of coordination. 

The most plausible hybrid architecture is headless at the periphery of reversible and verifiable execution and compact in the institutional core, where authority, authoritative state, irreversible transitions, accountability, and succession close. 

The transition to this form redistributes power by moving organizational state from personal monopolies into a shared executable perimeter. It also requires maintained human response capacity grounded in verified access and current context. Viable compactness therefore arises only when the firm passes architectural, legal, human, and political tests simultaneously. 

The final definition can be stated as follows: 

**A Compact Company is an organizationally closed and succession-capable graph of human, agentic, software, and external actors that can be represented to the external world as a single institutional actor. Its human core is minimized relative to legal, governance, capacity, and probabilistic viability constraints, while critical state and execution are maintained by a digital twin.** 

The company of the LLM era is a perimeter of accountability around a living graph of actors. 

**It can survive the replacement of its individual human and machine carriers.** 

## **A Table of Notation** 


Table 4: Table of notation. 

|**Symbol**|**Meaning**|
|---|---|
|𝑡|time point or time index|
|𝒪𝑡|organizational model at time𝑡|
|𝐾|set of critical functions|
|𝐴𝑡|active actors|
|𝑅𝑡|roles|
|𝑈𝑡|resources|
|𝐹𝑡|artifacts|
|𝑁𝑡|norms|
|𝐸𝑡|transactions and interactions|
|𝛽𝑡|assignment of roles to bearers|
|𝑥𝑡|current state|
|Π𝑡= ⟨ℛ𝑡, ≻𝑡⟩|policy rules and their strict partial priority order|
|ℒ𝑡|ledger of events and transactions|
|𝜏|internal unobservable action in the probabilistic semantics|
|𝐺𝐶|organizationally closed subgraph|
|P𝐶|probabilistic operational semantics of the subgraph|
|𝜒𝐶|fixed admissible scheduler|
|≈𝑤𝑝|weak probabilistic bisimulation|
|𝒬|organizational-closure operator|
|𝑎𝐶|composite actor of the company|


Table 4: Table of notation. (continued) 

|**Symbol**|**Meaning**|
|---|---|
|𝛼𝑡(𝑒)|transaction-attribution profile<br>|
|𝒜𝑡|space of admissible attribution profiles|
|ℳ= {𝐼, 𝐷, 𝑀, 𝑃}|base boundary modes: internal, delegated, market, prohibited|
|𝐵𝑡|partial boundary operator𝒜𝑡⇀ℳ|
|𝐵<sup>𝑈</sup><br>𝑡|totalized boundary operator with mode𝑈|
|𝑇<sup>adm</sup><br>𝑡<br>(𝑇)|subset of transactions in modes𝐼,𝐷, and𝑀used to measure internalization|
|𝑤𝑒|weight of the transaction’s economic significance or regulatory variety<br>|
|𝜌|partial-internalization coefcient for a delegated transaction,0 < 𝜌< 1|
|𝜇𝑡(𝑇)|internalization measure for a set of transactions|
|𝐻𝑡|set of bearers in the permanent human core|
|ℎ𝑡= |𝐻𝑡||size of the human core|
|𝑉𝑡|weighted controlled variety,𝑉𝑡> 0|
|𝜆𝑡|human intensityℎ𝑡/𝑉𝑡|
|𝑍|classes of relevant organizational situations|
|𝑅𝐻, 𝑅𝐴, 𝑅𝐷|human, agentic, and digital regulatory layers|
|𝛿|admissible residual uncertainty in distinguishing relevant situations|
|𝔉𝑘|family of anticipated failure scenarios|
|𝐹∈𝔉𝑘|individual failure scenario|
|𝑘|maximum cardinality of a standard failure set; the family may also contain<br>larger correlated scenarios|
|Δ|admissible recovery time|


Table 4: Table of notation. (continued) 

|**Symbol**|**Meaning**|
|---|---|
|𝑇rec(𝐹)|recovery time afer scenario𝐹<br>|
|Loss(𝐹)|loss incurred before recovery afer scenario𝐹|
|𝐿max|maximum admissible loss before recovery|
|𝜀|upper bound on the admissible probability of requirement violation|
|𝜀𝐹|admissible violation probability in scenario𝐹,0 ≤𝜀𝐹≤𝜀|
|𝒫|set of candidates for the human core|
|𝑅𝑐|set of critical human roles|
|𝐶𝑝|roles that candidate𝑝can assume legitimately and competently|
|𝑐𝑝|cost of including candidate𝑝in the permanent core|
|𝐶risk(𝐻), 𝐶coord(𝐻)|residual-risk and coordination costs of the selected core|
|𝜒|required human capacity reserve|
|𝐻LB|aggregate lower bound on human-core size|
|𝐻legal, 𝐻resilience, 𝐻segregation, 𝐻capacity|component lower bounds from law, resilience, segregation of authority, and<br>capacity|
|𝒯𝑡|telemetry and observations from the external environment|
|𝑦𝑡, 𝑦𝑡|observed and modeled states|
|𝜉𝑡|divergence between the digital twin and reality|
|𝑇detect, 𝑇mobilize, 𝑇context, 𝑇authorize|components of human-reserve activation time<br>|
|𝐶transition|total transition cost: technical, verifcation, political, and redistributive|


## **B Minimal Compactness Audit** 

Compact status requires more than a small workforce or the use of LLMs. A minimal audit includes the following tests. 

### **B.1 Closure Test** 

For a random sample of external actions, verify: 

- a valid mandate; 

- the chain of accountability; 

- the economic account; 

- an authoritative state record; 

- the capacity to halt and review the action. 

### **B.2 Role-Transfer Test** 

Transfer a critical role to a substitute without participation by the current bearer and measure: 

- time to assume control; 

- completeness of open obligations; 

- availability of rights; 

- the number of lost grounds for decisions; 

- the number of manual requests directed to the unavailable bearer. 

### **B.3 Failure Test** 

For every 𝐹∈𝔉𝑘, conduct a tabletop, sandbox, or controlled-failure exercise and verify condition (30). 

### **B.4 Provider Test** 

Disable the primary LLM or another critical external service and verify: 

- preservation of the agentic role; 

- availability of memory; 

- model switching; 

- safe degradation; 

- preservation of authoritative state. 

### **B.5 Boundary Test** 

Measure the share of mode-𝑈 transactions. For each transaction, identify whether the cause is: 

- incomplete data; 

- policy conflict; 

- unassigned accountability; 

- a new market configuration; 

- a model defect. 


### **B.6 Human-Reserve Test** 

Simulate a simultaneous operational and legal shock. For every critical role, classify reserve as hot, warm, or cold and measure: 

- failure-detection time; 

- mobilization time; 

- context-recovery time; 

- time to grant or restore authority; 

- the capacity to recover within Δ with probability at least 1 −𝜀; 

- the effect of reserve mobilization on core operations. 

A contract with an external expert qualifies as critical-role reserve only after exercises, current context, and preverified access have been established. 

### **B.7 Rule-Debt Test** 

Inventory prompts, saved tasks, scripts, and external-agent instructions that contain business rules. For a sample of actual transactions, verify that the applied rule has an owner, version, place in the priority order, tests, expiration date, and traceability in the ledger. Every divergence from formal policy must be classified and resolved. 

### **B.8 Political-Feasibility Test** 

Before migrating a critical function, determine: 

- who currently controls undocumented context, exclusive relationships, and zones of discretion; 

- which rights, status, or organizational rents will be lost through explication; 

- which shadow routes and alternative telemetry channels may emerge; 

- which incentives support voluntary transfer of knowledge and authority; 

- which migration sequence preserves the operational coalition; 

- who has authority to resolve conflicts between the declared and actual graphs. 

Migration is complete when actual actions no longer depend on a hidden personal route absent from the digital twin. 

## **Conflict of Interest Disclosure** 

The author is the founder of Corezoid Inc. and is involved in the development of Corezoid and Simulator.Company—systems designed for process execution, construction of actor graphs, and Digital Twins of Organizations. This creates financial and intellectual conflicts of interest. The product example in Section 15 is included solely to demonstrate the technical feasibility of selected constructions and provides no independent validation of the theory. Claims of comparative effectiveness require external empirical testing. 


## **References** 

- [1] Coase, R. H. “The Nature of the Firm”. In: _Economica_ 4.16 (1937), pp. 386–405. doi: 10.1111/j. 1468-0335.1937.tb00002.x. 

- [2] Williamson, O. E. _Markets and Hierarchies: Analysis and Antitrust Implications_ . New York: Free Press, 1975. 

- [3] Williamson, O. E. _The Economic Institutions of Capitalism_ . New York: Free Press, 1985. 

- [4] Grossman, S. J., & Hart, O. D. “The Costs and Benefits of Ownership: A Theory of Vertical and Lateral Integration”. In: _Journal of Political Economy_ 94.4 (1986), pp. 691–719. doi: 10.1086/ 261404. 

- [5] Hart, O., & Moore, J. “Property Rights and the Nature of the Firm”. In: _Journal of Political Economy_ 98.6 (1990), pp. 1119–1158. doi: 10.1086/261729. 

- [6] Alchian, A. A., & Demsetz, H. “Production, Information Costs, and Economic Organization”. In: _American Economic Review_ 62.5 (1972), pp. 777–795. 

- [7] Jensen, M. C., & Meckling, W. H. “Theory of the Firm: Managerial Behavior, Agency Costs and Ownership Structure”. In: _Journal of Financial Economics_ 3.4 (1976), pp. 305–360. doi: 10.1016/ 0304-405X(76)90026-X. 

- [8] Simon, H. A. “A Formal Theory of the Employment Relationship”. In: _Econometrica_ 19.3 (1951), pp. 293–305. doi: 10.2307/1906815. 

- [9] March, J. G., & Simon, H. A. _Organizations_ . New York: Wiley, 1958. 

- [10] Simon, H. A. “Organizations and Markets”. In: _Journal of Economic Perspectives_ 5.2 (1991), pp. 25– 44. doi: 10.1257/jep.5.2.25. 

- [11] Arrow, K. J. _The Limits of Organization_ . New York: W. W. Norton, 1974. 

- [12] North, D. C. _Institutions, Institutional Change and Economic Performance_ . Cambridge: Cambridge University Press, 1990. 

- [13] Malone, T. W., Yates, J., & Benjamin, R. I. “Electronic Markets and Electronic Hierarchies”. In: _Communications of the ACM_ 30.6 (1987), pp. 484–497. doi: 10.1145/214762.214766. 

- [14] Brynjolfsson, E., Malone, T. W., Gurbaxani, V., & Kambil, A. “Does Information Technology Lead to Smaller Firms”. In: _Management Science_ 40.12 (1994), pp. 1628–1644. doi: 10.1287/mnsc.40. 12.1628. 

- [15] Clemons, E. K., Reddi, S. P., & Row, M. C. “The Impact of Information Technology on the Organization of Economic Activity: The ”Move to the Middle” Hypothesis”. In: _Journal of Management Information Systems_ 10.2 (1993), pp. 9–35. doi: 10.1080/07421222.1993.11517998. 

- [16] Shahidi, P., Rusak, G., Manning, B. S., Fradkin, A., & Horton, J. J. _The Coasean Singularity? Demand, Supply, and Market Design with AI Agents_ . NBER Working Paper 34468. NBER, 2025. doi: 10.3386/w34468. 

- [17] Nelson, R. R., & Winter, S. G. _An Evolutionary Theory of Economic Change_ . Cambridge, MA: Harvard University Press, 1982. 

- [18] Cohen, M. D., & Bacdayan, P. “Organizational Routines Are Stored as Procedural Memory”. In: _Organization Science_ 5.4 (1994), pp. 554–568. doi: 10.1287/orsc.5.4.554. 

- [19] Polanyi, M. _The Tacit Dimension_ . Garden City, NY: Doubleday, 1966. 

- [20] Crozier, M., & Friedberg, E. _Actors and Systems: The Politics of Collective Action_ . Chicago: University of Chicago Press, 1980. 

- [21] Ashby, W. R. _An Introduction to Cybernetics_ . London: Chapman & Hall, 1956. 


- [22] Conant, R. C., & Ashby, W. R. “Every Good Regulator of a System Must Be a Model of That System”. In: _International Journal of Systems Science_ 1.2 (1970), pp. 89–97. doi: 10 . 1080 / 00207727008920220. 

- [23] Ashby, W. R. “Requisite Variety and Its Implications for the Control of Complex Systems”. In: _Cybernetica_ 1.2 (1958), pp. 83–99. 

- [24] Beer, S. _Brain of the Firm_ . London: Allen Lane, 1972. 

- [25] Beer, S. _Diagnosing the System for Organizations_ . Chichester: Wiley, 1985. 

- [26] Maturana, H. R., & Varela, F. J. _Autopoiesis and Cognition: The Realization of the Living_ . Dordrecht: D. Reidel, 1980. 

- [27] Luhmann, N. _Social Systems_ . Original German edition 1984. Stanford, CA: Stanford University Press, 1995. 

- [28] Hewitt, C., Bishop, P., & Steiger, R. “A Universal Modular ACTOR Formalism for Artificial Intelligence”. In: _Proceedings of the 3rd International Joint Conference on Artificial Intelligence_ . 1973, pp. 235–245. 

- [29] Agha, G. _Actors: A Model of Concurrent Computation in Distributed Systems_ . Cambridge, MA: MIT Press, 1986. 

- [30] Ferber, J., & Gutknecht, O. “A Meta-Model for the Analysis and Design of Organizations in Multi-Agent Systems”. In: _Proceedings of ICMAS 1998_ . 1998, pp. 128–135. 

- [31] Hübner, J. F., Sichman, J. S., & Boissier, O. “MOISE+: Towards a Structural, Functional, and Deontic Model for MAS Organization”. In: _Proceedings of AAMAS 2002_ . 2002, pp. 501–502. doi: 10.1145/544741.544858. 

- [32] Dignum, V. “A Model for Organizational Interaction: Based on Agents, Founded in Logic”. Doctoral dissertation. Utrecht University, 2004. isbn: 90-393-3568-0. 

- [33] Dignum, V., Dignum, F., & Meyer, J.-J. “An Agent-Mediated Approach to the Support of Knowledge Sharing in Organizations”. In: _The Knowledge Engineering Review_ 19.2 (2004), pp. 147–174. doi: 10.1017/S0269888904000244. 

- [34] Esteva, M., Rodríguez-Aguilar, J. A., Sierra, C., Garcia, P., & Arcos, J. L. “On the Formal Specification of Electronic Institutions”. In: _Agent Mediated Electronic Commerce, LNCS 1991_ . 2001, pp. 126–147. doi: 10.1007/3-540-44682-6_8. 

- [35] Esteva, M., Vasconcelos, W., Sierra, C., & Rodríguez-Aguilar, J. A. “Verifying Norm Consistency in Electronic Institutions”. In: _AAAI Workshop on Agent Organizations_ . 2004. 

- [36] McCarthy, W. E. “The REA Accounting Model: A Generalized Framework for Accounting Systems in a Shared Data Environment”. In: _The Accounting Review_ 57.3 (1982), pp. 554–578. 

- [37] McCarthy, W. E. “The REA Modeling Approach to Teaching Accounting Information Systems”. In: _Issues in Accounting Education_ 18.4 (2003), pp. 427–441. doi: 10.2308/iace.2003.18.4.427. 

- [38] Dietz, J. L. G. _Enterprise Ontology: Theory and Methodology_ . Berlin: Springer, 2006. doi: 10.1007/3540-33149-2. 

- [39] Gordijn, J., Akkermans, H., & van Vliet, H. “Business Modelling Is Not Process Modelling”. In: _Conceptual Modeling for E-Business and the Web, LNCS 1921_ . 2000, pp. 40–51. doi: 10.1007/3540-45394-6_5. 

- [40] Gordijn, J., & Akkermans, H. “Designing and Evaluating E-Business Models”. In: _IEEE Intelligent Systems_ 16.4 (2001), pp. 11–17. doi: 10.1109/5254.941353. 

- [41] The Open Group. _ArchiMate 3.2 Specification_ . The Open Group Standard. 2023. 

- [42] Kritzinger, W., Karner, M., Traar, G., Henjes, J., & Sihn, W. “Digital Twin in Manufacturing: A Categorical Literature Review and Classification”. In: _IFAC-PapersOnLine_ 51.11 (2018), pp. 1016– 1022. doi: 10.1016/j.ifacol.2018.08.474. 


- [43] Riss, U. V., Maus, H., Javaid, S., & Jilek, C. “Digital Twins of an Organization for Enterprise Modeling”. In: _The Practice of Enterprise Modeling, LNBIP 400_ . 2020, pp. 25–40. doi: 10.1007/9783-030-63479-7_3. 

- [44] Fornari, F., Compagnucci, I., Callisto De Donato, M., et al. “Digital Twins of Business Processes: A Research Manifesto”. In: _Internet of Things_ 30 (2025), p. 101477. doi: 10.1016/j.iot.2024. 101477. 

- [45] Davidow, W. H., & Malone, M. S. _The Virtual Corporation_ . New York: HarperBusiness, 1992. 

- [46] Ismail, S., Malone, M. S., & van Geest, Y. _Exponential Organizations_ . Diversion Books, 2014. 

- [47] Klein, T., & Wieczorek, S. _The Headless Firm: How AI Reshapes Enterprise Boundaries_ . arXiv:2602.21401. 2026. doi: 10.48550/arXiv.2602.21401. 

- [48] Hydari, M. Z., & Muzaffar, F. _Going Headless? On the Boundaries of Vertical AI Firms_ . arXiv:2605.17812. 2026. doi: 10.48550/arXiv.2605.17812. 

- [49] Zorzoli, C. _The Zero-Marginal-Cost Firm: Artificial Intelligence and the Algorithmic Transformation of Hierarchy_ . SSRN working paper, manuscript dated 2 March 2026. 2026. doi: 10.2139/ssrn. 6331219. 

- [50] Vityaz, A. _The Law of Functional Migration_ . ResearchGate publication 405206517. 2026. url: https: //www.researchgate.net/publication/405206517_The_Law_of_Functional_Migration (visited on 08/03/2026). 

- [[51]](../2026-active-transaction-graphs/) Vityaz, A. _Active Transaction Graphs: A Formal Framework for Transactional Interactive Systems_ . Zenodo. 2026. doi: 10.5281/zenodo.20747873. 

- [[52]](../2026-computable-boundary-of-the-firm/) Vityaz, A. _The Computable Boundary of the Firm: Information Conditions for Viability and the Transactional Architecture of the Digital Twin_ . Zenodo. 2026. doi: 10.5281/zenodo.20745927. 

- [[53]](../2026-noise-suppression-minimal-good-regulators/) Vityaz, A. _On the Necessity of Noise Suppression for Minimal Good Regulators: Factorization Theorems and a Closure Conjecture_ . Preprint. 2026. doi: 10.13140/RG.2.2.33143.07843. 

- [[54]](../2026-regulatory-quality-asymptotic-models/) Vityaz, A. _Regulatory Quality of Asymptotic Models: A Quantitative Framework with Arithmetic Benchmark_ . Preprint. 2026. doi: 10.13140/RG.2.2.31082.79042. 

- [55] Vityaz, A. _On the Nature of the Regulator: A Symposium on Frameworks and Actor Graphs_ . Preprint. 2026. doi: 10.13140/RG.2.2.30218.02244. 

- [[56]](../2026-company-brain/) Vityaz, A. _Company Brain: The Architecture of General Company Intelligence_ . Preprint. 2026. doi: 10.13140/RG.2.2.28274.88007. 

- [[57]](../2026-phase-model-of-enterprise-evolution/) Vityaz, A. _A Phase Model of Enterprise Evolution: From Fragmentation to the Autonomous Enterprise_ . Preprint. 2026. doi: 10.13140/RG.2.2.24883.39207. 

- [[58]](../2026-metaunderstanding/) Vityaz, A. _Metaunderstanding_ . ResearchGate publication 403758098. 2026. url: https://www. researchgate.net/publication/403758098_Metaunderstanding (visited on 08/03/2026). 

- [[59]](../2026-what-is-work/) Vityaz, A. _What Is Work? The Law of Information Conservation and the AI Productivity Paradox in High-Context Knowledge Work_ . ResearchGate publication 403936327. 2026. url: https://www. researchgate.net/publication/403936327_What_Is_Work_The_Law_of_Information_ Conservation_and_the_AI_Productivity_Paradox_in_High-Context_Knowledge_Work_ 1_The_Promise_That_Does_Not_Add_Up (visited on 08/03/2026). 

- [60] Vityaz, A. _Convergence Theory and Practice for Iterative Generation with Drifting Goals_ . ResearchGate publication 403496851. 2026. url: https : / / www . researchgate . net / publication / 403496851 _ Convergence _ Theory _ and _ Practice _ for _ Iterative _ Generation _ with _ Drifting_Goals (visited on 08/03/2026). 

- [61] Vityaz, A. _How to Become a Smart Company_ . ResearchGate publication 406377980. 2026. url: https: //www.researchgate.net/publication/406377980_How_to_Become_a_Smart_Company (visited on 08/03/2026). 


- [[62]](../2026-management-debt-part-i/) Vityaz, A. _Management Debt—Part I: Concept, Metrics, and Principles for Attributing Materialised Debts to Actor Accounts_ . Zenodo. 2026. doi: 10.5281/zenodo.21069692. 

- [63] Larsen, K. G., & Skou, A. “Bisimulation through Probabilistic Testing”. In: _Information and Computation_ 94.1 (1991), pp. 1–28. doi: 10.1016/0890-5401(91)90030-6. 

- [64] Segala, R., & Lynch, N. A. “Probabilistic Simulations for Probabilistic Processes”. In: _Nordic Journal of Computing_ 2.2 (1995), pp. 250–273. 

- [65] Menger, K. “Zur allgemeinen Kurventheorie”. In: _Fundamenta Mathematicae_ 10 (1927), pp. 96–115. 

- [66] Karp, R. M. “Reducibility Among Combinatorial Problems”. In: _Complexity of Computer Computations_ . New York: Plenum Press, 1972, pp. 85–103. 

- [67] Moshkovitz, D. “The Projection Games Conjecture and the NP-Hardness of ln 𝑛-Approximating Set-Cover”. In: _Theory of Computing_ 11.7 (2015), pp. 221–235. doi: 10.4086/toc.2015.v011a007. 

- [68] Dinur, I., & Steurer, D. “Analytical Approach to Parallel Repetition”. In: _Proceedings of the 46th Annual ACM Symposium on Theory of Computing (STOC 2014)_ . 2014, pp. 624–633. doi: 10.1145/ 2591796.2591884. 

- [69] Corezoid Inc. _Corezoid as a Back-end: Processes as API and Event Processing_ . Product documentation. 2026. url: https://corezoid.com/caab/ (visited on 08/03/2026). 

- [70] Corezoid Inc. _Simulator.Company: The Unified Enterprise System_ . Product description. 2026. url: https://simulator.company/ (visited on 08/03/2026). 

- [71] Corezoid Inc. _MCP Corezoid (AI Plugin)_ . Product documentation, 6 May 2026. 2026. url: https: //corezoid.com/blog/mcp-corezoid-ai-plugin/ (visited on 08/03/2026). 

- [72] Noy, S., & Zhang, W. “Experimental Evidence on the Productivity Effects of Generative Artificial Intelligence”. In: _Science_ 381.6654 (2023), pp. 187–192. doi: 10.1126/science.adh2586. 

- [73] Brynjolfsson, E., Li, D., & Raymond, L. “Generative AI at Work”. In: _The Quarterly Journal of Economics_ 140.2 (2025), pp. 889–942. doi: 10.1093/qje/qjae044. 

- [74] Dell’Acqua, F., McFowland, E., III, Mollick, E. R., Lifshitz, H., Kellogg, K. C., Rajendran, S., Krayer, L., Candelon, F., & Lakhani, K. R. “Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality”. In: _Organization Science_ 37.2 (2026), pp. 403–423. doi: 10.1287/orsc.2025.21838. 

- [75] Dillon, E. W., Jaffe, S., Immorlica, N., & Stanton, C. T. _Shifting Work Patterns with Generative AI_ . NBER Working Paper 33795. NBER, 2025. doi: 10.3386/w33795. 

- [76] Goodhart, C. A. E. “Problems of Monetary Management: The U.K. Experience”. In: _Papers in Monetary Economics, Vol. 1_ . Sydney: Reserve Bank of Australia, 1975. 

## **Status of the Work** 

This paper is a conceptual-theoretical position paper containing formal propositions. Propositions 1–4 are established within the specified models and provide no complete axiomatization of the economics of the firm. Weak probabilistic bisimulation supplies the semantics of valid external abstraction, and the NP-hardness result supplies a lower bound on the complexity of designing the human core. The hypothesis that the Compact Company will become the primary architecture of digitally representable activity requires empirical testing under the program specified in Section 16.
