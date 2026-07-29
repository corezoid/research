# System and methods for a resource-saving exchange protocol based on trigger-ready envelopes among distributed nodes

[![US Patent](https://img.shields.io/badge/US%20Patent-11,093,935-blue.svg)](https://patents.google.com/patent/US11093935B2/en)

**Inventor:** Oleksandr Vityaz — the same author as [Alexander Vityaz](https://orcid.org/0009-0006-0489-7881) of the papers in this repository
**Assignee:** Oleksandr Vityaz (unassigned)
**Application:** US 16/134,929 · **Filed:** September 18, 2018 · **Published:** US 2019/0019182 A1, January 17, 2019 · **Granted:** US 11,093,935 B2, August 17, 2021
**Legal status** (Google Patents, July 2026): Active - Reinstated

## Abstract

Disclosed is a resource-saving exchange protocol based on a safe transfer of envelopes among distributed nodes. The method comprises the steps of: authoring an envelope at an origin node, said envelope comprising at least a letter and a trigger card, wherein said letter is any one of an execution algorithm and said trigger card is any one of an event or algorithm that starts the execution of a logic; launching said envelope into the distributed network of nodes, whereby the envelope is transferred from at least one run-node to at least a second run-node according to an embedded exchange logic for safe transfer; checking the trigger from at least one envelope at least once by each run-node and transferred further if the trigger is not met and disabling trigger checking functionality of any one of nodes not actively checking for triggers to save resource, and analyzing the envelopes content upon trigger being fired to learn which run-node is eligible to execute the main logic of the envelope (execute-node).

## Publication history

| Event | Number | Date |
|---|---|---|
| Filed | US 16/134,929 | September 18, 2018 |
| Application published | [US2019/0019182A1](https://patents.google.com/patent/US20190019182A1/en) | January 17, 2019 |
| Patent granted | [US11093935B2](https://patents.google.com/patent/US11093935B2/en) | August 17, 2021 |

Continuation-in-part of application No. 15/268,802, filed on September 19, 2016, now abandoned, and a continuation-in-part of application No. 15/077,626, filed on March 22, 2016, now abandoned. Claims priority to provisional applications No. 62/221,124 (September 21, 2015) and No. 62/137,079 (March 23, 2015).

## Files

| File | Description |
|------|-------------|
| [patent.pdf](patent.pdf) | Official grant publication (USPTO, public record) |

## How to cite

> Vityaz, O. (2021). *System and methods for a resource-saving exchange protocol based on trigger-ready envelopes among distributed nodes*. US Patent 11,093,935. U.S. Patent and Trademark Office.

```bibtex
@patent{vityazUS11093935,
  author   = {Vityaz, Oleksandr},
  title    = {System and methods for a resource-saving exchange protocol based on trigger-ready envelopes among distributed nodes},
  number   = {US 11,093,935 B2},
  year     = {2021},
  assignee = {Oleksandr Vityaz (unassigned)},
  url      = {https://patents.google.com/patent/US11093935B2/en}
}
```

## Related work in this repository

- **See also** [Active Transaction Graphs](../../papers/2026-active-transaction-graphs/) — the resource-saving variant of the envelope protocol, where idle nodes disable trigger checking, addresses the same execution-cost concern the paper treats at graph scale.

## Links

- Google Patents: https://patents.google.com/patent/US11093935B2/en
- USPTO Patent Center (application 16/134,929): https://patentcenter.uspto.gov/applications/16134929
