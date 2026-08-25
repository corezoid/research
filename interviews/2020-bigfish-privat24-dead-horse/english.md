# Alexander Vityaz: "Privat24 Today Is a Dead Horse"

**Show:** Большая Рыба (Big Fish) with Alexander Kolb · **Recorded/published:** February 5, 2020 · **Length:** 1:14:53
**Original language:** Russian · **Recording:** https://www.youtube.com/watch?v=u5LZWq9m6aQ

> Unofficial English **edited transcript**, prepared by a person from the recording and provided
> for readers of this repository — not a machine transcription. The video at the link above is
> the version of record; copyright in the recording belongs to the show. Some passages are
> condensed in editing; timestamps refer to the recording. The transcript and the notes around
> it are offered under this repository's text license
> ([CC BY 4.0](../../LICENSE-CC-BY-4.0)), which does not extend to the underlying recording.

---

## About Alexander Vityaz

Alexander Vityaz is an applied mathematician, inventor, and technology entrepreneur. He headed PrivatBank's Electronic Business Center and was a principal architect of the bank's digital services, including Privat24. After leaving PrivatBank, he founded Middleware, the company behind Corezoid.

## Interview overview

In this wide-ranging Big Fish interview, Alexander Vityaz traces his path from applied mathematics and Ukraine's earliest card systems to the innovations developed at PrivatBank: SMS banking, one-time passwords by SMS, electronic mobile top-ups, an early eSIM concept, and Privat24. He explains how a growing backlog of technical assignments led to Corezoid and why he sees speed, architecture, and curiosity as the foundations of technological progress.

The conversation also covers company fragmentation, event graphs, technology procurement, accumulated team capability, Share.CreditCard, PrivatBank's nationalization, the digital state, hiring, education, health, books, and the personal habits behind Vityaz's approach to work.

## Full transcript

### Opening

#### [00:00] Teaser

*[Montage of excerpts from the interview.]*

**Alexander Vityaz:** We sat down to do the math - and there was more money than there should have been.

**Alexander Kolb:** You weren't upset?

**Alexander Vityaz:** No.

It changed everything. That is the kind of innovation that changes the infrastructure.

**Alexander Kolb:** You use rather proletarian language.

**Alexander Vityaz:** There are no banks in Ukraine that know how to do this. This was a case of a technology arriving ahead of its time. We were the first.

PrivatBank is a bank of collective farmers. Everything was clear. The question was how to scale it.

Success requires just one thing: curiosity.

*[Theme music.]*

#### [00:48] Introduction

**Alexander Kolb:** My guest today is Alexander Vityaz. What makes Alexander Vityaz so interesting? First, there is not a single video interview with him. Second, he headed PrivatBank's Electronic Business Center, which many people also called PrivatBank's innovation center.

Alexander Vityaz is credited with most - perhaps all - of the innovations that emerged at PrivatBank, including the development of the Privat24 application. After PrivatBank was nationalized, Alexander left and founded his own company, Middleware.

For a long time - perhaps even to this day - PrivatBank has operated on Corezoid. I am not sure what the correct term for it is: a system, an operating system...

I promise this will be very interesting. People see Alexander in very different ways: some call him a despot, some an innovator, some a sage or a genius. You will see all of that in today's interview, so stay with us and be sure to watch to the end. This is Big Fish.

### From applied mathematics to banking

#### [02:15] How Alexander Vityaz entered banking

**Alexander Kolb:** Alexander, tell us how you entered the banking industry.

**Alexander Vityaz:** That is the most boring question anyone could ask. There was nowhere to work. By my fourth year at university, I already had a family.

**Alexander Kolb:** In your fourth year?

**Alexander Vityaz:** Yes.

**Alexander Kolb:** At twenty-one?

**Alexander Vityaz:** Yes. I had also served in the army - students were still being drafted at the time. I was in one of the last cohorts to be called up.

**Alexander Kolb:** That was harsh.

**Alexander Vityaz:** It was all right. I served in reasonably normal forces, working with the S-300 air-defense system. It was a new system then, already using solid-fuel missiles. I consider myself lucky. People I knew served on liquid-fuel air-defense systems, and those were far more dangerous: the fuel had to be loaded, and it was toxic.

**Alexander Kolb:** Can you name anything good about the army?

**Alexander Vityaz:** There was nothing especially bad about it. Discipline. I think that is useful for young people.

**Alexander Kolb:** So they were not wasted years?

**Alexander Vityaz:** The Israeli army shows us that those years do not have to be wasted. In a properly functioning army, you gain discipline and friends. There is an American saying that you make friends at school, in the army, and in prison. That is about it.

**Alexander Kolb:** And where did you go after the army?

**Alexander Vityaz:** There were not many options. I studied applied mathematics. At the time, computers were mainly found in banks - there were practically none in the mines or factories. So the choice was limited.

The card business was also beginning to emerge, and it gave me somewhere to apply what I knew and wanted to do.

**Alexander Kolb:** But at that point a card was basically just a piece of plastic, wasn't it?

**Alexander Vityaz:** There were virtually no bank cards in Ukraine at the time. We built one of the first card systems - the first chip card. It was a payroll project for the Nord factory, covering about two thousand employees.

**Alexander Kolb:** So you were working at INKO Bank then?

**Alexander Vityaz:** Yes. When INKO closed, there were not many alternatives. PrivatBank had just opened in Donetsk. I went in - there were about twenty people there - and asked, "Do you want cards?" They said, "Of course we do." I replied, "I know how to do it."

#### [04:59] How Alexander Dubilet noticed him

**Alexander Kolb:** How did Alexander Dubilet come to notice you? Something must have led up to it.

**Alexander Vityaz:** We ranked first in card issuance. At the time, almost nobody believed in the card business. Banks traded foreign currency, gave loans to friends, felt happy, and waited for exchange rates to rise. Nobody really understood how to make money from cards.

**Alexander Kolb:** How did you meet Dubilet?

**Alexander Vityaz:** He came to Donetsk for a meeting with the mayor. He also stopped by our branch to look at the "star performer."

**Alexander Kolb:** Did he offer you a job immediately?

**Alexander Vityaz:** No, not immediately. Some time later - perhaps a year, I do not remember exactly - he called and said I needed to move to Dnipro for work.

**Alexander Kolb:** What were your conditions?

**Alexander Vityaz:** Do not get in my way.

#### [05:45] How they accelerated card issuance

**Alexander Kolb:** What was the main constraint at the time?

**Alexander Vityaz:** The cycle from a customer's arrival to receiving the card took three or four weeks. There was also a fee of one hundred dollars for urgent card issuance. Customers paid it when they needed to travel somewhere at short notice.

I arranged for us to spend that one hundred dollars on a taxi. The car drove to Dnipro and back, and we agreed with the processing center that they would produce our cards a little faster. It was a simple, nontechnical solution - a logistics technology.

**Alexander Kolb:** That is called entrepreneurship.

**Alexander Vityaz:** And the local oligarchs started coming to me. They understood that they could get a card quickly. Then they began recommending us to their friends.

#### [06:49] Pagers, SMS banking, and the first mobile transactions

**Alexander Vityaz:** Then a prototype mobile bank appeared.

**Alexander Kolb:** How did you connect a pager to a bank card?

**Alexander Vityaz:** We issued them as a package: a pager plus a card.

**Alexander Kolb:** Why a pager?

**Alexander Vityaz:** Mobile phones were still extremely rare. They appeared about a year later. As soon as SMS arrived, it became clear where we should go next. A pager could only receive messages, whereas a phone allowed people not only to see transactions but also to perform operations.

**Alexander Kolb:** How could you perform an operation on a phone of that era? It is obvious with a smartphone today.

**Alexander Vityaz:** You sent an SMS command. For example, "POP MOB 10" meant top up a mobile phone by ten hryvnias. It was like DOS, like working from a command line, only through SMS. But it worked.

**Alexander Kolb:** You say, "Everything was clear." It was clear to you. Why was it not clear to everyone else?

**Alexander Vityaz:** People are different.

**Alexander Kolb:** So it was the genius of your mind?

**Alexander Vityaz:** I do not know. There are periods when the window for innovation is wide open, and periods when there are fewer opportunities for fundamental innovation. At that time, there was a genuine window for fundamental innovation in banking.

My capabilities, Dubilet's ambitions, and the market's needs happened to coincide. Everything came together.

### Building banking infrastructure before the market was ready

#### [08:02] Why banks fall behind

**Alexander Vityaz:** But even today, broadly speaking, there is no bank in Ukraine that truly knows how to issue credit cards properly and build a proper internet bank.

**Alexander Kolb:** You believe nobody has learned how to do that even now?

**Alexander Vityaz:** Yes. Nobody has that competence. Nobody chose to develop it over all these years.

**Alexander Kolb:** But many banks have digital banking now: Ukrsibbank, Alfa-Bank...

**Alexander Vityaz:** Look at them and you are looking at roughly 2007\. At the banks I meet with, the queue of technical assignments stretches three years ahead. Yet 2019 is already coming to an end. They have no curiosity. They sit and wait for something to happen by itself.

Something will happen - but perhaps without them.

**Alexander Kolb:** Will PrivatBank take their place?

***Alexander Vityaz:** PrivatBank will not. It is a dead horse. Someone else will.*

#### [09:08] "Lipstick on a pig": how companies perform innovation

**Alexander Kolb:** Every business today, especially one connected with IT, tries to present itself as technological and innovative. Yet we understand that most of these companies are not actually technological or innovative. Why is that?

**Alexander Vityaz:** Most of them probably understand that themselves. They are human, after all.

I think it is an attempt to preserve youth. Large companies were almost always technological at the beginning - otherwise they would never have become successful. But looking young is easier than remaining young. So they have to pretend and use the word "innovation" in every other sentence, even though their technologies are no longer innovative.

There is an English saying: "put lipstick on a pig." You try to look prettier without changing your nature.

Many companies say, "We are innovative," meaning that they have introduced some new solution. A bank recently announced that it had completed its digital transformation. I happened to meet some people from the bank and asked, "What exactly did you do?" It turned out that Outlook used to run on an internal server, and now they had moved it to the Microsoft cloud.

**Alexander Kolb:** And that is called digital transformation?

**Alexander Vityaz:** Apparently so. That is exactly what "lipstick on a pig" means.

But it is not a death sentence. You can always change something if you have the desire.

#### [10:34] Patents, IBM, and "collective farmers"

**Alexander Kolb:** You invented many technologies and received many patents.

**Alexander Vityaz:** Not that many. About twenty.

**Alexander Kolb:** Twenty is quite a lot.

**Alexander Vityaz:** For collective farmers, it is good. For IBM, it is nothing. They file thousands of patents a year.

**Alexander Kolb:** So you consider yourself a collective farmer?

**Alexander Vityaz:** Yes. Why be embarrassed about it? We are all collective farmers.

**Alexander Kolb:** PrivatBank is a sort of collective-farm bank worth several billion dollars?

**Alexander Vityaz:** Everything is relative. A collective farm is already a collective enterprise: deliberate automation, technology. It is not an insult. IBM has simply gone further.

**Alexander Kolb:** Is your ambition to move further away from the "collective farm"?

**Alexander Vityaz:** Yes.

**Alexander Kolb:** You did not manage to build IBM inside PrivatBank?

**Alexander Vityaz:** Why not? Some things worked, some did not. But everything important stayed with us: our minds, our energy, our curiosity.

#### [11:38] The one-time password by SMS

**Alexander Kolb:** Returning to technology, what do you remember most vividly? Name a few systems or ideas you created.

**Alexander Vityaz:** It depends on my mood, the air temperature, the lighting... We can recall several things. The electronic SIM card, for example. Or the one-time password by SMS - one of those ideas people now use constantly.

We were among the first to do it. The whole world uses it today, and I am proud of it every day.

Without the SMS bank that came before it, the idea probably would not have emerged. Everything is connected; these are links in a single chain.

**Alexander Kolb:** How did the idea for the one-time password arise?

**Alexander Vityaz:** I had a Secure ID device - a one-time-password generator, a little gadget that looked like a calculator. One day I flew to Kyiv on a business trip and left it on the desk in my office. I urgently needed to log in.

I spent the whole day thinking: where is it, what can I do? Then I came back, put down my briefcase, took my phone out of my pocket, and placed it on the desk beside the Secure ID. At that moment everything clicked. The puzzle came together.

The password had to be sent to the phone.

I immediately gathered everyone, we started sketching, and we built it.

**Alexander Kolb:** Did Privat24 already exist at that point?

**Alexander Vityaz:** Yes. It used a static username and password.

**Alexander Kolb:** How difficult was the idea to implement?

**Alexander Vityaz:** We already had SMS banking, so it took a couple of weeks. That was all.

After that, we could acquire customers directly through the internet instead of catching them and luring them into a branch. That was an innovation that truly changed everything.

*Technology does not earn money by itself. It changes the infrastructure. Whether you can make money from it is a different question.*

**Alexander Kolb:** Had nobody used a similar solution before you?

**Alexander Vityaz:** We could not find anyone. As far as we knew, we were the first.

#### [16:01] How the electronic SIM card idea emerged

**Alexander Kolb:** How did the electronic SIM card come about?

**Alexander Vityaz:** We worked extensively with mobile operators. The first genuinely lucrative project involved electronic top-up vouchers. It took off very quickly. We solved the logistics problem.

Scaling physical top-up cards across the entire branch network was expensive and slow. So I came up with the idea of topping up a phone simply by entering its number.

The operators were not ready for that at the time. Working with engineers from Hypercom, a manufacturer of POS terminals, we developed a solution and became the first in the world to do it. Thousands of transactions went through on the very first day.

**Alexander Kolb:** So it was an instant success?

**Alexander Vityaz:** Yes.

The commission was about 15 percent for operators that knew how to count - Kyivstar, for example. UMC, however, paid us a 30 percent commission for two or three years.

At some point we sat down to calculate the numbers and saw that we had more money than we should have had.

**Alexander Kolb:** Were you upset?

**Alexander Vityaz:** No. But something else did upset me: we ourselves did not understand why it was happening. We had not assumed that UMC was staffed by idiots. On one of the most popular vouchers, the margin came to about 30.5 percent.

**Alexander Kolb:** You solved the top-up problem. What came next?

**Alexander Vityaz:** Starter packs. Mobile penetration in Ukraine was still low, and we understood that we could sell several million SIM cards.

But the physical logistics were terrible: a huge number of tariff plans, a vast product range, deliveries to hundreds of branches, and staff training. The operators also visited branches to check whether the point of sale, stickers, and branding had been set up correctly. They insisted that everything comply with their requirements.

At some point we thought: if we have already rewritten the POS-terminal software to sell electronic vouchers, why not rewrite it so that a SIM card can be programmed on the spot?

**Alexander Kolb:** So all you needed were blank chips and phone numbers?

**Alexander Vityaz:** Yes.

**Alexander Kolb:** What was missing from the infrastructure to make it happen?

**Alexander Vityaz:** Curiosity. The operators had a magnificent opportunity to use banks as a route into virtually anywhere. They blew it.

**Alexander Kolb:** But you eventually managed to do it?

**Alexander Vityaz:** We did, because the shareholders acquired a small operator called WellCOM. I no longer had to persuade anyone. I came in and said, "Let's do it." And we did.

As a learning experience and a way to develop us as technologists, it was a good story. As a business story, it was bad: we never managed to persuade the market.

*In practical terms, we invented eSIM about fifteen years too early.*

**Alexander Kolb:** Before Apple?

**Alexander Vityaz:** Apple is not really the point. There were no smartphones then, no ecosystem in which such a technology could take off at scale.

**Alexander Kolb:** Why did you not take the technology out into the world - to Jobs, for example?

**Alexander Vityaz:** Who were we supposed to approach? Smartphones did not exist. We went to Nokia and tried to talk to Motorola, but there was nobody with whom we could build enough momentum.

**Alexander Kolb:** So this was a case of a technology arriving ahead of its time?

**Alexander Vityaz:** Yes, far ahead - by fifteen years, perhaps more. I think some of my patents are about to expire already.

### Corezoid and the architecture of speed

#### [20:03] How Corezoid emerged

**Alexander Kolb:** The story of Corezoid's creation is about speed, isn't it?

**Alexander Vityaz:** It is about problems.

**Alexander Kolb:** About solving problems at high speed?

**Alexander Vityaz:** Yes.

**Alexander Kolb:** Tell us more. What problem were you solving?

**Alexander Vityaz:** At the bank, the backlog of technical assignments stretched about three years ahead.

And that was not unique to PrivatBank. In the past few weeks alone, I have held more than ten meetings with banks from CIS countries and met with European companies as well. In their thinking and their understanding of what is happening, many of them are about fifteen years behind.

**Alexander Kolb:** What paradigm do they live in?

**Alexander Vityaz:** The compliance paradigm. They think a bank's main job is to check a passport thoroughly.

But a bank has to make money. To make money, it has to move, develop, search, and investigate.

A Microsoft executive recently put the answer to the question of what success requires very well: just one factor - curiosity.

But curiosity cannot be bought. It comes from within.

Our curiosity drove us to search for solutions. We could not find a ready-made one, and that energy then flowed into the creation of Corezoid.

The decision itself was easy, almost instantaneous. But the research took a long time. It was not as though we suddenly looked up one day and said, "Oh, the backlog is already three years long." We had known that for a long time. We simply reached a moment when we said it aloud to one another: it is already three years long.

#### [21:53] What Corezoid is

**Alexander Kolb:** Tell us about Corezoid. Does it have any equivalents?

**Alexander Vityaz:** There are individual equivalents and combinations of two or three systems, of course. But as far as I know, there is no complete equivalent.

**Alexander Kolb:** What makes it unique?

**Alexander Vityaz:** We followed our own path. Other systems were also sound and useful in their time. We simply arrived at our own architecture.

**Alexander Kolb:** Can you explain it in very simple terms?

**Alexander Vityaz:** No, I cannot.

**Alexander Kolb:** So you sell magic?

**Alexander Vityaz:** No. We sell cloud computing, which itself looks like magic to many people.

We want to become the operating system for any company that has IT and digital processes.

#### [22:45] Business model and license pricing

**Alexander Kolb:** What is your business model? How do you make money?

**Alexander Vityaz:** Licenses.

**Alexander Kolb:** How much does a license cost?

**Alexander Vityaz:** There are different licenses. Limited licenses are inexpensive. A full license costs what it ought to cost. In practice, we charge as much as the client can pay.

**Alexander Kolb:** And how much "ought" a system license to cost?

**Alexander Vityaz:** Let me give you an example. We have a large French client, a payment service with a very significant share of its market. I cannot name it.

Naturally, every major vendor approaches them. They received proposals ranging from roughly 16 million to 60 million euros to solve their problems.

The difficulty is that they are integrated with hundreds of thousands of companies. All those connections have to be created and maintained. Implementing a traditional solution can take several years.

Account managers and five-person teams arrive, try to launch something, and it does not work.

Our people went to them for a three-day workshop and built two prototypes in those three days.

**Alexander Kolb:** So the price is an order of magnitude lower than what major vendors quote?

**Alexander Vityaz:** Yes. More importantly, it works now, not in two or three years.

**Alexander Kolb:** But a pilot is still only a pilot - a small piece.

**Alexander Vityaz:** Some competitors cannot even make the pilot work.

**Alexander Kolb:** How much did you charge for the three-day pilot?

**Alexander Vityaz:** Almost nothing. In substance, nothing at all. They covered travel and expenses.

#### [25:04] Why Corezoid is difficult to explain

**Alexander Vityaz:** We recently came up with an illustration. It resembles the old Indian parable about the blind men and the elephant: each person touches one part of the elephant and imagines the whole in a different way.

That is roughly how clients see Corezoid. Each has a different context and background, and each tries to see in Corezoid something already familiar and relevant.

Someone says, "Corezoid is BPM - business process management."

**Alexander Kolb:** And it is not?

**Alexander Vityaz:** That is two or three percent of what it can do. In our illustration, BPM is shown as one tiny part of the elephant. We poke a little fun at that class of software.

Everyone sees according to their own experience - a calendar, or something else. So we often do not try to explain Corezoid through existing categories. We start with the client's problems instead.

#### [26:32] The problem clients most often bring to Middleware

**Alexander Kolb:** What problem do people most often bring to Middleware?

***Alexander Vityaz:** There is one main problem: speed. Speed of what does not matter - integration, development, product launch. Say "speed" and then insert whatever word describes your pain.*

**Alexander Kolb:** How do you deliver that speed?

**Alexander Vityaz:** Through technology and architecture. By avoiding the friction and the manual effort of making dozens of disconnected components work together.

When you take a brick from here, cement from there, and something else from somewhere else, assembling everything becomes extremely expensive and slow. More importantly, by the time you finish, the train has already left. Products have changed, requirements have changed, and the market has changed.

The three- or four-year cycle is dead. Nobody accepts it anymore. Yet the market is still trying, through inertia, to live that way.

That is precisely why Revolut, TransferWise, and monobank appear.

#### [27:44] Competitors and scaling expertise

**Alexander Kolb:** How well does the system remain alive after you stop supporting a business?

**Alexander Vityaz:** It remains alive. We train clients. We recently launched remote certification at last. We are trying to automate communication that is uninteresting and does not require a human being.

**Alexander Kolb:** Who is your nearest competitor? I still do not understand.

**Alexander Vityaz:** Why do you need a competitor? We do not have one single competitor. You can move as far as you want to move. In individual segments, of course, there are competitors - we do not live in outer space. But nobody else solves the entire ecosystem in the same way.

We have our own vision, backed by more than twenty years of experience.

**Alexander Kolb:** Is the company currently hostage to Alexander Vityaz? Can it exist without you?

**Alexander Vityaz:** Today, probably not. But I hope it will be able to within five years. That is one of my strategic goals.

I love talking with clients and solving problems. It is a drug for me. But clearly, that model is difficult to scale.

Ideally, our goal is to reach a point where the product sells through the website. We are still far from that today, but we already have the first examples of it happening.

The difficulty is that this is a complex B2B product. We still see very few real examples anywhere of a genuinely complex B2B product in this class being sold completely without human involvement.

Microsoft, Oracle, and the major cloud and enterprise ecosystems all have enormous sales organizations - thousands or tens of thousands of people.

**Alexander Kolb:** So your challenge is either to learn how to scale the expertise or to bring the product to a point where people understand everything by themselves?

**Alexander Vityaz:** Yes. And that is the answer to your recurring question: what is Corezoid for?

### Company fragmentation and event graphs

#### [30:03] Company fragmentation and defragmentation

**Alexander Vityaz:** An ecosystem is a way to organize and control distributed systems. Here, at the bottom of the diagram, the colored area shows where most companies are located.

**Alexander Kolb:** So there are no names of specific systems or technologies here?

**Alexander Vityaz:** No. There are no technology names here at all. We are talking about the essence of the problem. It can be solved with us or without us - the important point is that there is always more than one possible method.

The problem at the bottom is fragmentation - fragmentation of anything: management, technology, data, processes. Technology inside a company is usually handled not by every executive but by one particular person or department. One person is responsible for accounting, another for a different area, a third for IT. That is what creates fragmentation.

Today, every executive should be involved in technology. But the task of defragmenting a company cannot be solved on the same plane where the problem arose. A common mistake is trying to solve it in 2D without stepping outside the existing system.

Suppose the advertising department does not talk to the IT department. The simple solution sounds like this: "Let's make them communicate." But that is not enough. You need to build additional management and technology layers that create a shared context. The problem is then solved in 3D.

**Alexander Kolb:** What examples of such solutions have you implemented?

**Alexander Vityaz:** For some clients, we create an integration layer. For others, billing in the broad sense, rather than merely a ledger. For others, a shared communications environment that brings chats, email, and other channels together.

But the highest level is thinking in events.

#### [31:53] Everything can be described as an event

**Alexander Vityaz:** At some point we realized that everything could be described as events, and we began building technology for that. We now have a product in beta called control.events. It can build event graphs from any data.

Everything we can digitize is joined together and represented as a graph. The graph lives, changes, and "breathes." The atom of that graph is an event.

**Alexander Kolb:** So your ultimate goal is to represent the whole world as a graph?

***Alexander Vityaz:** It already is a graph. We are trying to find an alphabet and a pen that will let us describe and calculate that world. Practically any entity can be represented through a graph. It is the most universal form.*

**Alexander Kolb:** Is control.events the final name?

**Alexander Vityaz:** A new name is already taking shape, but for now the product is called control.events.

#### [32:55] How control.events works

**Alexander Vityaz:** The idea is to represent all company activity as events. Someone writes an email, someone sends a chat message, someone creates a document - all of these are events.

On that basis, you can build an interaction graph. You can then manage the events through processes in Corezoid: create them, enrich them, add participants, and trigger reactions.

Each event has a set of fields: when it was created, who participated, and what attributes it has. An event can trigger a response, and the response itself becomes another event. Any action taken in response to an event is a new event.

**Alexander Kolb:** Can you monitor events associated with a particular person? Alexander, for example?

**Alexander Vityaz:** Of course. In this model, a person becomes a node around which a tree of events accumulates.

For example, we have already collected more than 170,000 events associated with Alexander over the selected period. We can see whom he communicates with. Each event is tagged, and some tags are generated automatically. That lets us classify events and see how many events of a particular type occurred and how their frequency changed over time.

The interaction graph is temporal. If events carrying a particular tag become more active, we can see it. New events can also be generated automatically according to the company's role matrix. In other words, we can see both the events themselves and the emerging trends.

#### [35:06] The event as the system's "building block"

**Alexander Vityaz:** The first thing we did was define an event primitive. It is our basic building block. A chat, a call, a meeting - anything you can name can be described as an event.

**Alexander Kolb:** So the event is an atom?

**Alexander Vityaz:** Yes. Events are assembled into a graph. Event graphs are assembled into a forest of graphs. Processes can be attached to an individual event, a branch, or an entire tree to track changes. The processes can be anything you design them to be.

That allows you to see even microchanges - or, conversely, the absence of expected changes.

When sources such as email and chats are connected, the graph begins to pulse. Emails and other digital traces can be retrieved through APIs. Office visits can be recorded with cameras if necessary. If you need to analyze calls, they can be obtained from the phone.

**Alexander Kolb:** What is the practical application of this system?

**Alexander Vityaz:** Managing a company. When you import the history and represent it as a graph, you structure what has already happened. You can see who communicated with whom, who did not communicate, where activity appeared, and where it did not.

#### [36:47] How to represent a person as a graph

**Alexander Kolb:** How difficult was it to arrive at the idea that the whole world could be represented as events? Not every entity is an event in itself. A person, for example, is not an event.

**Alexander Vityaz:** A person can be represented as a node described by many events.

Take you. What computer do you use?

**Alexander Kolb:** A MacBook.

**Alexander Vityaz:** What programs do you use? A calendar? Design applications? A text editor? How many documents do you create, and how many presentations?

Suppose you made six presentations over a certain period. That is already data. We can continue decomposing your activity into smaller elements. And we can go on almost indefinitely.

Microsoft sees one part of your activity. Apple sees another. Each provider sees its own fragment. Bring those fragments together and you get a more complete model of the person.

**Alexander Kolb:** So it is essentially the number of connections?

**Alexander Vityaz:** Not only that. Connections are fundamental, but the events themselves and their weights also matter. It is not enough to know that you use a particular program. You need to know what you do in it - that you created six presentations, for example.

If you create presentations actively but hardly ever use a text editor, that is also a characteristic. On the basis of such data, a provider can understand how you work and offer you a different product or scenario.

When data becomes a process, Corezoid can pick it up and use it according to a defined logic. We help extract and connect all this data and turn it into a manageable system.

You have a date of birth - that is an event. You have a date when you joined the company - that is another event. In a digital model, a person is therefore described not by one record but by a whole series of events.

#### [39:52] The company interaction graph

**Alexander Kolb:** Suppose I want to use this in my company. What do I have to do?

**Alexander Vityaz:** Register with control.events and connect your data sources.

Here is the graph as we see it in motion. It shows who interacts with whom and what events occur between them. The thicker the line, the more interactions there are.

**Alexander Kolb:** Is that me?

**Alexander Vityaz:** Yes. And this is Alexander Pavlovich. Every interaction with him affects the thickness of the line: the more intense the relationship, the more visible it becomes.

**Alexander Kolb:** And this line seems to disappear into empty space.

**Alexander Vityaz:** It leads to a domain. We tagged the emails by domain; a domain often serves as a proxy for a company. For example, the address after the @ sign lets us assign the communication to a particular organization.

You can view interactions among everyone in the company over the entire period or only for the current day.

**Alexander Kolb:** But the information is still incomplete. If I simply speak with someone, the system may not see it.

**Alexander Vityaz:** Some information comes to us directly and some indirectly. You can keep adding sources, and eventually the picture becomes sufficiently accurate. Even the data we already have shows who barely communicates with whom, which departments are disconnected from one another, and where interaction has suddenly disappeared.

#### [41:48] How the graph instantly revealed spammers

**Alexander Vityaz:** When we built a graph like this for the first time, we saw the spammers immediately.

**Alexander Kolb:** How?

**Alexander Vityaz:** Nobody replies to them. The graph makes that instantly visible.

We did not create the system specifically to combat spam. It was a side effect that demonstrated the universality of the technology.

Any event can be turned into a process. A meeting record, an email, or any other activity can be placed in this format. The activity can then be analyzed and processed by the process logic, and it can generate new events - including events for other people.

You get an endless chain: an event triggers processing, the processing creates new events, and those events trigger further processes. At the same time, the interaction graph is built. We can see communication shift from one group of people to another. When we tag events, we can also see the topics around which that communication is taking place.

**Alexander Kolb:** So an event can contain other events?

**Alexander Vityaz:** Yes. It is a deeply nested, recursive technology.

### Architecture, competition, and team capability

#### [43:23] Why tenders fragment companies

**Alexander Kolb:** What else is shown in your diagrams? There are so many of them. This is my third visit, and they change every time. I do not understand when you find time to redraw them.

**Alexander Vityaz:** Some colleagues try to build things with us, and I have to draw diagrams to explain why certain paths are dangerous.

Technology tenders are one example. The purpose of a tender is to minimize cost. But you cannot select technology solely on the basis of the lowest price.

Of course, a solution should not be unjustifiably expensive. But first and foremost it has to solve your problem; only then should it be inexpensive. It is a question of value, not simply price.

Tender specifications running to hundreds of pages usually drive you down a very narrow corridor toward a lower price. You end up with nonsense, but you can report, "I bought the cheapest option."

**Alexander Kolb:** But if nobody needs the cheapest option, there are no savings.

**Alexander Vityaz:** Exactly. From an architectural perspective, a tender becomes a way to fragment the company.

Today you need a server, so you buy the cheapest server. Tomorrow you need an expense-accounting system, so you buy the cheapest one. Then you need a CRM, so you hold another separate competition. You never see all the links at the same time.

*You are not building a system; you are buying fragments. Then you sit there wondering how to connect them all and why you did it that way in the first place.*

Each procurement is usually run by clerks who have been assigned one local task. On the one hand, a tender protects against corruption and uncontrolled spending. On the other, it breaks the company into pieces technologically.

You save ten kopecks here and lose far more in the future because integrating all those fragments becomes a separate, expensive project.

We are currently negotiating with several banks whose internal environments are so fragmented that they can no longer move effectively. When we show them this picture, it resonates immediately: people recognize their own situation at once.

**Alexander Kolb:** I completely agree with you here. I deal with tenders too. In my view, they have outlived their usefulness, and businesses need another way to obtain exactly what they need.

**Alexander Vityaz:** When a company with a very strong brand conducts hundreds of technology tenders, that is a dangerous symptom. Hundreds of people, the entire senior management team, and the board of directors all fragment the company together, even though each person is formally doing their job correctly.

You cannot evaluate a strategic technology through an ordinary tender. It requires the personal involvement of a top-level executive. If that executive delegates the choice to someone who does not understand the architecture and is responsible only for following procedure, the outcome will reflect that.

As a rule, the more technology tenders a company runs, the slower it becomes and the weaker its holistic understanding of IT.

#### [46:40] Competition: a good application is an effect, not a cause

**Alexander Kolb:** There are people and companies trying to compete with what your team once built: monobank, other banks... Do you still regard PrivatBank as colleagues?

**Alexander Vityaz:** Almost nobody I knew remains in PrivatBank's current senior management, so it is difficult for me to call them colleagues in the old sense.

**Alexander Kolb:** What would a competitor have to do to overtake them? Many people think it is enough to write a very good application.

***Alexander Vityaz:** The application should be good, of course. But a good application is an effect, not a cause. Good products appear because management is organized properly.*

One measurable quantity that characterizes the quality of management, expertise, and shared experience is the number of hours the team has spent working together.

Our teams have worked together for more than two million hours. You can argue about the exact counting method, but you cannot buy those hours instantly or replace them with a collection of individually strong specialists.

**Alexander Kolb:** But successful companies need fresh blood and renewal.

**Alexander Vityaz:** Of course they do. We have that. But there also has to be a backbone - the accumulated shared experience.

Why do national teams often play worse than clubs even though the national team brings together the best players? Because a club has cohesion. It is the same accumulated time spent together.

To catch up with the level of PrivatBank that our team built, people would need to work well together for at least five years - and that is assuming they are already at roughly the same professional level today that we were when we began.

#### [48:43] Does PrivatBank still run on Corezoid?

**Alexander Kolb:** How is it that PrivatBank still runs on Corezoid?

**Alexander Vityaz:** Let's leave that question aside. We have evidence relating to many processes, but, as they say in American films, it was not gathered in an entirely procedurally proper way. It is probably not the kind of evidence you can take to court or use to obtain a search warrant.

**Alexander Kolb:** How many clients do you have today?

**Alexander Vityaz:** Hundreds of large ones and thousands of small ones.

**Alexander Kolb:** Do you communicate personally with the large clients? How do you manage everything?

**Alexander Vityaz:** So far, I manage. With some, I discuss feedback. With others, I go deeply into the problem. It varies.

We recently hosted a large group of Austrian bankers. They came for three days - technology tourists of a sort. The last time I had gone through the material in detail was several months earlier, and I had already forgotten a great deal, so I had to reconstruct everything at high speed.

#### [49:40] How a friendship with a cryptographer brought in a french client

**Alexander Kolb:** You mentioned a large French client. How did you meet them?

**Alexander Vityaz:** It is a very interesting story. I have a friend, the French mathematician David Naccache, who is considered one of the world's leading cryptographers.

We have a very strong sense of empathy with one another. I am not afraid to say we are friends even though we may have met only eight times. But we are so completely on the same wavelength that after twenty minutes we stop noticing the language barrier. He speaks French and English; I speak Russian and English; somehow we understand one another. He is a mathematics professor, after all, and speaks four or five languages.

In July, a man wrote to me: "David Naccache recommended you. He said you could solve our problem."

The last time I had told David about Corezoid was about six years earlier. But he understood perfectly what kind of system it was. He is one of the few people who grasped the essence immediately: I drew the diagram on a napkin, and he understood. A mathematician.

**Alexander Kolb:** A beautiful story: a friendship that ultimately brought the company a great deal of money.

**Alexander Vityaz:** A few hundred thousand dollars, perhaps. But the amount is not really the point. The important thing is that it works. Now I think I should talk to David more often - we would make more sales.

And the person who contacted us turned out to be his former student.

### Share.CreditCard and life after PrivatBank

#### [51:14] How the idea for Share.CreditCard emerged

**Alexander Kolb:** At Middleware, you went even further and created a project that allows one person to give another access to a bank card. What is the essence of the innovation?

**Alexander Vityaz:** Let's begin with the problem.

My daughter's university issued an incorrect invoice. She needed to pay an additional two hundred dollars or so. For some reason, this small payment could not be made by an ordinary transfer or through the website. She had to go to the university cashier and pay in cash or by card through a POS terminal.

My daughter had forgotten her PIN. She could not resolve anything in the middle of the night and called me in tears. I quickly found someone through whom I could get money to her, but at that moment it struck me: why can't I simply share my card with her?

My colleagues began explaining that it could not be done, that it was difficult, and that the payment infrastructure worked differently. We gathered everyone and started building something, but then we were distracted, and the project gradually stalled.

About a year later, in August, I had a minor operation. I woke up from the anesthetic, and my first thought was, "We need to finish Share.CreditCard."

**Alexander Kolb:** Those are very normal thoughts to have after surgery.

**Alexander Vityaz:** I do not know why the anesthetic affected me that way. I began analyzing why we had not finished it and realized that we needed an external driver - an event that would force us to meet a deadline.

I quickly found a suitable hackathon at the Money20/20 conference, which was due to take place in October. It was mid-August. I deliberately gave myself only a short recovery period and set the task: build a technology that changes the world in two months.

In practice, we had even less time. We had to file the patent by September 24; otherwise, we would publicly disclose the solution at the hackathon.

**Alexander Kolb:** Did you win the hackathon?

**Alexander Vityaz:** Officially, we came second. By our standards, we won. Mastercard gave us a low score because we were competing on Visa's team. That was the rivalry between the payment systems.

#### [53:57] How card sharing works

**Alexander Kolb:** Explain it in simple terms. Suppose I have a problem: I am standing in a hotel in the middle of the night, I have lost my card or forgotten my PIN. You are my father. What happens?

**Alexander Vityaz:** You call and say, "Alexander, I need to pay."

I press a button, specify an amount or limit, and select your number from my phone book. Access to my card appears on your smartphone. You confirm that you have received access and can pay with your phone. At the moment of payment, the money is charged directly to my card.

*In other words, we do not move money from point A to point B. We move access to money under defined conditions.*

**Alexander Kolb:** You originally planned to launch this technology with PrivatBank?

**Alexander Vityaz:** Yes. Everything was supposed to be ready for launch in early January 2017\. But everyone knows what happened in December 2016\.

After the nationalization, we had to spend about another two and a half years finding a bank willing to implement it. And the bank that agreed did not yet have all the necessary infrastructure: mobile wallets had to be configured, licenses obtained, and the work coordinated with the payment systems.

In October 2019, we finally launched Share.CreditCard with A-Bank.

#### [55:10] Why the project was not launched with PrivatBank

**Alexander Kolb:** But the ecosystem remained at PrivatBank. Why did you not continue working with them after you left?

**Alexander Vityaz:** First, it is a matter of principle. Second, that question is better directed to them. And almost the entire team capable of building things like this had left the bank.

**Alexander Kolb:** When you call PrivatBank a "dead horse," what exactly do you mean? The accumulated work and ecosystem are still there.

**Alexander Vityaz:** The people are gone, and the living environment of a private business is gone.

GitHub contains an enormous number of artificial-intelligence programs. Do you use them simply because they are sitting on GitHub? No. 

*The accumulated capability does not exist only in code. It exists in people's minds and in the culture.*

*The culture left.*

#### [55:50] Can Share.CreditCard replace money transfers?

**Alexander Kolb:** What is your forecast for this technology? Could it repeat the electronic SIM-card story, with the idea emerging too early?

**Alexander Vityaz:** I think it will gradually displace traditional forms of money transfer. Western Union, TransferWise, and similar projects move money. Here, what moves is controlled access to money rather than the money itself.

Someone from Western Union once asked me, "What are we supposed to do now?" I replied, "Adapt."

In every country, I want to find a daring - in the best sense - curious person or bank willing to launch it. Once the first implementations are live, everyone else will begin copying them.

**Alexander Kolb:** What does a user in Ukraine have to do today?

**Alexander Vityaz:** Get a card from A-Bank. No other bank in Ukraine currently supports it, but we are working to expand the network.

**Alexander Kolb:** Do you not feel jealous that A-Bank is using the technology and part of PrivatBank's legacy?

**Alexander Vityaz:** Why would I? Privat is both us and them. I am only proud of what was built. A-Bank is our client, and I am proud of them too.

I do not want to work for a single bank again. The people who remained at PrivatBank stayed in banking in the singular. I moved into banks - plural.

**Alexander Kolb:** But in some respects, you were already doing the same thing through PrivatBank.

**Alexander Vityaz:** Yes. But when you are inside PrivatBank, which many banks see as a direct competitor and fear, very few are prepared to work with you.

#### [57:24] Why Vityaz did not leave the bank earlier

**Alexander Kolb:** Why did you wait so long? Why did you not enter the market earlier?

**Alexander Vityaz:** We were not exactly waiting. Middleware was established back in 2014, and we were gradually preparing. But new ideas appeared at the bank every day, and we always wanted to implement one more thing.

At PrivatBank, I would have launched Share.CreditCard about three years earlier. The distance from an idea to implementation was extremely short. That was what kept us there.

We understood that in the open market, we would have to go from company to company, spend an unpredictable amount of time, and explain again and again what we were offering and why anyone needed it.

### Nationalization, the digital state, and management

#### [57:58] Nationalization and the lawsuit against the state

**Alexander Kolb:** How do you personally view the nationalization of PrivatBank?

**Alexander Vityaz:** I have an ongoing lawsuit against the state of Ukraine over the expropriation of my shares. So my interpretation of the situation is unambiguous.

**Alexander Kolb:** What amount is involved?

**Alexander Vityaz:** I do not know; I do not remember. It is completely irrelevant. For me, it is a matter of principle: the Constitution was violated.

**Alexander Kolb:** But in public discussion, the nationalization is presented as a story in which something was stolen from the bank, or at least money was handled improperly.

**Alexander Vityaz:** That is how the media presents it. But separate court proceedings should not be conflated.

My case is clean and separate: shares belonging to me were confiscated. I had no loans connected with the bank or any other relationships that could explain their seizure. All the other disputes have nothing to do with my claim as a private individual.

**Alexander Kolb:** So your position is, "Nothing personal, just give me back the shares"?

**Alexander Vityaz:** Quite the opposite. It is all personal.

*[Musical transition.]*

#### [59:08] The digital state and bureaucracy

**Alexander Kolb:** How strongly do you believe that a digital state can be built on top of a bureaucratic structure?

**Alexander Vityaz:** The state is a bureaucratic structure. And that is not always bad.

Bureaucracy arose as a response to fragmentation. It is one way to defragment a large organization, make management reproducible, and reduce dependence on a particular individual.

The problem is not bureaucracy itself but how it is designed. From that perspective, digitizing the state is a logical and perhaps the only correct path: rules and actions should become transparent, computable, and consistently executable.

### People, culture, education, and curiosity

#### [59:50] How Vityaz conducts job interviews

**Alexander Kolb:** Do you look at a person's diploma when hiring them?

**Alexander Vityaz:** No.

**Alexander Kolb:** I know that you used to ask, "Who is Tom Sawyer?" What did that reveal to you - the context of a person's knowledge?

**Alexander Vityaz:** For me, it was a quick pregnancy test. I immediately understood whether the person had read books as a child.

**Alexander Kolb:** But they may have read other books.

**Alexander Vityaz:** Of course. But in our generation and at that age, the literary context was largely shared. Almost everyone knew Tom Sawyer.

**Alexander Kolb:** What questions do you ask new people today, especially younger candidates?

**Alexander Vityaz:** At some point it became clear that large numbers of people simply had not read the book. The question stopped being relevant.

Now I invent a question for each person. I may ask a developer who von Neumann was. Or Norbert Wiener, one of the fathers of cybernetics. Far from everyone knows those names either.

If the candidate is not a developer, I look at the person and try to understand what question will reveal their context.

**Alexander Kolb:** What context does Tom Sawyer reveal?

**Alexander Vityaz:** Entrepreneurship, friendship, the ability to use opportunities. It is a book about an open world - effectively about everything at once. But selection tools have to change as generations change.

#### [1:01:23] A test of contextual thinking

**Alexander Kolb:** Before the interview, you showed me a picture - a test you use in interviews. What else do you observe?

**Alexander Vityaz:** I watch the person's face as they try to complete this very simple test.

**Alexander Kolb:** What answers do people give?

**Alexander Vityaz:** Some come close, but so far nobody has answered correctly right away.

It is a good way to understand whether a person thinks in contexts. You have to see not twenty separate graphs but combine them and arrive at one result.

**Alexander Kolb:** How would you describe your company's culture?

**Alexander Vityaz:** We are a fast and curious company. Satisfying curiosity is a very broad mission, but it is the central thing for us.

To remain curious, you have to be able to test ideas and move quickly. Nobody specially taught or forced us to do that. We were born that way.

#### [1:02:17] The story of the blood tests and vitamin D3

**Alexander Kolb:** There was a story that you forced every employee to have a blood test.

**Alexander Vityaz:** I did not force them. I advised them to do it.

One day I became ill. We have a friend who is a well-known professor, and on his advice I had a blood test. It showed that my vitamin D3 level was very low.

I became interested in the subject, began observing employees, and noticed signs of a similar deficiency in some of them. I advised them to get tested. It turned out that two people had levels so low that, under Western medical standards, they might already have been hospitalized.

We began discussing the problem with colleagues and eventually bought D3 for employees. We needed energetic people capable of doing a great deal of work at peak intensity, so we treated the team's health as a real management issue.

At PrivatBank, we bought several million hryvnias' worth of vitamin D3 and distributed it to employees in the branches. I think that, at one point, we were among the largest private purchasers of D3 in Ukraine. We may genuinely have helped some people very seriously.

What people now call burnout is often related to biochemistry. Not always, of course, but sometimes the feeling of complete exhaustion is caused by an ordinary vitamin deficiency or another measurable physiological factor.

**Alexander Kolb:** What results did you see?

**Alexander Vityaz:** The highest D3 levels belonged to the idlers - the people who arrived later than everyone else and left earlier.

They simply had not had time to use up their health. The hard workers burned through everything: they worked in the office and then continued at home at night.

**Alexander Kolb:** Is that why all the idlers look good?

**Alexander Vityaz:** Yes. For their age, they look excellent.

**Alexander Kolb:** You look very good too. Is your D3 level high?

**Alexander Vityaz:** Very high. I monitor it.

#### [1:04:19] DNA tests as a gift for employees

**Alexander Kolb:** What else do you do for the team's health or performance?

**Alexander Vityaz:** At the current company, for example, last year we gave every employee a DNA analysis as a gift.

Some found relatives. We even discovered two people in the company who turned out to be related and had not known it.

It was an unusual gift, but useful and social at the same time. People are scattered all over the world, and genetic services sometimes allow them to find family or better understand their own origins. It is interesting.

#### [1:04:54] Childhood, books, and "the boy with the key around his neck"

**Alexander Kolb:** How did you become a professional? What was your childhood like?

**Alexander Vityaz:** I had a wonderful childhood: books, magazines, and all kinds of construction sets.

**Alexander Kolb:** In one conversation, you described yourself as "the boy with the key around his neck," referring to Alfred Böttcher's novella "Conduct: F." Its protagonist is largely left to his own devices and receives too little attention from his parents. Does that genuinely describe you well?

**Alexander Vityaz:** Not only me - almost our entire generation. Our parents were young: they worked, studied, and then studied again in the evenings. Children largely grew up on their own - in a good sense.

We lived in the city center. During parades, the streets were closed, and sometimes the entrance to our building was blocked as well, so we could only go into the courtyard. Ice cream was sold directly below my balcony.

To avoid spending a day off without ice cream, we learned to lower a bag of money from the balcony on a string and then pull the purchase back up. An aunt came to visit once and even filmed it. Another innovation.

#### [1:06:15] The book Elastic and a giveaway for viewers

**Alexander Kolb:** Today we are giving away Leonard Mlodinow's book "Elastic: Flexible Thinking in a Time of Change." Alexander will give a copy of the book, or a voucher for it, to the author of the best question. Leave your questions for Alexander Vityaz in the comments below the video.

#### [1:06:31] Hyperactivity as an advantage

**Alexander Vityaz:** Elastic includes an interesting account of how attitudes toward hyperactivity and attention deficit disorder have changed.

Twenty years ago, a child who could not sit still at school and constantly switched attention was seen primarily as a problem. People would say, "He has a firecracker up his ass." To some extent, that describes me too.

But Mlodinow shows that in a rapidly changing world, this trait can become an advantage. The ability to survive and remain valuable increasingly favors people who can hold several points of focus at once or switch quickly between them.

Among other examples, he discusses African tribes that split apart at some point. The people remained genetically close but began living under different conditions. In the more extreme environment, traits associated with attention deficit and hyperactivity were more common because they helped people notice change and respond to it faster.

A moderate degree of scattered attention can be an important quality today because it allows you to assemble a broader picture.

**Alexander Kolb:** What about focus, then?

**Alexander Vityaz:** You have to know how to zoom. An excessively narrow focus is also dangerous: you see only what is directly in front of you and stop noticing what is happening around you.

The important ability is to change scale, switch roles, and redirect attention - looking forward, then backward; at a specific detail, then at the system as a whole.

#### [1:08:15] Telescopes, "Young Chemist," and technical magazines

**Alexander Kolb:** What did you do as a child? What did you make with your hands?

**Alexander Vityaz:** I built telescopes. There were chemistry construction kits and a set called "Young Chemist." We subscribed to Young Technician and other science and technology magazines, and I read them from cover to cover.

**Alexander Kolb:** Did your parents instill that love of knowledge in you, or was it the environment?

**Alexander Vityaz:** Both my parents and the environment. And some of it was probably innate.

We lived in a building full of educated people. There was only one apartment on each floor, and the doors were often left open. I could visit the neighbors, borrow books, and talk with adults. An environment like that shapes a person very strongly too.

#### [1:09:12] Why his children do not study in Ukraine

**Alexander Kolb:** Is that one reason your children do not study in Ukraine? What advantages does Canada, where they study, offer?

**Alexander Vityaz:** Our country is still being built. The education system is still taking shape too. At the same time, the Soviet Union did not have as many good things as people sometimes like to remember.

**Alexander Kolb:** Do you think today's school is worse than the old one?

**Alexander Vityaz:** A direct comparison would be incorrect. Today, practically everyone has internet access; twenty years ago, it did not exist. The internet offers enormous opportunities. The other side is that, as it turns out, not everyone needs those opportunities or knows how to use them.

#### [1:09:50] A multidimensional assessment of a person

**Alexander Vityaz:** Something revealing happened this morning. My colleagues and I were discussing metrics - whether digital traces could be used to measure emotional intelligence and communication quality with sufficient accuracy, for example. When email and chats are connected, we can see how a person communicates.

One colleague said, "In my fifth year at university, I did not attend lectures at all, but I studied well. What would your attendance metric tell you?"

At that exact moment, my son sent me data from his university. For each subject, there were four separate indicators: how the student completed homework, how regularly they attended, how they worked and communicated in class, and one more engagement measure.

If we assessed our colleague under that system, he would receive the highest mark for completed assignments and zero for classroom work. He would no longer pass through the system simply as an "excellent student."

That is neither good nor bad. It is a more individual and multidimensional assessment. A simple attendance counter is primitive, but the more independent measurements you have, the more objective the picture becomes - provided the data is used correctly.

**Alexander Kolb:** So the broader the graph, the more information it contains?

**Alexander Vityaz:** Of course. The broader and more complex the graph, the more real context it contains.

We discover new meanings in this work every day. For every event, we now store not only a date or an empirical cost but also prior and posterior probabilities.

**Alexander Kolb:** Does that allow you to model the future?

**Alexander Vityaz:** Of course.

#### [1:11:39] Money, inheritance, and the children's education

**Alexander Kolb:** Do you consider yourself a multimillionaire?

**Alexander Vityaz:** How can you consider yourself one or not? There are numbers.

**Alexander Kolb:** Is it important for you to feel it?

**Alexander Vityaz:** It is pleasant.

**Alexander Kolb:** What do you spend money on?

**Alexander Vityaz:** My children and their education.

**Alexander Kolb:** Will you leave them an inheritance?

**Alexander Vityaz:** I do not know. I have already given them the main inheritance - knowledge and education. My daughter has one final semester left, and my son starts university in September.

**Alexander Kolb:** Yachts, cars, travel?

**Alexander Vityaz:** I already travel so much that I no longer know how not to travel.

#### [1:12:17] What Vityaz does in the evenings

**Alexander Kolb:** Alexander, what do you do in the evenings?

**Alexander Vityaz:** I walk the dog, work, play, and read.

When a person loses interest in play too early - whatever kind of play it may be - that is a bad sign. A living graph has to grow, breathe, and pulse. A person needs to play too: play is a way of learning and growing. Cards, intellectual games, any format - it does not matter.

I also talk with my children and employees.

**Alexander Kolb:** What can you discuss with employees in the evening?

**Alexander Vityaz:** Either there is a problem, an idea has emerged, or there is a question we want to test.

**Alexander Kolb:** So you work around the clock? You use rather "proletarian" language about work: the five-day week, working hours... Where does that come from?

***Alexander Vityaz:** The old idea of work as a fixed place and eight hours a day ended long ago. Laws and formal standards almost always describe the past.*

When a person is genuinely interested in what they do, the boundary between "I am working" and "I am not working" becomes conditional. It matters less where you are or what job title is written in a document. What matters is whether you are engaged with the problem.

#### [1:13:32] "A dog of convenience"

**Alexander Kolb:** What is the story behind your dogs?

**Alexander Vityaz:** Laziness and a sedentary lifestyle. It was a deliberate choice: a marriage of convenience - and a dog of convenience.

I sat down and chose a breed by process of elimination. A very large dog is inconvenient in an apartment. A very small one, in my view, is almost cruel and not especially interesting. It had to be reasonably intelligent and active. Most importantly, the dog had to make me walk several kilometers a day.

**Alexander Kolb:** What are the dogs called?

**Alexander Vityaz:** Their registered names are Kai and Niku. At home, one is called Chudik; [the other home nickname is unintelligible].

#### [1:14:23] Closing lightning round

**Alexander Kolb:** Our program, Big Fish, ends with three questions. [The first question cannot be reconstructed from the original automated transcript.]

**Alexander Vityaz:** D3.

**Alexander Kolb:** Why D3?

**Alexander Vityaz:** Fish is a source of vitamin D3. Eat fish.

**Alexander Kolb:** Answer accepted. And what is the main accumulator of your business?

**Alexander Vityaz:** A battery.

*[Music. End of interview.]*
---

## Related work in this repository

- **See also** [The Main Actor](../2020-forbes-main-actor/english.md) — the Forbes Ukraine profile published ten months later covers the same ground from the outside: the PrivatBank conflict, Corezoid's market, and the actor graphs this conversation explains first-hand.
- **See also** [A Phase Model of Enterprise Evolution](../../papers/2026-phase-model-of-enterprise-evolution/) — the interview's account of company fragmentation and the backlog that led to Corezoid is the experiential base of the model.
- **See also** [Company Brain](../../papers/2026-company-brain/) — event graphs and accumulated team capability, later formalized as the architecture of company intelligence.
- **See also** [The Computable Boundary of the Firm](../../papers/2026-computable-boundary-of-the-firm/) — Share.CreditCard and the digital state as boundary questions: which transactions belong to whom.
- **See also** [the press archive](../../press/) — the SMS banking, one-time passwords, and mobile top-ups recalled here are documented as dated primary records in the 2001–2009 releases.
