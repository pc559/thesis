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
0. **Abstract**
    - Goal is parameter scan.
    - Motivation: faster at primordial level, and suited to obeservable comparisons.
    - Core concepts are the basis expansion, and the cube vs tetra.
    - Result 1: Finding a basis with broad descriptive power.
    - Result 2: Validation of the methods.
    - Result 3: Actual constraints??

    
1. **Introduction to inflation**
    - General $\Lambda CDM$ intro.
    - Motivate inflation
        - Define SR params, $c_s$.
    - Perturbations
        - ICs.
        - MS equation at various times.
        - MS equation in $N$, $\tau_s$ - no numerics yet?
        - Define the power spectrum, discuss constraints.
    - Statistical observables (e.g. P.S.) - intuition coming from determining the weighting of a coin.
    - (How does what Wuhyun does differ from this? It's not Bayesian, right? I guess it's just "get the histogram from the Gaussian sims, see where we are in that".)
    - Define the primordial bispectrum.
        - Isotropy etc.
        - f_{NL} (various definitions).
    - Link inflaton non-linearity to primordial NG to the CMB, possibly with some simple example. 
    - Coming from part iii level, a derivation of the in-in formalism.
    - A calculation of the interaction Hamiltonian, through the simpler (and more observationally relevant) form of the self-interactions, i.e. neglecting the metric perturbations. 
    - Then DBI, then $P(X, \phi)$.
    - Lit-review of the Maldacena calculation giving explicit mention to the field-redefinition being unnecessary.
    - Examples of shapes, using $K_{pq}$ notation (link to Enrico's sym polys?)
        - Maldacena, DBI
        - $P(X, \phi)$, EFT
        - Features, with explicit details of how resonance and features generate large NG. 
    - F&RP's work...?
    - Previous config-by-config codes
        - What have these been used for recently?
    - Squeezed limit consistency.


2. **Introduction to bispectrum data analysis** 
    - Review estimators, KSW, separability.
    - Calculating the reduced bispectrum.
    - Separable approximations to non-separable templates
        - Equilateral to DBI.
        - Approximations to approximations.
    - Modal methods, constraints from Planck.
    - Wuhyun's stuff? Got to include some link...


3. **Expanding primordial shapes**
    - Pulling out the $k$-dependance
        - Motivate decomposition on the cube.
        - Defining the notation for the two main time integrals.
    - Inner product choice.
        - Notes on observable convergence being the deciding factor.
    - Template testing.
    - Decomposing shapes on the cube vs tetra.
        - FIGURE: DBI on cube vs tetra.
    - Setting up a basis: augmentation.
        - Using modified GS.
        - Legendre and Fourier as building blocks.
    - Basis choice matters! 
        - Why the basic expansion is so bad.
        - Nice table with descriptions and some single-number comparison on examples.
        - FIGURES: Recon for Malda, DBI, scale-inv, with P0, P1, F0, F1 vs $P_{max}$
        - FIGURES: Recon for cos, cosDBI, with P0, P1, F0, F1 vs $P_{max}$.
        - FIGURES: Recon for cos-log, cos-logDBI, with P0, P1, F0, F1 vs $P_{max}$.
        - FIGURES: Recon for scaled-DBI, with P0, P1, P1ns, P01ns, P_log vs $P_{max}$.
    - Not obvious, but $k_{ratio}$ matters!
    - "Probing..." results and stuff since then - extending to $k_{ratio}=1000$.
    - Log basis for scale-indep basis.
    - Loginv basis for resonant shapes.
    - Factor basis?
    - Intermediate result: the log basis is good!


4. **Methods and Validation**
    - Numerics of mode evolution (what do I do differently? $\tau_s$?).
        - When to set IC's for each mode.
        - Swapping variables.
        - How long to evolve them.
    - Integration choices.
        - The $i\varepsilon$ prescription.
        - Suppression from plane wave intuition.
        - Starting the integration with a pinch.
        - Validate this in the way suggested by the reviewer
            - Show how easy it is to swamp the result with a sharp cut.
        - FIGURE: Relative error for simple $\pi^3$ and for Reso, in ($\beta$, T).
            - Large $\beta$ is just a sharp start!  
        - Stopping the integration. A note on boundary terms and cancellations.
    - The interaction Hamiltonian, using RP by parts.
    - Set-up of DBI example scan, matching the PS etc.
    - Going to high $P_{max}$.
    - Validation (on numerical results)
        - FIGURE: the various tetrapyd limits.
        - Maldacena quadratic SR
            - FIGURE: residual for...
        - DBI
            - FIGURE: residual for...
        - Tanh step
            - FIGURE: residual for...
            - FIGURE: PyTransport scan across step size.
        - Resonance
            - FIGURE: residual for...
            - FIGURE: PyTransport time comparison.
        - DBI resonance
            - FIGURE: residual for...
    - Speed comparison vs PyTransport. Something BINGO can't do?
    - Map distinguishability of templates at primordial level.
        - If they're close then templates have broad applicability, if they're not then it's interesting to search across them...
    - Section on Transporting the Modal coeffs?


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














