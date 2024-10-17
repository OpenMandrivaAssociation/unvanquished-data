%define _build_pkgcheck_set %{nil}
%define _build_pkgcheck_srpm %{nil}

Name:           unvanquished-data
Version:        0.54.1
Release:        1
Summary:        Sci-fi RTS and FPS game
License:        CC-BY-SA-2.5 and CC-BY-SA-3.0
Group:          Games/Arcade
Url:            https://unvanquished.net/

Source1:        http://dl.unvanquished.net/pkg/unvanquished_0.25.0.pk3
Source2:        http://dl.unvanquished.net/pkg/unvanquished_0.26.0.pk3
Source3:        http://dl.unvanquished.net/pkg/unvanquished_0.27.0.pk3
Source4:        http://dl.unvanquished.net/pkg/unvanquished_0.28.0.pk3
Source5:        http://dl.unvanquished.net/pkg/unvanquished_0.29.0.pk3
Source6:        http://dl.unvanquished.net/pkg/unvanquished_0.30.0.pk3
Source7:        http://dl.unvanquished.net/pkg/unvanquished_0.31.0.pk3
Source8:        http://dl.unvanquished.net/pkg/unvanquished_0.32.0.pk3
Source9:        http://dl.unvanquished.net/pkg/unvanquished_0.33.0.pk3
Source10:       http://dl.unvanquished.net/pkg/unvanquished_0.34.0.pk3
Source11:       http://dl.unvanquished.net/pkg/unvanquished_0.35.0.pk3
Source12:       http://dl.unvanquished.net/pkg/unvanquished_0.36.0.pk3
Source13:       http://dl.unvanquished.net/pkg/unvanquished_0.37.0.pk3
Source14:       http://dl.unvanquished.net/pkg/unvanquished_0.38.0.pk3
Source15:       http://dl.unvanquished.net/pkg/unvanquished_0.39.0.pk3
Source16:       http://dl.unvanquished.net/pkg/unvanquished_0.40.0.pk3
Source17:       http://dl.unvanquished.net/pkg/unvanquished_0.41.0.pk3
Source20:       http://dl.unvanquished.net/pkg/tex-all_1.0.pk3
Source21:       http://dl.unvanquished.net/pkg/tex-common_2.0.pk3
Source22:       http://dl.unvanquished.net/pkg/tex-ex_1.0.pk3
Source23:       http://dl.unvanquished.net/pkg/tex-exm_1.0.pk3
Source24:       http://dl.unvanquished.net/pkg/tex-pk01_1.0.pk3
Source25:       http://dl.unvanquished.net/pkg/tex-pk02_1.0.pk3
Source26:       http://dl.unvanquished.net/pkg/tex-space_1.0.pk3
Source27:       http://dl.unvanquished.net/pkg/tex-tech_1.0.pk3
Source28:       http://dl.unvanquished.net/pkg/tex-trak5_1.0.pk3
Source29:       http://dl.unvanquished.net/pkg/tex-all_2.0.pk3
Source30:	http://dl.unvanquished.net/pkg/tex-ej01-clean_1.0.pk3
Source31:	http://dl.unvanquished.net/pkg/tex-ej01-common_1.0.pk3
Source32:	http://dl.unvanquished.net/pkg/tex-ej01-ice_1.0.pk3
Source33:       http://dl.unvanquished.net/pkg/unvanquished_0.42.0.pk3
Source34:       http://dl.unvanquished.net/pkg/unvanquished_0.43.0.pk3
Source35:	http://dl.unvanquished.net/pkg/unvanquished_0.43.1.pk3
Source36:       http://dl.unvanquished.net/pkg/unvanquished_0.44.0.pk3
Source37:       http://dl.unvanquished.net/pkg/unvanquished_0.44.1.pk3
Source38:       http://dl.unvanquished.net/pkg/unvanquished_0.45.0.pk3
Source39:       http://dl.unvanquished.net/pkg/unvanquished_0.46.0.pk3
Source40:       http://dl.unvanquished.net/pkg/unvanquished_0.47.0.pk3


BuildArch:      noarch
# suggested because I'm not very good on chain build on abf.Symbianflo
Suggests:       unvanquished = %{version}
		 
%description
Players fight online in team based 
combat in a war of aliens against humans.
This package only contains the game files.
  
%prep

%build

%install
mkdir -p  %{buildroot}%{_datadir}/unvanquished/pkg/
install -m 644 %{_sourcedir}/unvanquished_*.pk3 %{buildroot}%{_datadir}/unvanquished/pkg/
install -m 644 %{_sourcedir}/tex-*.pk3 %{buildroot}%{_datadir}/unvanquished/pkg/


%files
%{_datadir}/unvanquished/pkg/


