Thesis Outline
--------
0. **Abstract**
    - Goal: connecting inflation models directly to observations, through the bispectrum
        - Constraining the parameters of inflation models, not pheno templates ($f_{NL}$ etc).
        - Full shape information, not point samples or a limit.
        - Efficient numerics gives access to more accurate, and in some cases new, feature shapes.
    - Method: building separability into the tree-level in-in formalism
        - CMB calculation expensive, but need only be done once per primordial basis.
        - So, want a basis expansion that converges quickly for a broad range of inflation models.
        - Convergence on the cube is different to the tetrapyd.
        - Turns out to be much faster at primordial level than previous numerical methods.
    - Results:
        1. First development/implementation of the formalism for high orders, features.
        2. Pointed out the central issue of the cube vs tetra problem.
        3. Found a basis with broad descriptive power.
        4. Validated these methods on interesting examples.
        5. Explore and characterise DBI reso model TBC??
        6. Connect to CMB, get constraints TBC??

    
1. **Introduction to cosmology/inflation**
    - General $\Lambda CDM$ intro.
    - Motivate inflation
        - Define SR params.
    - Perturbations
        - $c_s$.
        - Bunch-Davies initial conditions.
        - MS equation, behaviour at various times.
        - MS equation in $N$, $\tau_s$ - no numerics here, though, just ref forward.
        - Define the power spectrum, discuss constraints.
    - Statistical observables
        - Estimators.
        - Determining the weighting of a coin.
        - Link to Wuhyun.
    - Define the primordial bispectrum.
        - Isotropy etc.
        - f_{NL} (various definitions).
        - Link inflaton non-linearity to primordial NG.
        - Link primordial NG to the CMB, possibly with some simple example. 
    - Coming from part iii level, a derivation of the tree-level in-in formalism.
    - Calculate the interaction Hamiltonian
        - Through the self-interactions, i.e. neglecting the metric perturbations.
        - Discuss DBI, then $P(X, \phi)$.
        - Review of the Maldacena calculation, with metric perturbations.
        - Discuss field-redefinition being unnecessary, as per 1103.4126.
    - Examples of shapes, using $K_{pq}$ notation (link to Enrico's sym polys?)
        - Maldacena, DBI
        - $P(X, \phi)$, EFT
        - Features, with explicit details of how resonance and features generate large NG. 
    - F&RP's work
        - Summary of the achievements and limitations, how I went beyond them.
    - Previous config-by-config codes
        - Their limitations.
        - Their usage in recent works.
    - The squeezed limit consistency condition.


2. **Introduction to bispectrum data analysis**
    - Estimating the bispectrum, complexity. 
    - Review estimators, KSW, separability.
    - Separable approximations to non-separable templates
        - Equilateral to DBI.
        - Approximations to approximations.
    - Modal methods, constraints from Planck.
    - Wuhyun's stuff?


3. **Expanding primordial shapes**
    - Pulling out the $k$-dependance
        - Set up formalism.
        - Forced to decompose on the cube.
        - Defining the notation for the two main time integrals.
    - Inner product choice
        - Easier to interpret, more stringent.
        - Notes on observable convergence being the deciding factor.
    - Template testing
        - Need to understand expected convergence before validation on numerical results.
    - Decomposing shapes on the cube vs tetrapyd
        - Large non-physical contributions.
        - FIGURE: DBI on cube vs tetra.
    - Setting up a basis: augmentation
        - Using modified GS.
        - Legendre and Fourier as building blocks.
    - Basis choice matters! 
        - Why the basic basis expansion is so bad.
        - My new basis sets, and their dramatic improvement.
        - Nice table with descriptions and some single-number comparison on examples.
        - FIGURES: Recon for Malda, DBI, scale-inv, with P0, P1, F0, F1 vs $P_{max}$.
        - FIGURES: Recon for cos, cosDBI, with P0, P1, F0, F1 vs $P_{max}$.
        - FIGURES: Recon for cos-log, cos-logDBI, with P0, P1, F0, F1 vs $P_{max}$.
        - FIGURES: Recon for scaled-DBI, with P0, P1, P1ns, P01ns, P_log vs $P_{max}$.
    - Not obvious, but $k_{ratio}$ matters!
    - The $P_{max}$-$k_{ratio}$ tradeoff (and DBI vs Equil).
    - Log basis for basis without PS info.
    - Loginv basis for resonant shapes.
    - Factor basis?
    - Conclusion:
        - Basic Legendres/Fourier are not sufficient.
        - Need to pay attention to the cube.
        - Including 1/k terms helps massively.
        - The log basis performs excellently, without being tied to a specific $n_s$.


4. **Methods and Validation**
    - Numerics of mode evolution
        - $tau_s$
        - When to set IC's for each mode.
        - Swapping variables.
        - Freeze-out.
    - Integration choices
        - The $i\varepsilon$ prescription
            - Expand on what F&RP wrote.
            - Suppression from plane wave expansion (intuition).
        - Starting the integration with a pinch
            - When to start.
            - Show how easy it is to swamp the result with a sharp start.
            - FIGURE: Relative error for simple $\pi^3$ and for Reso, in ($\beta$, T).
        - Oscillatory weights
            - When to swap.
            - Validation.
        - Stopping the integration
            - A note on boundary terms and difficult (time-dep) cancellations.
    - The interaction Hamiltonian
        - Using integration by parts from RP paper.
    - Set-up of DBI example scan
        - Matching A_s, n_s, r, N*, using $\beta_{IR}$ etc.
    - Going to high $P_{max}$
        - How high can I go, in terms of Planck $w$?
        - How high can I go, in terms parameters that can't be compared to Planck?
    - Validation (on numerical results)
        - FIGURE: the various tetrapyd limits.
        - Maldacena quadratic SR
            - FIGURE: residual for...
        - DBI
            - FIGURE: residual for...
        - Tanh step
            - FIGURE: residual for...
            - FIGURE: PyTransport comparison, scan across step size.
        - Resonance
            - FIGURE: residual for...
            - FIGURE: PyTransport time comparison.
        - DBI resonance
            - FIGURE: residual for...
    - Speed comparison vs PyTransport. Something BINGO can't do?
    - Map distinguishability of templates at primordial level
        - Determine where to usefully scan.
    - Conclusion:
        - My methods (and their implementation) have been validated on interesting examples.
        - Have successfully developed separable methods for high orders and features for the first time.
        - Can obtain full shape info far faster than previous numerical methods.
        

5. **Constraints TO DO** 
    - With either CMB-BEst, or James' coeffs, or both. 
    - Compare convergence at primordial level to convergence at $f_{NL}$ level
        - Talk about Wuhyun's work.
    - Validate this convergence by reproducing Planck constraint using DBI template decomp.
    - Then, check how the scaling from the real numerical result affects this. 
    - EFT stuff, build off Enrico's recent work.


6. **Future Work/Conclusions** 
    - Further SF constraints
        - (Depending on what gets done.)
    - Multi-field
        - Specific models, parameter goals.
        - Notes on implementation.
    - Factor basis to assess limits
        - (Unless this is already done)
        - Map shape space?
    - User guide for Primodal code, public release of Primodal
        - Not relevant to thesis, but could add some short notes on plans.


7. **Appendices** 
    - Numeric choices that aren't specific to mode evolution, etc.
    - Gauss-Legendre integration, fixed weights.
    - Tools used: Numpy, Scipy, Jupyter Notebooks...?
    - Transport method for the Modal coeffs
        - Infinite hierarchy of coupled equations.
        - Choose a basis to make it nice?
        - Real vs Imag...?
        - Sounds cool, not worth pursuing.















