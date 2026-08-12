# How to Become a Smart Company

AI makes most companies dumber. Architecture makes them smarter.

**Alexander Vityaz** · Corezoid Inc., Dnipro, Ukraine
[ORCID 0009-0006-0489-7881](https://orcid.org/0009-0006-0489-7881) · [corezoid.com](https://corezoid.com) · [simulator.company](https://simulator.company)
DOI: [10.5281/zenodo.21792643](https://doi.org/10.5281/zenodo.21792643)

#### **Abstract**

Artificial intelligence deployed within a fragmented enterprise architecture amplifies fragmentation accumulated across software, integrations, processes, vendor dependencies, and organisational routines. This article defines the resulting burden as the fragmentation tax and connects it to the grounding problem: different functions and systems operate through incompatible projections of the same company.

Drawing on the Conant–Ashby Good Regulator Theorem, the article argues that effective regulation requires a coherent model of the enterprise. It defines a Smart Company as an organisation with a proactive, executable digital twin in which actors, processes, connections, states, and transitions between states are represented explicitly.

This model gives the company two central properties: plasticity, which makes organisational structure available for deliberate change, and a Company Brain, which unifies memory, computation, routing, simulation, and the actions of people, software, and AI within a single operational loop.

API visibility is proposed as a practical diagnostic of whether the company possesses a coherent model of itself. The article concludes that AI becomes useful when embedded in an executable architecture that provides holistic operational context.

**Keywords:** Smart Company; executable digital twin; digital twin of the organisation; enterprise architecture; organisational cybernetics; Good Regulator Theorem; fragmentation tax; grounding; Company Brain; actor graphs; artificial intelligence; API architecture; metaprogramming

## **1 Introduction**

Since the beginning of the century, companies have endured a positively exhausting procession of technological tsunamis: cloud, APIs, smartphones, blockchain, machine learning, Big Data, AI. . . Not one of them has fundamentally changed the architecture of the enterprise. Each, however, has left a fresh little scar atop the old ones.

Every subsequent technological layer costs the company more than the one before it. It lands upon everything already accumulated: software, integrations, processes, vendor dependencies, organisational habits, and all the charming little compromises nobody dares to mention in board meetings. In engineering, this is called fouling. A ship loses speed not because the water has suddenly developed an attitude, but because its hull has become encrusted.

Fouling has a price: the fragmentation tax. Integrations, duplication, ‘consulting’, vendor lock-in, the synchronisation of changes between systems that were never designed as a whole in

*[Figure: a diagram of accumulated technology layers — cloud, API, ML, ESB, ETL, ERP, CRM, BI, blockchain, NFT, metaverse, RPA, process mining, digital twin — captioned "you started Corezoid Digital Transformation…". See the PDF.]*
_architecture does not make a company smarter. It merely makes it louder. It does not eliminate fragmentation; it amplifies it, rather brilliantly._

## **2 Why This Keeps Happening**

An ordinary car contains more than 30,000 parts. Behind every part are drawings, tolerances, specifications. Remove the drawings and the car becomes impossible. Engineering disciplines learnt long ago that one cannot build or improve what has not been modelled. Hence CAD, digital twins, and the whole rather sensible family of smart things: smartphone, smart city, smart home, smart vehicle.

Business, however, has never quite managed to create the notion of a Smart Company.

The CFO, COO, CIO, and CCO may sit in the same meeting room, but they are not discussing the same company. They are discussing different projections of it. The CEO carries another version; shareholders, naturally, carry several more. A single executable model of the company, one that everyone could actually rely upon, most often does not exist.

As a result, nearly every important decision is made not at the level of the system, but at the level of local pictures. Finance optimises one thing. Operations another. Sales a third. IT a fourth. The company appears unified only in presentations and financial reports. In reality, it survives on meetings, manual coordination, and the heroic stamina of people who should probably be on holiday.

Fragmentation attacks the very possibility of agreement. Clark and Brennan [7] showed that joint action requires common ground, established through a process they called grounding: a basis on which participants may reasonably believe they have understood one another well enough to perform the task. But in a fragmented company, the environment itself is hostile to grounding. Every function, system, and vendor adds a cost of coordination between different projections of the same reality.

The fragmentation tax is also, therefore, a grounding tax. A very elegant tax, naturally. Invisible, compounding, and never properly budgeted.

The architectural and economic consequences of organisational fragmentation are developed further in the phase model of enterprise evolution and in the management-debt framework [3, 6].

## **3 The Theorem Nobody Mentioned to You**

Conant and Ashby [8] formulated the Good Regulator Theorem in 1970—what may fairly be called the fundamental theorem of cybernetics: every good regulator of a system must be a model of that system.

Thus, building a model is not a charming optional extra. It is a mathematical necessity [1].

_This is not a metaphor. It is a requirement._

If a company has no coherent model of itself, it does not govern itself as a system. It coordinates fragments, compensates for symptoms, extinguishes deviations after the fact, and hopes that experienced people will somehow keep the entire contraption from embarrassing itself in public.

This mode can be sustained for years. Many firms have made a whole lifestyle of it. But it does not tolerate scale, speed, or technological shifts particularly well.

From this follows a simple and rather uncomfortable conclusion: a company needs an architecture that solves two tasks at once. It must provide a basis for regulation, and it must create a common operational ground for coordination between people, functions, and machines.

## **4 What a Smart Company Is**

A Smart Company is a company that has built its own proactive digital twin: an executable model of itself, in which all actors, processes, connections, states, and transitions between states are represented and made explicit [2–5].

Before such a twin exists, the enterprise is smeared across thousands of software categories, integrations, spreadsheets, chats, and local models. G2 reports more than 2,000 categories of enterprise software and services [9]. The company cannot see its own operational logic as a whole, because it assembled that logic in pieces—rather like building a manor house by ordering rooms from different catalogues.

Afterwards, a single executable model appears: a proper regulator of the company. Two properties follow.

### **4.1 The First Property: Plasticity**

Once a company is described as a model, its structure becomes available for conscious change—for metaprogramming [2].

In traditional corporate systems, most states are hidden: spread across databases, correspondence, spreadsheets, and the minds of employees who are, regrettably, mortal. Nobody sees the full state space in which the company exists at this very moment.

A digital twin makes these states explicit. Every actor, every process, every transition between them becomes visible and available for change.

To alter a process, reconfigure a connection, or switch a decision path is no longer a matter of months of cross-functional choreography. It becomes a change of parameters in the model. Much less dramatic. Much more civilised.

### **4.2 The Second Property: The Company Gets a Brain**

For the first time, the company’s memory and its ‘thinking’—the processes that transform data—are closed into a single loop.

The twin provides a unified memory: a graph of actors, connections, states, and the history of decisions. It provides an environment for thinking: computation, routing, simulation, and the actions of both humans and AI. [4]

When this model is connected to the flow of real events, the company gains not merely reporting about itself, but an operational digital organ of thought. This is precisely where AI belongs. Not on top of legacy. Not as yet another interface to chaos.

Not as a beautifully articulate concierge for a burning archive.

_AI is necessary as part of the company’s brain—but not instead of one. Architecture is what will make the company smarter._

## **5 Architectural Criteria of a Smart Company**

A Smart Company operates through an executable model that unifies actors, states, transitions, transactions, causal traces, and responsibility within one regulatory loop. Its digital twin remains connected to real events and provides governed operational context for people, programs, and AI.

## **6 The Test**

There is a simple way to discover whether your company has a model of itself.

Ask your CTO or CIO:

_How many external and internal APIs does the company use?_

APIs are the bloodstream of the enterprise. Every connection between systems, every data flow, every call from one service to another—all of this is API.

Not knowing how many there are is rather like a surgeon not knowing where the patient’s arteries are. One does not wish to be on that operating table.

## **7 What to Do**

It is impossible to stop reactive AI-ification. The budgets have already been allocated, the projects are under way, and the pressure to implement will only increase. The champagne has been opened; the deckchairs are being rearranged.

But in parallel, companies can—and must—begin a more fundamental piece of work: building what they have historically never had.

_An executable digital twin of the company itself. A model in which the enterprise can, for the first time, execute itself as a system._

This changes the meaning of what is happening. AI projects receive not fragments, but holistic context. Automation stops producing fragmentation, because fragmentation becomes visible. Board decisions cease to be detached from reality, because they are implemented at the level of a single model shared by everyone. The Smart Company, people, programs, and AI begin to operate within a coordinated version of reality [2–6].

A company without an executable model of itself is not merely badly managed. It is not managed.

## **Author Note**

At Corezoid, we have created a technology for growing digital twins of companies:

simulator.company.

Alexander Vityaz is the founder of Corezoid Inc. His work sits at the intersection of cybernetics, actor graphs, distributed computing architectures, and organisation theory.

## **References**

- [1] Vityaz, A. (2026). On the Necessity of Noise Suppression for Minimal Good Regulators: Factorization Theorems and a Closure Conjecture. Preprint. DOI: `10.13140/RG.2.2.33143.07843` .

- [2] Vityaz, A. (2026). Active Transaction Graphs: A Formal Framework for Transactional Interactive Systems. Article. DOI: `10.5281/zenodo.20747873` .

- [3] Vityaz, A. (2026). A Phase Model of Enterprise Evolution: From Fragmentation to the Autonomous Enterprise. Preprint. DOI: `10.13140/RG.2.2.24883.39207` .

- [4] Vityaz, A. (2026). Company Brain: The Architecture of General Company Intelligence. Preprint. DOI: `10.13140/RG.2.2.28274.88007` .

- [5] Vityaz, A. (2026). The Computable Boundary of the Firm: Information Conditions for Viability and the Transactional Architecture of the Digital Twin. Article. DOI: `10.5281/zenodo.20745927` .

- [6] Vityaz, A. (2026). Management Debt—Part I: Concept, Metrics, and Principles for Attributing Materialised Debts to Actor Accounts. Article. DOI: `10.5281/zenodo.21069692` .

- [7] Herbert H. Clark and Susan E. Brennan. Grounding in communication. In Lauren B. Resnick, John M. Levine, and Stephanie D. Teasley, editors, _Perspectives on Socially Shared Cognition_ , pages 127–149. American Psychological Association, Washington, DC, 1991. doi: 10.1037/10096-006.

- [8] Roger C. Conant and W. Ross Ashby. Every good regulator of a system must be a model of that system. _International Journal of Systems Science_ , 1(2):89–97, 1970. doi: 10.1080/00207727008920220.

- [9] Emily Malis Greathouse. New categories introduced to G2 in may 2025. G2, June 2025. URL `https://company.g2.com/news/new-categories-introduced-in-may-2025` .

- [10] Ray Kurzweil. The law of accelerating returns. Online essay, March 2001. URL `https://www.writ ingsbyraykurzweil.com/the-law-of-accelerating-returns` .

- [11] Gordon E. Moore. Cramming more components onto integrated circuits. _Electronics_ , 38(8):114–117, April 1965. URL `https://download.intel.com/newsroom/2023/manufacturing/moores-law-e lectronics.pdf` .

- [12] Chris Skinner. Banks with pre-internet age core systems have a heart that is no longer beating. The Finanser, December 2014. URL `https://thefinanser.com/2014/12/banks-with-pre-interne t-age-core-systems-have-a-heart-that-is-no-longer-beating` .
