import{H as w,j as x}from"./javascript-97e07392.js";import"./github-dark-dimmed-a528ba5f.js";import{I as a,_ as r}from"./index-dd2f8ebc.js";import{r as e,o as A,s as b,k as n,a as h,c as p,e as t,u as d}from"./index-08c72e63.js";const D={id:"app"},C={__name:"PluginMarkdown_mermaid",props:{message:Object},setup(o){const s=o;w.registerLanguage("javascript",x);const c=e(""),m=e(s.message[1]),u=async l=>{try{const k=await(await fetch(`../${l}`)).text();c.value=k}catch(i){console.error(i)}};A(()=>{u(m.value)}),b(()=>{}),e(`
requirementDiagram

    requirement test_req {
    id: 1
    text: the test text.
    risk: high
    verifymethod: test
    }

    functionalRequirement test_req2 {
    id: 1.1
    text: the second test text.
    risk: low
    verifymethod: inspection
    }

    performanceRequirement test_req3 {
    id: 1.2
    text: the third test text.
    risk: medium
    verifymethod: demonstration
    }

    interfaceRequirement test_req4 {
    id: 1.2.1
    text: the fourth test text.
    risk: medium
    verifymethod: analysis
    }

    physicalRequirement test_req5 {
    id: 1.2.2
    text: the fifth test text.
    risk: medium
    verifymethod: analysis
    }

    designConstraint test_req6 {
    id: 1.2.3
    text: the sixth test text.
    risk: medium
    verifymethod: analysis
    }

    element test_entity {
    type: simulation
    }

    element test_entity2 {
    type: word doc
    docRef: reqs/test_entity
    }

    element test_entity3 {
    type: "test suite"
    docRef: github.com/all_the_tests
    }


    test_entity - satisfies -> test_req2
    test_req - traces -> test_req2
    test_req - contains -> test_req3
    test_req3 - contains -> test_req4
    test_req4 - derives -> test_req5
    test_req5 - refines -> test_req6
    test_entity3 - verifies -> test_req5
    test_req <- copies - test_entity2

`),e(`
gantt
    dateFormat  YYYY-MM-DD
    title       Adding GANTT diagram functionality to mermaid
    excludes    weekends
    %% (\`excludes\` accepts specific dates in YYYY-MM-DD format, days of the week ("sunday") or "weekends", but not the word "weekdays".)

    section A section
    Completed task            :done,    des1, 2014-01-06,2014-01-08
    Active task               :active,  des2, 2014-01-09, 3d
    Future task               :         des3, after des2, 5d
    Future task2              :         des4, after des3, 5d

    section Critical tasks
    Completed task in the critical line :crit, done, 2014-01-06,24h
    Implement parser and jison          :crit, done, after des1, 2d
    Create tests for parser             :crit, active, 3d
    Future task in critical line        :crit, 5d
    Create tests for renderer           :2d
    Add to mermaid                      :1d
    Functionality added                 :milestone, 2014-01-25, 0d

    section Documentation
    Describe gantt syntax               :active, a1, after des1, 3d
    Add gantt diagram to demo page      :after a1  , 20h
    Add another diagram to demo page    :doc1, after a1  , 48h

    section Last section
    Describe gantt syntax               :after doc1, 3d
    Add gantt diagram to demo page      :20h
    Add another diagram to demo page    :48h

`),e(`
gantt
    dateFormat  YYYY-MM-DD
    title       Adding GANTT diagram functionality to mermaid
    excludes    weekends
    %% (\`excludes\` accepts specific dates in YYYY-MM-DD format, days of the week ("sunday") or "weekends", but not the word "weekdays".)

    section A section
    Completed task            :done,    des1, 2014-01-06,2014-01-08
    Active task               :active,  des2, 2014-01-09, 3d
    Future task               :         des3, after des2, 5d
    Future task2              :         des4, after des3, 5d

    section Critical tasks
    Completed task in the critical line :crit, done, 2014-01-06,24h
    Implement parser and jison          :crit, done, after des1, 2d
    Create tests for parser             :crit, active, 3d
    Future task in critical line        :crit, 5d
    Create tests for renderer           :2d
    Add to mermaid                      :1d
    Functionality added                 :milestone, 2014-01-25, 0d

    section Documentation
    Describe gantt syntax               :active, a1, after des1, 3d
    Add gantt diagram to demo page      :after a1  , 20h
    Add another diagram to demo page    :doc1, after a1  , 48h

    section Last section
    Describe gantt syntax               :after doc1, 3d
    Add gantt diagram to demo page      :20h
    Add another diagram to demo page    :48h
`),e(`

requirementDiagram

    requirement test_req {
    id: 1
    text: the test text.
    risk: high
    verifymethod: test
    }

    functionalRequirement test_req2 {
    id: 1.1
    text: the second test text.
    risk: low
    verifymethod: inspection
    }

    performanceRequirement test_req3 {
    id: 1.2
    text: the third test text.
    risk: medium
    verifymethod: demonstration
    }

    interfaceRequirement test_req4 {
    id: 1.2.1
    text: the fourth test text.
    risk: medium
    verifymethod: analysis
    }

    physicalRequirement test_req5 {
    id: 1.2.2
    text: the fifth test text.
    risk: medium
    verifymethod: analysis
    }

    designConstraint test_req6 {
    id: 1.2.3
    text: the sixth test text.
    risk: medium
    verifymethod: analysis
    }

    element test_entity {
    type: simulation
    }

    element test_entity2 {
    type: word doc
    docRef: reqs/test_entity
    }

    element test_entity3 {
    type: "test suite"
    docRef: github.com/all_the_tests
    }


    test_entity - satisfies -> test_req2
    test_req - traces -> test_req2
    test_req - contains -> test_req3
    test_req3 - contains -> test_req4
    test_req4 - derives -> test_req5
    test_req5 - refines -> test_req6
    test_entity3 - verifies -> test_req5
    test_req <- copies - test_entity2

`),e(`
pie title What Voldemort doesn't have?
         "FRIENDS" : 2
         "FAMILY" : 3
         "NOSE" : 45
`),e(`
pie title NETFLIX
         "Time spent looking for movie" : 90
         "Time spent watching it" : 10
`);const f=e(`
graph TD;
subgraph AA [Consumers]
A[Mobile app];
B[Web app];
C[Node.js client];
end
subgraph BB [Services]
E[REST API];
F[GraphQL API];
G[SOAP API];
end
Z[GraphQL API];
A --> Z;
B --> Z;
C --> Z;
Z --> E;
Z --> F;
Z --> G;
`),_=e(`
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#ff0000'}}}%%
        graph TD
          A[Christmas] -->|Get money| B(Go shopping)
          B --> C{Let me think}
          B --> G[/Another/]
          C ==>|One| D[Laptop]
          C -->|Two| E[iPhone]
          C -->|Three| F[fa:fa-car Car]
          subgraph section
            C
            D
            E
            F
            G
          end
`);e(`

graph LR;
    K([...........<img src='/vitepress-plugin-mermaid/K.png' width='60' >...........])-.->G((...........<img id='git' src='/vitepress-plugin-mermaid/Octocat.png' width='50' >...........));
    H([...........<img id='helm' src='/vitepress-plugin-mermaid/helm.png' width='60' >...........])-.->G
    G-->A;
    A(...........<img src='/vitepress-plugin-mermaid/argo-cd.png' width='60' >...........)-->D(...........<img src='/vitepress-plugin-mermaid/ocp.png' width='60' >...........);

`),e(`

graph TD;
 A[Start] --> B[Process 3];
 B --> C[Process 4];
 C --> D[End];
`),e(`

graph TD;
 A[Start] --> B[Process 3];
 B --> C[Process 4];
 C --> D[End];
`),e(`

gitGraph:
options
{
    "nodeSpacing": 150,
    "nodeRadius": 10
}
end

commit
branch develop
branch newbranch
checkout newbranch
commit
commit
checkout master
commit
branch very_nice_feature
checkout very_nice_feature

commit
branch develop
commit
branch develop
commit
merge develop
commit
merge newbranch
`);const g=e(`
flowchart LR
    subgraph Guide
        direction TB

        f[flow]
        s[[Step]]
        d[(Database)]
        Parameters>Parameters]
    end

    %% add in-line style
    Guide:::someclass
    classDef someclass fill:#f96;


    %%list of parameters
    p1>bank_name]
    p2>seller_info]


    %%list of steps
    s1[[1-withdraw_money]]
    s2[[2-purchase_bike]]


    %%list of flows
    f1[go_to_bank]
    f2[withdraw_from_atm]
    f3[contact_seller]
    f4[trade_bike]


    %%list of databases
    d1[(reads: customer_identification)]
    d2[(reads/writes: customer_balance)]
    d3[(writes: e_document_sign)]


    %% Create the step flows
    s1-.->s2;


    %% s1 flow
    p1-->|inputs|s1
    s1-->|calls|f1
    f1-->|calls|f2
    f2-->d1
    f2-->d2


    %% s2 flow
    p2-->|inputs|s2
    s2-->f3
    f3-->f4
    f4-->d3

`);e(`
mindmap
TRIEROOT => 6
  b => 4
    a => 4
      l => 1
        m => 1
      r => 3
        k => 1
        s => 1
  c => 2
    e => 2
      l => 1
        l => 1
      r => 1
        t => 
`);const y=n(()=>r`
${g.value}
`),v=n(()=>r`
${_.value}
`),q=n(()=>r`
${f.value}
`);return(l,i)=>(h(),p("div",D,[t(d(a),{value:y.value},null,8,["value"]),t(d(a),{value:v.value},null,8,["value"]),t(d(a),{value:q.value},null,8,["value"])]))}},R={class:"container-xxl m-1"},B={__name:"DevDescriptionView",setup(o){const s=e(["md/Usage/사용법모음 copy.md","md/Usage/server_chatgpt_a.md","md/Usage/git usage.md"]);return(c,m)=>(h(),p("div",R,[t(C,{message:s.value},null,8,["message"])]))}};export{B as default};
