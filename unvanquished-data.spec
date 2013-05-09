%define debug_package	%{nil}
%define oname Unvanquished
Name:           unvanquished-data
Version:        0.15.0
Release:        1
Summary:        Sci-fi RTS and FPS game
License:        CC-BY-SA-2.5 and CC-BY-SA-3.0
Group:          Games/Arcade
Url:            http://unvanquished.net/
#obtaining data files source
# mkdir -p %{name}-%{version} && cd %{name}-%{version}
#for file in pak{{0..9},{A..E}}.pk3; do
#if [ ! -e $file ]; then
#wget -O $file "http://sourceforge.net/projects/unvanquished/files/Assets/$file/download"
#fi
#done
#cd ..
# tar -jcvf %{name}-%{version}.tar.bz2 %{name}-%{version}

Source0:     %{name}-%{version}.tar.bz2   
BuildArch:      noarch
#Requires: unvanquished == %{version}

%description
Players fight online in team based combat in a war of aliens against humans.
This package only contains the game data files.

%prep
%setup -q

%build

%install
mkdir -p  %{buildroot}%{_datadir}/%{oname}/main
install -m0644 {pak0,pak1,pak2,pak3,pak4,pak5,pak6,pak7,pak8,pak9,pakA,pakB,pakC,pakD,pakE}.pk3 %{buildroot}%{_datadir}/%{oname}/main/
install -m0644 vms-%{version}.pk3 %{buildroot}%{_datadir}/%{oname}/main/

%files
%{_datadir}/%{oname}/main/*.pk3

