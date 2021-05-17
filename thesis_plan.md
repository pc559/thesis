To Do
-----
- Implement more realistic DBI scenario (e.g. 0710.1812, 1103.4126, 1801.02187).
- Efficient basis choices for features (different for linear vs log osc?).
- Explore factor basis.
- $c_s^{DBI}$ constraint:
    1. Reproduce *Planck* result using decomposed template.
        1. Via CMB-BEst (coeffs sent to Wuhyun, though he is busy writing).
        2. Via James' basis (need to learn how to use James' code).
    2. Sharpen constraint with more realistic Primodal scale/shape-dependence.
        1. Via CMB-BEst (coeffs sent to Wuhyun, though he is busy writing).
        2. Via James' basis (need to learn how to use James' code).
- Find other inflation parameters to target and constrain.
- EFT time dependence?

Thesis Writing Options
--------------
1. I begin thesis writing now, but do a bit more research when Wuhyun is available again.
2. I explore efficient feature basis for $k_{ratio}=1000$ **(question - what $k_{ratio}$ is James' code implemented for?)**, do some scans, then start writing.

Thesis Outline
--------
1. **Intro 1**
    - General $\Lambda CDM$ intro.
    - Motivate inflation.
    - Statistical observables (e.g. P.S.) - intuition coming from determining the weighting of a coin - how does what Wuhyun does differ from this? It's not Bayesian, right? I guess it's just "get the histogram from the Gaussian sims, see where we are in that".
    - Link primordial NG to the CMB, make explicit the link between NG and non-linearity, possibly with some simple example. 
    - Coming from part iii level, a derivation of the in-in formalism.
    - A calculation of the interaction Hamiltonian, through the simpler (and more observationally relevant) form of the self-interactions, i.e. neglecting the metric perturbations. 
    - Then DBI, then $P(X, \phi)$, then features. 
    - Lit-review of the Maldacena calculation giving explicit mention to the field-redefinition being unnecessary. 
    - Explicit details of how resonance and features generate large NG. 


2. **Intro 2** 
    - Review separability, KSW.
    - Modal methods, results of Planck.
    - Wuhyun's stuff? Got to include some link...
    - F&RP's work.
    - Previous config-by-config codes.


3. **Cube Decomp** 
    - Pulling out the $k$-dependance to motivate cube decomp. 
    - Inner product choice.
    - Decomposing shapes on the cube vs tetra.
    - Template testing.
    - Basis choice matters! Why is the basic expansion so bad?
    - Why does $k_{ratio}$ matter?
    - "Probing..." results and stuff since then - extending to $k_{ratio}=1000$.
    - Log basis for scale-indep basis.
    - Loginv basis for resonant shapes.
    - Factor basis?


4. **Methods and Validation**
    - Numerics of mode evolution (what do I do differently? $\tau_s$?).
        - When to set IC's for each mode.
        - Swapping variables.
        - How long to evolve them.
    - Integration choices.
        - The $i\varepsilon$ prescription.
        - Starting the integration with a pinch, validating this in the way suggested by the reviewer.
        - Stopping the integration. A note on boundary terms and cancellations.
    - The interaction Hamiltonian.
    - Set-up of DBI example scan, matching the PS etc.
    - Going to high $p_{max}$.
    - Validation (as in Probing).
    - Speed comparison.
    - Map distinguishability of templates at primordial level.


5. **Constraints** 
    - With either CMB-BEst, or James' modes, or both. If this actually gets done! 
    - Compare convergence at primordial level to convergence at $f_{NL}$ level (this is just Wuhyun's work though...). 
    - Validate this convergence by reproducing Planck constraint using DBI template decomp.
    - Then check how the scaling affects this. 
    - Enrico's suggestion?


6. **Future Work/Conclusions** 
    - Further constraints.
    - Multi-field motivation.
    - Factor basis to assess limits.
    - Public release of code.


7. **Appendices** 
    - Numeric choices that aren't specific to mode evolution, etc.
    - Gauss-Legendre integration, fixed weights.
    - Tools used: Numpy, Scipy, Jupyter Notebooks...?














