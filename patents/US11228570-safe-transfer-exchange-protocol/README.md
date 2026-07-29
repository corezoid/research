# Safe-transfer exchange protocol based on trigger-ready envelopes among distributed nodes

[![US Patent](https://img.shields.io/badge/US%20Patent-11,228,570-blue.svg)](https://patents.google.com/patent/US11228570B2/en)

**Inventor:** Oleksandr Vityaz — the same author as [Alexander Vityaz](https://orcid.org/0009-0006-0489-7881) of the papers in this repository
**Assignee:** Oleksandr Vityaz (unassigned)
**Application:** US 16/290,823 · **Filed:** March 1, 2019 · **Published:** US 2019/0199693 A1, June 27, 2019 · **Granted:** US 11,228,570 B2, January 18, 2022
**Legal status** (Google Patents, July 2026): Expired - Fee Related

## Abstract

A distributed exchange protocol method based on a safe transfer of envelopes among a distributed nodal network using a local ranking moderator comprising the steps of: authoring an envelope at one node, said envelope comprising at least a letter and a trigger, wherein said letter is any one of an execution algorithm and said trigger is any one of an event or algorithm that starts the execution of a logic; collecting information about at least one of an envelope or node (e/n) interacting with or interacted with another e/n by a ranking moderator and based on said collected information generate a ranking or listing of at least one of honest, dishonest, or unknown nodes and sharing this listing or ranking by at least one node to decide which nodes are eligible for envelopes to be transferred to or from; launching said envelope into the distributed network of nodes, whereby the envelope is transferred from at least the one node to at least another node that is moderator-approved and checking the trigger from at least one envelope at least once by at least the moderator-approved node and transferred further to another moderator-approved node if the trigger is not met and disabling trigger checking functionality of any one of nodes not actively checking for triggers to save resources; and analyzing the envelopes content upon trigger being fired to learn which node is eligible to execute the main logic of the envelope.

## Publication history

| Event | Number | Date |
|---|---|---|
| Filed | US 16/290,823 | March 1, 2019 |
| Application published | [US2019/0199693A1](https://patents.google.com/patent/US20190199693A1/en) | June 27, 2019 |
| Patent granted | [US11228570B2](https://patents.google.com/patent/US11228570B2/en) | January 18, 2022 |

Continuation-in-part of application No. 16/134,929, filed on September 18, 2018, now Patent No. 11,093,935.

## Files

| File | Description |
|------|-------------|
| [patent.pdf](patent.pdf) | Official grant publication (USPTO, public record) |

## How to cite

> Vityaz, O. (2022). *Safe-transfer exchange protocol based on trigger-ready envelopes among distributed nodes*. US Patent 11,228,570. U.S. Patent and Trademark Office.

```bibtex
@patent{vityazUS11228570,
  author   = {Vityaz, Oleksandr},
  title    = {Safe-transfer exchange protocol based on trigger-ready envelopes among distributed nodes},
  number   = {US 11,228,570 B2},
  year     = {2022},
  assignee = {Oleksandr Vityaz (unassigned)},
  url      = {https://patents.google.com/patent/US11228570B2/en}
}
```

## Related work in this repository

- **See also** [Active Transaction Graphs](../../papers/2026-active-transaction-graphs/) — the trigger-ready envelope, a unit of work carrying its own execution logic and firing condition, is the patented mechanism behind the transaction-graph model.

## Links

- Google Patents: https://patents.google.com/patent/US11228570B2/en
- USPTO Patent Center (application 16/290,823): https://patentcenter.uspto.gov/applications/16290823
