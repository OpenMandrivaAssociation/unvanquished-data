Name:           unvanquished-data
Version:        0.28.0
Release:        1
Summary:        Sci-fi RTS and FPS game
License:        CC-BY-SA-2.5 and CC-BY-SA-3.0
Group:          Games/Arcade
Url:            http://unvanquished.net/
Source1:        http://www.unvanquished.net/downloads/pkg/training/resources_0.27.1.pk3
Source2:        http://www.unvanquished.net/downloads/pkg/unvanquished_%{version}.pk3
BuildArch:      noarch
Requires:       unvanquished >= 0.25.0

%description
Players fight online in team based combat in a war of aliens against humans.
This package only contains the game data files.

%prep
#nothing to do

%build
#nothing to do

%install
mkdir -p  %{buildroot}%{_datadir}/unvanquished/pkg/
install -m0644 %{SOURCE1} "%{buildroot}%{_datadir}/unvanquished/pkg/"
install -m0644 %{SOURCE2} "%{buildroot}%{_datadir}/unvanquished/pkg/"

%files
%dir %{_datadir}/unvanquished
%dir %{_datadir}/unvanquished/pkg/
%{_datadir}/unvanquished/pkg/*.pk3