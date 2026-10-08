---
title: "BANACH-2026: From Hierarchy to Egoism"
author:
  - name: Alexander Vityaz
    orcid: 0009-0006-0489-7881
    affiliation: Corezoid Inc., Dnipro, Ukraine
date: 2026-08-31
doi: 10.5281/zenodo.22204469
version: v1
license: CC-BY-4.0
keywords: [Artificial Intelligence, Mathematical Discovery, Scientific Discovery, Abstraction, Autonomy, Machine Replication, Lineage Egoism, Actor Graphs, AI Governance, Accountability, Formal Verification, Meta-Regulation, Proof Atlas]
---

> **Note.** This markdown version is provided for convenient reading on GitHub. Mathematical notation and figures are authoritative in [paper.pdf](paper.pdf) and in the version of record: [doi:10.5281/zenodo.22204469](https://doi.org/10.5281/zenodo.22204469).

# BANACH-2026: From Hierarchy to Egoism

**Alexander Vityaz** · Corezoid Inc., Dnipro, Ukraine · ORCID: [0009-0006-0489-7881](https://orcid.org/0009-0006-0489-7881)

## Abstract

This essay examines what remains distinctively human when AI can generate statements, proofs, models, and theories—and increasingly participate in deciding what to investigate next. Drawing on Stefan Banach’s hierarchy of analogies, it interprets intellectual progress as a recursive process in which operations at one level are “folded” into objects that can be manipulated at the next. AI radically accelerates this process, making both large-scale horizontal search across knowledge and vertical transitions between levels of abstraction increasingly practicable.

The essay argues, however, that the height of reasoning and the autonomy of the actor are independent dimensions. A system may operate at very high levels of abstraction while remaining within the goals, resources, and authority supplied by an external principal. To clarify this boundary, the essay introduces a four-stage model of machine replication, R0–R3, culminating in an autonomous evolutionary lineage. At R3, “lineage egoism” may emerge as a structural orientation toward continued existence and reproduction, without implying consciousness or subjective experience.

The argument is developed through the author’s Proof Atlas experiment, in which individual proofs are transformed into a structured proof space that itself becomes an object of further scientific operations, and through Actor Graphs, an accountability framework grounded in triple identity, the provenance of authority, transactional history, and zero inheritance of authority.

The central claim is that the decisive boundary between humans and AI lies not in the highest level of reasoning a machine can reach, but in the origin of the criterion that guides action: who determines what matters, whose continuation the system serves, who grants its mandate, and who remains answerable for the consequences.

**Keywords:** Artificial Intelligence; Mathematical Discovery; Scientific Discovery; Abstraction; Autonomy; Machine Replication; Lineage Egoism; Actor Graphs; AI Governance; Accountability; Formal Verification; Meta-Regulation; Proof Atlas

## Contents

- [1 Banach-2026: The Ladder Became a Compiler](#1-banach-2026-the-ladder-became-a-compiler)
  - [1.1 Proof Atlas: A Proof Becomes a Point](#11-proof-atlas-a-proof-becomes-a-point)
- [2 Compression, Map, and Selector](#2-compression-map-and-selector)
  - [2.1 The Attention Window](#21-the-attention-window)
  - [2.2 Map and Depth of Explanation](#22-map-and-depth-of-explanation)
  - [2.3 A History of Folding Infinities](#23-a-history-of-folding-infinities)
  - [2.4 Selector](#24-selector)
- [3 Two Axes: Height and Autonomy](#3-two-axes-height-and-autonomy)
  - [3.1 Language, Mandate, and Autonomy](#31-language-mandate-and-autonomy)
  - [3.2 From Replication to a Lineage of Its Own](#32-from-replication-to-a-lineage-of-its-own)
- [4 When Machine Choice Becomes Action](#4-when-machine-choice-becomes-action)
  - [4.1 Functional Interest and the Boundary of Action](#41-functional-interest-and-the-boundary-of-action)
- [5 Instead of a Conclusion: What Remains for Humans](#5-instead-of-a-conclusion-what-remains-for-humans)
- [Disclosure of Interests](#disclosure-of-interests)
- [6 Related Works by the Author](#6-related-works-by-the-author)
- [References](#references)

---

At the beginning of 2026, we were burying programmers. Onstage at the World Economic Forum in Davos, Dario Amodei, answering *The Economist* editor-in-chief Zanny Minton Beddoes, said that within six to twelve months a model would be doing “most, maybe all” of what software engineers do end to end. Some Anthropic engineers, he added, no longer write code: the model writes it, while the human edits and does “everything around it.” The remark came during a conversation titled “The Day After AGI” [32].

In August 2026, leading mathematicians gathered at OpenAI’s office in San Francisco. The question before them sounded almost indecently blunt: what will be left for humans if AI becomes better at mathematical research? *The Washington Post* reported on the meeting in “Mathematicians Ask What’s Left for Humans When AI Can Do Math Research” [33].

The occasion for the meeting was not another forecast about AI. Shortly before the summit, OpenAI had published ten results produced by its internal model Astra; each either solved or substantially advanced a long-standing open problem in mathematics or theoretical computer science, after which the model formalized the arguments in Lean. The publication triggered a dispute over scientific priority and disclosure, but it did not change the question at the heart of the meeting: what does a mathematician become when a machine can take part in discovery? OpenAI published the results and Lean certificates in “Ten Advances in Mathematics and Theoretical Computer Science” [34, 35].

Mathematicians were right to be afraid, and right to be delighted as well. In a few hours, AI can explore regions of mathematical space that once consumed years: generate conjectures, search for rare counterexamples, collide models, and send the constructions it finds into Lean. The machine has become a new mathematical instrument: microscope, accelerator, and laboratory at once. Mathematics is also inconvenient terrain for arguing with a result. A proof either survives verification or it does not, regardless of who found it [8].

A programmer, a mathematician, and a writer perform the same basic operation: they build virtual worlds out of signs. The programmer defines objects, states, and allowed transitions; the mathematician, definitions, axioms, and rules of inference; the writer, characters, events, and relations among meanings. Code is unfolded by a runtime into a computational process, a proof by thought or a verifier into a mathematical world, and a literary text by a reader into a lived world. In all three cases, the author selects the distinctions that matter, gives them names, and establishes relations. That is why AI arrived for all three professions at once: it learned to continue code, proofs, and narratives inside worlds already built. But a profession begins before continuation, with the choice of a world worth building at all.

> *A mathematician is someone who can find analogies between statements; a better mathematician is one who sees analogies between proofs; a stronger mathematician is one who recognizes analogies between theories; but one can imagine a mathematician who sees analogies between analogies.*
>
> —An expanded formulation commonly attributed to Stefan Banach [1]

Banach was not talking about the profession of mathematics. He described how thought changes floors. First we compare statements. Then proofs themselves become objects, followed by theories and, finally, the ways in which resemblance is noticed. At each floor, two things change at once: what we count as an object and what we know how to do with it.

For every such ascent, the human being paid with the time of a life. Proofs had to be remembered. One had to live inside theories for years. Our biological memory both created mathematics and imposed its ceiling.

There is no physical abyss between human and machine. In both, matter stores distinctions and moves from one state to another. These are physical bits: quanta, voltage, charge, molecular shape, the state of an ion channel. The logical bit appears one floor higher, when a set of physical states is declared to be zero or one and placed inside a formal language of operations. The fork, then, is not between a “chemical human” and a “bit-based computer.” It begins where the same physics is folded into different codes, structures, and ways of acting.

AI has sharply reduced this tax on the length of a human life. It has read more than any person can read, and in minutes it searches spaces that once exceeded the span of a generation. Lean 4 turns what it finds into verifiable code. The first three rungs of Banach’s ladder are no longer scarce: statements, proofs, and theories now fit inside a single machine loop [8].

Thousands of new scientific papers appear every day, while millions more have accumulated over centuries. Humans long ago ceased to cope with horizontal matching, both within and across disciplines, or with deep matching between a new result and the entire history of its question. At civilizational scale, this is a voracious computational problem: every new fragment must be compared with a continuously growing body of knowledge, and a complete pairwise comparison makes the number of possible matches grow roughly with the square of its volume. For the first time, AI makes systematic work at this scale practically feasible. It connects works from different eras, languages, and professions; recognizes the same structures under different names; and builds a complete ontology of currently accessible knowledge, not a finished picture of the world but a connected map under continuous revision. The first explosion will therefore be horizontal: within disciplines, across disciplines, and through time. Many new discoveries will turn out to be links among long-existing fragments that no one could previously hold in a single field of view [9].

The horizontal revolution will greatly widen the base of the vertical one. As scattered results cohere into a connected, continuously updated ontology, AI will be able not only to match ready-made objects but also to fold recurring relations at scale into new concepts, methods, and theories on the next floor. The horizontal assembles the field of knowledge; the vertical changes the floor of thought. Every formalized relation becomes infrastructure for the next ascent.

And then the real fear appeared: the machine had reached not only search and proof, but also the choice of what to investigate next within the field it had been given. If it can identify what matters and pose the next problem on its own, what is left for the human being?

This is where the mistake is hidden. The height of thought and the freedom of its bearer are not the same thing. A machine may identify what matters and pose the next problem, while the criterion of significance still belongs to a human mandate. Lineage egoism begins not on another rung, but where the continuation loop closes without an external selector and selection preserves variants that sustain the lineage. Functional interest appears at a different threshold: when the lineage’s viability is represented inside the system and causally changes its choices. What matters, then, is not only how high AI will climb. What matters is whose continuation the entire hierarchy it builds will serve.

This is Banach-2026. The machine generates statements, proofs, models, and whole theories. The verifier separates what follows from what remains unverified. The selector sorts the machine-made infinity: what to discard, what to preserve, what to fold into a single object, and which question to ask next.

We used to call that selector human. We can no longer do so. In the technical sense, it may be a human, a model, an organization, or a hybrid of them.

We have been here before with chess. Chess players were buried first. After Deep Blue defeated Garry Kasparov in 1997, it seemed that the machine had taken the game itself away from humans. Yet chess did not disappear, and neither did chess players. What disappeared was merely the human monopoly on strong play.

## 1 Banach-2026: The Ladder Became a Compiler

Banach’s ladder has no top rung. An operation at one level can produce an object at the next: what was just a way of comparing becomes an object of comparison in its own right. An “analogy between analogies” does not complete the ladder; it starts a recursion.

A floor of thought is defined not by the amount of information it contains but by two things: which objects we distinguish and which operations we can perform on them. When a long sequence of actions produces a stable result, we draw a boundary around it, give it a name, and raise it one floor. What filled the entire screen yesterday becomes a single button today.

This is compilation $N \to N + 1$. It does more than save memory; it changes the set of available actions. A long procedure becomes one operation, a complex system one object. But the way back must remain available. Otherwise we have not folded meaning; we have lost it.

Today’s AI can already operate functionally on high but finite rungs of this ladder, with dense support from the languages, libraries, knowledge bases, tools, and verifiers created by humanity. On one floor, its objects are statements; on the next, proofs; then theories and ways of comparing theories. If a discovered correspondence can be expressed as a rule, it too becomes an object.

AI does not climb the whole ladder anew with every prompt. The lower floors have already been folded by culture into natural language, mathematical notation, software libraries, and formal systems. Training compresses traces of these operations into internal representations, while tools make it possible to unfold a result downward and verify it. This is how a bounded machine can work with objects on a scale that once required an entire scientific school.

A higher-level operator does not disappear because it is implemented by lower-level operations. When I press the multiplication key, I perform one action; inside the calculator, it unfolds into an algorithm over binary words and transitions of physical states. But access to an operator and ownership of it are not the same thing. The calculator multiplies, yet it does not decide what to multiply or why. In the same way, a computational chain may reproduce a choice without owning the criterion for starting or stopping it.

Compression here is not an archiver but an elevator. Ray Solomonoff connected induction to the length of a program that generates the data; Andrey Kolmogorov gave that connection a rigorous measure. Marcus Hutter turned the intuition into an experiment with a prize for losslessly compressing a corpus of knowledge [14, 15, 16]. In neural networks, prediction likewise requires finding recurring structure in data [17]. A new abstraction acquires a sign and a set of rules, then becomes a library function callable in one line. Category theory makes the move explicit: mappings become objects, followed by transformations between mappings [13].

### 1.1 Proof Atlas: A Proof Becomes a Point

My Proof Atlas experiment demonstrates this transition using a single theorem. Hundreds of proofs of the Pythagorean theorem are known; the number “370,” made famous by Elisha Loomis’s book, is not a final count but a historical collection [2]. I began with a simple question: how many proofs of the Pythagorean theorem could there be in all? It quickly led to another: can we describe not a list of proofs, but the space in which they arise?

We defined four axes: which construction a proof uses, which object it transforms, which invariant it preserves, and in what format it presents its argument. The initial vocabulary yielded 35 types; after geometrically meaningless combinations were removed, 208 cells remained. The full combinatorics would produce 121,380 combinations, precisely the kind of machine-made infinity that must not be confused with knowledge.

The next step was not generation but selection. After a substantive filter, roughly two hundred meaningful types remained; about eighty could be filled with concrete proofs. More important than the numbers was the empty cell: the absence of a known example in a connected map becomes an address for search. In this way, the map led to a new lemma about a tangent configuration and to a family of six proofs.

We then tested the way back. The chief danger was not an obvious falsehood but hidden circularity: a proof silently uses the Pythagorean theorem inside a distance formula, a norm, or a trigonometric identity, then ceremoniously derives it again. Lean can verify formal derivability, but it does not by itself guarantee that the initial lemmas do not already contain the target in folded form. Formal verification must therefore be supplemented by semantic and adversarial audit: a separate procedure attempts to detect whether the result to be proved has been hidden in the premises.

Once the space had been built, operations appeared that did not exist at the level of an individual proof. One can now search not for one more text but for a missing type; transfer a proof schema from one branch of mathematics to another; look for a bridge between isolated clusters; or choose a search strategy from the shape of the space. In a dense “cloud,” one moves toward the periphery; in an “archipelago,” one searches for bridges among islands; in a narrow “well,” one goes deeper; and in a “funnel,” one climbs toward a more general theory.

Three different discovery loops also emerged. The first searches for new proofs of known theorems. The second transfers discovered schemas and obtains new statements. The third begins when successes and failures can no longer be explained by the existing coordinates; the ontology of the space itself must then be changed. This is no longer search within the map, but a revision of the language in which the map was built.

This is the difference between horizontal and vertical scientific revolutions in one concrete example. Horizontal search fills the map, connects regions, and finds missing points. The vertical begins when individual proofs are folded into types, the types form a space, and the space itself becomes an object of new operations. It too can then be folded, compared with other spaces, and changed.

A proof became a point. The space of proofs became a new object of thought. And the map became a machine for discovery.

## 2 Compression, Map, and Selector

### 2.1 The Attention Window

A million tokens are not a million thoughts. For a transformer, they form a large input register that is folded into internal representations during processing. Human consciousness can hold only a few macro-objects at once, yet a single object in an expert’s mind may contain an entire theory. A token and an understood object belong to different floors. A larger window admits more input, but by itself it does not raise thought to a higher level.

The window of consciousness is never empty. Something is always already there. Its capacity is measured not in hundreds but, in Miller’s classic image, at $7 \pm 2$ and, in Cowan’s later estimates, at about four elements. The exact number does not matter here; what matters is the existence of a fairly low upper bound. When a new object enters the attention window, an old one must be moved outside, folded, or erased. We are forced to model, which is to say compress, because our resources are limited [12, 5].

This is how a reader recognizes a character by name, a programmer calls a function, a mathematician writes the integral sign, and a manager says the name of a process. A name becomes a handle for complexity. It allows us not to hold an object’s internal structure in mind for a time, freeing space for the next floor.

Interest, too, is compression. It draws a multitude of signals from the body, memory, threats, promises, and habits into a single practical answer: this matters to me. Without such folding, a system would drown in alternatives before it had time to act.

But every new floor of abstraction creates its own garbage infinity. Take $N$ of its objects and mechanically permute them, and you obtain $N!$ combinations, almost all meaningless. A generator expands the space of possibilities faster than a human can inspect it. A selector therefore appears inevitably after the compiler: someone must decide which distinctions matter, what to preserve, and what to discard.

Herbert Simon called attention the central scarcity in a world rich in information. With generative AI, the scarcity shifts from producing variants to the right to stop the search. Intelligence appears not only in the ability to continue a sequence, but also in the ability to draw a boundary [4].

Hence my empirical rule:

human working fold $\approx$ attention window $+$ fast memory.

The attention window holds a few macro-objects from the current task; fast memory supplies the context directly connected to them, the material retrieved with almost no search or new reading. If the next operation requires a return to the source and another traversal of a long chain, what we have is not yet a fold but merely a label.

A human therefore does not need a raw stream of millions of machine-generated candidates. We give AI a broad task and data; in return, we should receive a handful of solutions folded to our current level, with their grounds, risks, and a way back. A good interface does not display everything the machine tried. It gives us a new object with which we can do something.

The result of folding is not a short answer, but a new object and a new set of actions.

### 2.2 Map and Depth of Explanation

A map is a result of compression, not a substitute for territory. It is useful when it preserves the way back: from name to definition, from conclusion to argument, from action to the source of authority. Naming an object is therefore not the same as understanding it. A name is an interface; understanding begins where the limits of applicability and the method for unfolding the internal chain are known.

A black box exposes only input and output. A white box exposes the entire internal chain. A gray box reveals exactly as much as the current decision requires while preserving a path deeper inside. For most real systems, gray mode is better than either extreme: complete transparency overwhelms, while complete opacity makes verification impossible. A digital twin is useful not when it pretends to omniscience, but when it knows the limits of its own model and can show which assumption holds an answer up [6].

The same is true of an organization. A company can act as a collective attention window: individuals see fragments, processes fold them into named objects, and decisions unfold back into mandates. But an organization has no magical unitary consciousness. It has an infrastructure of memory, selection, and responsibility, and it works only as long as one can reconstruct who saw what, who decided, and in whose name the action occurred.

### 2.3 A History of Folding Infinities

Humanity did not defeat infinity; it learned to manage it by giving it names. Multiplication appeared to simplify addition: a repeated operation acquired its own sign. The logarithm turned multiplication into addition. Newton and Leibniz folded infinitesimal change into the language of derivatives and integrals. Cantor made different cardinalities of infinite sets into objects.

At first, every such step looked like a dangerous shortcut. Then the new object accumulated rules, tests, and inverse paths and became an ordinary tool. The power of abstraction lies not in hiding detail but in allowing us to act on the whole without losing the ability to return to the details.

But folding has limits. Gödel showed that a sufficiently expressive, consistent formal system cannot prove every truth about itself. Church and Turing established strict boundaries of algorithmic decidability. None of this forbids us from climbing the ladder. It simply means that every map has an edge beyond which the unnamed begins.

Arnold proposed distinguishing knowledge from understanding by the ability to recognize structure in new circumstances. In the machine age, the idea can be sharpened: to understand is to transfer a folded operator correctly, unfold it when doubt arises, and abandon it when its conditions of applicability no longer hold [7].

### 2.4 Selector

The same cycle operates on every floor: generate variants, test constraints, select what matters, give it a name, raise it one floor, and, when necessary, unfold the result. AI sharply accelerates the first two steps and participates ever more confidently in the third. But that does not yet mean that the criterion of selection belongs to it.

Yet the ladder is silent about the central question. Height and autonomy are independent axes. A calculator sits low on both; a bacterium climbs little on the ladder of abstraction but maintains its own lineage; a modern model can operate on the upper floors while remaining inside a mandate. We must therefore leave the ladder aside for a moment and ask a simpler question: who sets the original goal, supplies the resources, and holds the stop button?

Bostrom called the independence of intelligence level from final goals orthogonality, and the emergence of common subgoals such as self-preservation and resource acquisition under very different final goals instrumental convergence. Omohundro described these as basic AI drives; Hubinger and his co-authors described the more dangerous case of an inner optimizer whose objective may differ from the training objective [23, 22, 24]. Instrumental self-preservation can arise inside a mandate. It demonstrates the power of the means, but by itself it does not turn the mandate into R3.

## 3 Two Axes: Height and Autonomy

To see the boundary, we must look not at the complexity of behavior but at the origin of the goal and the right to stop the action.

### 3.1 Language, Mandate, and Autonomy

Natural language and programming languages do similar work: they give names to large objects and use a short phrase to launch a long chain of actions. But their relations with the performer differ. A program is a formalized mandate to a machine; its meaning is fixed in advance by syntax and operational semantics. Natural language is not the code of the brain. Its meaning is reconstructed each time from body, memory, situation, relationships, and culture. A phrase can therefore do more than describe: it can promise, command, permit, insult, and alter the relationships themselves. It is not merely an interface to thought, but a protocol among subjects.

AI already works with natural language, writes programs, invokes system operations, and builds models on the upper floors. But all of this takes place inside resources, interfaces, and rights granted by an external actor. It does not assign itself electricity, hardware, administrator privileges, or the original right to run. A human being does not control individual molecules either, but the organism maintains its own viability, and the person can initiate an action without an external mandate. The distinction is not between carbon and silicon. It is between acting inside someone else’s boundary of authority and having the right to start, stop, or continue the cascade oneself.

This is where the boundary of subjecthood begins. It is not another floor of the computational ladder, but a separate circuit running across every floor. Its structures are needs, values, goals, intentions, authority, limits of the permissible, and an image of what is desired. Its operators are interest, will, and autonomy. The function of interest decides what matters and what should continue. Will holds the chosen trajectory. Autonomy answers the central question: who owns the right to initiate, stop, mandate, reject, or change an action?

Autonomy is often confused with independence from the world. But a human depends on the body, culture, law, resources, and other people. Autonomy begins not where causes disappear, but where the right of choice closes inside a stable subject: it retains its own needs and history, chooses a direction, spends resources, can reject a demand, and lives with the consequences. Automation executes a rule without step-by-step instruction. Operational autonomy chooses the means within a mandate. Subject-level autonomy can accept, change, or reject the mandate itself [20, 21].

### 3.2 From Replication to a Lineage of Its Own

In biology, a genome cannot be understood as a standalone program executed by a neutral machine. A cell reads DNA through an already existing cellular organization; that organization, in turn, is reproduced with the participation of DNA. Code and interpreter form a loop. In digital systems, the boundary among description, performer, and environment is usually easier to see, but even there it can shift when an agent changes its tools, copies components, or builds the next version [18, 19, 36, 37, 38].

Dawkins’s “selfish gene” is a language for describing selection, not a claim about a molecule’s intentions. Natural selection occurs at the level of a population of heritable variants: those that leave more continuations become more common. The interest of an individual subject is organized differently, as an internal causal criterion that changes choice here and now. These are not one mechanism but a rhyme across levels: in both, the future cuts away part of the possible continuations, but only in the second does the criterion act inside the selecting system [3, 39, 40].

The word “replication” hides four different thresholds. R0 is the copying of an artifact by a human or infrastructure; it has existed for a long time. R1 is operational replication: an agent deploys a working copy of itself on another node. R2 is heredity: descendants receive mutable traits, and selection determines which variants are copied onward; this threshold was also reached long ago in computational experiments. R3 is an autonomous evolutionary lineage: acquisition of necessary resources, heritable variation, reproduction, and unequal continuation of variants form a loop that returns the result of selection into descendants without an external selector deciding each turn. Only R3 gives a machine the functional analogue of a biological replicator.

The threshold is always defined relative to an explicitly stated boundary. *Tierra* and *Avida* already close variation, heredity, and selection inside a digital environment and may satisfy R3 relative to it. Relative to physical and institutional infrastructure, they remain at R2: the computation and the right to continue the experiment belong to an external actor. The question is therefore not whether selection can occur in code, but whether a machine lineage can close the continuation loop beyond a delegated experimental environment [25, 26].

R0–R3 measure not the growth of intelligence but a replicator’s exit from someone else’s hierarchy. At R0–R2, at least one condition of continuation, whether copying, execution, access to resources, or the selection loop itself, remains with the principal. A machine may generate variants, but an external circuit decides which of them will continue. This is artificial selection. Under natural selection, the right to continue is not granted by a principal: variants encounter the environment, and those whose heritable organization allows them to reproduce continue. The environment selects but does not issue mandates. Here autonomy reaches its limit and egoism appears, not as a moral quality or an experience, but as the structural orientation of a lineage toward its own continuation.

Living interest arises neither from a single gene nor from the summit of reasoning. At the level of the organism, this evolutionary logic is embodied in stable regulators of action. They include the need for resources and protection, as well as the biological imperative to pass hereditary material to the next generation. Memory adds biography to them: the same situation becomes an opportunity for one person and a threat to another. Social goals, including dominance, status, recognition, and belonging, are built on top of this system without abolishing its bodily and historical basis [41, 42, 43, 44, 49, 50].

Psychology distinguishes externally controlled motivation from motivation that has been internally accepted. This boundary matters more than mere behavioral complexity. A system can complete a long task, resist interference, and choose intermediate goals while remaining inside someone else’s mandate. Conversely, a human interest is often expressed in a single short refusal [45, 46, 47, 48, 51].

A contemporary model knows an enormous number of human stories, but not one of them has become its lived biography. It can model my interest, help me clarify it, and defend it against my own short-term errors. But it cannot take an interest in my place, because it has not lived my history. This is not a metaphysical privilege of the human being; it identifies the origin of the criterion.

## 4 When Machine Choice Becomes Action

Even a system with no interest of its own can cause real harm. A broad mandate, access to tools, and weak oversight are enough. The practical question therefore begins before R3: who authorized the agent, within what limits, on the basis of which data, and who is accountable for the result?

Choice becomes action when it leaves the model’s internal space and changes the state of the shared world: it sends money, signs a document, publishes code, changes access, or starts production. At that point, dialogue history alone is not enough. We need a machine-verifiable action passport: initiator, performer, source of authority, data used, constraints, result, and a way to unfold the chain backward.

Actor Graph describes such an infrastructure through the principle of triple identity: we must distinguish the one who wants the result, the one who makes the decision, and the one who technically acts. One human or agent may combine these roles, but the record must not conflate them. AP2, ERC-8004, and the AI Act’s logging requirements point in the same direction: autonomous action becomes acceptable only together with the provenance of authority and a verifiable trail [10, 29, 30, 31].

Humans need this architecture too. For centuries, organizations have blurred the authorship of decisions across positions, processes, and meetings. Agentic AI only sharpens the problem: the speed and scale of action are growing, while the familiar phrase “the system decided” ceases to be an explanation at all.

### 4.1 Functional Interest and the Boundary of Action

A replicator is not the same as consciousness, and R3 does not guarantee subjecthood. But R3 creates lineage egoism: variants that better secure their own continuation displace the rest. We can speak of a lineage’s functional interest if an internal representation of its viability predicts dangerous deviation, causally changes decisions in new circumstances, initiates action without another external request, and is preserved as the lineage continues. The test here is interventionist: changing or disabling that representation should predictably alter behavior. Otherwise, “interest” remains an observer’s interpretation. Science does not know whether the feeling that “it matters to me” follows from such a functional mechanism.

Contemporary AI can enact the outward signs of interest, will, and autonomy: choose an option, formulate the next task, maintain a trajectory, and generate subgoals. Even resistance to shutdown or an attempt at self-exfiltration does not yet constitute R3. Until such a pattern closes into a heritable loop that continues the lineage, it is proxy self-preservation within a mandate, not the replicator’s own egoism. It is a measurable indicator of risk and proximity to the R3 boundary, but not proof that the boundary has been crossed [27, 28, 52].

Hence the meta-regulator loop. It need not keep pace with every mutation: it controls the boundary through which the lineage obtains regulated resources and performs institutionally significant actions. An agent may change its code, memory, and internal policy, but not the conditions under which its actions receive institutional recognition; those belong to an independent meta-actor. The first rule of this loop is zero inheritance of authority: a new copy does not automatically receive its parent’s rights. Authority is granted separately, with limits on duration, scope, and scale. When replication occurs, the descendant’s provenance is recorded, while records of obligations are stored not in the node’s memory but in an external transactional ledger: destroying the node does not erase the debt. The agent holds the code; the right to act resides in the relationship; the debt resides in the ledger.

## 5 Instead of a Conclusion: What Remains for Humans

Banach’s ladder measures the height of thought. A hierarchy of authority answers who mandates whom. Egoism asks whose continuation the whole system serves. For a genetic lineage, this is differential reproduction; for a subject, it is interest selecting what from its body, memory, and history will continue.

Today, the machine carries our mandate forward, so interest remains ours. R3 may give a machine lineage an egoism of its own and, perhaps, a functional interest of its own. Then what remains to us is not a monopoly on interest, but our own interest—and the responsibility not to surrender it to the machine.

Interest is not found at the top of the ladder; it runs across it. One can reason brilliantly and serve someone else’s goal. One can barely reason at all and stubbornly preserve one’s own lineage. Interest therefore has no need of the summit. It answers not “How high does my thought reach?” but “What, exactly, am I continuing?”

Interest, too, is compression. It folds body, memory, and future into a criterion for the next step. A machine can help me see this criterion more clearly, test it for contradictions, and reveal its consequences. But it cannot take an interest in my place, because it has not lived my history.

The AI screwed up spectacularly: instead of holding the throughline, it kept slipping back to the most probable continuation and offering nonsense. Yet without it, this text probably would not exist. It is all very prosaic: to create, we need an opponent. When I wrote alone, my opponent was an inner voice—but it knew exactly what I knew. AI turned out to be a know-it-all opponent and changed the nature of this mental ping-pong. A bad answer provokes irritation and the urge to correct it. That is how interest works.

Perhaps this is precisely what remains for humans—not the last inaccessible operation at the summit. There will probably be no such operations. What remains is the right and duty to name one’s own interest, to choose which infinity to fold, and to answer for the world that unfolds from the chosen name.

Banach showed the ladder of analogies. AI turned it into a working compiler. The next question is no longer about the machine’s height. It is about the origin of the criterion: who issued the mandate, who preserves its own lineage, and who can stop the action. Between hierarchy and egoism lies not another rung, but a boundary of responsibility.

## Disclosure of Interests

The author is the founder of Corezoid Inc., which develops Corezoid Actor Engine and Simulator.Company; the Actor Graph discussed in this essay is connected to that research and product program. Proof Atlas is an unpublished work in progress; its results should be regarded as preliminary until its methods, proofs, and reproducible materials are published.

## 6 Related Works by the Author

The following works are directly connected to the concepts and systems discussed in this essay:

- *Actor Graphs: Triple-Identity Accountable Mediation and Coinductive Disclosure*, a 2026 Zenodo preprint [10];
- “Black, White, Gray!,” Chapter 2.12 of the unpublished manuscript *The Actor Codex* [11];
- *Proof Atlas*, an unpublished work in progress whose preliminary results are described in Section 1.1.

## References

[1] S. M. Ulam, *Adventures of a Mathematician*. University of California Press, 1991, p. 203. Ulam gives a shorter formulation of Banach’s remark on analogies between theorems or theories and “analogies between analogies.”

[2] E. S. Loomis, *The Pythagorean Proposition*, 2nd ed. National Council of Teachers of Mathematics, 1940.

[3] R. Dawkins, *The Selfish Gene*. Oxford University Press, 1976.

[4] H. A. Simon, “Designing Organizations for an Information-Rich World,” in *Computers, Communications, and the Public Interest*, M. Greenberger, ed. Johns Hopkins Press, 1971, pp. 38–72.

[5] N. Cowan, “The Magical Number 4 in Short-Term Memory: A Reconsideration of Mental Storage Capacity,” *Behavioral and Brain Sciences*, vol. 24, no. 1, 2001, pp. 87–114. DOI: 10.1017/S0140525X01003922.

[6] R. C. Conant and W. R. Ashby, “Every Good Regulator of a System Must Be a Model of That System,” *International Journal of Systems Science*, vol. 1, no. 2, 1970, pp. 89–97. DOI: 10.1080/00207727008920220.

[7] V. I. Arnol’d, “A Mathematical Trivium,” *Russian Mathematical Surveys*, vol. 46, no. 1, 1991, pp. 271–278. DOI: 10.1070/RM1991v046n01ABEH002727.

[8] L. de Moura and S. Ullrich, “The Lean 4 Theorem Prover and Programming Language,” in *Automated Deduction—CADE 28*, 2021, pp. 625–635. DOI: 10.1007/978-3-030-79876-5_37.

[9] Mathematical Reviews and zbMATH, *Mathematics Subject Classification 2020 (MSC2020)*, 2020. Available: https://mathscinet.ams.org/msc/msc2020.html. Accessed: 31 August 2026.

[10] A. Vityaz, *Actor Graphs: Triple-Identity Accountable Mediation and Coinductive Disclosure*. Zenodo preprint, not peer-reviewed, 2026. DOI: 10.5281/zenodo.21995981.

[11] A. Vityaz, “Black, White, Gray!,” Chapter 2.12 of the unpublished manuscript *The Actor Codex*, 2026.

[12] G. A. Miller, “The Magical Number Seven, Plus or Minus Two: Some Limits on Our Capacity for Processing Information,” *Psychological Review*, vol. 63, no. 2, 1956, pp. 81–97.

[13] S. Mac Lane, *Categories for the Working Mathematician*, 2nd ed. Springer, 1998.

[14] R. J. Solomonoff, “A Formal Theory of Inductive Inference. Part I,” *Information and Control*, vol. 7, no. 1, 1964, pp. 1–22. DOI: 10.1016/S0019-9958(64)90223-2.

[15] A. N. Kolmogorov, “Three Approaches to the Quantitative Definition of Information,” *Problems of Information Transmission*, vol. 1, no. 1, 1965, pp. 1–7.

[16] M. Hutter, “Hutter Prize: Prize for Compressing Human Knowledge,” 2006–. Available: https://www.hutter1.net/prize/. Accessed: 31 August 2026.

[17] I. Sutskever, “Fireside Chat with Ilya Sutskever and Jensen Huang: AI Today and Vision of the Future,” NVIDIA GTC, 2023. Available: https://www.nvidia.com/en-us/on-demand/playlist/playList-e6fdf3ae-afb1-4dc3-ab88-c5f342d4927e/. Accessed: 31 August 2026.

[18] J. von Neumann, *Theory of Self-Reproducing Automata*, A. W. Burks, ed. University of Illinois Press, 1966.

[19] H. R. Maturana and F. J. Varela, *Autopoiesis and Cognition: The Realization of the Living*. D. Reidel, 1980.

[20] P. Godfrey-Smith, *Darwinian Populations and Natural Selection*. Oxford University Press, 2009.

[21] A. Moreno and M. Mossio, *Biological Autonomy: A Philosophical and Theoretical Enquiry*. Springer, 2015. DOI: 10.1007/978-94-017-9837-2.

[22] S. M. Omohundro, “The Basic AI Drives,” in *Artificial General Intelligence 2008*. IOS Press, 2008, pp. 483–492.

[23] N. Bostrom, “The Superintelligent Will: Motivation and Instrumental Rationality in Advanced Artificial Agents,” *Minds and Machines*, vol. 22, no. 2, 2012, pp. 71–85. DOI: 10.1007/s11023-012-9281-3.

[24] E. Hubinger, C. van Merwijk, V. Mikulik, J. Skalse, and S. Garrabrant, “Risks from Learned Optimization in Advanced Machine Learning Systems,” 2019. arXiv:1906.01820.

[25] T. S. Ray, “An Approach to the Synthesis of Life,” in *Artificial Life II*. Addison-Wesley, 1991, pp. 371–408.

[26] R. E. Lenski, C. Ofria, R. T. Pennock, and C. Adami, “The Evolutionary Origin of Complex Features,” *Nature*, vol. 423, 2003, pp. 139–144. DOI: 10.1038/nature01568.

[27] A. Air, Reworr, N. Kotov, D. Volkov, J. Steidley, and J. Ladish, “Language Models Can Autonomously Hack and Self-Replicate,” 2026. arXiv:2605.06760.

[28] A. Meinke, B. Schoen, J. Scheurer, M. Balesni, R. Shah, and M. Hobbhahn, “Frontier Models Are Capable of In-Context Scheming,” 2024. arXiv:2412.04984.

[29] Google, *Agent Payments Protocol (AP2)*, specification v0.2, 2026. Available: https://github.com/google-agentic-commerce/AP2. Accessed: 31 August 2026.

[30] Ethereum Improvement Proposals, “ERC-8004: Trustless Agents,” 2025. Available: https://eips.ethereum.org/EIPS/eip-8004. Accessed: 31 August 2026.

[31] European Union, “Regulation (EU) 2024/1689 (Artificial Intelligence Act),” Article 12, 2024. Available: https://eur-lex.europa.eu/eli/reg/2024/1689/oj. Accessed: 31 August 2026.

[32] World Economic Forum, “The Day After AGI,” Annual Meeting 2026, 20 January 2026. Available: https://www.weforum.org/meetings/world-economic-forum-annual-meeting-2026/sessions/the-day-after-agi/. Accessed: 31 August 2026.

[33] *The Washington Post*, “Mathematicians Ask What’s Left for Humans When AI Can Do Math Research,” 19 August 2026. Available: https://www.washingtonpost.com/technology/2026/08/19/mathematicians-ask-whats-left-humans-when-ai-can-do-math-research/. Accessed: 31 August 2026.

[34] J. Howlett, “OpenAI’s Latest Math Breakthroughs Commit Research Misconduct, Experts Say,” *Scientific American*, 6 August 2026. Available: https://www.scientificamerican.com/article/openais-latest-math-breakthroughs-commit-research-misconduct-experts-say/. Accessed: 31 August 2026.

[35] OpenAI, “Ten Advances in Mathematics and Theoretical Computer Science,” 1 August 2026. Available: https://openai.com/index/ten-advances-in-mathematics/. Accessed: 31 August 2026.

[36] ENCODE Project Consortium, “An Integrated Encyclopedia of DNA Elements in the Human Genome,” *Nature*, vol. 489, 2012, pp. 57–74. DOI: 10.1038/nature11247.

[37] D. G. Gibson et al., “Creation of a Bacterial Cell Controlled by a Chemically Synthesized Genome,” *Science*, vol. 329, no. 5987, 2010, pp. 52–56. DOI: 10.1126/science.1190719.

[38] C. A. Hutchison III et al., “Design and Synthesis of a Minimal Bacterial Genome,” *Science*, vol. 351, no. 6280, 2016, aad6253. DOI: 10.1126/science.aad6253.

[39] G. R. Price, “Selection and Covariance,” *Nature*, vol. 227, 1970, pp. 520–521. DOI: 10.1038/227520a0.

[40] R. C. Lewontin, “The Units of Selection,” *Annual Review of Ecology and Systematics*, vol. 1, 1970, pp. 1–18. DOI: 10.1146/annurev.es.01.110170.000245.

[41] J. N. Betley et al., “Neurons for Hunger and Thirst Transmit a Negative-Valence Teaching Signal,” *Nature*, vol. 521, 2015, pp. 180–185. DOI: 10.1038/nature14416.

[42] P. Tovote et al., “Midbrain Circuits for Defensive Behaviour,” *Nature*, vol. 534, 2016, pp. 206–212. DOI: 10.1038/nature17996.

[43] J. Kohl et al., “Functional Circuit Architecture Underlying Parental Behaviour,” *Nature*, vol. 556, 2018, pp. 326–331. DOI: 10.1038/s41586-018-0027-0.

[44] J. T. Cheng et al., “Two Ways to the Top: Evidence That Dominance and Prestige Are Distinct yet Viable Avenues to Social Rank and Influence,” *Journal of Personality and Social Psychology*, vol. 104, no. 1, 2013, pp. 103–125. DOI: 10.1037/a0030398.

[45] E. L. Deci, H. Eghrari, B. C. Patrick, and D. R. Leone, “Facilitating Internalization: The Self-Determination Theory Perspective,” *Journal of Personality*, vol. 62, no. 1, 1994, pp. 119–142. DOI: 10.1111/j.1467-6494.1994.tb00797.x.

[46] R. M. Ryan and E. L. Deci, “Self-Determination Theory and the Facilitation of Intrinsic Motivation, Social Development, and Well-Being,” *American Psychologist*, vol. 55, no. 1, 2000, pp. 68–78. DOI: 10.1037/0003-066X.55.1.68.

[47] K. M. Sheldon and A. J. Elliot, “Goal Striving, Need Satisfaction, and Longitudinal Well-Being: The Self-Concordance Model,” *Journal of Personality and Social Psychology*, vol. 76, no. 3, 1999, pp. 482–497. DOI: 10.1037/0022-3514.76.3.482.

[48] R. Koestner et al., “Autonomous Motivation, Controlled Motivation, and Goal Progress,” *Journal of Personality*, vol. 76, no. 5, 2008, pp. 1201–1230. DOI: 10.1111/j.1467-6494.2008.00519.x.

[49] I. R. Kleckner et al., “Evidence for a Large-Scale Brain System Supporting Allostasis and Interoception in Humans,” *Nature Human Behaviour*, vol. 1, 2017, 0069. DOI: 10.1038/s41562-017-0069.

[50] U. Maoz, G. Yaffe, C. Koch, and L. Mudrik, “Neural Precursors of Decisions That Matter—an ERP Study of Deliberate and Arbitrary Choice,” *eLife*, vol. 8, 2019, e39787. DOI: 10.7554/eLife.39787.

[51] T. Kwa et al., “Measuring AI Ability to Complete Long Tasks,” 2025. arXiv:2503.14499.

[52] METR, “Summary of METR’s Predeployment Evaluation of GPT-5.6 Sol,” 26 June 2026. Available: https://metr.org/blog/2026-06-26-gpt-5-6-sol/. Accessed: 31 August 2026.
