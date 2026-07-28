---
title: "Management Debt—Part I: Concept, Metrics, and Principles for Attributing Materialised Debts to Actor Accounts"
author:
  - name: Alexander Vityaz
    orcid: 0009-0006-0489-7881
    affiliation: Corezoid Inc., Dnipro, Ukraine
date: 2026-06-30
doi: 10.5281/zenodo.21069692
version: v1
license: CC-BY-4.0
keywords: [management debt, omission debt, materialised management debt, loss attribution, Vibe Management, risk attribution, enterprise management, business process, managerial accounting]
---

> **Note.** This markdown version is provided for convenient reading on GitHub. Mathematical notation and figures are authoritative in [paper.pdf](paper.pdf) and in the version of record: [doi:10.5281/zenodo.21069692](https://doi.org/10.5281/zenodo.21069692).

# Management Debt—Part I: Concept, Metrics, and Principles for Attributing Materialised Debts to Actor Accounts

Alexander Vityaz · *Corezoid Inc., Dnipro, Ukraine* · ORCID: [0009-0006-0489-7881](https://orcid.org/0009-0006-0489-7881)

## Abstract

This article develops a formal framework for conceptualising and accounting for management debt as a distinct accounting object. Management debt is defined as the consequence of a management decision that has not been made, has been deferred, has been inadequately formalised, or has not been executed, where such absence increases organisational ambiguity, delays, dependence on manual intervention, redundant coordination, the probability of errors, and the probability of loss. Particular attention is given to *omission debt*, understood as management debt arising from the failure of an obligated party to make a required decision. The article specifies the relevant terminology, accounting metrics, recognition principles, and attribution rules for recording materialised omission debt and direct losses on the accounts of responsible actors. The proposed measurement approach deliberately excludes survey-based indicators and relies instead on observable organisational evidence, including events, decisions, unmade decisions, timelines, approval routes, digital traces, and materialised consequences. The framework contributes to the formalisation of managerial accountability by linking unmade decisions, responsible decision owners, materialised risks, and measurable economic consequences.

## 1 General Provisions

1.1. This document establishes the conceptual apparatus and core provisions for accounting for management debt.

1.2. Management debt is recognised as an independent accounting object.

1.3. Management debt may exist both before and after the materialisation of consequences.

1.4. Where management debt results in a materialised loss, such loss shall be attributed to the accounts of the appropriate actors in their designated roles.

1.5. Surveys are deliberately excluded from the measurement perimeter. Measurement is grounded in observable events, states, timelines, decisions, unmade decisions, repeated discussions, rework, escalations, and losses.

## 2 Subject Matter

2.1. The subject matter of this document comprises: management debt and its special case—omission debt; accounting metrics; and the principles for attributing materialised debts and direct losses to the accounts of actors in the role of Decision Owner.

## 3 Terms and Definitions

#### Definition 3.1. Management Debt.

Management debt is an accounting object arising from a management decision that has not been made, has been deferred, has been inadequately formalised, or has not been executed—the absence of which increases organisational ambiguity, delays, dependence on manual intervention, redundant coordination, the probability of errors, and the probability of loss.

#### Definition 3.2. Materialised Management Debt.

Materialised management debt is management debt for which an observable negative consequence has occurred, expressed as a loss, delay, rework, loss of controllability, breach of control, or other measurable damage.

#### Definition 3.3. Omission Debt.

Omission debt is management debt arising from the failure of an obligated party to make a decision.

#### Definition 3.4. Decision Owner.

A Decision Owner is the party obligated to make the corresponding management decision.

#### Definition 3.5. Direct Loss.

A direct loss is a loss that stands in direct causal connection with the corresponding unmade decision.

#### Definition 3.6. Actor Account.

An actor account is an accounting object on which debts, losses, and other amounts attributable to a given party in a designated role are recorded. (The actor account operates on the principle of double entry: posting a debt to one party's account implies a corresponding entry. The account structure and posting mechanics are detailed in Part II.)

#### Definition 3.7. Actor.

An actor is a party for accounting purposes. In this document the term "actor" is not used without specifying the party's role.

#### Definition 3.8. Unmade Decisions Account.

The unmade decisions account is the portion of an actor account on which omission debts and direct losses arising from unmade decisions are recorded.

#### Definition 3.9. Debt Materialisation.

Debt materialisation is the transition of management debt from a state of potential negative impact to a state of observable damage.

## 4 Classes of Management Debt

4.1. The following classes of management debt are distinguished for accounting purposes:

- 4.1.1. role clarity debt;
- 4.1.2. process debt;
- 4.1.3. decision-making debt;
- 4.1.4. delegation debt;
- 4.1.5. priority debt;
- 4.1.6. communication debt;
- 4.1.7. personnel debt;
- 4.1.8. management observability debt.

4.2. The class central to this document is decision-making debt.

4.3. The most strictly formalisable special case of decision-making debt is omission debt.

4.4. Definitions of classes 4.1.1–4.1.2 and 4.1.4–4.1.8 are the subject of a separate document.

## 5 Recognition of Omission Debt

5.1. Omission debt arises when all of the following conditions are simultaneously present:

- 5.1.1. a management question requiring a decision exists, and a party obligated to make that decision exists;
- 5.1.2. the decision has not been made;
- 5.1.3. as a result of the unmade decision, a risk, ambiguity, absence of control, or absence of constraint persists that is capable of materialising into damage.

#### Rule 5.2. Recognition of Omission Debt.

Where management debt is expressed as the failure to make a decision, such debt is recognised as omission debt.

5.3. In an omission case, the absence of subsequent execution tasks does not negate the existence of the debt.

5.4. Where the negative consequence is attributable to the very fact that a decision was not made, the accounting object is omission debt, not execution debt.

## 6 Measurement Principles

6.1. Measurement is grounded in the observable consequences of the management construct.

6.2. Surveys are deliberately excluded from the measurement perimeter.

6.3. Measurement relies on decisions, absence of decisions, timelines, approval routes, repeated discussions, rework, escalations, delays, and losses.

6.4. No single metric is considered sufficient.

6.5. The basis for accounting is a traceable link between the debt, the party, the risk, and the consequence.

The requirement that accounting be grounded in a traceable link between the debt, the party, the risk, and the consequence can be implemented in the transaction-trace language of [Active Transaction Graphs](../2026-active-transaction-graphs/) [9], where interactive executions are observed through result, trace, and ledger semantics.

## 7 Accounting Metrics

### 7.1 General Provisions

Accounting metrics are used for:

- 7.1.1.1. identifying management debt;
- 7.1.1.2. assessing its age;
- 7.1.1.3. assessing its severity;
- 7.1.1.4. assessing the degree of materialisation;
- 7.1.1.5. establishing direct loss;
- 7.1.1.6. attributing omission debt and the associated loss to the accounts of the corresponding actors.

### 7.2 Metric Definitions

#### Definition 7.2.1. Debt Age.

Debt Age is the period from the date a management debt arose or was identified to the date of its closure or to the reporting date.

#### Definition 7.2.2. Decision Latency.

Decision Latency is the time interval between the emergence of a question requiring a decision and the fact of the decision being made.

#### Definition 7.2.3. Open Decision Delay.

Open Decision Delay is the open overdue period for a decision where no decision has been made. Applicable to any type of management debt.

#### Definition 7.2.4. Rework Ratio.

Rework Ratio is the ratio of rework volume to completed work volume.

#### Definition 7.2.5. Clarification Density.

Clarification Density is the density of clarifying messages per unit of work communication.

#### Definition 7.2.6. Escalation Density.

Escalation Density is the density of escalations per unit of work cases.

#### Definition 7.2.7. Repeat Discussion Index.

Repeat Discussion Index is the frequency with which previously discussed topics are reopened.

#### Definition 7.2.8. Ownership Ambiguity Rate.

Ownership Ambiguity Rate is the proportion of work objects for which no unambiguous owner exists.

#### Definition 7.2.9. Priority Volatility.

Priority Volatility is the frequency of priority changes relative to the number of active work objects.

#### Definition 7.2.10. Omission Duration.

Omission Duration is the period during which a decision remained unmade. The formula coincides with Open Decision Delay (Formula 8.3); the metric is distinguished for explicit linkage to omission debt.

#### Definition 7.2.11. Direct Loss.

Direct Loss is the monetary expression of the direct loss arising from an unmade decision.

## 8 Formulae

**Formula 8.1. Debt Age**

$$DebtAge = ReportDate - DebtStartDate$$

**Formula 8.2. Decision Latency**

$$DecisionLatency = DecisionDate - DecisionNeedDate$$

**Formula 8.3. Open Decision Delay / Omission Duration**

$$OpenDecisionDelay = OmissionDuration = ReportDate - DecisionNeedDate$$

**Formula 8.4. Rework Ratio**

$$ReworkRatio = \frac{ReworkVolume}{CompletedWorkVolume}$$

**Formula 8.5. Clarification Density**

$$ClarificationDensity = \frac{ClarificationMessages}{WorkMessages}$$

**Formula 8.6. Escalation Density**

$$EscalationDensity = \frac{EscalationCount}{CaseCount}$$

**Formula 8.7. Repeat Discussion Index**

$$RepeatDiscussionIndex = \frac{ReopenedTopics}{ResolvedTopics}$$

**Formula 8.8. Ownership Ambiguity Rate**

$$OwnershipAmbiguityRate = \frac{ObjectsWithoutClearOwner}{AllObjects}$$

**Formula 8.9. Priority Volatility**

$$PriorityVolatility = \frac{PriorityChangeCount}{ActiveObjectCount}$$

## 9 Tables

#### Table 9.1. Summary of Accounting Metrics

| # | Metric | Meaning | Formula | Unit |
|---|---|---|---|---|
| 1 | Debt Age | age of the debt | 8.1 | days |
| 2 | Decision Latency | time to decision | 8.2 | days |
| 3 | Open Decision Delay | open overdue period | 8.3 | days |
| 4 | Rework Ratio | proportion of rework | 8.4 | ratio |
| 5 | Clarification Density | density of clarifications | 8.5 | ratio |
| 6 | Escalation Density | density of escalations | 8.6 | ratio |
| 7 | Repeat Discussion Index | reopening of topics | 8.7 | ratio |
| 8 | Ownership Ambiguity Rate | ambiguity of ownership | 8.8 | ratio |
| 9 | Priority Volatility | volatility of priority | 8.9 | ratio |
| 10 | Omission Duration | duration of omission debt | 8.3 | days |
| 11 | Direct Loss | direct loss from unmade decision | per case | monetary |

## 10 Posting of Omission Debt

#### Rule 10.1. Posting of Omission Debt.

Omission debt shall be posted to the accounts of actors in the role of Decision Owner.

10.2. For omission debt expressed as the failure to make a decision, the base posting role is Decision Owner.

10.3. Omission debt is recorded on the unmade decisions account of the corresponding actor.

## 11 Attribution of Direct Loss

#### Rule 11.1. Attribution of Direct Loss.

Where an unmade decision directly led to a materialised loss, such loss is attributed to the unmade decisions account of the corresponding Decision Owner.

#### Rule 11.2. Multiple Participation.

Where multiple parties contributed to the creation of a given debt, the loss is distributed across their accounts in proportion to their contribution to the creation of the debt. The procedure for determining shares and a case involving distributed attribution are detailed in Part II.

## 12 Accounting for Materialised Debts

12.1. The sequence for accounting for a materialised omission debt comprises:

- 12.1.1. recording the debt;
- 12.1.2. qualifying the debt as omission debt;
- 12.1.3. establishing the Decision Owner;
- 12.1.4. recording the fact of materialisation;
- 12.1.5. establishing the direct loss;
- 12.1.6. posting the omission debt to the unmade decisions account;
- 12.1.7. attributing the direct loss to the same account.

12.2. Minimum set of accounting fields:

- 12.2.1. `debt_id`;
- 12.2.2. `debt_type`;
- 12.2.3. `decision_need_date`;
- 12.2.4. `report_date`;
- 12.2.5. `decision_owner_id`;
- 12.2.6. `direct_loss`;
- 12.2.7. `attribution_note`.

## 13 Core Principle of the Omission Case

#### Rule 13.1. Core Principle of the Omission Case.

Where a materialised management debt is expressed as the failure to make a decision, and it is established that the absence of such decision caused the direct loss, the omission debt and the corresponding loss are recorded on the unmade decisions account of the Decision Owner.

## 14 Case: Materialised Omission Debt (Single Decision Owner)

*This case is fully documented. A detailed description of the circumstances may be included in a subsequent revision.*

14.1. The case under consideration is one in which:

- 14.1.1. a management question requiring a decision existed;
- 14.1.2. the decision was not made;
- 14.1.3. no execution actions followed;
- 14.1.4. the absence of the decision preserved an open risk;
- 14.1.5. the open risk materialised as fraud;
- 14.1.6. a loss occurred.

14.2. The management context in which this debt arose is characterised by a pattern in which the leader's emotional state, impulsive reactions to situational external or intra-corporate triggers became the primary factor in decision-making, displacing systematic planning and data analysis.

*[Figure 1. Vibe Management — see the figure in [paper.pdf](paper.pdf), Section 14.]*

14.3. On the basis established in clause 5.4, the accounting object is recognised as omission debt, not execution debt.

14.4. Under Rule 10.1 and Rule 11.1, the omission debt and the associated direct loss are attributed to the account of the given Decision Owner.

## 15 Example

#### Example 15.1. Direct Attribution of Loss.

If a party in the role of Decision Owner failed to make a decision, and it is established that precisely this unmade decision directly led to a loss of $7,000,000, then the amount of $7,000,000 shall be posted to the unmade decisions account of that Decision Owner.

15.2. In this example:

- 15.2.1. the omission debt is recorded on the unmade decisions account;
- 15.2.2. the direct loss is attributed to the same account;
- 15.2.3. no further decomposition of the loss is required within this document.

## 16 Prohibition on Unspecified Party Designation

#### Rule 16.1. Prohibition on Unspecified Use of the Term "Actor".

The use of the term "actor" without specifying the party's accounting role is not permitted in this document.

#### Rule 16.2. Role in the Omission Case.

For omission debt expressed as the failure to make a decision, that role is Decision Owner.

16.3. Formulations such as "the loss is attributed to actor accounts" without specifying the role are considered inadmissible.

## 17 Standalone Formulations for Direct Insertion

*This section contains standalone formulations of key rules intended for direct insertion into related documents.*

#### Definition 17.1.

A Decision Owner is the party obligated to make the corresponding management decision.

#### Rule 17.2.

Where management debt is expressed as the failure to make a decision, such debt is recognised as omission debt.

#### Rule 17.3.

Omission debt shall be posted to the accounts of the Decision Owner.

#### Rule 17.4.

Where an unmade decision directly led to a materialised loss, such loss is attributed to the unmade decisions account of the corresponding Decision Owner.

#### Rule 17.5.

Where multiple parties contributed to the creation of a given debt, the loss is distributed across their accounts in proportion to their contribution to the creation of the debt.

## 18 Conclusion

18.1. This model establishes a direct link between the unmade decision, the decision holders in the role of Decision Owner, the materialised risk, and the economic consequence.

18.2. Practical procedures for measurement, causal attribution, determination of shares in distributed attribution, a case involving multiple Decision Owners, and the implementation of accounting on the platform are the subject of Part II.

## References

[1] Hubbard, D. W. *How to Measure Anything: Finding the Value of Intangibles in Business.* 3rd ed. John Wiley & Sons, 2014.

[2] Argyris, C., and Schön, D. A. *Organizational Learning: A Theory of Action Perspective.* Addison-Wesley, 1978.

[3] Argyris, C., and Schön, D. A. *Organizational Learning II: Theory, Method, and Practice.* Addison-Wesley, 1996.

[4] Reason, J. *Human Error.* Cambridge University Press, 1990.

[5] Reason, J. *Managing the Risks of Organizational Accidents.* Ashgate, 1997.

[6] Reason, J. *Organizational Accidents Revisited.* Routledge, 2016.

[7] Merchant, K. A., and Van der Stede, W. A. *Management Control Systems.* 5th ed. Pearson, 2023.

[8] Hiebl, M. R. W. "The Integration of Risk into Management Control Systems: Towards a More Comprehensive Framework." *Journal of Management Control*, 2024.

[9] Vityaz, A. *Active Transaction Graphs: A Formal Framework for Transactional Interactive Systems*. March 2026. https://doi.org/10.5281/zenodo.20747873 — in this repository: [../2026-active-transaction-graphs/](../2026-active-transaction-graphs/)
