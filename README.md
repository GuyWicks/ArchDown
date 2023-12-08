# ArchDown
Proof of concept for an architecture domain specific language to support modelling and documentation

The idea is that you can write plain language specifications, that can create a model that can be visualised.

Example DSL: _suggested, work in progress_
```
Accounts_Payable is a Business_Service
    it is managed by Finance_Department
    it is supported by IT_Department
    is uses the Finance_System
    it supports the Account_Recievable 

Finance_Service is a Application_Service
    it is realized by 

Finance_System is a Application_Component

Finance_Department is a Business_Role
    managed by Dave Johnson

```

Visualisation: _not correct yet!_

![img](example_ArchiShape_application)
## ToDo
- [ ] Make it work!
- [x] Develop proto-language model with textX
- [x] Develop proto-model visualisation with pixie-python
- [ ] Join the two above
- [ ] Develop a 'heirarchy' of concepts
- [ ] Build lines
- [ ] Build line routing algo
- [ ] Review pixie vs native SVG

## Idea's
- Use 'weight' (vertical) and 'attraction' (horiz) to layout concepts
- Business are lighter, technology is heavier
- Interfaces are lighter than components
- Composed components add weight
- Simplify the Archi model
- Services are light
- Collaboration increases attraction 

